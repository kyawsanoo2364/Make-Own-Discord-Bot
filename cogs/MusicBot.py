import nextcord
from nextcord.ext import commands
import yt_dlp
import asyncio
from nextcord import Interaction

ytdl_format_options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
}

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
}

ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

class YTDLSource(nextcord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # Takes the first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(nextcord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)



class MusicBot(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.command()
    async def play_youtube(self,ctx,url:str):
       await ctx.message.delete()
       if not ctx.author.voice:
           await ctx.send(f"{ctx.author.mention} is not connected to voice channel.")
           return
       try:
            channel =ctx.author.voice.channel
            if not ctx.voice_client:  
               await channel.connect()
        
        
            async with ctx.typing():
                if ctx.voice_client.is_playing():
                    ctx.voice_client.stop()
                player = await YTDLSource.from_url(url,loop=self.client.loop,stream=True)
                ctx.voice_client.play(player,after=lambda e: print(f"Player error:{e}") if e else None)
            await ctx.send(f"Now playing: {player.title}")  
       except Exception as e:
            print(e)  
     
    @commands.command()
    async def pause(self,ctx):
        if not ctx.voice_client:
            await ctx.send(f"No audio is playing.")
            return
        ctx.voice_client.pause()
        await ctx.send('Paused ⏸️')

    @commands.command()
    async def resume(self,ctx):
        ctx.voice_client.resume()
        if not ctx.voice_client:
            await ctx.send(f"No audio is playing.")
            return
        await ctx.send('Resumed ⏯️')

    @commands.command()
    async def stop(self,ctx):
        if not ctx.voice_client:
            await ctx.send(f"No audio is playing.")
            return
        ctx.voice_client.stop()
        await ctx.send('Stopped ⏹️')      
        
        
    @commands.command()
    async def leave(self,ctx):
        if not ctx.voice_client:
            await ctx.send(f"I'm not in voice channel")
            return
        await ctx.voice_client.disconnect()
        
def setup(client):
    client.add_cog(MusicBot(client))        