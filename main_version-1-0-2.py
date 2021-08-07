import discord
import os
import random
import requests
import aiohttp
import json

#from keep_alive import keep_alive
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='monke ')

#Monke Manual
monke_manual = ('MONKE COMMANDS:\n'
            '\n> monke manual: Ask bot to show commands!\n'
            '\n> monke greet: Ask bot to greet you!\n'
            '\n> monke kick: Ask bot to kick someone form the server\n'
            '\n> monke ban: Ask bot to ban someone form the sever\n'
            '\n> monke quote: Ask bot for a quote!!\n'
            '\n> monke meme: When you are itching for a good laugh!\n'
            '\n> monke holup: When you are itching for a spicy hol!\n'
            '\n> monke wholesome: Medicine for your spirit!\n'
            '\n> monke tumblr: When you need tumblr crazyness!\n'
            '\n> monke hentai: nani!\n'
)

#Monke Manual
@bot.command(name='manual')
async def manual(ctx):
    manual_embed = discord.Embed(
        title="Monke  Manual",
        description=monke_manual,
        color=discord.Color.green()
    )
    manual_embed.add_field(name='Version Code:', value='v1.0.2', inline=False)
    manual_embed.set_footer(text='Author: Aayush Shrestha')
    manual_embed.set_author(name="Monke")
    await ctx.message.channel.send(embed=manual_embed)

#Monke Greet
greetings = ['Hello!', 'Bonjour!', 'Hi!']
@bot.command(name='greet')
async def greet(ctx):
    await ctx.send(random.choice(greetings))

#Monke Kick
@bot.command(name='kick')
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason=reason)

#Monke Ban
@bot.command(name='ban')
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason=reason)

#Monke Meme
@bot.command(name='meme')
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/memes.json") as r:
            memes = await r.json()
            memes_embed = discord.Embed(
                color = discord.Color.green()
            )
            memes_embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
            memes_embed.add_field(name="Powered by:", value="r/memes", inline = True)
            memes_embed.set_footer(text=f"Bot developed by Aayush Shrestha | Requested by {ctx.author}")
            await ctx.message.channel.send(embed=memes_embed)

#Monke Holup
@bot.command(name='holup')
async def holup(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/HolUp.json") as r:
            HolUp = await r.json()
            holup_embed = discord.Embed(
                color = discord.Color.green()
            )
            holup_embed.set_image(url=HolUp["data"]["children"][random.randint(0, 25)]["data"]["url"])
            holup_embed.add_field(name="Powered by:", value="r/HolUp", inline = True)
            holup_embed.set_footer(text=f"Bot developed by Aayush Shrestha | Requested by {ctx.author}")
            await ctx.message.channel.send(embed=holup_embed)

#Monke Wholesome memes
@bot.command(name='wholesome')
async def wholesome(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/wholesomememes.json") as r:
            wholeSome = await r.json()
            wholesome_embed = discord.Embed(
                color = discord.Color.green()
            )
            wholesome_embed.set_image(url=wholeSome["data"]["children"][random.randint(0, 25)]["data"]["url"])
            wholesome_embed.add_field(name="Powered by:", value="r/wholesomememes", inline=True)
            wholesome_embed.set_footer(text=f"Bot develped by Aayush Shrestha | Requested by {ctx.author}")
            await ctx.message.channel.send(embed=wholesome_embed)

#Monke Tumblr
@bot.command(name='tumblr')
async def tumblr(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/tumblr.json") as r:
            Tumblr = await r.json()
            tumblr_embed = discord.Embed(
              color = discord.Color.green()
            )
            tumblr_embed.set_image(url=Tumblr["data"]["children"][random.randint(0, 25)]["data"]["url"])
            tumblr_embed.add_field(name="Powered by:", value="r/tumblr", inline=True)
            tumblr_embed.set_footer(text=f"Bot developed by Aayush Shrestha | Requested by {ctx.author}")
            await ctx.message.channel.send(embed=tumblr_embed)

#Monke Quote
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)
@bot.command(name='quote')
async def quote(ctx):
    quote = get_quote()
    quote_embed = discord.Embed(
      title="Quote for you!",
      description=quote,
      color=discord.Color.green()
    )
    quote_embed.set_footer(text=':)')
    await ctx.message.channel.send(embed=quote_embed)

#Monke Hentai
@bot.command(name='hentai')
async def hentai(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/hentai.json") as r:
            Hentai = await r.json()
            hentai_embed = discord.Embed(
                color = discord.Color.green()
            )
            hentai_embed.set_image(url=Hentai["data"]["children"][random.randint(0, 25)]["data"]["url"])
            hentai_embed.add_field(name="Powered by:", value="r/tumblr", inline=True)
            hentai_embed.set_footer(text=f"Bot developed by Aayush Shrestha | Requested by {ctx.author}")
            await ctx.message.channel.send(embed=hentai_embed)


#Monke Ready
@bot.event 
async def on_ready():
    print("Monke Bot is Ready!")

#Monke check
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    msg = message.content.lower()

#Monke check for sad words
    sad_words = ['sad', 'depressed', 'unhappy', 'depressing']
    encouragements = ['Cheer up!', 'Hang in there!', "It's okay to not feel okay"]
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(encouragements))

#Monke check for bad words
    bad_words = ['fuck', 'shit', 'bitch', 'dick', 'pussy', 'rascal', 'bastard', 'hore', 'hoe']
    if any(word in msg for word in bad_words):
        await message.channel.send('Language!')

    await bot.process_commands(message)

#keep_alive()
load_dotenv()
#my_secret = os.environ['TOKEN']
bot.run(os.getenv('TOKEN'))