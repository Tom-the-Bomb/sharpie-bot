import interactions
from interactions import Client, Intents
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

bot = Client(token=os.getenv('TOKEN'), intents=Intents.GUILD_MESSAGE_CONTENT)

guild_ids = [918591198799749240]

async def changePres():
    await bot.wait_until_ready()
    await bot.change_presence(interactions.ClientPresence(activities=[interactions.PresenceActivity(name='Against Pens',type=interactions.PresenceActivityType.GAME)]))


@bot.event
async def on_ready():
    print('Ready!')
    print('------')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        print(f'Loaded: {filename[:-3]}')
        bot.load(f'commands.{filename[:-3]}')

bot.start()
