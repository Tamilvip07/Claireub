from telethon import types
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from claire import user
from claire.functions.misc import eor, get_user
from claire.functions.handler import cmd

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

@cmd(pattern="ban$")
async def ban_ (event):
    if event.is_private:
        return await eor(event, "This command is only available in groups.")
    user_ = await get_user(event)
    if not user_:
        return await eor(event, "No user found.")
    await user(EditBannedRequest(event.chat_id, user_, BANNED_RIGHTS))
    await eor(event, f"**{user_}** has been banned.")
