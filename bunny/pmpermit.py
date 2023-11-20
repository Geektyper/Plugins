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
            await message.reply_text("  ╔════════════════════╗\n
  ⛑ 𝗔𝗧𝗧𝗘𝗡𝗧𝗜𝗢𝗡 𝗣𝗟𝗘𝗔𝗦𝗘 ⛑ \n ╚════════════════════╝\n
    𝙍𝘼𝘽𝘽𝙄𝙏𝙓 𝙋𝙈 𝙎𝙚𝙘𝙪𝙧𝙞𝙩𝙮 \n\n ʜᴇʟʟᴏ!! ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ᴍᴇꜱꜱᴀɢᴇ ᴏɴ ʙᴇʜᴀʟꜰ ᴏꜰ ᴍʏ ᴏᴡɴᴇʀ \n ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴍʏ ᴏᴡɴᴇʀ ᴄᴏᴍᴇꜱ 🙂👍")
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
