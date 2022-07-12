import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1ebc3393692680b98c7ef.jpg",
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
                        "•sᴏᴜʀᴄᴇ•", url=f"https://github.com/BANNA-XD143/Aaru_Music"
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
                    InlineKeyboardButton(
                        " •ɢʀᴏᴜᴘ•", url="https//t.me/LOVE_BIRDS_123"
                       )
                ]        
            ]
       ),
    )

