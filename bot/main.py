import discord
from discord.ext.commands import Bot
from discord.ext import commands
TOKEN = "OTI1MTM1MTA1MzIyNzc4Njk2.YcotNQ.ZoQtlwZHMArPswkroRkgDeUl4Pc"
BOT = Bot(command_prefix='alpha')

BOT.run(os.getenv('DISCORD.TOKEN'))
