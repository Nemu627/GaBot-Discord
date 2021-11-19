import discord
from discord.ext import commands

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(
    command_prefix=["Te!", "te!"],
    help_command=None,
    intents=intents,
    allowed_mentions=discord.AllowedMentions(replied_user=False, everyone=False),
)


token = os.environ["token"]

def restart_bot():
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.event
async def on_ready():
    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1
    await bot.change_presence(
        activity=discord.Activity(name=f"test client | {str(servers)}servers | {str(members)}users", type=3)
    )
    print("on")

bot.load_extension("Cog.event")
bot.load_extension("Cog.bot")
bot.load_extension("Cog.tool")
bot.load_extension("Cog.data")
bot.load_extension("Cog.variety")

bot.run(token)
