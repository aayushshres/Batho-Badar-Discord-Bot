import discord
import os
import json
import random
import aiohttp
import requests

#from keep_alive import keep_alive
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix='monke ')

sad_words = ['sad', 'depressed', 'unhappy', 'depressing']

bad_words = ['fuck', 'shit', 'bitch', 'dick', 'pussy', 'rascal', 'bastard', 'hore', 'hoe']

manual = ('MONKE COMMANDS:\n'
            '\n> monke manual: Ask bot to show commands!\n'
            '\n> monke greet: Ask bot to greet you!\n'
            '\n> monke inspire: When you need a little push!\n'
            '\n> monke meme: When you are itching for a good laugh!\n'
            '\n> monke hentai: Horny Bastard!\n'
            '\n> monke holup: When you are itching for a spicy hol!\n'
)

encouragements = ['Cheer up!', 'Hang in there!', "It's okay to not feel okay"]

greetings = ['Hello!', 'Bonjour!', 'Hi!']

#Quotes API
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@bot.event
async def on_ready():
    print("Monke Bot is Ready!")

#Monke check
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    msg = message.content.lower()

    #await message.send("Ping Pong! Batho Badar here!\nEnter 'monke manual' for Batho Badar's Manual")
#Monke check for sad words
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(encouragements))

#Monke check for bad words
    if any(word in msg for word in bad_words):
        await message.channel.send('Language!')

#Monke Greet
    if msg == ("monke greet"):
        await message.channel.send(random.choice(greetings))

#Monke Meme
    if message.content == ('monke meme'):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/memes.json") as r:
                memes = await r.json()
                embed = discord.Embed(
                    color = discord.Color.green()
                )
                embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
                embed.add_field(name="Powered by:", value="r/memes", inline = True)
                embed.set_footer(text="Bot developed by: Aayush Shrestha")
                await message.channel.send(embed=embed)

#Monke Hentai
    if message.content == ('monke hentai'):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/hentai.json") as r:
                hentai = await r.json()
                embed = discord.Embed(
                    color = discord.Color.green()
                )
                embed.set_image(url=hentai["data"]["children"][random.randint(0, 25)]["data"]["url"])
                embed.add_field(name="Powered by:", value="r/hentai", inline = True)
                embed.set_footer(text="Bot developed by: Aayush Shrestha")
                await message.channel.send(embed=embed)

#Monke HolUp
    if message.content == ('monke holup'):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://www.reddit.com/r/HolUp/.json") as r:
                HolUp = await r.json()
                embed = discord.Embed(
                    color = discord.Color.green()
                )
                embed.set_image(url=HolUp["data"]["children"][random.randint(0, 25)]["data"]["url"])
                embed.add_field(name="Powered by:", value="r/HolUp", inline = True)
                embed.set_footer(text="Bot developed by: Aayush Shrestha")
                await message.channel.send(embed=embed)

#Monke Inspire
    if message.content == ("monke inspire"):
        quote = get_quote()
        myEmbed = discord.Embed(
            title="Inspiration for you!",
            description=quote,
            color=discord.Color.green()
        )
        myEmbed.set_footer(text=':)')
        await message.channel.send(embed=myEmbed)

#Monke Manual
    if message.content == ('monke manual'):
        myEmbed = discord.Embed(
            title="Monke  Manual",
            description=manual,
            color=discord.Color.green()
        )
        myEmbed.add_field(name='Version Code:', value='v1.0.1', inline=False)
        myEmbed.set_footer(text='Author: Aayush Shrestha')
        myEmbed.set_author(name="Monke")
        await message.channel.send(embed=myEmbed)

#keep_alive()
load_dotenv()
#my_secret = os.environ['TOKEN']
bot.run(os.getenv('TOKEN'))