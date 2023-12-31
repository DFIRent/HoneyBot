import discord
from discord.ext import commands
import random
import datetime

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Prefix: #"))
    print(f"Login Success: {bot.user.name}")

@bot.event
async def on_command(ctx):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = str(ctx.author)
    command = str(ctx.command)
    print(f"[{timestamp}] {user} used command: {command}")

@bot.remove_command('help') # removes default help
@bot.command(name='help')
async def help(ctx):
    await ctx.send("Create a ticket for help from staff!")

# Fake random error messages
error_messages = [
    "Oops, something went wrong!",
    "Error 404: Command not found.",
    "I'm not sure what you're asking for.",
    "Please try again later."
]
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = str(ctx.author)
        message = ctx.message.content

        print(f"[{timestamp}] {user} tried to use an unknown command: {message}")

        await ctx.send(random.choice(error_messages))
    else:
        print(f"Error: {error}")

bot.run('token')