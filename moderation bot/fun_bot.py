# This is fully made by syteno. Please give credit if you use 1 of the function i made here thank you! :)
# Before you can run this you need to install some modules, like embeds and stuff. Error codes will occur with the right name for them as i made this a time ago and forgot wich modules you need to install LOL.
# Also keep in mind this is really standard, you can allways advance it how you want.
# Btw keep in mind that the bot needs a high tier role, and all premissions (i recommend giving administrator as i made multiple checks).
import discord 
from datetime import timedelta 
from discord.ext import commands
from discord import message
from discord import guild
from discord import embeds
from discord import app_commands
import random 

intents = discord.Intents.default()
client = commands.Bot(command_prefix=".", intents=discord.Intents.all()) # Choose here the command prefix, it can be everything.
@client.event
async def on_ready():
    print("Bot is running", {client.user}, on_ready)
    await client.change_presence(status=discord.Status.idle) # This sets the bot on idle, you can delete this if you like.
    return

# fun commands
@client.command(aliases=["Ping"]) # This is a ping pong command, for fun.
async def ping(ctx):
    verified = 0 # Put here the ID of the verified role, this makes sure that non verified users cant use this command.
    owner = 0 # The same right here but this is just so it says something else for you if you trigger it, you can also delete this part if you like.

    if (verified not in [role.id for role in ctx.author.roles]) and (ctx.author.id != owner): # This makes it sure non verified users cant use the command/checks if the person that triggers it has the specified role.
        print("Unauthorized user attempted to execute the command.") # This shows in the command prompt that somebody without the specified role tried to do the command.
        await ctx.message.delete(delay=5)
        return

    if ctx.author.id == owner: # You can delete this part, i just did it for fun.
        await ctx.reply("Pong my maker!")
    else:
        await ctx.reply("Pong!")
        return
print("ping command: loaded.") # This just shows how many commands are loaded, and where a error can occur.

@client.command(aliases=["Hug"]) # This is a hug command, for fun.
async def hug(ctx, member: discord.Member=None):
    verified = 0
    player = ctx.author.name

    if verified not in [role.id for role in ctx.author.roles]:
        print("Unauthorized user attempted to execute the command.")
        return
    
    if member is None:
        await ctx.reply("Please select a player to hug.", delete_after=5) # Checks if a person is mentioned to hug.
        await ctx.message.delete(delay=5)
        print({player}, "didint mention someone...")
        return
    
    await ctx.send(f"{player} gave {member.name} a hug ❤️") 
    await ctx.message.delete(delay=0)
    print({player}, "gave an hug to", {member.name})
    return
print("hug command: loaded.")

@client.command(pass_context=True, aliases=["Cute", "cutie", "Cutie"]) # This command lets the bot rate the person you mention how cute they are, fun command.
async def cute(ctx, user: discord.Member=None):
    verified = 0
    
    if verified not in [role.id for role in ctx.author.roles]:
        print("Unauthorized user attempted to execute the command.")
        await ctx.message.delete(delay=5)
        return
    
    if user is None:
        await ctx.reply("Please specify a user.", delete_after=5)
        await ctx.message.delete(delay=5)
        print({ctx}, "wasnt there.")
        return
    
    rnd = random.randint(0, 100)
    message = f"{user.mention} ({user.display_name}) is {rnd}% cute."
    await ctx.send(message)
    print(f"{user.mention} ({user.display_name}) is {rnd}% cute.")
    return

print("cute command: loaded.")

@client.command(pass_context=True, aliases=["Gay", "GAY", "homo", "Homo", "HOMO"]) # This command lets the bot choose how gay the person mentioned is.
async def gay(ctx, user: discord.Member=None):
    verified = 0
    
    if verified not in [role.id for role in ctx.author.roles]:
        print("Unauthorized user attempted to execute the command.")
        await ctx.message.delete(delay=5)
        return
    
    if user is None:
        await ctx.reply("Please specify a user.", delete_after=5)
        await ctx.message.delete(delay=5)
        print({ctx}, "wasnt there.")
        return
    
    rnd = random.randint(0, 100)
    message = f"{user.name} ({user.display_name}) is {rnd}% gay."
    await ctx.send(message)
    print(f"{user.name} ({user.display_name}) is {rnd}% gay.")
    return

print("gay command: loaded.")

@client.command(pass_context=True, aliases=["Sigma", "SIGMA"]) # This command lets the bot say how sigma somebody is.
async def sigma(ctx, user: discord.Member=None):
    verified = 0
    
    if verified not in [role.id for role in ctx.author.roles]:
        print("Unauthorized user attempted to execute the command.")
        await ctx.message.delete(delay=5)
        return
    
    if user is None:
        await ctx.reply("Please specify a user.", delete_after=5)
        await ctx.message.delete(delay=5)
        print({ctx}, "wasnt there.")
        return
    
    rnd = random.randint(0, 100)
    message = f"{user.name} ({user.display_name}) is {rnd}% sigma."
    await ctx.send(message)
    print(f"{user.name} ({user.display_name}) is {rnd}% sigma.")
    return

print("sigma command: loaded.")

# moderation commands
@client.command(aliases=["Kick"]) #Kick command.
async def kick(ctx, member: discord.Member=None, *, reason=None):
    owner = 0 
    coowner = 0
    admin = 0
    creatorofbot = 0
    if owner not in [role.id for role in ctx.author.roles] and coowner not in [role.id for role in ctx.author.roles]  and admin not in [role.id for role in ctx.author.roles] and (ctx.author.id != creatorofbot):
        print("Unauthorized user attempted to execute the command.")
        await ctx.message.delete(delay=5)
        return
    
    if member is None:
        await ctx.reply("Please specify a user.", delete_after=5)
        await ctx.message.delete(delay=5)
        return
    
    ctx.author.id == owner
    if member is owner:
     await ctx.reply("I cant kick my maker.", delete_after=5)
     await ctx.message.delete(delay=5)
     print("a bitch tried to kick you", ctx)
     return
    
    if reason is None:
        reason = "No reason provided."

    await member.kick(reason=reason)
    await ctx.send(f"User {member.mention} has been kicked for: {reason}", delete_after=5)
    await ctx.message.delete(delay=5)
    print("User", {member.mention}, "Got kicked L")
    return

print("kick command: loaded.")

@client.command(aliases=["Ban"]) # Ban command.
async def ban(ctx, member: discord.Member=None, *, reason=None):
    owner = 0 
    coowner = 0
    admin = 0
    creatorofbot = 0
    
    if owner not in [role.id for role in ctx.author.roles] and coowner not in [role.id for role in ctx.author.roles]  and admin not in [role.id for role in ctx.author.roles] and (ctx.author.id != creatorofbot):
        print("Unauthorized user attempted to execute the command.")
        await ctx.message.delete(delay=5)
        return

    if member is None:
        await ctx.reply("Please specify a user.", delete_after=5)
        await ctx.message.delete(delay=5)
        return
    
    ctx.author.id == creatorofbot
    if member is creatorofbot:
         await ctx.reply("I cant ban my maker.", delete_after=5)
         await ctx.message.delete(delay=5)
         print("a bitch tried to ban you", ctx)
         return
    
    if reason is None:
        reason = "No reason provided."
        
    await ctx.guild.ban(member, reason=reason)
    await ctx.send(f"User {member.mention} has been banned for: {reason}", delete_after=5)
    await ctx.message.delete(delay=5)
    print("User",  {member.mention}, "got banned, L")
    return

print("ban command: loaded.")

@client.command(aliases=["Purge", "clear", "Clear", "delete", "Delete"]) #Purge command.
async def purge(ctx, amount: int = None):
    owner = 0 
    coowner = 0
    admin = 0
    if owner not in [role.id for role in ctx.author.roles] and coowner not in [role.id for role in ctx.author.roles]  and admin not in [role.id for role in ctx.author.roles]:
        print("Unauthorized user attempted to execute the command.")
        await ctx.message.delete(delay=5)
        return

    if amount is None:
        await ctx.reply("Please specify the number of messages to delete.", delete_after=5)
        await ctx.message.delete(delay=5)
        return

    if amount <= 0:
        await ctx.reply("Please specify a positive number of messages to delete.", delete_after=5)
        await ctx.message.delete(delay=5)
        return

    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"Successfully deleted {amount} message(s) in {ctx.channel}.", delete_after=5)
    print("Succesfully purged", {amount},)
    return

print("purge command: loaded.")

@client.command(pass_content=True, aliases=["nick", "nickname", "Nick", "Nickname", "Changenick"]) # Nickname of somebody changer.
async def changenick(ctx, member: discord.Member = None, *, nick: str = None):
    owner = 0 
    coowner = 0
    admin = 0
    
    if owner not in [role.id for role in ctx.author.roles] and coowner not in [role.id for role in ctx.author.roles]  and admin not in [role.id for role in ctx.author.roles]:                                 
        print("Unauthorized user attempted to execute the command.")
        await ctx.message.delete(delay=5)
        return

    if member is None:
        await ctx.reply("Please specify a user.", delete_after=5)
        await ctx.message.delete(delay=5)
        return
    
    if nick is None:
        await ctx.reply("Please specify a new nickname.", delete_after=5)
        await ctx.message.delete(delay=5)
        return
    
    await member.edit(nick=nick)
    await ctx.reply(f"Succesfully changed the nickname of: {member.mention}", delete_after=5)
    await ctx.message.delete(delay=5)
    print("changed nick of", member.mention)
    return

print("nickname command: loaded.")

@client.command(aliases=["Unban"]) # Unban command, by id only!
async def unban(ctx, user: discord.User=None):
    guild = ctx.guild
    owner = 0
    coowner = 0
    admin = 0
    if owner not in [role.id for role in ctx.author.roles] and coowner not in [role.id for role in ctx.author.roles] and admin not in [role.id for role in ctx.author.roles]:
     print("Unauthorized user attempted to execute the command.")
     await ctx.message.delete(delay=5)
     return
    
    if user is None:
     await ctx.reply("Please specify a user.", delete_after=5)
     await ctx.message.delete(delay=5)
     return
    
    await guild.unban(user=user)
    await ctx.reply(f"Succesfully unbanned: {user}", delete_after=5)
    await ctx.message.delete(delay=5)
    print("Succesfully unbanned:", {user})
    return

print("unban command: loaded.")
client.run("0") # Put here your bot token.
