import win32api
import time
import pickle
import win32con


#ignore
coords = {}



n=input('setting coordinates, press any key if ready')
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on garage icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['garage']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on market icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

coords['storage']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on my offers icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-myoffers']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on history icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-history']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on parts icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-parts']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on common rarity icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-common']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on rare rarity icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-rare']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on special rarity icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-special']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on epic rarity icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-epic']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on legendary rarity icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-legendary']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on cabin category icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-cabin']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on weapon category icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-weapon']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on hardware category icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-hardware']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on wheels category icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-wheels']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on all category icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-all']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on profit icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-profit']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on popularity icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-popularity']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on sold for icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-sellprice']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on offers icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-saleoffers']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on bought for icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-buyprice']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on orders icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-buyorders']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on next page icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-next']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on previous icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-previous']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on search icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-search']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on reset icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-reset']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on name top left')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-nametopleft']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on name bottom right ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-namebottomright']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on sold for top left')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-soldtopleft']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on sold for bottom right ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-soldbottomright']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on bought for top left')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-boughttopleft']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on bought for bottom right ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-boughtbottomright']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on profit top left')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-profittopleft']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on profit bottom right ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['market-profitbottomright']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break


print('click on storage icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['storage']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break


print('click on common rarity icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['storage-common']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on rare rarity icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['storage-rare']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on special rarity icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['storage-special']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on epic rarity icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['storage-epic']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on legendary rarity icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['storage-legendary']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on cabin category icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['storage-cabin']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on weapon category icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['storage-weapon']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on hardware category icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['storage-hardware']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on wheels category icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['storage-wheels']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on all category icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['storage-all']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('click on search icon ')
while True:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break
coords['storage-search']=win32api.GetCursorPos()
while True:
    if not win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        break

print('icon coordinates configured')

coinInvest = int(input('enter coins to flip'))
minBuyOrder = int(input('enter min no. of buy orders'))
minSellOrder = int(input('enter min no. of sell offers'))
minDemandSupply=int(input('enter min demand/supply ratio'))

f = open('usercoords.bin','wb')

#coords ,coins allowed to spend,{item:[how much current offer]} {item:[bought for how much]},{item:[sold for how much],}
user = [coords,coinInvest,minBuyOrder,minSellOrder,minDemandSupply]
pickle.dump(coords,f)
