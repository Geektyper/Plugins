import asyncio
from io import BytesIO

from pyrogram import Client, filters
from pyrogram.types import Message

from config import STUFF
from bunny import aiosession
from bunny.helpers.basic import edit_or_reply
from bunny.helpers.PyroHelpers import ReplyCheck

cmd = STUFF.COMMAND_HANDLER

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@Client.on_message(filters.command("carbon", cmd) & filters.me)
async def carbon_func(client: Client, message: Message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    Man = await edit_or_reply(message, "`Preparing Carbon . . .`")
    carbon = await make_carbon(text)
    await Man.edit("`Uploading . . .`")
    await asyncio.gather(
        Man.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"**Carbonised by** {client.me.mention}",
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    carbon.close()



