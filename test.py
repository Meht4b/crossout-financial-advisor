import pickle
import pytesseract
import pyautogui
import win32api, win32con
import time
import PIL

def click(coord):
    win32api.SetCursorPos(coord)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


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


click(coords['market'])
time.sleep(3)
screenshot = pyautogui.screenshot(region=(coords['market-topleft'][0],coords['market-topleft'][1],coords['market-bottomright'][0]-coords['market-topleft'][0],coords['market-bottomright'][1]-coords['market-topleft'][1]))
a =pytesseract.image_to_string(screenshot).split('\n')
for i in a:
    if i == '':
        a.remove('')
