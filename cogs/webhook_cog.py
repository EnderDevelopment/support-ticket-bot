import discord
from discord.ext import commands
import aiohttp

class WebhookCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.webhook_url = 'https://your-webhook-url.com'

    async def send_to_dashboard(self, data):
        async with aiohttp.ClientSession() as session:
            async with session.post(self.webhook_url, json=data) as response:
                return response.status

    @commands.Cog.listener()
    async def on_ticket_created(self, channel, user):
        data = {
            'event': 'ticket_created',
            'channel_id': channel.id,
            'user_id': user.id
        }
        await self.send_to_dashboard(data)

    @commands.Cog.listener()
    async def on_ticket_approved(self, channel, user):
        data = {
            'event': 'ticket_approved',
            'channel_id': channel.id,
            'user_id': user.id
        }
        await self.send_to_dashboard(data)

    @commands.Cog.listener()
    async def on_ticket_denied(self, channel, user):
        data = {
            'event': 'ticket_denied',
            'channel_id': channel.id,
            'user_id': user.id
        }
        await self.send_to_dashboard(data)

async def setup(bot):
    await bot.add_cog(WebhookCog(bot))