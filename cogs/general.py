import disnake
import logging
from disnake.ext import commands

# настройки
fileLog = logging.FileHandler(
    filename="cog-general.py.log",
    mode="a",
    encoding="utf-8"
)
streamLog = logging.StreamHandler()

logging.basicConfig(
    #хендлеры для работы и в консоли и в файле
    handlers=(fileLog, streamLog),
    format="[%(asctime)s] <%(levelname)s> %(message)s",
    level=logging.INFO
)

class General(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        
    
    @commands.command(name="help",
                      brief="Показывает это",
                      description="Показывает список всех доступных команд")
    async def general_help_all(self, ctx, cmdToFind: str | None = None):
        allCmds = []
        for cmd in self.bot.walk_commands():
            if cmd.hidden == True:
                continue
            else:
                allCmds.append(cmd)
        
        if cmdToFind is None:
            resText = ""
            for cmd in allCmds:
                resText += f"{cmd.name} - {cmd.brief}\n"
        else:
            for cmd in allCmds:
                if cmd.name == cmdToFind:
                    resText = f"{self.bot.command_prefix}{cmd.name} - {cmd.brief}\n>{cmd.description}"
                    break
            else:
                resText = "Ничего не найдено"
                
        embed = disnake.Embed(
            title="Help"
        )
        embed.description = resText
        
        await ctx.reply(embed=embed)
        

    
def setup(bot):
    bot.add_cog(General(bot))