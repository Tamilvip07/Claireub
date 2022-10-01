import logging
import time

from telethon import TelegramClient

from config import Vars


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
LOGGER = logging.getLogger(__name__)

StartTime = time.time()

bot = TelegramClient("user.session", Vars.APP_KEY, Vars.APP_HASH).start(bot_token=Vars.TOKEN)
user = TelegramClient("bot.session", Vars.APP_KEY, Vars.APP_HASH).start()

