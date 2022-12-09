import discord
import config
from pyshorteners import Shortener

bot = discord.Bot()
short = Shortener()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(guild_ids=[1006776654934323260], name="shorturl", description="Short your URL")
async def shorturl(ctx, url: str):
    shortened_link = short.tinyurl.short(url)
    await ctx.respond(f"Your shortened URL is:" + shortened_link)

bot.run(config.TEST_TOKEN)