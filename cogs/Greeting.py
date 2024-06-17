import nextcord
from nextcord.ext import commands
import time
from collections import defaultdict

MAX_JOINS     = 10 
TIME_FRAME = 10 * 60# within this frame rate

join_times = defaultdict(list)

class Greeting(commands.Cog):
    def __init__(self,client):
        self.client =client
    
    @commands.Cog.listener()
    async def on_member_join(self,member):
        guild = member.guild
        embed = nextcord.Embed(title=f"Welcom to {member.guild.name}, {member.mention}! Enjoy your stay.",color= 0x85FF18)
        await member.send(embed =embed)
        
        #=================== Anti-raid protection ===========================
        current_time = time.time()
        join_times[member.guild.id].append(current_time)
        
        join_times[member.guild.id] = [t for t in join_times[member.guild.id] if current_time - t <= TIME_FRAME]
        
        if len(join_times[member.guild.id]) > MAX_JOINS:
            
            channel = nextcord.utils.get(nextcord.TextChannel,name="alerts")
            if not channel:
                channel =await guild.create_text_channel("alerts")
            await channel.send(f'🚨 Raid alert! {len(join_times[member.guild.id])} users have joined in the last {TIME_FRAME // 60} minutes.')    
                   
            for join_time in join_times[member.guild.id]:
                if current_time - join_time < 60:
                    try:
                        await member.kick(reason ="Anti-raid Measure")
                        await channel.send(f"I have kicked {member.mention}.")
                    except nextcord.Forbidden:
                         print("Failed to ban a member due to lack of permissions.")
                    except nextcord.HTTPException:
                        print("Failed to ban a member due to HTTPException.")
        
         
    
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        embed = nextcord.Embed(title =f"Goodbye From {member.guild.name}!!",color = 0xFF9618)
        await member.send(embed = embed)
   
def setup(client):
    client.add_cog(Greeting(client))        