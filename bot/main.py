import discord
import config

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@bot.slash_command(guild_ids=1006776654934323260)
async def hello(ctx):
    await ctx.respond("Hello!")

bot.run(config.TEST_TOKEN)