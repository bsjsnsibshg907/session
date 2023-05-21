from data import Data
from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)


ask_ques = f"""◉ ¦ مرحبا {message.from_user.mention} 
◉ ¦ اختر نوع الجلسه التي تريد استخراجها .

✦ pyrogram اذا كان السورس علي مكتبه pyrogram 🖤.
✦ Telethon اذا كان السورس علي مكتبه Telethon 🖤.
"""
buttons_ques = [
    [
        InlineKeyboardButton("◉ : Pyrogram", callback_data="pyrogram1"),
        InlineKeyboardButton("◉ : Telethon", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("◉ : Pyrogram v2 [New]", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("◉ : Pyrogram Bot", callback_data="pyrogram_bot"),
        InlineKeyboardButton("◉ : Telethon Bot", callback_data="telethon_bot"),
    ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "Telethon"
    else:
        ty = "Pyrogram"
        if not old_pyro:
            ty += " v2"
    if is_bot:
        ty += " Bot"
    await msg.reply(f"❥ بدا استخراج جلسه {ty} عزيزي ❍")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id,"❍ حسنا ارسل API_ID   .",filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply(' ⚠️ ¦ عذرا ال API_ID خاطئ يحب ان تكون من 8 ارقام .', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, '❍ حسنا ارسل API_HASH   .', filters=filters.text)
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "❍ حسنا الان ارسل رقم هاتفك مع كود الدوله كمثال : `+20xxxxxxxxx`'"
    else:
        t = "❍ حسنا ارسل توكن بوتك الان كمثال  : `12345:abcdefghijklmnopqrstuvwxyz`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("جاري ارسال رمز التحقق ❥ ")
    else:
        await msg.reply("جاري تسجيلك كمستخدم روبوت ❥")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply('ال API_ ID و ال API_ HASH غير صالحين للاستخراج الرجاء محاوله الاستخراج مجددا ♡', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply('رقم الهاتف غير صحيح الرجاء المحاوله مرة اخرى ♡.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, " ◉ : تم ارسال رمز التحقق لحسابك يمكنك ان تحصل عليه من اشعارات خدمه تليجرام اذا كان رمز التحقق مثل 12345 الرجاء ارساله بالشكل 1 2 3 4 5   بين كل رقم و رقم مسطرة .", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply('⚠️ : عذرا انتهى وقت الانتظار 10 دقائق .. الرجاء المجاوله مرة اخرى .', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply('⚠️ : عذرا كود التحقق خاطئ .. الرجاء المحاوله من جديد .', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply('⚠️ : عذرا كود التحقق خاطئ .. الرجاء المحاوله من جديد .', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, ' 👨‍💻 يحتوى حسابك علي رمز التحقق بخطوتين ... الرجاء ارسال باسوورد حسابك .,' ,filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply('⚠️ عذرا انتهي وقت الانتظار 5 دقائق .. اارجاء المحاوله مجددا .', reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply('⚠️ : عذرا قد ادخلت كلمه مرور غير صحيحه .. الرجاء المحاوله مجددا .', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"**{ty.upper()} STRING SESSION** \n\n`{string_session}` \n\nGenerated by @em_source"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, "Successfully generated {} string session. \n\nPlease check your saved messages! \n\nBy @em_source".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("🚫 : تم الغاء الاستخراج بنجاح !", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("تم اعادة تشغيل البوت بنجاح ♻️", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
 
