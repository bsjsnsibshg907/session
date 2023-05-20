from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("◉ ¦ بدء استخراج جلسه •", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="💸 ¦ الرئيسية •", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("🗯 ¦ مساعدة •", callback_data="help"),
            InlineKeyboardButton("🔎 ¦ حول •", callback_data="about")
        ],
               [InlineKeyboardButton("☣️ ¦ 𝒆𝒎 𝒔𝒐𝒖𝒓𝒄𝒆 •", url="https://t.me/pyth_on1")]
    ]

    START = f"""
- مرحبا بك عزيزى ❤

- من هنا يمكنك استخراج جلسات البيروجرام والتليثون . 💸
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ 
- اذا كنت لا تثق في البوت ف توقف عن القراءه واحظر البوت ⚠️
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ 
◉ ¦ 𝒎𝒂𝒅𝒆 𝒃𝒚 : [⛥ .✘𝙀𝘽𝙉 𝙈𝘼𝙎𝙍 🇪🇬⛧’!×](https://t.me/UG_U4)
"""

    HELP = """
✨ ¦ اوامر البوت الكتابيه ..

/about - لمعرفه معلومات حول البوت 💸

/help - نفس نص هذة الرساله 💸

/start - بدء البوت 💸

/generate - استخراج جلسه 💸

/cancel - ايقاف الاستخراج 💸

/restart - اعادة تشغيل البوت وتحديث الملفات 💸

/reload - تحديث ملفات البوت 💸
"""

    ABOUT = """
❇️ ¦ حول هذا البوت ¦ ❇️

◉ ¦ بوت استخراج جلسات للحساب 

✦ pyrogram.
✦ Telethon .
✦ pyrogram [ V2 ] .
✦ Telethon ( Bot ) .
✦ pyrogram ( Bot ) « V2 » .
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ 
🗯 [ ➥ Є𝒎 𝒔𝒐𝒖𝒓𝒄𝒆 ☠ ](https://t.me/pyth_on1) .

🗯 [[⛥ .✘𝙀𝘽𝙉 𝙈𝘼𝙎𝙍 🇪🇬⛧’!×](https://t.me/UG_U4) .
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ 
    """
