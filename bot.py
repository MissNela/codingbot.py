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
        
        **(ping**
        :ping_pong: Pong!
        
        **(dog**
        Shows a cute dog!
        
        **(meme**
        Shows a meme!
        
        **(update**
        Shows bot update!
        
        """,
        color = 0x800000
        

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
    
@client.command()
async def invite():
    await client.say("https://discordapp.com/oauth2/authorize?client_id=513497138143952906&permissions=8&scope=bot")
    
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
    
    embed = discord.Embed(color = 0xB22222,
        
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
 

    embed = discord.Embed(color = 0xB22222,
        
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

@client.command()
async def dog():
         embed = discord.Embed(title="This dog is so cute!")
         embed.set_footer(text="Tip: If the image didnt load try to use this command again! | Developer Nela | Bot version: 1.3")
         embed.set_image(url = random.choice([
             "https://cdn.discordapp.com/attachments/516388114550226944/518782783951339520/15437578341941184284651.jpg",
             "https://img.buzzfeed.com/buzzfeed-static/static/2015-02/10/12/enhanced/webdr06/anigif_enhanced-20559-1423589960-10.gif",
             "https://cdn.discordapp.com/attachments/516388114550226944/518786921640493076/1543758832313970521957.jpg",
             "https://i2-prod.mirror.co.uk/incoming/article9769854.ece/ALTERNATES/s615/PROD-Mixed-breed-lab-cross-8-week-old-puppy-in-farm-yard-near-Cochrane-AlbertajpgED.jpg",
             "https://www.waterworldsons.it/wp-content/uploads/2018/07/golden-americano-inglese.jpg",
             "https://www.mynd.nu/wp-content/uploads/2017/07/cute-golden-retriever-puppies-202-5967223e5ba31__605.jpg",
             "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRyJ4fIfgtKv-Fv_YquF8IZUKqicFfDaSQwanf-neMJMkhAhvqm",
             "https://www.rspcansw.org.au/wp-content/uploads/2017/08/50_a-feature_dogs-and-puppies_mobile.jpg"]))
         await client.say(embed=embed) 

@client.command(pass_context=True)
async def ping(ctx):
    t = await client.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.edit_message(t, new_content=':ping_pong: Pong! Actual ping: {}ms'.format(int(ms)))
    
@client.command()
async def meme():
         embed = discord.Embed(title="Take my meme!", color = 0xFFD700)
         embed.set_footer(text="Tip: If the image didnt load try to use this command again! | Developer Nela | Bot version: 1.3")
         embed.set_image(url = random.choice([
             "https://www.reddit.com/r/dankmemes/comments/9r9d4y/elonchan/",
             "https://cdn.discordapp.com/attachments/516388114550226944/518799301498109963/ocqc6cds8jf01.jpg",
             "https://cdn.discordapp.com/attachments/516388114550226944/518801762069774336/Screenshot_2018-08-01-15-45-12-586_com.google.android.youtube.jpg",
             "https://cdn.discordapp.com/attachments/516388114550226944/518801762069774337/IMG_20181017_152337.jpg",
             "https://cdn.discordapp.com/attachments/516388114550226944/518801762602319892/Screenshot_2018-06-16-14-17-03-445_com.google.android.youtube.png",
             "https://cdn.discordapp.com/attachments/516388114550226944/518801762602319893/Who_needs_FB_or_Twitter_Funny_Meme.jpg",
             "https://cdn.discordapp.com/attachments/516388114550226944/518801763134865409/stealth-mode-activated_o_1168408.png",
             "https://cdn.discordapp.com/attachments/516388114550226944/518801763655221249/Screenshot_2018-08-14-14-19-14-224_com.google.android.youtube.png"]))
         await client.say(embed=embed)
    
@client.command()
async def dyk():
         embed = discord.Embed(title="Did you know?", color = 0x00FFFF)
         embed.set_footer(text="Tip: If the image didnt load try to use this command again! | Developer Nela | Bot version: 1.3")
         embed.set_image(url = random.choice([
             "https://cdn.discordapp.com/attachments/516388114550226944/518810156000215041/IMG_20181202_162609.jpg"]))
         await client.say(embed=embed)

@client.command()
async def update():
    embed = discord.Embed(title = "Update log!", color = 0xFFFF00)
    embed.set_footer(text="Update log | Made by: Nela! | v1.3")
    embed.add_field(name = "Bot prefix:", value = "(", inline=True)
    embed.add_field(name = "Updates:", value = """Added:
    Update log! :white_check_mark:
    ===================""", inline=False)
    embed.add_field(name = "Removed:", value=":x: Nothing has been removed. :x:",inline=False)
    await client.say(embed=embed)
   
   
            
client.run(os.getenv("BOT_TOKEN"))
