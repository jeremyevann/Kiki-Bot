import discord
from discord import emoji
from discord.ext import commands

client = commands.Bot(command_prefix=".")

f = open("menu.txt", "r")
m = f.readlines()   # menu
n = ["Cappucino", "Americano", "Espresso", "Caramel Machiatto", "Hazelnut Latte", "Chocolate Milk", "Hot Tea", "Lemon Tea", "Thai Tea", "Milkshake"]
l = ["https://i.imgur.com/S8jYElZ.png", 
"https://i.imgur.com/t0kF8wm.png",
"https://i.imgur.com/OpVcbJH.png",
"https://i.imgur.com/N7MQUoB.png",
"https://i.imgur.com/rW9CZus.png",
"https://i.imgur.com/ffFvmou.png",
"https://i.imgur.com/g7JBE9l.png",
"https://i.imgur.com/zuc3QM3.png",
"https://i.imgur.com/iFTAiEl.png",
"https://i.imgur.com/2YHofQB.png"]

@client.event
async def on_ready():
    print("Bot is ready")

@client.command(aliases=['m'])
async def menu(ctx):
    embed = discord.Embed(title = "Menu di Café de Jervan", color = discord.Color.orange())
    for menu in m:
        embed.add_field(name = "\u200b", value = menu, inline = True)
    embed.set_footer(text = 'Order: ".order [menu number]"')
    await ctx.send(embed = embed)

@client.command(aliases=['o'])
async def order(ctx, *, number):
    embed = discord.Embed(title = "Food delivered!", color = discord.Color.green())
    embed.add_field(name = n[int(number)-1], value = "has been delivered to you. Enjoy your drink! 😄", inline = False)
    embed.set_thumbnail(url = l[int(number)-1])
    await ctx.send(embed = embed)

client.run("ODQ4MDY1MjU1Nzc0NzQ4Njky.YLHMUQ.QCVnd-dsnw816C3GoCLQs7SNq4Y")