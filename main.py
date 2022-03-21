import discord
from discord import app_commands
from discord.ext import commands
bot = discord.Client()
tree = app_commands.CommandTree(bot)
@bot.event
async def on_ready():
    await tree.sync()
    print("login")
@tree.command(name = 'test', description = 'testcommand')
async def test(interaction: discord.Interaction):
    await interaction.response.send_message('test succeed')
@tree.command(name="awesome",description="🤔")
async def awesome(interaction: discord.Interaction,content: str,num: int):
    await interaction.response.send_message(f"{content} {num}")
bot.run("TOKEN")
