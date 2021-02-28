import ptbot
from pytimeparse import parse
token="1594751729:AAEZd4HdD1WVf1AHaDty3oU8rkzJ1w0ZwmM"
chatid="367392748"



def notify():
    bot.up(chatid, "Times up")

def notify_progress(secs_left):
    message_id = bot.send_message(chatid, secs_left)
    
def reply(text):
    time=parse(text)
    timerr=str(time)
    msg= "Timer set on "+ timerr +" seconds"
    bot.send_message(chatid, msg)
    bot.create_countdown(time, notify_progress)
    bot.create_timer(time, notify)

bot=ptbot.Bot(token)
bot.send_message(chatid, 'How much time do you want?')
bot.reply_on_message(reply)

bot.run_bot()
