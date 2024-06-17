import nextcord
from nextcord.ext import commands,tasks
from nextcord import Interaction
import datetime
import pytz

alert_time =None
channel_id = None
messages =None
meetings = {
    "alert_time":None,
    "channel_id":None,
    "message":None
}

class MeetingAlert(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.check_time.start()
        
    
   
    @nextcord.slash_command(name="schedule_meeting",description="Schedules a meeting alert.[Date format: YYYY-MM-DD],[Time format: HH:MM (24-hour)]")
    async def alert(self,interaction:Interaction,date:str = nextcord.SlashOption(description="Date format: YYYY-MM-DD"),time:str =nextcord.SlashOption(description="Time format: HH:MM (24-hour)") ,message:str =nextcord.SlashOption(description="Enter your message"),alert_in:nextcord.TextChannel =nextcord.SlashOption(description="Enter you want to alert in which channel"),timezone:str = nextcord.SlashOption(description="For example: Asia/Yangon")):
        if not interaction.user.guild_permissions.manage_messages:
            await interaction.response.send_message("You don't permission to manage message",ephemeral=True)
            return
        try:
            if timezone in pytz.all_timezones:
                
                user_tz = pytz.timezone(timezone)
                native_time =datetime.datetime.strptime(f"{date} {time}",'%Y-%m-%d %H:%M')
                meeting_time = user_tz.localize(native_time)
                meetings["alert_time"] = meeting_time
                meetings["channel_id"] = alert_in.id
                meetings["message"]=message
                await interaction.response.send_message(f"Schedule for meeting:  {meetings['alert_time']}  (note: if set new schedule,the bot will automatically remove old schedule time. )",ephemeral=False)

            else:
                await interaction.response.send_message(f"{timezone} timezone not found.for example: Asia/Yangon or see detail:https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568 ",ephemeral=True)
        except ValueError:
            await interaction.response.send_message(f"Invalid date or time format. Please use YYY-MM-DD and HH:MM (24-hours) format",ephemeral=True)    
    
    @tasks.loop(minutes=1)
    async def check_time(self):
        now = datetime.datetime.now(pytz.utc)
        if meetings["alert_time"] is not None:
            if now >= meetings["alert_time"]:
                if meetings["channel_id"] is not None:
                    channel = await self.client.fetch_channel(meetings["channel_id"])
                    await channel.send(f"Reminder: {meetings['message']}")
                    meetings["alert_time"] = None
                    meetings["channel_id"] = None
                    meetings["message"] = None               
            
    @check_time.before_loop
    async def before_check_time(self):
        await self.client.wait_until_ready()      
    
    def cog_unload(self):
        self.check_time.cancel()  # Stop the loop when the cog is unloaded
                 

def setup(client):
    client.add_cog(MeetingAlert(client))
          

        