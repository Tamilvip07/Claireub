import logging
import sys
from functools import wraps
from time import gmtime, strftime
from traceback import format_exc

from html_telegraph_poster import TelegraphPoster
from config import Vars
from telethon import events

from claire import bot, user
from .owner import authorized_

t = TelegraphPoster(use_api=True)
t.create_api_token("bot")


def telegraph_(text):
    link = t.post("CLAIRE", "CLAIRE - ERROR", text)["url"]
    return link

def cmd(**args):
    args["pattern"] = "^[" + Vars.HANDLER + "](?i)" + args["pattern"]
    args["outgoing"] = True

    def decorator(func):
        async def wrapper(ev):
            try:
                await func(ev)
            except BaseException as exception:
                logging.info(exception)
                await log_error(ev)

        user.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper

    return decorator





def bot_inline(**args):
    pattern = args.get("pattern", None)
    args["from_users"] = authorized_
    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    def decorator(func):
        async def wrapper(ev):
            try:
                await func(ev)
            except BaseException as exception:
                logging.info(exception)
                await log_error(ev)

        bot.add_event_handler(wrapper, events.InlineQuery(**args))
        return wrapper

    return decorator


def bot_callback(**args):
    args["from_users"] = authorized_
    def decorator(func):
        async def wrapper(ev):
            try:
                await func(ev)
            except BaseException as exception:
                logging.info(exception)
                await log_error(ev)

        bot.add_event_handler(wrapper, events.CallbackQuery(**args))
        return wrapper

    return decorator


async def log_error(event):
    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    text = "**NEW ERROR**\n"
    ftext = "<br>--------ERROR LOG--------<br>"
    ftext += f"<b>Date:</b> {date}<br>"
    if event:
        ftext += f"<b>Group ID:</b> {event.chat_id}<br>"
        ftext += f"<b>Sender ID:</b> {event.sender_id}<br><br>"
        ftext += f"<b>Event Trigger:</b>\n"
        ftext += f"{event.text}<br><br>"
    ftext += "<b>Traceback info</b><br><br>"
    ftext += f"<code>{format_exc()}</code><br><br>"
    ftext += f"<b>Error text:</b>\n"
    ftext += f"<code>{sys.exc_info()[1]}</code><br><br>"
    ftext += f"<b>--------THE END--------</b>"
    mtext = telegraph_(ftext)
    text += f"[logs]({mtext}) | [support](t.me/botbotsupport)"
    await bot.send_message(Vars.LOGGER, str(text), link_preview=False)