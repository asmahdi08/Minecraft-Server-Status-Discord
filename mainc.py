import discord
import dotenv
import os
import aiohttp
import asyncio
import json
from discord.ext import commands

# Load environment variables
dotenv.load_dotenv()
TOKEN: str = os.getenv("DISCORD_TOKEN")

# Server to query
SERVER_ADDRESS = "forennofficial.aternos.me"

# Intents setup
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True

# Create bot client
client = commands.Bot(command_prefix="!", intents=intents)

# When the bot is ready
@client.event
async def on_ready():
    try:
        synced = await client.tree.sync(guild= discord.Object(id=1371854101608009748))
        print(f"✅ Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")
    print(f"🟢 Logged in as {client.user}")

# @client.event
# async def on_ready():
#     print(f'Logged in as {client.user}')

#     # Clear GLOBAL commands
#     client.tree.clear_commands(guild=None)
#     await client.tree.sync(guild=None)
#     print("❌ Cleared global commands")

#     # Clear commands for a specific GUILD
#     GUILD = discord.Object(id=1371854101608009748)  # Replace with your server ID
#     client.tree.clear_commands(guild=GUILD)
#     await client.tree.sync(guild=GUILD)
#     print("❌ Cleared guild commands")


# Make a request to mcstatus API
async def make_rq():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.mcstatus.io/v2/status/java/{SERVER_ADDRESS}") as response:
            return await response.json()

# Slash command
@client.tree.command(name="mcserverstatus", description="Get Minecraft server status with player list",guild= discord.Object(id=1371854101608009748))
async def mcserverstatus(interaction: discord.Interaction):
    await interaction.response.defer()  # Defer the response if it might take a second
    data = await make_rq()  

    if data["online"]:
        activePlayerCount = data["players"]["online"]
        player_list = data["players"].get("list", [])
        players = [player["name_clean"] for player in player_list]
        name_string = "\n".join(players) if players else "No players online."

        embed = discord.Embed(
            title="Forenno Minecraft Server Status",
            description="✅ The server is **online!**",
            color=discord.Color.green()
        )
        embed.add_field(name="Players Online", value=f"{activePlayerCount}/20", inline=False)
        embed.add_field(name="Player List", value=name_string, inline=False)
    else:
        embed = discord.Embed(
            title="Forenno Minecraft Server Status",
            description="❌ The server is **offline.**",
            color=discord.Color.red()
        )

    await interaction.followup.send(embed=embed)

# Optional legacy message-based trigger
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "yo srvr stat":
        await message.channel.send("Use `/mcserverstatus` instead 😎")

# Run bot
client.run(TOKEN)
