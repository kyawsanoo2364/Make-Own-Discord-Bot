import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class Manage(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @nextcord.slash_command(name="create_channel",description="Create new channel")
    async def create_channel(self,interaction:Interaction,channel_name:str,channel_type:str,category_name:str):
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message("This command can use in only server.",ephemeral=True) 
            return
        if not interaction.guild.me.guild_permissions.manage_channels:
            await interaction.response.send_message("I don't have permission to manage channel",ephemeral=True)
            return
        
        if not interaction.user.guild_permissions.manage_channels:
            await interaction.response.send_message("You don't have permission to manage channel",ephemeral=True)
            return
        
        category = nextcord.utils.get(guild.categories,name = category_name)
        if not category:
            text = "/create_category"
            formatted_text = f"```bash\n {text}\n```"
            await interaction.response.send_message(f"Category {category_name} not found.if you want to create new category, you can use this command {formatted_text}")
            return 
        if channel_type.lower() == "text": 
            await guild.create_text_channel(channel_name,category=category)
            await interaction.response.send_message(f"Text Channel '{channel_name}' has been created!",ephemeral=True)
        elif channel_type.lower() == "voice":
            await guild.create_voice_channel(channel_name,category=category)
            await interaction.response.send_message(f"Voice channel '{channel_name}' has been created.",ephemeral=True)
        else:
            await interaction.response.send_message(f"Invalid channel type. Use Only 'text' or 'voice'.",ephemeral=True)          
    
    @nextcord.slash_command(name="remove_text_channel",description="Delete channel")
    async def remove_text_channel(self,interaction:Interaction,channel:nextcord.TextChannel):
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message("This command can use in only server.",ephemeral=True) 
            return
        if not interaction.guild.me.guild_permissions.manage_channels:
            await interaction.response.send_message("I don't have permission to manage channel",ephemeral=True)
            return
        if not interaction.user.guild_permissions.manage_channels:
            await interaction.response.send_message("You don't have permission to manage channel",ephemeral=True)
            return
        
  
        await channel.delete()
        await interaction.response.send_message(f"Successfully! {channel.name} has been removed....",ephemeral=True)
        
        
    @nextcord.slash_command(name="remove_voice_channel",description="Delete channel")
    async def remove_voice_channel(self,interaction:Interaction,channel:nextcord.VoiceChannel):
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message("This command can use in only server.",ephemeral=True) 
            return
        if not interaction.guild.me.guild_permissions.manage_channels:
            await interaction.response.send_message("I don't have permission to manage channel",ephemeral=True)
            return
        if not interaction.user.guild_permissions.manage_channels:
            await interaction.response.send_message("You don't have permission to manage channel",ephemeral=True)
            return
        
  
        await channel.delete()
        await interaction.response.send_message(f"Successfully! {channel.name} has been removed....",ephemeral=True)  
        
    @nextcord.slash_command(name="create_category",description="Create new category")
    async def create_category(self,interaction:Interaction,name:str):
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message("This command can use in only server.",ephemeral=True) 
            return
        if not interaction.guild.me.guild_permissions.manage_channels:
            await interaction.response.send_message("I don't have permission to manage channel",ephemeral=True)
            return
        if not interaction.user.guild_permissions.manage_channels:
            await interaction.response.send_message("You don't have permission to create category",ephemeral=True)   
            return
        await guild.create_category_channel(name=name)
        await interaction.response.send_message(f"{interaction.user.mention} has been created {name} category.")   
        
    @nextcord.slash_command(name="delete_category",description="Delete existing category")
    async def delete_category(self,interaction:Interaction,name:nextcord.CategoryChannel):
        guild= interaction.guild
        
        if not guild:
            await interaction.response.send_message("This command can use in only server.",ephemeral=True) 
            return
        if not interaction.guild.me.guild_permissions.manage_channels:
            await interaction.response.send_message("I don't have permission to manage channel",ephemeral=True)
            return
        if not interaction.user.guild_permissions.manage_channels:
            await interaction.response.send_message("You don't have permission to create category",ephemeral=True)   
            return
        await name.delete()
        await interaction.response.send_message(f"{interaction.user.mention} has been removed {name} category.")   
        
    
      
def setup(client):
    client.add_cog(Manage(client))        