# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID", ""))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283, -1001687155877]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "0.2.0@main"
BRANCH = "main"
CHANNEL = getenv("CHANNEL", "CilikProject")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX1R1VVNqaml0Y0EwU1Y0a2Y3NDlkTnc2aFBuNXJ4UzFsbFdjTw==").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "CilikSupport")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))

STRING_1 = getenv("STRING_1", "")
STRING_2 = getenv("STRING_2", "")
STRING_3 = getenv("STRING_3", "")
STRING_4 = getenv("STRING_4", "")
STRING_5 = getenv("STRING_5", "")
STRING_6 = getenv("STRING_6", "")
STRING_7 = getenv("STRING_7", "")
STRING_8 = getenv("STRING_8", "")
STRING_9 = getenv("STRING_9", "")
STRING_10 = getenv("STRING_10", "")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
