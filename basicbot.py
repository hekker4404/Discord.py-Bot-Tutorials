import discord
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.members = True  # this allows the bot to receive member events
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is ready!')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command()
async def info(ctx, member: discord.Member):
    embed = discord.Embed(title=member.name, description=member.mention, color=discord.Color.blue())
    embed.add_field(name='ID', value=member.id, inline=False)
    embed.add_field(name='Status', value=member.status, inline=False)
    embed.add_field(name='Top Role', value=member.top_role.mention, inline=False)
    embed.add_field(name='Joined', value=member.joined_at.strftime('%d/%m/%Y %H:%M:%S'), inline=False)
    embed.set_thumbnail(url=member.avatar.url)
    await ctx.send(embed=embed)

@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    

bot.run(os.environ.get("TOKEN"))
