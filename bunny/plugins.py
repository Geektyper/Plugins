from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import DEV, STUFF
import time
from .data import KeshavX
from external_client import BOT
from pyrogram import Client, filters
from external_client import BOT

hl = STUFF.COMMAND_HANDLER
from .verify import verify

SPARE = "https://telegra.ph/file/31f1906a790ec93ace4e2.jpg"

START_PIC = STUFF.START_PIC if STUFF.START_PIC else SPARE

HELP_PIC = STUFF.HELP_PIC if STUFF.HELP_PIC else SPARE

LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID] + KeshavX

START_MARKUP_STR = IKM(
               [
               [
               IKB("💭 Owner 💭", url="t.me/Notrealgeek"),
               IKB("✨ Support ✨", url="t.me/neiman_chat")
               ],
               [
               IKB("🔥 Repo 🔥", url="https://github.com/Geektyper/RABBITX")
               ]
               ]
               )

START_MARKUP_DEV = IKM(
               [
               [
               IKB("💫 Commands 💫", callback_data="cmds"),
               IKB("💭 Support 💭", url="t.me/DevsX_Community")
               ]
               ]
               )  

@BOT.on_message(filters.command("start", [hl, "/"]))
async def start(_, m):
    DEV.SUDO_USERS.append(DEV.OWNER_ID)
    x = DEV.SUDO_USERS
    bot_name = " 𝙍𝘼𝘽𝘽𝙄𝙏𝙓"
    if await verify(m.from_user.id):
        txt = f"**Hello Boss !!, It's Me {bot_name}, Your ʀᴀʙʙɪᴛx Bot !! \n\n Click Below Buttons For Help. 🌚**"
        await m.reply_photo(START_PIC, caption=txt, reply_markup=START_MARKUP_DEV)
        return
    if str(m.chat.id)[0] == "-":
        return
    men = m.from_user.mention
    txt = f"**Hello !! {men}\nNice To Meet You, Well I Am {bot_name}, A Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Given Below.** \n\n**Powered By : [𝙎𝙥𝙇](https://t.me/SpLBots)**"
    await m.reply_photo(START_PIC, caption=txt, reply_markup=START_MARKUP_STR)
    return

HELP_TEXT = "★   𝙍𝘼𝘽𝘽𝙄𝙏𝙓 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n𝐂𝐥𝐢𝐜𝐤 𝐎𝐧 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐅𝐨𝐫 𝐇𝐞𝐥𝐩"

SPAM_HELP = spam_msg = f"""
**Help Spam Cmds**

**Spam :** Spams a Message For Given Counter(<= 100).
Command :
1) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}spam <count> <replying any message>

**DelaySpam :** Delay Spam a Text For Given Counter After Given Time.
Command :
1) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
2) {hl}delayspam <delay> <count> <replying any message>

** © @Notrealgeek**
"""

RAID_HELP = f"""
**Help Raid Cmds**

**Raid :** Activates Raid on Any individual User For Given Range.
Command :
1) {hl}raid <count> <username
2) {hl}raid <count> <reply to user>

**ReplyRaid :** Activates Reply Raid on The User!!
Command :
1) {hl}replyraid <replying to user>
2) {hl}dreplyraid <username>

**DReplyRaid :** Deactivates Reply Raid on The User!!
Command :
1) {hl}dreplyraid <replying to user>
2) {hl}dreplyraid <username>


**© @NotKeshav**
"""

PM_HELP = f"""
**Help PM GAURD Cmds**

**PM GAURD :** To Activate Pm Gaurd On Any User
Command :
1) {hl}a To Approve a User's dm <reply to user>
2) {hl}da To Dapprove a User's dm <reply to user>



**© @userbot_crack**
"""

ECHO_HELP = f"""
**Help Echo Cmds**

**Echo :** To Active Echo On Any User
Command :
1) {hl}addecho <reply to user>
2) {hl}rmecho <reply to user>



**© @userbot_crack**
"""



EXTRA_HELP = f"""
**Help Extra Cmds**

**Alive and Ping :** Ping Cmds
Command :
1) {hl}ping 
2) {hl}alive

**Echo :** To Active Echo On Any User
Command :
1) {hl}addecho <reply to user>
2) {hl}rmecho <reply to user>

**Leave:** To Leave Group/Channel
Command :
1) {hl}leave <group/chat id>
2) {hl}leave : Type in the Group bot will auto leave that group

**Join:** To Leave Group/Channel
Command :
1) {hl}Join <group/chat id>
2) {hl}Join : Type in the Group bots will join that group.

**© @Notrealgeek**
"""

