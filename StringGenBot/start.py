from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""📟¦اهلا بـك عزيـزي 📬 المدمر,
🖱 ¦ يـمكنك استـخـراج الـتـالـي 📥
📟 ¦ تيرمـكـس تليثون للحسـابـات 🥷
📡 ¦ تيرمـكـس تليثون للبوتــات 🎭
🎸 ¦ بايـروجـرام مـيوزك للحسابات 🥷
🔮 ¦ بايـروجـرام مـيوزك للبوتات 🎭
🔗 ¦ بايـروجـرام مـيوزك احدث اصدار 📀

- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت

بواسطـة>> .༊ 𝙼𝙰𝚁𝙻𝙾𝚆 👨‍💻 ttps://t.me/MA_RL_O_W)"""

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="أٍ🏆☜ ضغط لبدا استخراج كود ☞🏆ْٖ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("♥️️ [{ قناه السورس}] ٍُٓ😈 ️", url="https://t.me/SR_MARLOW"),
                    InlineKeyboardButton("مطور البوت ُْٖ", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
