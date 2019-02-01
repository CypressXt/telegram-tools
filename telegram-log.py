#!/usr/bin/python
import requests, json, sys, datetime

telegram_url="https://api.telegram.org/bot"
bot_token="XXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
chat_id="XXXXXXXXXXXXX"

# Send a text message ----------------------------------------------------------
def send_message(chat_id,title, text, parse_mode="HTML", disable_notification="false"):
    url = telegram_url+bot_token+"/sendMessage"
    title = title+" - "+datetime.datetime.now().strftime("%A %d %B %y | %H:%M:%S")
    text = "<strong>"+title+"""</strong>
"""+text
    req = requests.post(url, data={'chat_id':chat_id, 'text':text, 'parse_mode':parse_mode,'disable_notification':disable_notification})
    return req.status_code
# ------------------------------------------------------------------------------

# Args management --------------------------------------------------------------
def handle_args():
    args_lenght = len(sys.argv)
    if (args_lenght < 3):
        print "usage: telegram-log title message notifEN"
        sys.exit(1)
    else:
        title = sys.argv[1]
        message = sys.argv[2]
        notif = sys.argv[3]
        send_message(chat_id,title, message, "HTML", notif)
#-------------------------------------------------------------------------------
handle_args()
