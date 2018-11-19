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

@client.command
async def help():
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name= "Help Commanda")
    embed.add_field(name = 'BASIC', value = ' ',inline = False)
    embed.add_field(name = '(noncoder', value = 'Makes you a Non Coder (You cant use Verify then.)',inline = False)
    embed.add_field(name = '(verify', value = 'Makes you coding newbie. (you cant use this when you used ``(noncoder)``)',inline = False)
    embed.add_field(name = '(modmail', value = 'Writes something to the mod logs. If abused that command. you will be muted.',inline = False)
    embed.add_field(name = '(suggest', value = 'Writes a suggestion in a Suggestions channel.',inline = False)
    embed.add_field(name = 'MODERATION', value = ' ',inline = False)
    embed.add_field(name = '(mute', value = 'Mutes a user! Usage: (mute @user',inline = False)
    embed.add_field(name = '(mmod', value = 'Makes mod. For admin only! Ysage: (mmod @user',inline = False)
    embed.add_field(name = '(dmod', value = 'Removes mod! Usage: (dmod @user. For admins only!',inlind = False)
    embed.add_field(name = '(madmin', value = ' Makes a user admin! Usage: (madmin @user. Head of coding only!',inline = False)
                    
    embed.add_field(name = '(dadmin', value = ' Removes a admin. Usage: (dadmin @user. Head of coding only!',inline = False)
    
    embed.add_field(name = '(mute', value = 'Mutes a user. Uasge: (mute @user.',inline = False)
    embed.add_field(name = '(unmute', value = 'Unmutes a user. Usage: (unmute @user.',inline = False)
    embed.add_field(name = '(warn', value = 'Warns a user. Uasage: (warn @user.',inline = False)
    await client.send_message(embed=embed)
    
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

@client.command(pass_context=True)
async def noncoder(ctx):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='NON BOT CODER')
    await client.add_roles(ctx.message.author, role)
    
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

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)

async def warn(ctx, userName: discord.User, *, message:str):
        await client.send_message(userName, "You have been warned for: {}".format(message)) 
        await client.say("warning {0} Has Been Warned! Warning Reason : {1} ".format(userName,message))
        pass
    

@client.command(pass_context=True)
async def modmail(ctx, *, msg=None):
    channel = discord.utils.get(client.get_all_channels(), name='logs-1')
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


    channel = discord.utils.get(client.get_all_channels(), name='suggestions')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    color = discord.Color((r << 16) + (g << 8) + b)
    if not msg:
        await client.say("Please specify a message to send")
    else:
        await client.send_message(channel, embed=discord.Embed(color=color, description=msg + '\n Message From-' + ctx.message.author.id))
        await client.delete_message(ctx.message)
    return

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


client.run(os.getenv("BOT_TOKEN"))
