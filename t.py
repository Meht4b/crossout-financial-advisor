'''import pickle
import win32con,win32api
import time

f = open('usercoords.bin','rb')
coords = pickle.load(f)
time.sleep(3)
coords['garage']=win32api.GetCursorPos()
f.close()
f = open('usercoords.bin','wb')
pickle.dump(coords,f)'''

