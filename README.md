# Minecraft Server Status Discord Bot

A Discord bot that provides the online status and player list of a Minecraft Java Edition server using the `/mcserverstatus` slash command.

---

## Features

- `/mcserverstatus` slash command to check Minecraft server status.
- Shows if the server is online or offline.
- Displays current number of players and their usernames.
- Legacy text command support: replies to `"yo srvr stat"` with a prompt to use slash commands.
- Uses the [mcstatus.io API](https://mcstatus.io/) for server data.
- Built with `discord.py` and `aiohttp`.

---

## Requirements

- Python 3.8+
- Discord bot token
- Discord server (guild) ID for command syncing
- Packages:
  - `discord.py`
  - `python-dotenv`
  - `aiohttp`

---

## Installation

1. Clone or download the bot code.

2. Install dependencies via pip:

   ```bash
   pip install discord.py python-dotenv aiohttp
3. Create a .env file in the project root with the following contents:
    ```
    DISCORD_TOKEN=your_discord_bot_token
    GUILD_ID=your_discord_guild_id
    ```

4. Open the Python script and set the Minecraft server address:

    ```python
    SERVER_ADDRESS = "your.minecraft.server"
    ```
## Running the Bot
Run the bot with:

```bash
python your_bot_script.py
```

Once running:

- Use `/mcserverstatus` slash command in your Discord server to check the Minecraft server status.

