import pyautogui as pg
import time
import datetime
import pyperclip
import pymsgbox
from playsound import playsound

pg.FAILSAFE = False

# this is a dictionary about the number of a particular month
monthDict = {
    1:"Jan",
    2:"Feb",
    3:"Mar",
    4:"Apr",
    5:"May",
    6:"Jun",
    7:"Jul",
    8:"Aug",
    9:"Sep",
    10:"Oct",
    11:"Nov",
    12:"Dec"
}

# creating a function that will run until a buyer request shows up

def request():
    time.sleep(10)

    width = pg.size().width;
    height = pg.size().width;

    pg.moveTo(width/16.38, height/1.66) # the coordinates where mouse will move
    current_date = datetime.datetime.now()
    month = current_date.strftime("%m")

    month = month.replace("0", "")
    month = int(month)
    monthName = monthDict.get(month)

    print(monthName)

    time.sleep(1)

    pg.doubleClick()
    pg.hotkey("ctrl", "c")

    if monthName in pyperclip.paste():
        pyperclip.copy("")
        playsound("play-music.mp3")
        pymsgbox.alert(title="Requests Found", text="Requests Found on Fiverr !! Check Them Now")

    else:
        pg.hotkey("ctrl", "r")
        print("No Requests Found")

        request()


request()
