import discord
import config
from pyshorteners import Shortener

bot = discord.Bot()
short = Shortener()

cogs_list = [
    'hello',
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(guild_ids=[1006776654934323260])
async def url(ctx):

    await ctx.respond("Hello!")

bot.run(config.TEST_TOKEN)