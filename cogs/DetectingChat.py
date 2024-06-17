import nextcord 
from nextcord.ext import commands
import time
from collections import defaultdict
import asyncio
import logging

word_to_check =["fuck","mmsp","kmkl","motherfucker","lee"]

message_counts = defaultdict(lambda:defaultdict(int))
TIME_FRAME = 10 
MESSAGE_LIMIT = 5

class DetectingChat(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.client.user:
            return
        
        if "lol" in message.content.lower():
            await message.add_reaction("🤣")
        
        if "sad" in message.content.lower():
            await message.add_reaction("😥")
        
        if "happy" in message.content.lower():
            await message.add_reaction("😀")
            
        if "love" in message.content.lower():
            await message.add_reaction("❤️‍🔥")    
        
        for word in word_to_check:
            if word in message.content.lower():
                await message.delete()
                channel = message.channel
                await channel.send("Don't send again like this.") 
                   
        #============================== Anti-raid protection ============================
        current_time=time.time()
        message_counts[message.guild.id][message.author.id] +=1
        guild = message.guild
        await self.client.process_commands(message)
        
        if message_counts[message.guild.id][message.author.id] > MESSAGE_LIMIT:
            await message.channel.send(f'🚨 {message.author.mention} is spamming!')
            try: 
                mute_role = nextcord.utils.get(guild.roles,name = "Mute")
                if not mute_role:
                    mute_role = await guild.create_role(name="Mute")
                    for channel in guild.channels:
                        await channel.set_permissions(mute_role, speak=False, send_messages=False)
                        logging.info(f'Set permissions for Mute role in channel {channel.name}')           
                await message.author.add_roles(mute_role,reason="Anti-Raid reason.")
                await message.channel.send(f"{message.author.mention} has muted reason for: Anti-Raid reason")
                message_counts[message.guild.id][message.author.id] =0
            except nextcord.Forbidden:
                print("Failed to ban a member due to lack of permissions.")
            except nextcord.HTTPException:
                print("Failed to ban a member due to HTTPException.")
                del message_counts[message.guild.id][message.author.id]
        await asyncio.sleep(TIME_FRAME)
        if message_counts[message.guild.id][message.author.id] > 0:
             message_counts[message.guild.id][message.author.id] -=1
           
            

        
    
    @commands.Cog.listener()
    async def on_reaction_add(self,reaction,user):
         message = reaction.message 
         time.sleep(3)
         await message.add_reaction(reaction) 
        
def setup(client):
    client.add_cog(DetectingChat(client))        