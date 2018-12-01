import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType







client = commands.Bot(command_prefix = '(')

client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name= "Prefix: ("))
    print("The bot is online and connected with Discord!") 
    
    
@client.event
async def on_member_join(member):
    print("In our server" + member.name + " just joined")
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Welcome message')
    embed.add_field(name = '__Welcome to Our Server__',value ='''**Hope you will be active here. Rules:
**No raiding
No dangerous/IP booter code
No asking for admin
No abusing ranks
No racism 

Do not insult other people
Do not start fights
Do. Not ask for admin unless you are applying
No staff disrespect this will result in a ban**  ''',inline = False)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')

    await client.send_message(member,embed=embed)
    print("Sent message to " + member.name)
    channel = discord.utils.get(client.get_all_channels(), server__name='Bot Support Central', name='welcome')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='''Do not forget to read our rules @here  is the rules
No raiding
No dangerous/IP booter code
No asking for admin
No abusing ranks
No racism 
Do not insult other people
Do not start fights
Do. Not ask for admin unless you are applying
No staff disrespect this will result in a ban and never try to break any one of them''', color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
    embed.add_field(name='Your join position is', value=member.joined_at)
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    embed.set_thumbnail(url=member.avatar_url)
    await client.send_message(channel, embed=embed)
    

@client.command(pass_context = True)
async def restart():
    if message.author.id == "342364288310312970":
        await client.logout()

@client.command()
async def help():
    embed = discord.Embed(
        title = "Help Commands!",
        description = """
        **(help**
        Shows this message.
        
        **(verify**
        If you are coder use this command.
        
        **(noncoder**
        If you arent coder use this.
        
        **(modmail**
        Sends mail to our logs!
        
        **(mmod @user**
        Makes a user mod.
        
        **(dmod @user**
        Removes a user from moderators.
        
        **(madmin @user**
        Makes user to be admin.
        
        **(dadmin @usrr**
        Removes admin from user.
        
        **(warn @user**
        Warns a user
        
        **(suggest**
        Makes a suggestion in suggeations channel
        
        **(mute @user**
        Mutes a user 
        
        **(unmute @user**
        Unmutes a user.
        
        **(announce**
        Announces something. \manage roles permission needed./
        
        **(userinfo**
        Gets info about user!
        
        **(cube**
        Chooses randome number between 1-6.
        
        **(createC**
        Creates a channel **ADMINISTRATOR permission needed.**
        
        **(play**
        Plays a music [BETA]
        
        **(joinvoice**
        Bot joines a voice channel!
        
        **(stop**
        Stops playing music!
        
        **(restart**
        Developer Only. Bot will restart
        """

)
    await client.say(embed=embed)
  
@client.command(pass_context=True)
async def verify(ctx):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='coding newbie')
    await client.add_roles(ctx.message.author, role)
 
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def mmod(ctx, user: discord.Member):
    nickname = '[Helper]' + user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='coding helper')
    await client.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for mod.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)
    
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def dmod(ctx, user: discord.Member):
    nickname = user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='coding helper')
    await client.remove_roles(user, role)
    await client.delete_message(ctx.message)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def madmin(ctx, user: discord.Member):
    nickname = '[Admin]' + user.name
    
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='admin coder')
    await client.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for mod.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)
    
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def dadmin(ctx, user: discord.Member):
    nickname = user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='admin coder')
    await client.remove_roles(user, role)
    await client.delete_message(ctx.message)

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)

async def warn(ctx, userName: discord.User, *, message:str):
    channel = discord.utils.get(client.get_all_channels(), name='🎀logs-1🎀')
    
    embed = discord.Embed(
        
        title = "Warning",
        description = """ __**You has been warned!**__
        User warned:
        ``{0}``
        Moderator:
        ``{1}`` 
        Reason:
        ``{2}``""".format(userName, ctx.message.author, message)
        
)
    await client.send_message(userName, embed=embed)
 

    embed = discord.Embed(
        
        title = "Warning",
        description = """ __**You has been warned!**__
        User warned:
        ``{0}``
        Moderator:
        ``{1}`` 
        Reason:
        ``{2}``""".format(userName, ctx.message.author, message)
)
    await client.send_message(channel, embed=embed)
    
    

@client.command(pass_context=True)
async def modmail(ctx, *, msg=None):
    channel = discord.utils.get(client.get_all_channels(), name='🎀logs-1🎀')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    color = discord.Color((r << 16) + (g << 8) + b)
    if not msg:
        await client.say("Please specify a message to send")
    else:
        await client.send_message(channel, embed=discord.Embed(color=color, description=msg + '\n Message From-' + ctx.message.author.id))
        await client.delete_message(ctx.message)
    return

@client.command(pass_context=True)
async def suggest(ctx, *, msg=None):


    channel = discord.utils.get(client.get_all_channels(), name='🎀logs-1🎀')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    color = discord.Color((r << 16) + (g << 8) + b)
    if not msg:
        await client.say("Please specify a message to send")
    else:
        await client.send_message(channel, embed=discord.Embed(color=color, description=msg + '\n Message From-' + ctx.message.author.id))
        await client.delete_message(ctx.message)
    return

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)

async def announce(ctx, userName: discord.User, *, message:str):
    channel = discord.utils.get(client.get_all_channels(), name='🎀announcements🎀')
    
    embed = discord.Embed(
        
        title = "Succesful!",
        description = """ __**Announce has been successfully made!**__"""
        
)
    await client.delete_message(ctx.message)
    await client.send_message(userName, embed=embed)
 

    
        
        
    await client.send_message(channel, """**New Announcement!**
    __Announcement:__
    
    {0}
    
    __Announced by:__
    ``{1}``""".format(message, ctx.message.author))
    

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def mute(ctx, user: discord.Member):
    nickname = '[Muted] ' + user.name
    
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Muted')
    await client.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Mute Announce')
    embed.add_field(name = '__Announce__',value ='**You has been muted!.**',inline = False)

    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)
    
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def unmute(ctx, user: discord.Member):
    nickname = user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Muted')
    await client.remove_roles(user, role)
    await client.delete_message(ctx.message)




@client.command(pass_context=True)
async def chat1(ctx, *, msg=None):


    channel = discord.utils.get(client.get_all_channels(), name='bot-chat1')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    color = discord.Color((r << 16) + (g << 8) + b)
    if not msg:
        await client.say("Please specify a message to send")
    else:
        await client.send_message(channel, embed=discord.Embed(color=color, description=msg + '\n Message From-' + ctx.message.author.id))
        await client.delete_message(ctx.message)
    return

@client.command(pass_context=True)
async def chat2(ctx, *, msg=None):


    channel = discord.utils.get(client.get_all_channels(), name='bot-chat2')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    color = discord.Color((r << 16) + (g << 8) + b)
    if not msg:
        await client.say("Please specify a message to send")
    else:
        await client.send_message(channel, embed=discord.Embed(color=color, description=msg + '\n Message From-' + ctx.message.author.id))
        await client.delete_message(ctx.message)
    return



@client.command(pass_context = True)
     
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)

@client.command()
async def cube():
    choices = [
        "You dropped cube and have 1",
        "You dropped cube and have 2",
        "You dropped cube and have 3",
        "You dropped cube and have 4",
        "You dropped cube and have 5",
        "You dropped cube and have 6",]
    await client.say(random.choice(choices))
    
@client.command(pass_context = True)


async def updates(ctx, *, message:str):
    channel = discord.utils.get(client.get_all_channels(), name='coder-bot')
    
    embed = discord.Embed(
        
        title = "Update log",
        description = """ __**Bots update:**__
        Update:
        ``{0}``
        
        Bot Developer:
        ``{1}`
        
        Prefix:
        **(**` 
        """.format(message, ctx.message.author)
        
)
    await client.send_message(channel, embed=embed)
 
@client.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member, *, nickname):
    await client.change_nickname(user, nickname)
    await client.delete_message(ctx.message)

@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)  
async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await client.delete_messages(mgs)          
        await client.say(str(number)+' messages deleted')
     
    except discord.Forbidden:
        await client.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await client.say('clear failed.')
        return         
   
 
    await client.delete_messages(mgs)
    
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def embed(ctx, *args):
    """
    Sending embeded messages with color (and maby later title, footer and fields)
    """
    argstr = " ".join(args)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    text = argstr
    color = discord.Color((r << 16) + (g << 8) + b)
    await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
    await client.delete_message(ctx.message)

@client.command(pass_context = True)
async def play(ctx, *, url):
    author = ctx.message.author
    voice_channel = author.voice_channel
    try:
        vc = await client.join_voice_channel(voice_channel)
        msg = await client.say("Loading...")
        player = await vc.create_ytdl_player("ytsearch:" + url)
        player.start()
        await client.say("Succesfully Loaded ur song!")
        await client.delete_message(msg)
    except Exception as e:
        print(e)
        await client.say("Reconnecting")
        for x in client.voice_clients:
            if(x.server == ctx.message.server):
                await x.disconnect()
                nvc = await client.join_voice_channel(voice_channel)
                msg = await client.say("Loading...")
                player2 = await nvc.create_ytdl_player("ytsearch:" + url)
                player2.start()


@client.command(pass_context = True)
async def stop(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()

    return await client.say("I am not playing anyting???!")

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def joinvoice(ctx):
    author = ctx.message.author
    channel = author.voice_channel
    await client.join_voice_channel(channel)
    

    
client.run(os.getenv("BOT_TOKEN"))
