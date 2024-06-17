import nextcord
from nextcord.ext import commands
import requests


with open("w.txt","r") as f: 
    API =f.read()
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

class Weather(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @nextcord.slash_command(name="weather",description="Get current weather")
    async def weather(self,interaction:nextcord.Interaction,city:str):
        url = f"{BASE_URL}?q={city}&appid={API}&units=metric"
        response =requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            
            #prepare information
            city_name = data["name"]
            country = data["sys"]["country"]
            temp = main["temp"]
            temp_feels =main["feels_like"]
            humidity = main["humidity"]
            description = weather['description']

            # Create an embed message
            embed = nextcord.Embed(
                title=f"Weather in {city_name}, {country}",
                description=f"{description.capitalize()}",
                color=0x00FF00
            )
            embed.add_field(name="Temperature", value=f"{temp}°C", inline=True)
            embed.add_field(name="Feels Like", value=f"{temp_feels}°C", inline=True)
            embed.add_field(name="Humidity", value=f"{humidity}%", inline=True)

            # Send the embed message
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message(f"City {city} not found. Please check the name and try again.",ephemeral=True)    

def setup(client):
    client.add_cog(Weather(client))        