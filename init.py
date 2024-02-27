import win32api
import time
import pickle

coords = {}

print('hover over market icon in 2 seconds')
time.sleep(2)
coords['market']=win32api.GetCursorPos()

print('hover over storage icon in 2 seconds')
time.sleep(2)
coords['storage']=win32api.GetCursorPos()

print('enter market')
time.sleep(2)

print('hover over parts icon in 2 seconds')
time.sleep(2)
coords['parts']=win32api.GetCursorPos()

print('hover over my offers icon in 2 seconds')
time.sleep(2)
coords['myOffers']=win32api.GetCursorPos()

print('hover over history icon in 2 seconds')
time.sleep(2)
coords['history']=win32api.GetCursorPos()

f = open('userdata.bin','wb')
pickle.dump(coords,f)
