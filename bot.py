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







client = commands.Bot(command_prefix = '/')


@client.event
async def on_ready():
    print("The bot is online and connected with Discord!")


client.run(os.getenv("BOT_TOKEN"))
