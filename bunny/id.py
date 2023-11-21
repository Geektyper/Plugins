from pyrogram import Client, filters

from config import STUFF , DEV
from bunny import neko

HANDLER = STUFF.COMMAND_HANDLER

OWNER_ID = DEV.OWNER_ID


app = Client("my_bot")

@app.on_message(filters.command("id", prefixes=".") & filters.reply)
async def get_user_id(client, message):
    replied_user = message.reply_to_message.from_user
    await message.reply_text(f"The ID of the user is {replied_user.id}")

return
