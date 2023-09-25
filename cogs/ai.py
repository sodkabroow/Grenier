import disnake
import ai
from io import BytesIO
from disnake.ext import commands


class Ai(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="generate", brief="Генерирует изображения", description="Генерирует изображения на основе текста на английском")
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def ai_gen_image(self, ctx, *, req: str):
        embed = disnake.Embed(
            title="Generate"
        )
        
        embed.description = "Ожидайте..."
        
        originalMsg = await ctx.reply(embed=embed)
        
        imageBytes = await ai.genImage(req)
        
        # запрос пустой
        if imageBytes == b"0":
            embed.description = "Запрос не может быть пустым"
            await originalMsg.edit(embed=embed)
            
            return
        
        elif imageBytes == b"1":
            embed.description = "Произошла ошибка при запросе, пожалуйста, попробуйте снова или сообщите об этом создателю"
            await originalMsg.edit(embed=embed)
            
            return
        else:
            embed.description = f"Запрос - \"{req}\""
            img = BytesIO(imageBytes)
            embed.set_image(file=disnake.File(img,
                                              filename=f"{hash(imageBytes)}.jpeg",
                                              ))
            
            await originalMsg.edit(embed=embed)
            
            return
    

def setup(bot):
    bot.add_cog(Ai(bot))
