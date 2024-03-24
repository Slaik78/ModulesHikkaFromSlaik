import asyncio
import random

from .. import loader, utils

Haha = ["да", "нет", "возможно да", "возможно нет", "вероятно да", "вероятно нет", "скорее всего да", "скорее всего нет", "да, но это не точно", "нет, но это не точно"]

@loader.tds
class MagicBall(loader.Module):
    "Ask a question to the magic ball🔮"
    strings = {"name": "MagicBall"}
    
    @loader.command(ru_doc="- загадать вопрос")
    async def mblcmd(self, message):
        "- make a question"
        args = utils.get_args_raw(message)
        await message.edit(f"Шар, {args}")
        if args:
            args = args.split(" ", 1)
            if args[0]:
                lol = await message.reply("<b>Магический шар думает над вопросом.</b>")
                await asyncio.sleep(0.5)
                await lol.edit("<b>Магический шар думает над вопросом..</b>")
                await asyncio.sleep(0.5)
                await lol.edit("<b>Магический шар думает над вопросом...</b>")
                for i in range(0, 2):
                    await lol.edit("<b>Магический шар думает над вопросом.</b>")
                    await asyncio.sleep(0.5)
                    await lol.edit("<b>Магический шар думает над вопросом..</b>")
                    await asyncio.sleep(0.5)
                    await lol.edit("<b>Магический шар думает над вопросом...</b>")
                    await asyncio.sleep(0.5)
                await asyncio.sleep(0.5)
                result = random.choice(Haha)
                await lol.edit(f"<b>Магический шар думает что {result}</b><emoji document_id=5361837567463399422>🔮</emoji>")
            else:
                await message.respond("Введи свой вопрос")
        else:
            await message.edit("Введён неккоректный ввод<emoji document_id=5467928559664242360>❗️</emoji>")
    