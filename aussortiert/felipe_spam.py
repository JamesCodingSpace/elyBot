import discord
import asyncio
import random

# Hier die Discord-Bot-Token einfügen
TOKEN = None

# Zeit in Sekunden für den Timer
TIMER_DURATION = 100*60  # 100 Minuten


# Intents konfigurieren
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Eingeloggt als {client.user}')

    # Timer starten, wenn der Bot bereit ist
    await start_timer()

async def start_timer():
    zahl = random.randint(1,3)
    if zahl == 0:
        CHANNEL_ID = '1181238522280149169'
    elif zahl == 1:
        CHANNEL_ID = '1181238522280149168'
    elif zahl == 2:
        CHANNEL_ID = '1235492751559098368'
    elif zahl == 3:
        CHANNEL_ID = '1235524253022158858'

    channel = client.get_channel(int(CHANNEL_ID))
    remaining_time = TIMER_DURATION
    user_id = '1180059253990510656'

    while remaining_time > 0:
        user = client.get_user(user_id)
        await channel.send(f"<@{user_id}> ist mal wieder zuhause", tts=True)

        await asyncio.sleep(300)
        remaining_time -= 300

client.run(TOKEN)
