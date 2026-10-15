import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class SupportTicketBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.all())

    async def setup_hook(self):
        await self.tree.sync()

bot = SupportTicketBot()

async def load_extensions():
    await bot.load_extension('cogs.ticket_cog')
    await bot.load_extension('cogs.webhook_cog')

@bot.event
async def on_ready():
    await load_extensions()
    print(f'Logged in as {bot.user}')

@bot.tree.command(name='setup-panel', description='Set up the support ticket panel')
@app_commands.checks.has_permissions(administrator=True)
async def setup_panel(interaction: discord.Interaction):
    # Create embed with custom banner
    embed = discord.Embed(title='Support Ticket', description='Click the button below to create a support ticket', color=discord.Color.blue())
    embed.set_image(url='https://example.com/banner.png')

    # Create select menu
    select_menu = discord.ui.Select(
        placeholder='Select a category',
        options=[
            discord.SelectOption(label='General', value='general'),
            discord.SelectOption(label='Technical', value='technical'),
            discord.SelectOption(label='Billing', value='billing')
        ]
    )

    # Create modal form
    modal = discord.ui.Modal(title='Support Ticket Form')
    modal.add_item(discord.ui.InputText(label='Name', placeholder='Enter your name'))
    modal.add_item(discord.ui.InputText(label='Email', placeholder='Enter your email'))
    modal.add_item(discord.ui.InputText(label='Issue', style=discord.InputTextStyle.long, placeholder='Describe your issue'))

    # Create view with select menu and modal
    view = discord.ui.View()
    view.add_item(select_menu)
    view.add_item(discord.ui.Button(label='Create Ticket', style=discord.ButtonStyle.primary, custom_id='create_ticket'))

    await interaction.response.send_message(embed=embed, view=view)

@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type == discord.InteractionType.component:
        if interaction.data['custom_id'] == 'create_ticket':
            modal = discord.ui.Modal(title='Support Ticket Form')
            modal.add_item(discord.ui.InputText(label='Name', placeholder='Enter your name'))
            modal.add_item(discord.ui.InputText(label='Email', placeholder='Enter your email'))
            modal.add_item(discord.ui.InputText(label='Issue', style=discord.InputTextStyle.long, placeholder='Describe your issue'))
            await interaction.response.send_modal(modal)

bot.run(TOKEN)