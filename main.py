import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_iklim1_image_url():
    url = 'http://127.0.0.1:4000/'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_iklim2_image_url():
    url = 'http://127.0.0.1:5000/'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('iklim1')
async def iklim1(ctx):
    '''The duck command returns the photo of the duck'''
    print('hello')
    image_url = get_iklim1_image_url()
    await ctx.send(image_url)

@bot.command('iklim2')
async def iklim2(ctx):
    '''The duck command returns the photo of the duck'''
    print('hello')
    image_url = get_iklim2_image_url()
    await ctx.send(image_url)



@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Image '{file_name}' saved successfully.")
    else:
        await ctx.send("You forgot to upload the image :(")

        
bot.run("bot token")
