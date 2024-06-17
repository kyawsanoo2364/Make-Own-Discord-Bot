import nextcord
from nextcord.ext import commands
import requests
from nextcord import Interaction

with open("y.txt","r") as f:
    YOUTUBE_API_KEY =f.read()
#search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={YOUTUBE_API_KEY}&maxResults=1"

class Search(commands.Cog):
    def __init__(self,client):
        self.client =client
        
    @nextcord.slash_command(name="search_youtube",description="Search video in YouTube")
    async def search_youtube(self,interaction:Interaction,query:str=nextcord.SlashOption(description="search")):
        search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={YOUTUBE_API_KEY}&maxResults=1"
        try:
            response = requests.get(search_url)
            response.raise_for_status()
            search_data =response.json()
            if "items" in search_data and search_data["items"]:
                video = search_data["items"][0]
                video_url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"

                await interaction.response.send_message(video_url)
            else:
                await interaction.response.send_message("No results found.")    
        except requests.RequestException as e:
            await interaction.response.send_message("Failed to fetch the search results.")
            print(e)
   
def setup(client):
    client.add_cog(Search(client))        
    