import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "20263428") #⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "f9dc42564f6e6eb9920912b09f729e3f") #⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5929288082:AAEu_0romVWR3NEOKVxnz45w_Oe2KLrjx0k") #⚠️ Required
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Ai_Hoshino")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Luciferbin:9339119160@cluster0.kmbiojj.mongodb.net/?retryWrites=true&w=majority") #⚠️ Required
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/46d198cdb447619e45e52.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()] #⚠️ Required
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Hentaii_flix") #⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001944217427")) #⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hᴀɪ {} 👋,
Tʜɪs Is Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ
Usɪɴɢ Tʜɪs Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ & Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oꜰ Yᴏᴜʀ Fɪʟᴇ
Yᴏᴜ Cᴀɴ Aʟsᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ & Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ
Tʜɪs Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛs Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 <b>ᴍy ɴᴀᴍᴇ</b> : {}
├👨‍💻 <b>Pʀᴏɢʀᴀᴍᴇʀ</b> : <a href=http://telegram.me/Lucifer_x0o>ᴀʙʀᴀʜᴀᴍ™ [𝕃𝕠𝕤𝕥]</a>
├👑 <b>Instagram</b> : <a href=https://www.instagram.com/hanime_flix?igsh=MWFxOXVxOTBjcnZvdA==>Hᴀɴɪᴍᴇ_Fʟɪx</a> 
├☃️ <b>ꜰᴏᴜɴᴅᴇʀ ᴏꜰ</b> : <a href=https://t.me/Anime_Flix_Network>Fʟɪx Nᴇᴛᴡᴏʀᴋ</a>
├📕 <b>Lɪʙʀᴀʀy</b> : <a href=https://github.com/pyrogram>Pʏʀᴏɢʀᴀᴍ</a>
├✏️ <b>Lᴀɴɢᴜᴀɢᴇ</b> : <a href=https://www.python.org>Pʏᴛʜᴏɴ 3</a>
├💾 <b>Dᴀᴛᴀ Bᴀꜱᴇ</b> : <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ Dʙ</a>
├🌀 <b>ᴍʏ ꜱᴇʀᴠᴇʀ</b> : <a href=https://dashboard.heroku.com>Hᴇʀᴏᴋᴜ</a>
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.
📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>
<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}
✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
❗ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=http://telegram.me/Lucifer_x0o><b>Sᴜᴘᴘᴏʀᴛ</b></a>
"""


    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
