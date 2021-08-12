import discord
import os
import random
import requests
import aiohttp
import json
import music

#from keep_alive import keep_alive
from discord.ext import commands
from dotenv import load_dotenv

client = commands.Bot(command_prefix='monke ')

#Monke Manual
monke_manual = ('\nMONKE BASIC COMMANDS:\n'
            '\n> monke manual: Ask bot to show commands!\n'
            '\n> monke greet: Ask bot to greet you!\n'
            '\n> monke kick: Ask bot to kick someone form the server\n'
            '\n> monke ban: Ask bot to ban someone form the sever\n'
            '\n> monke quote: Ask bot for a quote!!\n'
            '\nMONKE MEME COMMANDS:\n'
            '\n> monke meme: When you are itching for a good laugh!\n'
            '\n> monke holup: When you are itching for a spicy hol!\n'
            '\n> monke wholesome: Medicine for your spirit!\n'
            '\n> monke tumblr: When you need tumblr crazyness!\n'
            '\nMONKE NSFW COMMANDS:\n'
            '\n> monke hentai: nani!\n'
            '\nMONKE MUSIC COMMANDS:\n'
            '\n> monke join: Ask bot to join voice channel!\n'
            '\n> monke play: Ask bot to play music!\n'
            '\n> monke pause: Ask bot to pause music!\n'
            '\n> monke resume: Ask bot to resume music!\n'
            '\n> monke disconnect: Ask bot to disconnect!\n'
            '\nMONKE GAME COMMANDS:\n'
            '\n> monke tictactoe: Play tictactoe with your friend!\n'
)

#Monke Music
cogs = [music]
for i in range(len(cogs)):
    cogs[i].setup(client)

#Monke Manual
@client.command(name='manual')
async def manual(ctx):
    manual_embed = discord.Embed(
        title="Monke  Manual",
        description=monke_manual,
        color=discord.Color.green()
    )
    manual_embed.add_field(name='Version Code:', value='v1.0.4', inline=False)
    manual_embed.set_footer(text='Author: Aayush Shrestha')
    manual_embed.set_author(name="Monke")
    await ctx.message.channel.send(embed=manual_embed)

#Monke Greet
greetings = ['Hello!', 'Bonjour!', 'Hi!']
@client.command(name='greet')
async def greet(ctx):
    await ctx.send(random.choice(greetings))

#Monke Kick
@client.command(name='kick')
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason=reason)

#Monke Ban
@client.command(name='ban')
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason=reason)

#Monke Meme
@client.command(name='meme')
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
@client.command(name='holup')
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
@client.command(name='wholesome')
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
@client.command(name='tumblr')
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
@client.command(name='quote')
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
@client.command(name='hentai')
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

#Monke Game
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command(name='tictactoe')
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
            await ctx.send("Enter 'monke place <position integer>'")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
            await ctx.send("Enter 'monke place <position integer>'")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command(name='place')
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


#Monke Ready
@client.event 
async def on_ready():
    print("Monke Bot is Ready!")

#Monke check
@client.event
async def on_message(message):
    if message.author == client.user:
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

    await client.process_commands(message)

#keep_alive()
load_dotenv()
#my_secret = os.environ['TOKEN']
client.run(os.getenv('TOKEN'))