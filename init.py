import win32api
import time
import pickle

coords = {}

n=input('setting coordinates, press any key if ready')

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
print('icon coordinates configured')


n = int(input('enter coins to flip'))

f = open('userdata.bin','wb')

#coords ,coins allowed to spend,{item:[how much current offer]} {item:[bought for how much]},{item:[sold for how much],}
user = [coords,n,{},{},{}]
pickle.dump()
