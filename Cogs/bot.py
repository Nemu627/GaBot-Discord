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
        embed = discord.Embed(title="ヘルプ", description="次の対戦相手はあなた？\nバラエティ特化型の派生BOT！Geだよ！", colour=0xffa500)
        embed.add_field(
            name=":robot: 》コマンドリスト",
            value="`help`：ヘルプを表示します。\n"
                  "`ping`：GeBOTのping値を表示します。\n"
                  "`fortune`：おみくじが引けます。\n"
                  "`rps`：じゃんけんができます。\n"
                  "`dice`：サイコロを振れます。\n"
                  "`pun`：ダジャレが聞けます。\n"
                  "`cquiz`：暗算クイズができます。\n"
                  "`coin`：コイントスができます。\n"
                  "`slot`：スロットができます。\n"
                  "`totusi`：突然の死AAを作成します。\n",
                  "`5000`：5000兆円を生成します。",
        )
        await ctx.reply(embed=embed)

    @commands.command()
    async def ping(self,ctx):
        async with ctx.typing():
            await asyncio.sleep(0)
        embed = discord.Embed(title="PING", description=f"ただいまのping値は**{round(self.bot.latency * 1000)}**msです！",
                              color=0xffa500)
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    return bot.add_cog(AppCmdBot(bot))
