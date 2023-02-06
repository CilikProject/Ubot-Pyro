# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# Cilik-PyroBot

from pyrogram import idle
from uvloop import install

from Cilik import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from Cilik.helpers.misc import create_botlog, git, heroku
from config import BOT_VER

MSG_ON = """
✅ **Near PyroBot Activated.**
**🏷️ Userbot Version -** `{}`
**Ketik** `.ping` **untuk Mengecheck Bot**
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("ressnearpedia")
            await bot.join_chat("lpmnearpedia")
            await bot.join_chat("nearpediastore")            
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER))
            except BaseException:
                pass
            LOGGER("Near").info(f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]")
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("Near").info(f"Ubot v{BOT_VER} ⚙️[⚡ Activated ⚡]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Near").info("Starting Near-Ubot")
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
