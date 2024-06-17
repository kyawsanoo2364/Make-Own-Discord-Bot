import nextcord
from nextcord.ext import commands
import os
from nextcord import Interaction

with open("token.txt","r") as f:
    Token = f.read()

intents = nextcord.Intents.default()
intents.message_content= True
intents.members = True
intents.dm_messages = True
intents.dm_reactions = True
intents.dm_typing = True
intents.guilds = True
client =commands.Bot(command_prefix="$",intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.idle,activity=nextcord.Activity(type=nextcord.ActivityType.watching,name="YouTube"))
    print("The bots is ready for now.")
    print("-------------------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hi! I'm reflex bot. How can i help you today?")


@client.slash_command(name="help")
async def help(interaction:Interaction):
    h_text ="""
    ```
     /help    => help
     
     #================ Usefull slash commands =========================
     /search_youtube <Enter you want to search>   => Search YouTube Video
     /create_channel <category_name> <channel_name> <channel_type> =>Create new channel
     /remove_text_channel <channel>               => Remove text channel
     /remove_voice_channel <channel>              => Remove voice channel
     /create_category <name>                      => Create new category
     /delete_category <name>                      => Delete existing category
     /schedule_meeting <date> <time> <message> <alert_in> => Schedule For Meeting
     /weather <city> => Get current weather
     
       ================= Moderation =======================
     /assign_role <role_name> <member> <reason> => Assign role to member
     /remove_role <role_name> <member> <reason> => Remove role from member
     /ban_member <member> <reason>              => Ban the member
     /kick_member <member> <reason>             => Kick the member
     
     ================== Music ============================
     $play_youtube [Enter youtube video url] => Play the song from YouTube
     $pause  => Pause the audio 
     $resume => Resume the audio
     $stop   => Stop the audio
     $leave  => Leave from the voice channel
     
    ```
    """
    await interaction.response.send_message(h_text,ephemeral=True)
    
@client.command()
async def echo(ctx,*,message:str):
    await ctx.send(message)
    
@client.command()
async def userinfo(ctx, member: nextcord.Member):
    embed = nextcord.Embed(title=f"{member.name}'s info", description="Here is what I could find:", color=0x00ff00)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Username", value=member.display_name, inline=True)
    embed.add_field(name="Account Created", value=member.created_at.strftime("%b %d, %Y"), inline=True)
    await ctx.send(embed=embed)
    
@client.command()
async def ping(ctx):
    await ctx.send("Pong!")     

#Run Cogs
initail_extensions=[]
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        initail_extensions.append(f"cogs.{filename[:-3]}") 

if __name__ == "__main__":
    for extension in initail_extensions:
        client.load_extension(extension)        
        

    
client.run(Token)    

