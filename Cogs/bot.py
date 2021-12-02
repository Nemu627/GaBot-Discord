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
    async def list(self,ctx):
        embed = discord.Embed(title="コマンドリスト", description="使用可能なコマンド一覧です♪\n各コマンドの詳細は`Cu!help [コマンド名]`で確認できます♪", colour=0x3498DB)
        embed1.add_field(
            name=":robot: 》BOT",
            value="`help`：困ったときはを表示します。\n`list`：コマンドリストを表示します。\n`prof`：CuBOTのプロフィールを表示します。\n`ping`：CuBOTのping値を表示します。",
        )
        embed.add_field(
            name=":video_game: 》バラエティ",
            value="`fortune`：おみくじが引けます。\n"
                  "`rps`：じゃんけんができます。\n"
                  "`dice`：サイコロを振れます。\n"
                  "`pun`：ダジャレが聞けます。\n"
                  "`cquiz`：暗算クイズができます。\n"
                  "`coin`：コイントスができます。\n"
                  "`slot`：スロットができます。\n"
                  "`totusi`：突然の死AAを作成します。",
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
