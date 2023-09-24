import disnake
import os
import psutil
import json
import logging
from disnake.ext import commands, tasks

# инит всех настроек и т.д и т.п
with open("config/discord.json", "r", encoding='utf-8') as file:
    rawData = file.read()
    configs = json.loads(rawData)
    
selfProcess = psutil.Process()

fileLog = logging.FileHandler(
    filename="bot.py.log",
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

bot = commands.Bot(
    command_prefix="?",
    help_command=None,
    asyncio_debug=True,
    intents=disnake.Intents.all()
)


# инит первых когов
async def initCogs(): 
    for file in os.listdir("cogs"):
        if not file.endswith(".py"):
            continue
        
        try:
            bot.load_extension(f"cogs.{file[:-3]}")
            
            logging.info(f"Ког {file} был запущен")
        except:
            logging.error(f"Ког {file} не был запущен из-за ошибки", exc_info=True)


# ивенты бота
@bot.event
async def on_ready():
    logging.info(f"Бот запущен, информация: \nID - {bot.user.id}\nНик - {bot.user}")
    
    # дефолт цвет для эмбедов
    disnake.Embed.set_default_color(disnake.colour.Color.from_rgb(141, 255, 160))
    
    await initCogs()

# дефолтные команды бота
@bot.command(name="ping", brief="Отклик бота", description="Отклик бота на сервер и обратно за последнии 60 секунд")
async def default_ping(ctx):
    embed = disnake.Embed(
        title="Ping",
    )
    
    embed.description = f"Отклик сервера за последнии 60 секунд -\n``{round(bot.latency * 1000, 3)}``\nИспользуется RAM/mb программой -\n``{round(selfProcess.memory_info().rss / 1024 / 1024)}``"
    
    await ctx.reply(embed=embed)
    
    
# запуск
bot.run(configs["TOKEN"])