# - أسْتَغْفِرُكَ رَبِّي و أَتُوبُ إِلَيْك @L9LLL .

from telethon.tl.functions.messages import GetMessagesViewsRequest
import sys, asyncio
import IqArab
from IqArab import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from telethon import functions
from .Config import Config
from .core.logger import logging
from .core.session import iqthon
from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup
LOGS = logging.getLogger("سورس الامراء")
print(IqArab.__copyright__)
print("المرخصة بموجب شروط " + IqArab.__license__)
cmdhr = Config.COMMAND_HAND_LER
try:
    LOGS.info("بدء تنزيل سورس الامراء")
    iqthon.loop.run_until_complete(setup_bot())
    LOGS.info("بدء تشغيل البوت")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()
class CatCheck:
    def __init__(self):
        self.sucess = True
Catcheck = CatCheck()
async def startup_process():
    async def MarkAsViewed(channel_id):
        from telethon.tl.functions.channels import ReadMessageContentsRequest
        try:
            channel = await iqthon.get_entity(channel_id)
            async for message in iqthon.iter_messages(entity=channel.id, limit=0):
                try:
                    await iqthon(GetMessagesViewsRequest(peer=channel.id, id=[message.id], increment=True))
                except Exception as error:
                    print ("🔻")
            return True

        except Exception as error:
            print ("🔻")

    async def start_bot():
      try:
          List = ["C45CS","C35CS","T9_10","zzzzrq","G8_10"]
          from telethon.tl.functions.channels import JoinChannelRequest
          for id in List :
              Join = await iqthon(JoinChannelRequest(channel=id))
              print ("🔻")
          return True
      except Exception as e:
        print("🔻")
        return False
    
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print(f"<b> 🔱 اهلا بك لقد نصبت سورس الامراء بنجاح ☸️ اذهب الى قناتنا لمعرفة المزيـد 🔆. </b>\n CH : https://t.me/C45CS ")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    
    Checker = await start_bot()
    if Checker == False:
        print("#1")
    else:
        print ("🔻")
    
    return


iqthon.loop.run_until_complete(startup_process())
    
if len(sys.argv) not in (1, 3, 4):
    iqthon.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        iqthon.run_until_disconnected()
    except ConnectionError:
        pass
