import interactions
from interactions import Client, Intents
import os
from dotenv import load_dotenv
import asyncio
import random

load_dotenv()
token = os.getenv('TOKEN')

bot = Client(token=os.getenv('TOKEN'), presence=interactions.ClientPresence(activities=[interactions.PresenceActivity(name="Drawing Tutorials", type=interactions.PresenceActivityType.WATCHING)]), intents=Intents.GUILD_MESSAGE_CONTENT)

guild_ids = [918591198799749240]

@bot.event
async def on_ready():
    print('Ready!')
    print('------')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        print(f'Loaded: {filename[:-3]}')
        bot.load(f'commands.{filename[:-3]}')

bot.start()
