import discord
import asyncio

# Hier die Discord-Bot-Token einfügen
TOKEN = None

# Hier die Kanal-ID einfügen, in dem der Bot die Nachricht senden soll
CHANNEL_ID = '1235524253022158858'

# Hier die Rollen-ID einfügen, die den Timeout repräsentiert
TIMEOUT_ROLE_ID = '1237038309675503697'

# Zeit in Sekunden für den Timeout
TIMEOUT_DURATION = 20  # in sek

# Intents konfigurieren
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Eingeloggt als {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('!testout'):
        print("works")
        # Nachricht vom Bot löschen
        await message.delete()

        # Benutzer, der den Befehl ausführt, identifizieren
        author = message.author

        # Timeout-Rolle suchen
        timeout_role = message.guild.get_role(int(TIMEOUT_ROLE_ID))

        # Benutzer für Timeout sperren
        await author.add_roles(timeout_role)

        # Nachricht senden, dass der Timeout angewendet wurde
        await message.channel.send(f'{author.mention} wurde für {TIMEOUT_DURATION / 60} Minuten getimeoutet.')

        # Timeout aufheben, nachdem die Zeit abgelaufen ist
        await asyncio.sleep(TIMEOUT_DURATION)
        await author.remove_roles(timeout_role)
        await message.channel.send(f'{author.mention} Timeout ist vorbei. Willkommen zurück!')

client.run(TOKEN)
