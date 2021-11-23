import discord
from discord.ext import commands
import asyncio
import random

class AppCmdBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.command()
    async def help(self,ctx):
        await ctx.reply("coming soon ...")

    @commands.command()
    async def ping(self,ctx):
        async with ctx.typing():
            await asyncio.sleep(0)
        embed = discord.Embed(title="PING", description=f"ただいまのping値は**{round(self.bot.latency * 1000)}**msです！",
                              color=0x3498DB)
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    return bot.add_cog(AppCmdBot(bot))
