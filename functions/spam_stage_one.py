import discord
import asyncio
import sys

sys.path.append("./functions")
sys.path.append("./settings")
sys.path.append("./BotMedien")

from get_token import get_token
from setting_functions import get_channel_id, get_duration, get_spam_user_id

TOKEN = get_token()
CHANNEL_ID = get_channel_id("channel_felipe_spam:")
TIMER_DURATION = 60 * get_duration("duration_felipe_spam:")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await start_timer()

async def start_timer():
    channel = client.get_channel(int(CHANNEL_ID))
    remaining_time = TIMER_DURATION
    user_id = get_spam_user_id("spam_user_id:")

    while remaining_time > 0:
        await channel.send(f"<@{user_id}> ist mal wieder zuhause", tts=True)
        await asyncio.sleep(300)
        remaining_time -= 300

client.run(TOKEN)
