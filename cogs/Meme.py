import nextcord
from nextcord.ext import commands
import requests

MEME_API_URL = "https://meme-api.com/gimme" 

class Meme(commands.Cog):
    def __init__(self,client):
        self.client =client
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.client.user:
            return
        
        #random post meme for detection
        if "meme" in message.content.lower():
             try:
                 response = requests.get(MEME_API_URL)
                 response.raise_for_status()
                 meme_data = response.json()
                 meme_title = meme_data["title"]
                 meme_url = meme_data["url"]
                 embed = nextcord.Embed(title = meme_title,color = 0x80008E)
                 embed.set_image(meme_url)
                 await message.channel.send(embed = embed)
                 
                 
             except Exception as e:
                 print(e)  
        
        
def setup(client):
    client.add_cog(Meme(client))        
        