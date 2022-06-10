import pywhatkit
import pyautogui
import requests
import json
import time
import datetime
import schedule
from tkinter import *

win = Tk()
# Gets the resolution (width) and (height) of your monitor
screen_width = win.winfo_screenwidth() 
screen_height= win.winfo_screenheight()

#User input for who they'll be sending the message to and at what interval
targetOption = int(input("Where do you want to send this messeges to?\n\n1. Groups\n2. Contact\nChoose on of the option above => "))
if targetOption == 1:
    target = str(input("Please enter the group name : "))
elif targetOption == 2:
    target = str(input("Please enter the target WhatsApp number (+628...) : "))
interval = int(input("Please enter the delay duration (in  minutes) : "))

#A function to send the quote
def sendQuote():
    #getting date and time
    now = datetime.datetime.now()
    #sending request to the API provider
    requestSent = requests.get('https://animechan.vercel.app/api/random')
    response = json.loads(requestSent.content)
    quote = response['quote']

    #sending the quote based on who the target is
    if targetOption == 1:
        pywhatkit.sendwhatmsg_to_group_instantly(target, quote, now.hour, now.minute + 1)
    elif targetOption == 2:
        pywhatkit.sendwhatmsg(target, quote, now.hour, now.minute + 1)

    #Moves the cursor to the message bar in WhatsApp, click it, and hit enter
    pyautogui.moveTo(screen_width * 0.694, screen_height* 0.964)
    pyautogui.click()
    pyautogui.press('enter')

#schedule how the quotes will be send in the future (only for contact)
schedule.every(interval).minutes.do(sendQuote)

while True:
    schedule.run_pending()
    #time.sleep won't work on Group option
    time.sleep(1)