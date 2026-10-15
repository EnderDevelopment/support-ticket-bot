import discord
from discord.ext import commands
from discord import app_commands

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type == discord.InteractionType.modal_submit:
            if interaction.data['custom_id'] == 'support_ticket_form':
                name = interaction.data['components'][0]['components'][0]['value']
                email = interaction.data['components'][1]['components'][0]['value']
                issue = interaction.data['components'][2]['components'][0]['value']

                # Create ticket channel
                guild = interaction.guild
                category = discord.utils.get(guild.categories, name='Support Tickets')
                if not category:
                    category = await guild.create_category('Support Tickets')

                channel = await guild.create_text_channel(f'ticket-{name}', category=category)

                # Send ticket details
                embed = discord.Embed(title='Support Ticket', color=discord.Color.blue())
                embed.add_field(name='Name', value=name, inline=False)
                embed.add_field(name='Email', value=email, inline=False)
                embed.add_field(name='Issue', value=issue, inline=False)

                # Add approval/denial buttons
                view = discord.ui.View()
                view.add_item(discord.ui.Button(label='Approve', style=discord.ButtonStyle.success, custom_id='approve_ticket'))
                view.add_item(discord.ui.Button(label='Deny', style=discord.ButtonStyle.danger, custom_id='deny_ticket'))

                await channel.send(embed=embed, view=view)
                await interaction.response.send_message('Ticket created successfully!', ephemeral=True)

    @commands.Cog.listener()
    async def on_button_click(self, interaction: discord.Interaction):
        if interaction.data['custom_id'] == 'approve_ticket':
            # Approve ticket logic
            await interaction.response.send_message('Ticket approved!', ephemeral=True)
        elif interaction.data['custom_id'] == 'deny_ticket':
            # Deny ticket logic
            await interaction.response.send_message('Ticket denied!', ephemeral=True)

async def setup(bot):
    await bot.add_cog(TicketCog(bot))