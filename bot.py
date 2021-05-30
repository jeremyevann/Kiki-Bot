import discord
from discord import emoji
from discord.ext import commands

client = commands.Bot(command_prefix=".")
client.remove_command("help")

f = open("menu.txt", "r")
m = f.readlines()   # menu
n = ["Cappucino", "Americano", "Espresso", "Caramel Machiatto", "Hazelnut Latte", "Chocolate Milk", "Hot Tea", "Lemon Tea", "Thai Tea", "Milkshake", "Affogato", "Gelato Hazelnut", "Salad", "Kentang Goreng", "Waffle", "Bagel", "Pancake", "Almond Croissant", "Seblak", "Bubur Ayam", "SOTO AYAM BU KARTI 👉😎👈"]
l = ["https://i.imgur.com/S8jYElZ.png", 
"https://i.imgur.com/t0kF8wm.png",
"https://i.imgur.com/OpVcbJH.png",
"https://i.imgur.com/N7MQUoB.png",
"https://i.imgur.com/rW9CZus.png",
"https://i.imgur.com/ffFvmou.png",
"https://i.imgur.com/g7JBE9l.png",
"https://i.imgur.com/zuc3QM3.png",
"https://i.imgur.com/iFTAiEl.png",
"https://i.imgur.com/2YHofQB.png",
"https://i.imgur.com/yTXt7wH.png",
"https://i.imgur.com/1YAi384.png",
"https://i.imgur.com/jtPNvXQ.png",
"https://i.imgur.com/D8ZP3uU.png",
"https://i.imgur.com/dol7z88.png",
"https://i.imgur.com/8ZVwOZL.png",
"https://i.imgur.com/2G4GgHF.png",
"https://i.imgur.com/eAG94aM.png",
"https://i.imgur.com/l3xdc16.png",
"https://i.imgur.com/UkGi1oY.png",
"https://i.imgur.com/RCQNVv0.png"]

@client.event
async def on_ready():
    print("Bot is ready")

@client.group(invoke_without_command = True)
async def help(ctx):
    embed = discord.Embed(title = "Help", description = 'Gunakan ".help <command>" untuk penjelasan lebih lanjut tentang commands yang ada pada Kiki Bot', color = discord.Color.red())
    embed.add_field(name = "Pesan makanan/minuman", value = "menu (aliases: m)\norder(aliases: o)")
    await ctx.send(embed = embed)

@help.command()
async def menu(ctx):
    embed = discord.Embed(title = "Menu", description = "Menampilkan menu makanan/minuman yang bisa dimasak oleh Kiki", color = discord.Color.orange())
    embed.add_field(name = "**Syntax**", value = ".menu")
    await ctx.send(embed = embed)

@help.command()
async def order(ctx):
    embed = discord.Embed(title = "Order", description = "Kiki akan menyiapkan makanan/minuman yang kalian order dari menu", color = discord.Color.green())
    embed.add_field(name = "**Syntax**", value = ".order [amount] [menu number]")
    await ctx.send(embed = embed)

@client.command(aliases=['m'])
async def menu(ctx):
    embed = discord.Embed(title = "Menu di Café de Jervan", color = discord.Color.orange())
    embed.add_field(name = "Minuman Enak", value = "1. Cappucino\n2. Americano\n3. Espresso\n4. Caramel Machiatto\n5. Hazelnut Latte\n6. Chocolate Milk\n7. Hot Tea\n8. Lemon Tea\n9. Thai Tea\n10. Milkshake\n11. Affogato", inline = False)
    embed.add_field(name = "Makanan Lezat", value = "12. Gelato Hazelnut\n13. Salad\n14. Kentang Goreng\n15. Waffle\n16. Bagel\n17. Pancake\n18. Almond Croissant\n19. Seblak\n20. Bubur Ayam\n21. SOTO AYAM BU KARTI 👉😎👈", inline = False)
    embed.set_footer(text = 'Order: ".order [amount] [menu number]"')
    await ctx.send(embed = embed)

@client.command(aliases=['o'])
async def order(ctx, amount = 1, *, number):
    j = str(amount)
    a = int(number)
    if 0 < a <= 11:
        embed = discord.Embed(title = "Minuman sudah diantar!", color = discord.Color.green())
        embed.add_field(name = j + " " + n[int(number)-1], value = "yang enak sudah ada di tangan kamu. Selamat menikmati! 😄", inline = False)
        embed.set_thumbnail(url = l[int(number)-1])
        await ctx.send(embed = embed)
    elif 12 <= a <= 20:
        embed = discord.Embed(title = "Makanan sudah diantar!", color = discord.Color.green())
        embed.add_field(name = j + " " + n[int(number)-1], value = "yang lezat sudah ada di tangan kamu. Selamat menikmati! 😄", inline = False)
        embed.set_thumbnail(url = l[int(number)-1])
        await ctx.send(embed = embed)
    elif a == 21:
        embed = discord.Embed(title = "Makanan sudah diantar!", color = discord.Color.green())
        embed.add_field(name = j + " " + n[int(number)-1], value = "yang rasany nak skali sudah ada di tangan kamu. Wis mangan ora udud! 🚬", inline = False)
        embed.set_thumbnail(url = l[int(number)-1])
        await ctx.send(embed = embed)
    else:
        await ctx.send("Maaf, Kiki belum bisa bikin itu. (>.<) \nKamu bisa request makanan favorit kamu di <#846598992996466708>, lalu nanti Kiki akan pelajari cara memasaknya yaah hyung.")

client.run("ODQ4MDY1MjU1Nzc0NzQ4Njky.YLHMUQ.jc3suGFtTYXb8SRInT52A0G27yI")