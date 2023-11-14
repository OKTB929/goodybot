import discord
from discord.ext import commands 
intents = discord.Intents.default()
intents.message_content = True
intents.presences=True
intents.members=True

TOKEN ='DISCORD_TOKEN'

bot = commands.Bot(command_prefix='!', activity = discord.Activity(type=discord.ActivityType.watching, name="Pornhub Kids"), intents=intents)



@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send(f'Hey {message.author.mention}, you called?')
    

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel is not None:
        await channel.send(f'Welcome {member.mention} to {member.guild.name}!')
    else:
        print('No "general" channel found.')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel is not None:
        await channel.send(f'Goodbye {member.mention}, you will be missed')
    else:
        print('No general channel found')
@bot.command(name="Ping", description="ping command")
async def ping(ctx):
    await ctx.send("Pong")

@bot.command(name="hello", description="greets")
async def hello (ctx):
    await ctx.send(f'Hello,{ctx.message.author.mention},how are you?')

@bot.command(name="add", description="adds two numbers")
async def add(ctx, num1 : float ,num2 : float):
    await ctx.send(f'{ctx.message.author.mention} The sum of {num1}+{num2} is equal to {num1+num2}.')

@bot.command(name="subtract", description="Subtracts two numbers")
async def subtract(ctx, num1: float, num2: float):
    await ctx.send(f'{ctx.message.author.mention} The sum of {num1}-{num2} is equal to {num1-num2}.')

@bot.command(name="multiply", description="multiplies two numbers")
async def multiply(ctx, num1: float, num2: float):
    await ctx.send(f'{ctx.message.author.mention} The product of {num1}x{num2} is equal to {num1*num2}.')

@bot.command(name="divide", description="Divides two numbers")
async def divide(ctx, num1: float, num2: float):
    await ctx.send(f'{ctx.message.author.mention} The division of {num1}/{num2} is equal to {num1/num2}.')

@bot.command(name="power", description="takes a power of a number")
async def power(ctx, base: float, exponent: float):
    await ctx.send(f'{ctx.message.author.mention} {base} to the power of {exponent} is equal to {base**exponent}')

@bot.command(name="root", description="finds the nth root of a number")
async def root(ctx, number: float, root: float):
    if number >= 0:
        result = number**(1/root)
        await ctx.send(f'{ctx.message.author.mention} The {root}th root of {number} is equal to {result:.2f}')
    else:
        await ctx.send(f'{ctx.message.author.mention} Invalid input! The root of a negative number cannot be real.')


bot.run(TOKEN)