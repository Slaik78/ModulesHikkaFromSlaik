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
# meta developer: @Hicota

import asyncio
from .. import loader, utils

@loader.tds
class AsArtsmod(loader.Module):
    """ASCII Arts | Различные прикольные арты 0_o"""

    strings = {'name': 'AsArts'}

    @loader.command()
    async def ascat(self, message):
        '- ASCII Cat'
        await message.edit("""▄───▄
█▀█▀█
█▄█▄█
─███──▄▄
─████▐█─█
─████───█
─▀▀▀▀▀▀▀""")
        
    @loader.command()
    async def asdevil(self, message):
        '- ASCII Devil'
        await message.edit("""|╮╰╮╮▕╲╰╮╭╯╱▏╭╭╭╭
╰╰╮╰╭╱▔▔▔▔╲╮╯╭╯
┏━┓┏┫╭▅╲╱▅╮┣┓╭║║║
╰┳╯╰┫┗━╭╮━┛┣╯╯╚╬╝
╭┻╮╱╰╮╰━━╯╭╯╲┊  ║
╰┳┫▔╲╰┳━━┳╯╱▔┊  ║
┈┃╰━━╲▕╲╱▏╱━━━┬╨╮
┈╰━━╮┊▕╱╲▏┊╭━━┴╥╯""")
    
    @loader.command()
    async def asfuck(self, message):
        '- ASCII Fuck'
        await message.edit(r"""............./´¯/).................(\¯`\
............/...//...................\\...\
.........../...//......................\\...\
...../´¯/..../´¯\................/¯` \....\¯`\
.././.../..../..../.|_........._|.\....\....\...\.\
(.(....(....(..../..)..)…......(..(.\....)....)....).)
.\................\/.../.........\...\/................/
..\.................. /.............\................../
....\................(................).............../""")
        
    @loader.command()
    async def asgift(self, message):
        '- ASCII Gift'
        await message.edit("""───▄█▄
──▀▄█▄▀
▒▒▒▒█▒▒▒▒
▒▒▒▒█▒▒▒▒
█████████
▒▒▒▒█▒▒▒▒
▒▒▒▒█▒▒▒▒""")

    @loader.command()
    async def asflow(self, message):
        '- ASCII Flower'
        await message.edit("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢔⣒⠂⣀⣀⣤⣄⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣿⠋⢠⣟⡼⣷⠼⣆⣼⢇⣿⣄⠱⣄
⠀⠀⠀⠀⠀⠀⠀⠹⣿⡀⣆⠙⠢⠐⠉⠉⣴⣾⣽⢟⡰⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠤⢴⣿⠿⢋⣴⡏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡙⠻⣿⣶⣦⣭⣉⠁⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠈⠉⠉⠉⠉⠇⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣘⣦⣀⠀⠀⣀⡴⠊⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⢻⣿⣿⣿⣿⠻⣧⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠫⣿⠉⠻⣇⠘⠓⠂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢶⣾⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣧⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠙⠻⢿⣿⣿⠿⠛⣄⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀""")

    @loader.command()
    async def aspika(self, message):
        '- ASCII Pikachu'
        await message.edit("""⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿""")

    @loader.command()
    async def ascandle(self, message):
        '- ASCII Candle'
        await message.edit(r"""── )\
──(,,")───── )\
──╫╫─────(,,")─────)\ 
[▒▒▒▒▒▒]──╫╫─────(,,")───── )\
▒▒ █▒▒▒][▓▓▓▓▓▓]──╫╫─────(,,")
[▒▒█▄▒▒][▓█▀█▓▓][░░░░░░]▄▄██▄▄
[▒▒▒▒▒▒][▓█▄█▓▓][░█░█░░]█─▄███
[▒▒▒▒▒▒][▓▓▓▓▓▓][░▀▄▀░░]█─▄███
[▒▒▒▒▒▒][▓▓▓▓▓▓][░░░░░░]█▄▄███""")

    @loader.command()
    async def asbat(self, message):
        '- ASCII Bat'
        await message.edit("""─────▄───▄
─▄█▄─█▀█▀█─▄█▄
▀▀████▄█▄████▀▀
─────▀█▀█▀""")

    @loader.command()
    async def asbeer(self, message):
        '- ASCII Beer'
        await message.edit("""░░░░░░▄█▀█▄░░░░░░░░░░░░░░░
░▄█▀▀▀▀░░░░▀█▄▄▄▄▄▄▄░░░░░░
█▀░░░░░░░░░░░░░░░░░▀█░░░░░
▀▄░▄░░░░░░░░░░░░░░░▄█░░░░░
░█████▄▄▄▄▄██▄▄▄█▀▀█░░░░░░
░█▀█░░░░▀░░░░░▀░░░░█▀▀▀▀▀█
░█░███▄▄▄▄░░░▄▄▄▄▄██▀▀██░█
░█░███░████▀████░███░░█░░█
░█▄███░████░████░███░░█░█▀
░░░███░████░████░███░░█░█░
░░░███░████░████░███▄▄█░█░
░░░███░████░████░███░░░▄█░
░░░███░████░████░███▀▀▀▀░░
░░▄███▄████░████▄███▄░░░░░
░░███▀███████████▀███░░░░░
░░░░▀▀▀██▄▄▄▄▄██▀▀▀░░░░░░░""")

    @loader.command()
    async def asic(self, message):
        '- ASCII Ice Cream'
        await message.edit("""░░░░░░░▄▄█████▄░░░░░░░
░░░░░▄█▀░░░░░░▀█▄░░░░░
░░░░▄█▀░░░░░░░░░█▄░░░░
░░░▄██████▄▄██████▄▄░░
░▄█▀░░░░░░▀██░░░░░▀██░
▄█░░░░░░░░░░█▄░░░░░░██
██░░░░░░░░░░▀█▄░░░░░██
▀█▄░░░░░░░░░░░▀░░░░░█▀
░▀█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▀░
░░░▀██████████████▀░░░
░░░░░█████████████░░░░
░░░░░░███████████░░░░░
░░░░░░▀█████████▀░░░░░
░░░░░░░█████████░░░░░░
░░░░░░░░███████░░░░░░░
░░░░░░░░▀█████▀░░░░░░░
░░░░░░░░░█████░░░░░░░░
░░░░░░░░░▀███▀░░░░░░░░
░░░░░░░░░░▀█▀░░░░░░░░░""")

    @loader.command()
    async def ascake(self, message):
        '- ASCII Cake'
        await message.edit("""┈┈┈☆☆☆☆☆☆☆┈┈┈
┈┈╭┻┻┻┻┻┻┻┻┻╮┈┈
┈┈┃╱╲╱╲╱╲╱╲╱┃┈┈
┈╭┻━━━━━━━━━┻╮┈
┈┃╱╲╱╲╱╲╱╲╱╲╱┃┈
┈┗━━━━━━━━━━━┛┈""")
        
    @loader.command()
    async def asimpo(self, message):
        '- ASCII Imposter'
        await message.edit("""⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⢻⡻⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣟⣫⡾⠛⠛⠛⠛⠛⠛⠿⣾⣽⡻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⣼⠏⠄⠄⠄⠄⠄⠄⣀⣀⡀⣙⣿⣎⢿⣿⣿⣿
⣿⣿⣿⣿⣿⢹⡟⠄⠄⠄⣰⡾⠟⠛⠛⠛⠛⠛⠛⠿⣮⡻⣿⣿
⣿⡿⢟⣻⣟⣽⠇⠄⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⡹⣿
⡟⣼⡟⠉⠉⣿⠄⠄⠄⠄⢿⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣼⢟⣿
⣇⣿⠁⠄⠄⣿⠄⠄⠄⠄⠘⢿⣦⣄⣀⣀⣀⣀⣤⡴⣾⣏⣾⣿
⡇⣿⠄⠄⠄⣿⠄⠄⠄⠄⠄⠄⠈⠉⠛⠋⠉⠉⠄⠄⢻⣿⣿⣿
⢃⣿⠄⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣧⣿⣿
⡻⣿⠄⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⣧⣿⣿
⡇⣿⠄⠄⠄⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⢹⣿⣿
⣿⡸⢷⣤⣤⣿⡀⠄⠄⠄⠄⢠⣤⣄⣀⣀⣀⠄⠄⢠⣿⣿⣿⣿
⣿⣿⣷⣿⣷⣿⡇⠄⠄⠄⠄⢸⡏⡍⣿⡏⠄⠄⠄⢸⡏⣿⣿⣿
⣿⣿⣿⣿⣿⢼⡇⠄⠄⠄⠄⣸⡇⣷⣻⣆⣀⣀⣀⣼⣻⣿⣿⣿
⣿⣿⣿⣿⣿⣜⠿⢦⣤⣤⡾⢟⣰⣿⣷⣭⣯⣭⣯⣥⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")