import disnake
import logging
import os
from disnake.ext import commands

# настройки
fileLog = logging.FileHandler(
    filename="cog-cogmanager.py.log",
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

class CogManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # загрузка
    @commands.group(name="cog", hidden=True)
    @commands.is_owner()
    async def group_cog(self, ctx):
        if ctx.invoked_subcommand is None:
            logging.error("Неизвестная суб-команда")
            await ctx.reply("Неизвестная суб-команда", delete_after=3)
            
    @group_cog.command(name="disable", hidden=True)
    async def group_cog_disable(self, ctx, cogName: str = "all"):
        
        status = []
        
        for file in os.listdir("cogs"):
            if cogName == "all":
                try:
                    self.bot.unload_extension(f"cogs.{file[:-3]}")
                    status.append(f"Ког {file} был выгружен")
                except commands.errors.ExtensionNotLoaded:
                    status.append(f"Ког {file} не был выгружен, т.к не был загружен")
            else:
                if cogName == file:
                    try:
                        self.bot.unload_extension(f"cogs.{file[:-3]}")
                        status.append(f"Ког {file} был выгружен")
                    except commands.errors.ExtensionNotLoaded:
                        status.append(f"Ког {file} не был выгружен, т.к не был загружен")
        
        fStatus = '\n'.join(status)
           
        embed = disnake.Embed(
            title="Cogs disable"
        )
        
        embed.description = f"```{fStatus}```"
        
        await ctx.reply(embed=embed)
        
        
    @group_cog.command(name="enable", hidden=True)
    async def group_cog_enable(self, ctx, cogName: str = "all"):
        
        status = []
        
        for file in os.listdir("cogs"):
            if cogName == "all":
                try:
                    self.bot.load_extension(f"cogs.{file[:-3]}")
                    status.append(f"Ког {file} был выгружен")
                except commands.errors.ExtensionAlreadyLoaded:
                    status.append(f"Ког {file} не был загружен, т.к не был выгружен")
                except Exception as exp:
                    status.append(f"Ког {file} не был загружен из-за ошибки\n->{exp}")
            else:
                if cogName == file:
                    try:
                        self.bot.load_extension(f"cogs.{file[:-3]}")
                        status.append(f"Ког {file} был загружен")
                    except commands.errors.ExtensionAlreadyLoaded:
                        status.append(f"Ког {file} не был загружен, т.к не был вызагружен")
                    except Exception as exp:
                        status.append(f"Ког {file} не был загружен из-за ошибки\n->{exp}")
        
        fStatus = '\n'.join(status)
           
        embed = disnake.Embed(
            title="Cogs enable"
        )
        
        embed.description = f"```{fStatus}```"
        
        await ctx.reply(embed=embed)
        
    @group_cog.command(name="status", hidden=True)
    async def group_cog_status(self, ctx):
        embed = disnake.Embed(
            title="Cogs status"
        )
        
        cogStat = []
        for cog in self.bot.cogs:
            cogStat.append(f"{cog} находится в активном состоянии")
            
        fCogStat = '\n'.join(cogStat)
        
        embed.description = f"```{fCogStat}```"
        
        await ctx.reply(embed=embed)
                
        

def setup(bot):
    bot.add_cog(CogManager(bot))
