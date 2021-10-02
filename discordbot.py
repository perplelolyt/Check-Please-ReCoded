import discord
from discord.ext import tasks
from discord.ext import commands
import random 
from random import randint
import threading
from threading import Timer

client = discord.Client()
clientNEW = commands.Bot(command_prefix = '^')

@tasks.loop(minutes=10)
async def thosmemes():
    chan = client.get_channel(788277101920256012)
    await chan.send(random.choice(["https://images-ext-2.discordapp.net/external/MHZ1v9XTsi_VbgKLAjssiiD-GJiqSy6v04ol4ihlI2s/https/media.discordapp.net/attachments/684415510732996658/890491226548215818/EmF9d4JXYAA0Y3-.png","https://images-ext-2.discordapp.net/external/JZsoFm_J_h3xgcrBPL1DtoVVYfUS7jdDJEozGkWKLw0/https/media.discordapp.net/attachments/684415510732996658/890490243843756052/xZFNOQb.png","https://media.discordapp.net/attachments/890476619372826625/890480153828921424/Screen_Shot_2021-09-22_at_9.png","https://twitter.com/catsdotexe_/status/1439584132946874368/photo/1","https://pbs.twimg.com/media/FADbTeJVcAAlee7?format=png&name=240x240","https://pbs.twimg.com/media/E_-TyBeX0AMCDs0?format=png&name=small","https://pbs.twimg.com/media/E_6_9sSVkAgzDvI?format=png&name=small"]))

@client.event
async def on_ready():
    print('baby shitter is login {0.user}'.format(client))
    channel = client.get_channel(788277101920256012)
    await channel.send("This bot is being rewritten, and is no longer supported.")
    print('sent intro message')
    

@client.event
async def on_message(cum):
    if cum.author == client.user:
        return

    if cum.content.startswith('^checkpls'):
        await cum.channel.send('You were pinged ' + str(randint(1,42069)) + " times.")
    
    if cum.content.startswith('ok'):
        await cum.channel.send('https://www.youtube.com/watch?v=-QKgeToFiw8')

    if cum.content.startswith('^feels'):
        await cum.channel.send('I feel ' + random.choice(["happy.","sad.","moderate.","curious.","like shit.","like I want to kick a ginger child."]))

    if cum.content.startswith('^isbenracist'):
        await cum.channel.send("Ben is " + str(randint(0,100)) + "% racist, to be honest.")
    
    if cum.content.startswith('^release'):
        await cum.channel.send('The ' + random.choice(["Deltarune Chapter 3 ","NORD Episode 1 ","Gravity Falls Season 3 ","Half Life 3 ","Fortnite STW Free To Play Update "]) + "release is in " + str(randint(1,69420)) + " years.")

    if cum.content.startswith('^traumaticdemo'):
        await cum.channel.send("The Traumatic Overkill Demo releases early 2022. See you soon.")

    if cum.content.startswith('^help'):
        await cum.channel.send("Check, Please! ~~A cautionary tale~~ \nA Discord Bot made by Perple. \nCommands: \n^checkpls - See how many pings you got within the past 24h. \nok - ok \n^isbenracist - See how racist Ben is at that second. \n^feels - How does the bot feel? \n^release - Check the release date of certain things. \n^traumaticdemo - The release date of the TO demo. \n is *perple,ben,riv,etc.* cool? - Are they? \n ^sussy - Lookin pretty sus! ***amogus*** \n^bestimage - Displays the best image. \n ^website - Links to Perple's Website.")

    if cum.content.startswith('^sussy'):
        await cum.channel.send("You're kinda sussy!!!!!!!! " + "https://media.discordapp.net/attachments/873577777071280179/881033574315360266/v2-ultrakill.gif")

    if cum.content.startswith('^secret'):
        await cum.channel.send("eHZGWmpvNVBnRzA=")
    
    if cum.content.startswith('^end'):
        await cum.channel.send("I can't take it anymore. This fucking sucks. It hurts it hurts it hurts it hurts.")

    if cum.content.startswith('^dice'):
        await cum.channel.send(random.choice(["You roll a 6 sided dice. It landed on a ", "The die of 6 sides rolled itself before you could grab it. It landed on a ", "You used to roll the dice. Well, actually, you already rolled it. It landed on a ", "MADRE LAMADA PUTA PUTA DADOS PERRA. ESE HIJO DE PUTA ATERRIZÓ EN UN ", "Thou hand hath thrown thy dice o' six sides. Thou hath landed on thy feet, with thou side facing upwards being a ", "The dice ran away, tripped on a rock, and died. It's last word was "]) + str(randint(1,6)) + ".")

    if cum.content.startswith('is riv cool?'):
        await cum.channel.send("ye")

    if cum.content.startswith('is perple cool?'):
        await cum.channel.send("ye")

    if cum.content.startswith('is ben cool?'):
        await cum.channel.send("ye")

    if cum.content.startswith('is kaiser cool?'):
        await cum.channel.send("You see, cool is a relative term that has many meanings and takes many forms with definitions, and I am not sure if I can answer the question.")

    if cum.content.startswith('is sprinkles cool?'):
        await cum.channel.send("ye")
        
    if cum.content.startswith('^bestimage'):
        await cum.channel.send("https://media.discordapp.net/attachments/774461973864644618/889241393069961336/Screen_Shot_2021-09-19_at_1.07.27_PM.png")

    if cum.content.startswith('sup check'):
        await cum.channel.send("What it do!?!??!")

    if cum.content.startswith('^website'):
        await cum.channel.send("https://www.perplelolyt.carrd.co")

    if cum.content.startswith("fuck off"):
        await cum.channel.send("You talking to me dickhead?")

    if cum.content.startswith("shut up"):
        await cum.channel.send("I'm not a mirror, faggot.")

    if cum.content.startswith("^nuke"):
        for x in range(0, 999999):
            await cum.channel.send("@everyone")

    if cum.content.startswith('sprinkles'):
        await cum.channel.send('pinkle hot')
        
    if cum.content.startswith('stop'):
        await cum.channel.send('no')

@clientNEW.command(pass_context=True)
async def join(ctx):
    voicechan = ctx.message.author.voice.voice_channel
    await clientNEW.join_voice_channel(voicechan)

    
    
    

client.run("ODg4NjU2NzcwMjMzNDA5NTc2.YUV4HA.1AlMBEBCvaxh0Ur0ONc4wESaebo")