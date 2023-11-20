from pyrogram import Client
import asyncio
from config import DEV
from config import STUFF
from pyrogram import filters
from pyrogram.types import Message
from os import getenv

from dotenv import load_dotenv

load_dotenv()

PMPERMIT = getenv("PMPERMIT","ENABLE")

PMSET =True
pchats = []
BOT_NAME = "RABBITX"
PMPERMIT = PMPERMIT
SUDO_USERS = DEV.SUDO_USERS

@Client.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: Client, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await Client.send_message(
                message.chat.id,
                "ʜɪ ᴛʜᴇʀᴇ, ᴛʜɪs ɪs ʀᴀʙʙɪᴛx sᴇʀᴠɪᴄᴇ .\n•────────────────•\n •➢ 𝘙𝘶𝘭𝘦𝘴:\n   » ɴᴏ sᴘᴀᴍ ᴀʟʟᴏᴡᴇᴅ \n   » ᴅᴏɴ'ᴛ ᴀᴅᴅ ᴛʜɪs ᴜsᴇʀ ᴛᴏ sᴇᴄʀᴇᴛ ɢʀᴏᴜᴘs.\n   » ᴅᴏɴ'ᴛ sʜᴀʀᴇ ᴘʀɪᴠᴀᴛᴇ ɪɴғᴏ ʜᴇʀᴇ\n•────────────────•\n •➢  𝗪𝗔𝗜𝗧 𝗨𝗡𝗧𝗜𝗟 𝗠𝗬 𝗢𝗪𝗡𝗘𝗥 𝗖𝗢𝗠𝗘𝗦.\n•────────────────•\n•➢ 𝘕𝘖𝘛𝘌 :  ɪғ ʏᴏᴜ ᴀʀᴇ sᴇɴᴅɪɴɢ ᴀ ᴍᴇssᴀɢᴇ ʜᴇʀᴇ ɪᴛ ᴍᴇᴀɴs ᴀᴅᴍɪɴ ᴡɪʟʟ sᴇᴇ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ ᴀɴᴅ ᴊᴏɪɴ ᴄʜᴀᴛ",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("ᴘᴍᴘᴇʀᴍɪᴛ ᴛᴜʀɴᴇᴅ ᴏɴ")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("ᴘᴍᴘᴇʀᴍɪᴛ ᴛᴜʀɴᴇᴅ ᴏғғ")
            return

@Client.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: Client, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("ᴀᴘᴘʀᴏᴏᴠᴇᴅ ɪɴ ᴘᴍ")
        return
    message.continue_propagation()    
    
@Client.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: Client, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("ᴀᴘᴘʀᴏᴏᴠᴇᴅ ɪɴ ᴘᴍ")
        return
    message.continue_propagation()    
    

@Client.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: Client, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("ᴅɪsᴘᴘʀᴏᴏᴠᴇᴅ ɪɴ ᴘᴍ")
        return
    message.continue_propagation()
