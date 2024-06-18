import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class Admin(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @nextcord.slash_command(name="kick_member",description="Kick any member")
    async def kick_member(self,interaction:Interaction,member:nextcord.Member,reason:str):
       guild = interaction.guild
       if not guild:
            await interaction.response.send_message("This command can use in only server.",ephemeral=True) 
            return
       if not interaction.guild.me.guild_permissions.kick_members:
           await interaction.response.send_message("I don't have permission to kick members.",ephemeral=True)   
           return 
       
       if not interaction.user.guild_permissions.kick_members:
           await interaction.response.send_message("You don't have permission to kick members.",ephemeral=True)   
           return 
       try:
        await member.kick(reason=reason)
        await interaction.response.send_message(f"Successfully! {member.name} has been kicked.",ephemeral=True)
       except Exception as e:
         print(e)
    
    @nextcord.slash_command(name="ban_member",description="Ban members")
    async def ban_member(self,interaction:Interaction,member:nextcord.Member,reason:str):
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message("This command can use in only server.",ephemeral=True) 
            return
        if not interaction.guild.me.guild_permissions.ban_members:
           await interaction.response.send_message("I don't have permission to ban members.",ephemeral=True)   
           return  
        
        if not interaction.user.guild_permissions.ban_members:
           await interaction.response.send_message("You don't have permission to ban members.",ephemeral=True)   
           return 
       
        await member.ban(reason=reason)
        await interaction.response.send_message(f"Successfully! {member.name} has been banned.",ephemeral=True)
        
        
    @nextcord.slash_command(name="assign_role",description="Assign role to any member",dm_permission=False)
    async def assign_role(self,interaction:Interaction,role_name:nextcord.Role,member:nextcord.Member,reason:str): 
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message("This command can use in only server.",ephemeral=True) 
            return 
        if not interaction.guild.me.guild_permissions.manage_roles:
            await interaction.response.send_message("I don't have permission to manage role",ephemeral=True)
            return
        
        if not interaction.user.guild_permissions.manage_roles:
             await interaction.response.send_message("You don't have permission to manage role",ephemeral=True)
             return
        if role_name.position >= interaction.guild.me.top_role.position:
            await interaction.response.send_message("I can't assign a role that is higher or equal to my highest role",ephemeral=True)
            return
        try:
            await member.add_roles(role_name,reason=reason)
            await interaction.response.send_message(f"Assigned {role_name} role to {member.mention}")
        except nextcord.Forbidden:
            await interaction.response.send_message("I don't have permission to assign the role.",ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {str(e)}", ephemeral=True)
            
            
    @nextcord.slash_command(name="remove_role",description="Remove role from any member")
    async def remove_role(self,interaction:Interaction,role_name:nextcord.Role,member:nextcord.Member,reason:str):
        guild = interaction.guild
        if not guild:
            await interaction.response.send_message("This command can use in only server.",ephemeral=True) 
            return
        if not interaction.guild.me.guild_permissions.manage_roles:
            await interaction.response.send_message("I don't have permission to manage role",ephemeral=True)
            return
        if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message("You don't have permission to manage role",ephemeral=True)
            return
        if role_name.position >= interaction.guild.me.top_role.position:
            await interaction.response.send_message("I can't remove a role that is higher or equal to my highest role",ephemeral=True)
            return
        await member.remove_roles(role_name,reason=reason)
        await interaction.response.send_message(f"Removed {role_name} role from {member.mention}. ") 
        
    @nextcord.slash_command(name="mute",description="Mute the member")
    async def mute(self,interaction:Interaction,member:nextcord.Member):
        if not interaction.guild.me.guild_permissions.manage_roles:
            await interaction.response.send_message("I don't have permission to manage member.")
            return
        if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message("You don't have permission to manage member.")
            return
        mute_role = nextcord.utils.get(interaction.guild.roles,name = "Mute")
        if not mute_role:
            mute_role = await interaction.guild.create_role(name="Mute")
            for channel in interaction.guild.channels:
                await channel.set_permissions(mute_role, speak=False, send_messages=False)
                            
        await member.add_roles(mute_role)
        await interaction.response.send_message(f"{member.mention} has been muted.")
        
    @nextcord.slash_command(name="unmute",description="Unmute the member")
    async def unmute(self,interaction:Interaction,member:nextcord.Member):
        if not interaction.guild.me.guild_permissions.manage_roles:
            await interaction.response.send_message("I don't have permission to manage member.")
            return
        if not interaction.user.guild_permissions.manage_roles:
            await interaction.response.send_message("You don't have permission to manage member.")
            return
        mute_role = nextcord.utils.get(interaction.guild.roles,name = "Mute")
        if not mute_role:
            return                  
        await member.remove_roles(mute_role)
        await interaction.response.send_message(f"{member.mention} has been unmuted.")       
      
  
  
def setup(client):
    client.add_cog(Admin(client))        