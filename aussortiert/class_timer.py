import discord
import asyncio
import random
from get_token import get_token
from setting_functions import get_channel_id, get_duration

TOKEN = get_token()
CHANNEL_ID = get_channel_id()
TIMER_DURATION = 60 * get_duration()

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Eingeloggt als {client.user}')

    await start_timer()

async def start_timer():
    channel = client.get_channel(int(CHANNEL_ID))
    remaining_time = TIMER_DURATION

    while remaining_time > 0:
        rndm_spruch = random.randint(1,4)

        if rndm_spruch == 1:
            await channel.send("Ely ist so toll! Danke dass du uns nicht wegen deinem Bild verklagst")

        hours = remaining_time // 3600
        minutes = (remaining_time % 3600) // 60
        percent = 100 - ((remaining_time / (195*60)) * 100)
        percent_formatted = "{:.2f}".format(percent)
        percent_event = int(percent)
        if hours > 1:
            str_stunde = "Stunden und"
        elif hours == 1:
            str_stunde = "Stunde und"
        elif hours == 0:
            hours = ""
            str_stunde = ""

        if  minutes > 1:
            str_minute = "Minuten"  
        elif minutes == 1:
            str_minute = "Minute"

        await channel.send(f'**Verbleibende Zeit: {hours} {str_stunde} {minutes} {str_minute}. Das heißt wir haben {percent_formatted}% geschafft! Ein YaY in den Chat!**')

        if percent_event == 75:
            await channel.send("3/4 To Go!")
            await channel.send(file=discord.File("C:/Users/jamie/Documents/DHBW/BotMedien/this-is-fine-fire.mp4"))
        elif percent_event == 50:
            await channel.send("Wir sind über 50% der Zeit!")
            await channel.send(file=discord.File("C:/Users/jamie/Documents/DHBW/BotMedien/despicable-me-gru.mp4"))
        elif percent_event == 25:
            await channel.send("Nur noch 25% der Zeit übrig!")
            await channel.send(file=discord.File("C:/Users/jamie/Documents/DHBW/BotMedien/its-only-the-beginning-buddy.mp4"))

        await asyncio.sleep(60)
        remaining_time -= 60

    await channel.send('**Die Stunde ist endlisch vorbei! Wir haben es geschafft Leute!**')
    await channel.send(file=discord.File("C:/Users/jamie/Documents/DHBW/BotMedien/done-so-done.mp4"))

client.run(TOKEN)
