import os

from pyrogram import Client, filters, enums
from pyrogram.types import Message

from bunny.utils.misc import modules_help, prefix
from bunny.utils.scripts import with_reply


@Client.on_message(filters.command("msave", prefix) & filters.me)
@with_reply
async def msave(client: Client, message: Message):
    media = message.reply_to_message.media

    if not media:
        await message.edit("<b>Media is required</b>", parse_mode=enums.ParseMode.HTML)
        return
    await message.delete()

    path = await message.reply_to_message.download()
    await getattr(client, "send_" + media)("me", path)
    os.remove(path)


