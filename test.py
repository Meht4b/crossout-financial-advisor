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
    for string in lis:
        if string =='':
            continue
        a = ''
        decimalflag = True
        negativeflag = True
        for i in string:
            if i.isdigit():
                a+= i
            elif i == '-' and negativeflag:
                a+=i
                negativeflag = False
            
            elif i=='.' and decimalflag:
                a+=i
                flag = False
            else:
                break
        if a!='':
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

        res[name[i*2]]=(sell[i],buy[i],profit[i])

    return res

def move(lis:list,sleep:int):
    global coords
    for i in lis:
        click(coords[i])
        time.sleep(sleep)

def init():
    try:
        f = open('usercoords.bin','rb')
        coords = pickle.load(f)
    except:
        import init
        coords = init.coords
    
    return coords

def scraper(pages:int,category:str,rarity:list,sortby:str):

    move(['garage','market','market-reset',category]+rarity+[sortby],3)
    win32api.SetCursorPos((0,0))
    time.sleep(0.5)
    res = {}
    for i in range(pages):
        res.update(ScreenshotMarket())
        move(['market-next'],3)
    return res

coords = init()

a = scraper(3,'market-weapon',['market-epic','market-rare','market-special'],'market-profit')
for i in a:
    print(i,':',a[i])