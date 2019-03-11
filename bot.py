import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Üdv a Fotkyosképzőben! :smile_cat: ')
    print('Sent message to ' + member.name)


@client.event
async def on_message(message):
    if message.content == '!kor':
        await client.send_message(message.channel,'Ki találjam <@%s>, hogy hány éves vagy? (!igen vagy !nem)'  %(message.author.id))
    if message.content == '!igen':
        await client.send_message(message.channel,'Oks. Kezdjük!')
        from time import sleep
        sleep (1)
        await client.send_message(message.channel,'Gondolj a korodra!')
        from time import sleep
        sleep (4)
        await client.send_message(message.channel,'Adj hozzá tizet :nerd: ')
        from time import sleep
        sleep (4)
        await client.send_message(message.channel,'Adj hozzá ötöt! :nerd: ')
        from time import sleep
        sleep (4)
        await client.send_message(message.channel,'Vonj ki belőle hatot! :nerd:')
        from time import sleep
        sleep (4)
        await client.send_message(message.channel,'Mennyi jött ki? ')
        from time import sleep
        sleep (2)
        await client.send_message(message.channel,'Jah tényleg! Én nem tudom felismerni a számot amit írtál...')
        from time import sleep
        sleep (1)
        await client.send_message(message.channel,'Mert a programozóm még mindig egy lőcs...')
        from time import sleep
        sleep (1)
        await client.send_message(message.channel,'Akkor leegyszerűsítem!')
        from time import sleep
        sleep (1)
        await client.send_message(message.channel,'Vonj ki a számodból kilencet...')
        from time import sleep
        sleep (2)
        await client.send_message(message.channel,'És TÁDÁÁÁÁÁÁÁÁÁÁÁM')




    if message.content == '!kivagyok':
        await client.send_message(message.channel,'<@%s>'  %(message.author.id))

    if message.content == '!ping':
        await client.send_message(message.channel,'pong')

    if message.content == '!meghivo':
            await client.send_message(message.channel,'https://discord.gg/3xjKTt3 :money_mouth: ')

    if message.content == '!tejfog':
        await client.send_message(message.channel,'Hol jártál, báránykám?')
        await client.send_message(message.channel,'Zöld erdőben, asszonykám.')
        from time import sleep
        sleep (2)
        await client.send_message(message.channel,'Mit ettél, báránykám?')
        await client.send_message(message.channel,'Édes füvet, asszonykám.')
        from time import sleep
        sleep (2)
        await client.send_message(message.channel,'Mit ittál, báránykám?')
        await client.send_message(message.channel,'Forrásvizet, asszonykám.')
        from time import sleep
        sleep (2)
        await client.send_message(message.channel,'Ki vert meg báránykám?')
        await client.send_message(message.channel,'Szomszéd legény asszonykám.')
        from time import sleep
        sleep (2)
        await client.send_message(message.channel,'Mivel vert báránykám?')
        await client.send_message(message.channel,'Fütykösbottal asszonykám.')
        from time import sleep
        sleep (2)
        await client.send_message(message.channel,'Sírtál-e báránykám?')
        await client.send_message(message.channel,'Sírtam biz én asszonykám.')
        from time import sleep
        sleep (2)
        await client.send_message(message.channel,'Hogy sírtál báránykám?')
        await client.send_message(message.channel,'Ehem-behem asszonykám.')
        from time import sleep
        sleep (4)
        await client.send_message(message.channel,'Bocsi, hogy akadozva töltöttem be, csak a programozóm egy FOTYKOS! <@%s>'  %(message.author.id))

    if message.content == '!mentem':
        await client.send_message(message.channel,'Szia, <@%s>! Remélem még látni foglak! '  %(message.author.id))

    if message.content == '!help':
        await client.send_message(message.channel,'Parancsok: !ping !img !igenvagynem !hello !mentem !hogyvagy !meghivo !cat !MAMA')

    if message.content == '!givmiarp':
        await client.send_message(message.channel,'Rendeltem egy gamert... de csak egy fejhallgató jött! :disappointed_relieved: ')

    if message.content == '!barni':
        await client.send_message(message.channel,'Indiai Barbi?!')

    if message.content == '!david':
        await client.send_message(message.channel,'A szerveren csak Davee!! :sunglasses: ')

    if message.content == '!MAMA':
        await client.send_message(message.channel,'https://open.spotify.com/track/3z8h0TU7ReDPLIbEnYhWZb?si=xBbmiw_lQGyvaOPwhcNoWA')

    if message.content == '!lotti':
        await client.send_message(message.channel,'Mostantól Ázsiai Lola :yum: ')

    if message.content == '!combi':
        await client.send_message(message.channel,'Khm.. Mármint Kínai Hurka? :joy: ')

    if message.content.startswith('!hogyvagy'):
        randomlist = ["Éppen szolgálatban vagyok! Nem érek rá csevegni... :confused: "," Köszi jól! :heart: És te? "]
        await client.send_message(message.channel,(random.choice(randomlist)))

    if message.content == '!img':
        em = discord.Embed(description='PUTÁMÁDRE')
        em.set_image(url='https://cdn.discordapp.com/attachments/551711327857410090/553507268901994496/IMG_20190308_100512_384.jpg')
        await client.send_message(message.channel, embed=em)

    if message.content.startswith('!hello'):
        await client.send_message(message.channel,'Hello, <@%s>'  %(message.author.id))

    if message.content.startswith('!igenvagynem'):
        randomlist = ["igen","nem"]
        await client.send_message(message.channel,(random.choice(randomlist)))

    if message.content == '!cat':
        em = discord.Embed(description='')
        em.set_image(url='https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif')
        await client.send_message(message.channel, embed=em)

client.run('NEMTOMMIT')
