import pickle
import pytesseract
import pyautogui
import win32api, win32con
import time
import PIL
import urllib.request

def click(coord):
    win32api.SetCursorPos(coord)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def clean(lis):
    for i in lis:
        if i == '':
            lis.remove(i)
    return lis

def cleanNum(lis):
    cleanLis = []
    for i in lis:
        if i != '':
            a = ''
            for j in i:
                if j.isdigit() or j=='.':
                    a+=j
            if a!= '':
                cleanLis.append(a)

    return cleanLis

def ScreenshotMarket():
    
    nameSS = pyautogui.screenshot(region=(coords['market-nametopleft'][0],coords['market-nametopleft'][1],coords['market-namebottomright'][0]-coords['market-nametopleft'][0],coords['market-namebottomright'][1]-coords['market-nametopleft'][1]))
    name = clean(pytesseract.image_to_string(nameSS).split('\n'))

    sellSS = pyautogui.screenshot(region=(coords['market-soldtopleft'][0],coords['market-soldtopleft'][1],coords['market-soldbottomright'][0]-coords['market-soldtopleft'][0],coords['market-soldbottomright'][1]-coords['market-soldtopleft'][1]))
    sell = cleanNum(pytesseract.image_to_string(sellSS).split('\n'))

    buySS = pyautogui.screenshot(region=(coords['market-boughttopleft'][0],coords['market-boughttopleft'][1],coords['market-boughtbottomright'][0]-coords['market-boughttopleft'][0],coords['market-boughtbottomright'][1]-coords['market-boughttopleft'][1]))
    buy = cleanNum(pytesseract.image_to_string(buySS).split('\n'))

    profitSS = pyautogui.screenshot(region=(coords['market-profittopleft'][0],coords['market-profittopleft'][1],coords['market-profitbottomright'][0]-coords['market-profittopleft'][0],coords['market-profitbottomright'][1]-coords['market-profittopleft'][1]))
    profit = cleanNum(pytesseract.image_to_string(profitSS).split('\n'))

    res = {}
    n = len(buy)

    for i in range(n):
        res[name[i*2]]=(float(sell[i]),float(buy[i]),float(profit[i]))

    return res

#initialising 
f = open('userdata.bin','rb')
userdata = pickle.load(f)
f.close()
if userdata!= None:
    coords = userdata[0]
else:
    import init
    f = open('userdata.bin','rb')
    coords = init.coords
    userdata = init.user

items = {}



a = ScreenshotMarket()
for i in a:
    print(i,':',a[i])