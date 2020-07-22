#HEY! Before running, please fill out the info below. This is REQUIRED for the bot to run properly.

#Paste your token in the quotations (this is so the bot can actually run on your account)
token = ""

#Type your prefix in the quotations, this will be placed in front of the chat commands.
prefix = ""

#Enjoy! :)




import discord
import colorama
from colorama import Fore as Color
import os
import datetime
import inputimeout
from inputimeout import inputimeout, TimeoutOccurred

os.system('clear')
print("Logging in...")
class MyClient(discord.Client):
  async def on_connect(self):
    os.system('clear')
    print(f"""
{Color.YELLOW}
______ _                       _   _   _ _   _ _     
|  _  (_)                     | | | | | | | (_) |    
| | | |_ ___  ___ ___  _ __ __| | | | | | |_ _| |___ 
| | | | / __|/ __/ _ \| '__/ _` | | | | | __| | / __|
| |/ /| \__ \ (_| (_) | | | (_| | | |_| | |_| | \__ \ 
|___/ |_|___/\___\___/|_|  \__,_|  \___/ \__|_|_|___/
                   -rewritten-
{Color.LIGHTBLACK_EX}
                 Made by Chaotic
                  

{Color.GREEN}Client has successfully logged in as {Color.WHITE}{client.user.name}#{client.user.discriminator}{Color.GREEN}!
{Color.GREEN}Your discord ID is {Color.WHITE}{client.user.id}

{Color.WHITE}Run {Color.YELLOW}'{prefix}help' {Color.WHITE}in any channel on discord to get started!
""")
  
  async def on_message(self, message):
    if message.author != client.user:
      return
    if message.content == f"{prefix}help":
      await help(message)
    if message.content == f"{prefix}chanclear":
      await channelclear(message)
    if message.content == f"{prefix}logout":
      await logout(message)
    if message.content.lower().startswith(f"{prefix}msgedit"):
      await msgedit(message)
    if message.content.lower().startswith(f"{prefix}spam"):
      await spam(message)
    if message.content.lower().startswith(f"{prefix}gspam"):
      await gspam(message)
    if message.content.lower().startswith(f"{prefix}rspam"):
      await gmspam(message)
    if message.content == f"{prefix}nuke":
      await nuke(message)
  
  async def on_message_delete(self, message):
    if message.author != client.user:
      if isinstance(message.channel, discord.DMChannel):
        print(
          f"{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\n{message.author} deleted a message.\n{Color.GREEN}DM CHANNEL: {Color.WHITE}@{message.channel.recipient}\n{Color.GREEN}CONTENT:\n{Color.WHITE}{message.content}\n \n"
        )
      elif isinstance(message.channel, discord.GroupChannel):
        print(
          f"{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\nA message was deleted from {message.author}.\n{Color.GREEN}GROUP CHANNEL: {Color.WHITE}{message.channel.name}\n{Color.GREEN}CONTENT:\n{Color.WHITE}{message.content}\n \n"
        )
      elif isinstance(message.channel, discord.TextChannel):
        print(
          f"{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\nA message was deleted from {message.author}.\n{Color.GREEN}GUILD: {Color.WHITE}{message.guild.name}\n{Color.GREEN}CHANNEL: {Color.WHITE}#{message.channel}\n{Color.GREEN}CONTENT:\n{Color.WHITE}{message.content}\n \n"
        )
    else:
      return
    return

  async def on_message_edit(self, before, after):
    if before.author.bot == True:
        return
    if before.content == after.content:
        return
    else:
        if before.author == client.user:
            return
        else:
            if isinstance(before.channel, discord.DMChannel):
                print(
                    f"{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\n{before.author.name}#{before.author.discriminator} edited their message.\n{Color.GREEN}DM CHANNEL: {Color.WHITE}@{before.channel.recipient}\n{Color.GREEN}CURRENT CONTENT:\n{Color.WHITE}{after.content}\n{Color.GREEN}PREVIOUS CONTENT:\n{Color.WHITE}{before.content}\n \n"
                )
            if isinstance(before.channel, discord.GroupChannel):
                print(
                    f"{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\n{before.author.name}#{before.author.discriminator} edited their message.\n{Color.GREEN}GROUP CHANNEL: {Color.WHITE}{before.channel.name}\n{Color.GREEN}CURRENT CONTENT:\n{Color.WHITE}{after.content}\n{Color.GREEN}PREVIOUS CONTENT:\n{Color.WHITE}{before.content}\n \n"
                )
            if isinstance(before.channel, discord.TextChannel):
                print(
                    f"{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\n{before.author.name}#{before.author.discriminator} edited their message.\n{Color.GREEN}GUILD: {Color.WHITE}{before.guild.name}\n{Color.GREEN}CHANNEL: {Color.WHITE}#{before.channel.name}\n{Color.GREEN}CURRENT CONTENT:\n{Color.WHITE}{after.content}\n{Color.GREEN}PREVIOUS CONTENT:\n{Color.WHITE}{before.content}\n \n"
                )
    return

async def logout(message):
  await message.delete()
  await client.logout()
  print(f"{Color.YELLOW}[{datetime.datetime.now()} UTC]\n{Color.GREEN}Client has successfully logged out.")

async def help(message):
  await message.delete()
  emHelp = discord.Embed(
    title = "DiscordUtils - Help",
    description = f"""
**__CHAT COMMANDS__**
```
{prefix}help
Shows this message.

{prefix}chanclear
Purges your messages in the channel.

{prefix}msgedit [edit-to]
Edits all your messages to edit-to in the channel.

{prefix}logout
Logs the client out.
```
**__RAID COMMANDS__**
```
{prefix}spam [message]
Spams messages in the channel.

{prefix}gspam [message]
Spams ghost messages in the channel.

{prefix}rspam*
Ghost pings a list of all roles.

{prefix}nuke*
Nukes the server. You will be asked for confirmation in the console.

*servers only
```
    """)
  await message.channel.send(embed = emHelp, delete_after = 30)



async def servernuke(message):
  guild = message.guild
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"{Color.WHITE}{channel.name} {Color.GREEN}was deleted in {Color.WHITE}{guild.name}")
    except:
      print(f"{Color.WHITE}{channel.name} {Color.RED}was not deleted in {Color.WHITE}{guild.name}")
  for member in guild.members:
    try:
      await member.kick()
      print(f"{Color.WHITE}{member.name}#{member.discriminator} {Color.GREEN}was banned in {Color.WHITE}{guild.name}")
    except:
      print(f"{Color.WHITE}{member.name}#{member.discriminator} {Color.RED}was not banned in {Color.WHITE}{guild.name}")
  await guild.create_text_channel("nuked")
  print(f"{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\n{guild.name}{Color.GREEN} was nuked successfully.{Color.WHITE}\n")


async def nuke(message):
  await message.delete()
  if isinstance(message.channel, discord.DMChannel):
    print(f"{Color.RED}Nuke cancelled. {Color.WHITE}[Command was not sent in a server]\n")
    return
  if isinstance(message.channel, discord.GroupChannel):
    print(f"{Color.RED}Nuke cancelled. {Color.WHITE}[Command was not sent in a server]\n")
    return
  try:
    confirmation = inputimeout(f"{Color.YELLOW}[{datetime.datetime.now()} UTC]\n{Color.WHITE}Are you sure you want to nuke {Color.YELLOW}{message.guild.name}{Color.WHITE}? Please type {Color.YELLOW}'Yes'{Color.WHITE} or {Color.YELLOW}'Cancel'{Color.WHITE} to continue.\nThis is case sensitive {Color.RED}and cannot be undone.{Color.WHITE}\nNuke will be cancelled in 30 seconds if no confirmation is given.\n \n>", timeout = 30)
    if confirmation == "Cancel":
      print(f"\n{Color.GREEN}Nuke has been cancelled.\n")
      return
    elif confirmation == "Yes":
      print(f"\n{Color.GREEN}Nuking {Color.WHITE}{message.guild.name}.\n")
      member = message.guild.get_member(client.user.id)
      perms = member.guild_permissions
      if perms.manage_channels == True and perms.ban_members == True:
        await servernuke(message)
      else:
        print(f"\n{Color.RED}Nuke cancelled. {Color.WHITE}[Missing Permissions]\n")
        return
  except TimeoutOccurred:
    print(f"\n{Color.RED}Nuke cancelled. {Color.WHITE}[Time Expired]\n")
    return




async def channelclear(message):
  await message.delete()
  print(f"{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\nDeleting messages...")
  async for message in message.channel.history(limit=None):
    if message.author == client.user and message.type == discord.MessageType.default:
      await message.delete()
  print(f"{Color.GREEN}All messages deleted!{Color.WHITE}\n")



async def spam(message):
  await message.delete()
  spammsg = message.content[len(prefix)+5:]
  while True:
    try:
      await message.channel.send(spammsg)
    except discord.HTTPException:
      print(f"{Color.RED}Spam has been interrupted. {Color.WHITE}[Unknown Error]")
      return
    except discord.Forbidden:
      print(f"{Color.RED}Spam has been interrupted. {Color.WHITE}[Missing Access]")
      return


async def gspam(message):
  await message.delete()
  spammsg = message.content[len(prefix)+6:]
  while True:
    try:
      await message.channel.send(spammsg, delete_after = 0)
    except discord.HTTPException:
      print(f"{Color.RED}Spam has been interrupted. {Color.WHITE}[Unknown Error]")
      return
    except discord.Forbidden:
      print(f"{Color.RED}Spam has been interrupted. {Color.WHITE}[Missing Access]")
      return


async def gmspam(message):
  await message.delete()
  spammsg = "\n".join(role.mention for role in message.guild.roles)
  while True:
    try:
      await message.channel.send(spammsg, delete_after = 0)
    except discord.HTTPException:
      print(f"{Color.RED}Spam has been interrupted. {Color.WHITE}[Unknown Error]")
      return
    except discord.Forbidden:
      print(f"{Color.RED}Spam has been interrupted. {Color.WHITE}[Missing Access]")
      return

async def msgedit(message):
    edit_to = message.content[len(prefix)+8:]
    messages = await message.channel.history(limit=None).flatten()
    if isinstance(message.channel, discord.DMChannel):
        print(
            f"{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\nEditing all messages with @{message.channel.recipient} to {edit_to}..."
        )
    if isinstance(message.channel, discord.GroupChannel):
        print(
            f"{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\nEditing all messages in {message.channel.name} to {edit_to}..."
        )
    if isinstance(message.channel, discord.TextChannel):
        print(
            f"{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\nEditing all messages in {message.channel.name} to {edit_to}..."
        )
    for message in messages:
        try:
            await message.edit(content=edit_to)
        except:
            pass
    print(
        f"{Color.GREEN}Finished editing all messages to {Color.WHITE}{edit_to}"
    )



client = MyClient()
try:
  client.run(token, bot = False)
except discord.LoginFailure:
  print(f"{Color.RED}Client failed to log in. {Color.WHITE}[Invalid token]")
except discord.HTTPException:
  print(f"{Color.RED}Client failed to log in. {Color.WHITE}[Unknown Error]")
