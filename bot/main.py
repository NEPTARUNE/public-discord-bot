import discord
import config

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@bot.slash_command(guild_ids=[your, guild_ids, here])
async def hello(ctx):
    await ctx.respond("Hello!")

client.run(config.TEST_TOKEN)