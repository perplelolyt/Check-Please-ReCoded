import discord
from discord.ext import commands, tasks
import random
import datetime as dt
from random import randint
import itertools
from itertools import cycle
import discord.utils
import os
import dotenv
from dotenv import load_dotenv

#load the .env
load_dotenv()

#making the bot and creating the prefix and shit
client = commands.Bot(command_prefix = '^')

#grabbing the token through the .env file (you'll need to make one)
TOKEN = os.getenv("TOKEN")

#setting up the status cycle
status = cycle(["with hot pizza rolls...", "with these balls!!!", "with a mind.","Minecraft Battle Royale", "ur mum lol", "Muck", "Terraria Battle Grounds", "shitnite", "Stick Fight: The Game", "THE XYLOBONES", "FL Studio", "wit p00s"])

#ready, join, and leave events
@client.event
async def on_ready():
    reload_status.start()
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('with hot pizza rolls...'))
    print("baby shitter is online")

@tasks.loop(seconds=10)
async def reload_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_member_join(member):
    print(f'{member} joined a server. Grab the popcorn.')

@client.event
async def on_member_remove(member):
    print(f'{member} went bye bye.')

#commands



#check please
@client.command(aliases=["checkplease","checkpls","chkplease"])
async def chkpls(bepis):
    await bepis.send('You were pinged a total of ' + str(randint(0,69420)) + " times in the past 24 hours.")
    print(f"the client's ping is {round(client.latency * 1000)}ms")

#eight ball
@client.command(aliases=["8ball","eightball","8bll"])
async def _8ball(ctx, *, question):
    Ballresponses = ["It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes definitely.",
        "Yes absolutely.",
        "Reply not certain, try again.",
        "Ask again later.",
        "Can’t really tell you now.",
        "Can’t predict that right now.",
        "I wouldn’t count on it.",
        "You’re outta luck.",
        "My sources say no.",
        "Yeah, uh…..no.",
        "Not a chance."]
    await ctx.send(f'{random.choice(Ballresponses)}')

#dice roll
@client.command(aliases=["6dice","roll"])
async def dice(bepis):
    await bepis.send(random.choice(["You roll a 6 sided dice. It landed on a ", "The die of 6 sides rolled itself before you could grab it. It landed on a ", "You used to roll the dice. Well, actually, you already rolled it. It landed on a ", "MADRE LAMADA PUTA PUTA DADOS PERRA. ESE HIJO DE PUTA ATERRIZÓ EN UN ", "Thou hand hath thrown thy dice o' six sides. Thou hath landed on thy feet, with thou side facing upwards being a ", "The dice ran away, tripped on a rock, and died. It's last word was ", "Couldn't get enough dice rolls from last client, eh? Well, good news, it landed on a "]) + str(randint(1,6)) + ".")

#commented because it was added to sprinkles' server

#emoji nuke
#@client.command()
#async def endmoji(bepis):
 #   for _ in itertools.repeat(None, 99999999999999999):
  #   await bepis.send(random.choice([":shit:",":zany_face:",":eggplant:",":money_with_wings:",":flag_de:",":hot_face:",":rofl:",":100:"]))

#bacon
@client.command(aliases=["thatveganteacher"])
async def vegan(bepis):
    await bepis.send(":pig: :axe: :bacon: :fork_and_knife:")

#erase
@client.command()
async def erase(bepis, amount=5):
    await bepis.channel.purge(limit=amount + 1)

#website
@client.command()
async def website(bepis):
    await bepis.send("https://perplelolyt.carrd.co")

#bestimage
@client.command()
async def bestimage(bepis):
    await bepis.send("https://cdn.discordapp.com/attachments/818147856480469042/892134716701032568/Screen_Shot_2021-09-27_at_12.44.37_PM.png")

#kick
@client.command()
async def kick(bepis, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await bepis.send(f"{member} just got kicked out the club.")

#ban
@client.command()
async def ban(bepis, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await bepis.send(f"{member} got themselves a BIG OL' concussion from the ban hammer.")

#pardon
@client.command()
async def pardon(bepis, *, member):
    banned_users = await bepis.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await bepis.guild.unban(user)
            await bepis.send(f'Pardoned {user.name}#{user.discriminator}. They are now free from the clutches of the ban hammer.')
            return


#traumaticdemo
@client.command()
async def traumaticdemo(bepis):
    await bepis.send("Lets get the job done. ***Together.***")

#stupid selfpromotion

#music
@client.command()
async def soundcloud(bepis):
    await bepis.send("https://soundcloud.com/perplelolyt/sorta-not-kinda")

#together
@client.command()
async def together(bepis):
    await bepis.send("https://cdn.discordapp.com/attachments/890476619372826625/891184728131108934/Untitled_3.png")

#updowndownup
@client.command()
async def updownupdownupdownbutterhotdogyes(bepis):
    await bepis.send("nein")

#october31
@client.command()
async def halloween(bepis):
    await bepis.send("Aphrodite was the goddess of love, sex, and beauty. Unsurprisingly for a love goddess, she was said to have emerged from the foam generated when the severed testicles of her father, Uranus, were thrown into the sea by his son, the Titan Cronus. (Or is that surprising?) Kind of makes clientticelli’s surreally lovely Birth of Venus—which depicts Aphrodite’s Roman counterpart emerging from the waves—a little more visceral, doesn’t it?")

#help
@client.command()
async def cmds(bepis):
    await bepis.send("Check, Please! Re-Coded is a client made by Perple.\n*Damn right it is.*\nCommands:\n^cmds: Shows this page.\n^chkpls: Shows you how many pings you got in the last 24 hours.\n^8ball: Ask a question to the magic 8ball and see if it will happen!\n^dice: Roll a basic, 6 sided dice.\n^music: Listen to Perple's music.\n^traumaticdemo: You're doing fine.\n^kick/^ban/^pardon: Kicks, bans, and unbans respectively.\n^erase: Purge a certain amount of messages (default is 5).\n^website: Link to Perple's website.\n^bestimage: Shows the best image ever.\n^vegan/^thatvganteacher: My favorite activity.\nSource code will be released at a later time.")

#meaning
@client.command()
async def whats_the_meaning_of_life(bepis):
    await bepis.send("dread.")

client.run(TOKEN)