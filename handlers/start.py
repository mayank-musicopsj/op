import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker()
    await message.reply_photo(
        photo=f"https://telegra.ph/file/336544dbebf58dadb1e6f.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━
💔 ʜᴇʏ {message.from_user.mention()} !

        ᴛʜɪs ɪs [{bn}](t.me/{bu}),  ɪ ᴀᴍ ᴀ ᴍᴜsɪᴄ ʙᴏᴛ, ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ....

ᴀʟʟ ᴏꜰ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ᴍʏ ᴄᴏᴍᴍᴀɴᴅ ʜᴀɴᴅʟᴇʀs : ( `/ . • $ ^ ~ + * ?` )
┏━━━━━━━━━━━━━━┓
┣★
┣★ ᴍᴀᴅᴇ ʙʏ: [❛-𝐌𝐑'𝐁𝐀𝐍𝐍𝐀-𝐱𝐃°](t.me/BANNA_XD)
┣★
┗━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴍᴇ ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ_xᴅ](t.me/BANNA_XD) ʙᴀʙʏ...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ᴀᴅᴅ ᴍᴇ ᴍʀᴇɪ ᴊᴀᴀɴ​•", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        " ❣ᴏᴡɴᴇʀ ❣ ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "•sᴜᴘᴘᴏʀᴛ•", url=f"https://t.me/AARU_SUPPORT"
                    )
                ],[
                    InlineKeyboardButton(
                        "•ᴄʜᴀɴɴᴇʟ•", url="https://t.me/MISS_AARU_143"
                    ),
                    InlineKeyboardButton(
                        "•ᴅᴇᴠᴇʟᴏᴘᴇʀ•", url="https://t.me/BANNA_XD"
                    )
               ],[
                    )
                    InlineKeyboardButton(
                        " •ᴄʜᴀᴛᴛɪɴɢ ɢʀᴏᴜᴘ• ",url="https//t.me/LOVE_BIRDS_123
                    )
               ]
       ),
    )

