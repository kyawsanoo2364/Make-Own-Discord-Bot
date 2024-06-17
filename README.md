# How to make Discord Bot
[!Note]
> Sorry for my bad english

step1: Download this project files. (clone or zip download)

step2: Go to the https://discord.com/developers/docs/quick-start/getting-started and Click Create App button.The create app form will appear. 
> If you haven't signed in yet, please do so first
> 
step3: After creating app, click Bot menu (see left side menu bar) and then reset token. Please fill your password and copy your token code.

step4: Click the OAuth2 menu. Then check ```bot``` in OAuth2 URL Generator. Under Bot Permissions, check ```Administrator```. Then copy the Generated URL, enter the link and connect to your server
[!Note]
> You need to all enable Privileged Gateway Intents in `bot` menu

step5: Open downloaded this project files. Find ```token.txt``` file and paste your bot token inside.

# Test Bot

> You need to have Python installed on your pc.
>
step1: Open your downloaded project file. 

step2: Open your `terminal` or `cmd` inside project file.

step3: Please run this command in terminal or cmd:
       ```pip3 install -r requirements.txt ``` or ```pip install -r requirements.txt```
       
step4: Then run this command```python3 main.py```

step5: Open your discord and see your bot is active now.


# What Can do this bot?
- Moderation ( ban, kick, assign role)
- Search Functional ( YouTube video search )
- Anti-Raid Protection to your Discord server
- See current weather
- Sent you meme (if you write `meme` in your message)
- Automatic Reaction
- Auto Detection chats 
- Auto Greeting new member and Goodbye for leave member in their direct message.
- You can play YouTube music in voice channel
- Schedule for your meeting

  # Commands
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

  # Contacts
  Email    - skyaw6736@gmail.com
  
  Facebook - https://www.facebook.com/chirstopher.kyawsanoo 


       





