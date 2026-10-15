# Support Ticket Bot

A Discord bot for creating and managing support tickets with customizable forms and webhook integration.

## Features

- Create support ticket panels with custom banners and select menus
- Integrate with an external dashboard via webhooks
- Approve or deny tickets with simple button interactions

## Requirements

- Python 3.8 or higher
- discord.py
- python-dotenv

## Installation

1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Create a `.env` file based on `.env.example` and add your Discord bot token
4. Run the bot using `python bot.py`

## Usage

### Commands

- `/setup-panel`: Set up the support ticket panel (requires administrator permissions)

### Permissions

- Administrator: Required to set up the support ticket panel

## Configuration

- `DISCORD_TOKEN`: Your Discord bot token (required)
- `WEBHOOK_URL`: The URL of your external dashboard webhook (optional)

---

## Generated with EnderDevelopment

This plugin was generated in minutes with [EnderDevelopment](https://enderdevelopment.com) — the AI platform that turns your ideas into working Minecraft plugins, Discord bots and FiveM scripts.

**Want your own?** [Generate this project on EnderDevelopment](https://dash.enderdevelopment.com?utm_source=github&utm_medium=readme&utm_campaign=support-ticket-bot&utm_content=bottom) — describe it in one sentence and get the full source code.