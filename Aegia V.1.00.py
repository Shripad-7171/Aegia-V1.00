import datetime

import datetime

n = datetime.datetime.now()

n = n.strftime("%d%m20%y")

import datetime

from pyautogui import printInfo

k = datetime.datetime.now()

c = int(k.strftime("%d"))
b = int(k.strftime("%m"))
a = int(k.strftime("20%y"))

week_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
week_num = datetime.date(a, b, c).weekday()
day = week_days[week_num]
print(day)
day = str(day)

day = str(day)

time = int(datetime.datetime.now().strftime("%H%M"))
print(time)

import pyautogui


def english():
    pyautogui.press("e")
    pyautogui.press("e")
    pyautogui.click(1660, 364, duration=1)


def sanskrit():
    pyautogui.press("s")
    pyautogui.click(1660, 364, duration=1)


def economics():
    pyautogui.press("e")
    pyautogui.click(1660, 364, duration=1)


def maths():
    pyautogui.press("m")
    pyautogui.press("m")
    pyautogui.click(1660, 364, duration=1)


def physics():
    pyautogui.press("p")
    pyautogui.press("p")
    pyautogui.click(1660, 364, duration=1)


def geography():
    pyautogui.press("g")
    pyautogui.click(1660, 364, duration=1)


def chemistry():
    pyautogui.press("c")
    pyautogui.click(1660, 364, duration=1)


def history():
    import pyautogui

    import datetime

    n = datetime.datetime.now()
    n = n.strftime("%d%m20%y")
    print(n)

    k = datetime.datetime.now()
    c = int(k.strftime("%d"))
    b = int(k.strftime("%m"))
    a = int(k.strftime("20%y"))

    week_days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    week_num = datetime.date(a, b, c).weekday()
    day = week_days[week_num]
    print(day)
    day = str(day)

    time = int(datetime.datetime.now().strftime("%H%M"))
    print(time)

    pyautogui.press("h")
    pyautogui.press("h")
    pyautogui.click(1660, 364, duration=1)

    pyautogui.click(1775, 21, duration=1)
    pyautogui.click(1775, 21, duration=1)
    pyautogui.click(1775, 21, duration=1)
    pyautogui.doubleClick(1569, 39, duration=1)
    pyautogui.click(1725, 615, duration=3)
    pyautogui.click(1730, 637, duration=1.5)
    pyautogui.click(132, 461, duration=3)
    pyautogui.click(189, 510, duration=3)
    pyautogui.click(471, 271, duration=3)
    pyautogui.click(627, 329, duration=3)
    pyautogui.click(800, 359, duration=2)
    pyautogui.write(n, interval=1)
    pyautogui.click(1157, 365, duration=1)
    pyautogui.write(n, interval=1)
    pyautogui.click(1657, 362, duration=1)
    pyautogui.click(1470, 367, duration=1)

    pyautogui.press("d")
    pyautogui.press("d")
    pyautogui.click(1660, 364, duration=1)


def biology():
    pyautogui.press("b")
    pyautogui.click(1660, 364, duration=1)


def tabla():
    pyautogui.press("t")
    pyautogui.click(1660, 364, duration=1)


def end():
    pyautogui.rightClick(582, 1053, duration=1)
    pyautogui.click(515, 992, duration=1)


def notch():
    pyautogui.click(1775, 21, duration=1)
    # esc from code
    pyautogui.doubleClick(1569, 39, duration=2)
    # in entab
    pyautogui.click(1725, 615, duration=5)
    # sign in 1
    pyautogui.click(1730, 637, duration=5)
    # sign in 2
    pyautogui.click(132, 461, duration=5)
    # academic
    pyautogui.click(189, 510, duration=5)
    # assignment
    pyautogui.click(471, 271, duration=5)
    # homework
    pyautogui.click(627, 329, duration=5)
    # activity
    pyautogui.click(800, 359, duration=5)
    # movetodate1
    pyautogui.write(n, interval=1)
    # movetodate2
    pyautogui.click(1157, 365, duration=1)
    # date2
    pyautogui.write(n, interval=1)
    # subselect
    pyautogui.click(1479, 368, duration=2)


first = 850
second = 950
third = 1050
fourth = 1150
fifth = 1250
sixth = 1350

first_end = 910
second_end = 1010
third_end = 1110
fourth_end = 1210
fifth_end = 1310

if day == "Monday" and first < time < first_end:
    notch()
    english()
elif day == "Monday" and second < time < second_end:
    end()
    notch()
    sanskrit()
elif day == "Monday" and third < time < third_end:
    end()
    notch()
    economics()
elif day == "Monday" and fourth < time < fourth_end:
    end()
    notch()
    maths()
elif day == "Monday" and fifth < time < fifth_end:
    end()
    notch()
    physics()
elif day == "Tuesday" and first < time < first_end:
    notch()
    english()
elif day == "Tuesday" and second < time < second_end:
    end()
    notch()
    sanskrit()
elif day == "Tuesday" and third < time < third_end:
    end()
    notch()
    physics()
elif day == "Tuesday" and fourth < time < fourth_end:
    end()
    notch()
    geography()
elif day == "Tuesday" and fifth < time < fifth_end:
    end()
    notch()
    maths()
elif day == "Wednesday" and first < time < first_end:
    notch()
    sanskrit()
elif day == "Wednesday" and second < time < second_end:
    end()
    notch()
    english()
elif day == "Wednesday" and third < time < third_end:
    end()
    notch()
    chemistry()
elif day == "Wednesday" and fourth < time < fourth_end:
    end()
    notch()
    geography()
elif day == "Wednesday" and fifth < time < fifth_end:
    end()
    notch()
    maths()
elif day == "Thursday" and first < time < first_end:
    notch()
    english()
elif day == "Thursday" and second < time < second_end:
    end()
    notch()
    sanskrit()
elif day == "Thursday" and third < time < third_end:
    end()
    notch()
    chemistry()
elif day == "Thursday" and fourth < time < fourth_end:
    end()
    notch()
    history()
elif day == "Thursday" and fifth < time < fifth_end:
    end()
    notch()
    maths()
elif day == "Friday" and first < time < first_end:
    notch()
    english()
elif day == "Friday" and second < time < second_end:
    end()
    notch()
    sanskrit()
elif day == "Friday" and third < time < third_end:
    end()
    notch()
    biology()
elif day == "Friday" and fourth < time < fourth_end:
    end()
    notch()
    history()
elif day == "Friday" and fifth < time < fifth_end:
    end()
    notch()
    maths()
elif day == "Saturday" and first < time < first_end:
    notch()
    english()
elif day == "Saturday" and second < time < second_end:
    end()
    notch()
    tabla()
elif day == "Saturday" and third < time < third_end:
    end()
    notch()
    biology()
elif day == "Saturday" and fourth < time < fourth_end:
    end()
    notch()
    history()
elif day == "Saturday" and fifth < time < fifth_end:
    end()
    notch()
    maths()
elif fifth_end < time:
    notch()
    jaja = input("friend-")

pyautogui.click(1656, 364, duration=1)
pyautogui.click(1205, 505, duration=1)

import pyautogui
import time

time.sleep(3)

hari = pyautogui.locateOnScreen("C:\python\Aegia Version 1\su1.png")
radha = pyautogui.locateOnScreen("C:\python\Aegia Version 1\ind1.png")

if hari != None:
    pyautogui.click(hari)
elif radha != None:
    pyautogui.click(radha)
else:
    op = input("waiting")

import pyautogui
import time

time.sleep(3)

jaimata = pyautogui.locateOnScreen("C:\python\Aegia Version 1\pak1.png")
if jaimata != None:
    pyautogui.click(jaimata)
else:
    paja = input("waiting")

time.sleep(5)

import pyautogui
import time

time.sleep(5)

long= pyautogui.locateOnScreen('C:\python\Aegia Version 1\llstu1.png')

if long != None:
    pyautogui.click(long)
else:
    print('problem - ')

time.sleep(5)

live= pyautogui.locateOnScreen('C:\python\Aegia Version 1\c1.png')

if live != None:
    pyautogui.click(live)
else:
    print('problem - ')






















def end():
    pyautogui.rightClick(582, 1053, duration=1)
    pyautogui.click(515, 992, duration=1)


king = input("")
if king == "end":
    end()
else:
    print("please type end")
