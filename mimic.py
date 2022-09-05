from email import message
import discord
from discord.ext import commands

intents=discord.Intents.all()


prefix = '!'
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.event
async def on_ready():
    print("Bora pro abate! ")


@bot.command(name='hello')
async def msg(ctx):
    if ctx.author == bot.user:
        return
    else:
        re = "Eae gay"
        await ctx.send(re)

@bot.command(name= 'kv')
async def kv(ctx):
    re = ctx.author.name
    await ctx.send(f'Olá {re}, sabia que o Kelvin mama no sigilo ?')

@bot.command(name='menspv',)
async def msg(message):
    i=0
    while i < 10:   
        await message.author.send('Olá bela moça vem sempre aqui?')
        i+=1

@bot.command(name='kk')
async def a(ctx, message):
    a = message.content
    await message.chanel.send(a)



bot.run("MTAxNDI0MzI4NzYwMDczNDIzOA.GDtcnP.7Cul4iAoO_bAIscuoA2I5QY_5WULY5azaAWOXg") 