#------------------------------------------------------------------
#      ___           ___       ___                       ___     
#     /\  \         /\__\     /\  \          ___        /\__\    
#    /::\  \       /:/  /    /::\  \        /\  \      /:/  /    
#   /:/\ \  \     /:/  /    /:/\:\  \       \:\  \    /:/__/     
#  _\:\~\ \  \   /:/  /    /::\~\:\  \      /::\__\  /::\__\____ 
# /\ \:\ \ \__\ /:/__/    /:/\:\ \:\__\  __/:/\/__/ /:/\:::::\__\
# \:\ \:\ \/__/ \:\  \    \/__\:\/:/  / /\/:/  /    \/_|:|~~|~   
#  \:\ \:\__\    \:\  \        \::/  /  \::/__/        |:|  |    
#   \:\/:/  /     \:\  \       /:/  /    \:\__\        |:|  |    
#    \::/  /       \:\__\     /:/  /      \/__/        |:|  |    
#     \/__/         \/__/     \/__/                     \|__|   
#------------------------------------------------------------------ 
# meta developer: @hicota

import asyncio
import random

from .. import loader, utils

Haha = ["да", "нет", "возможно да", "возможно нет", "вероятно да", "вероятно нет", "скорее всего да", "скорее всего нет", "да, но это не точно", "нет, но это не точно"]

@loader.tds
class MagicBall(loader.Module):
    "Что же тебе скажет магический шар?"
    strings = {"name": "MagicBall"}
    
    async def mblcmd(self, message):
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
                await asyncio.sleep(1)
                result = random.choice(Haha)
                await lol.edit(f"<b>Магический шар думает что {result}</b><emoji document_id=5361837567463399422>🔮</emoji>")
            else:
                await message.respond("Введи свой вопрос")
        else:
            await message.edit("Введён неккоректный ввод<emoji document_id=5467928559664242360>❗️</emoji>")
    