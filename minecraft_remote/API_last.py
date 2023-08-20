user_input = input("表示する秒数を指定してください")
try:
    kaisu= float(user_input)
    print("入力された数字は:", kaisu)
except ValueError:
    print("数字を入力してください。") 


import math

# 小数点以下を切り捨てる
kaisu = math.floor(kaisu) 
# 消したらダメなやつ
from mcje.minecraft import Minecraft
import param_MCJE as param
mc = Minecraft.create(port=param.PORT_MC)
mc.setBlocks (0, 0, 0,  0, 10, 0,  param.cyan_terracotta)
# 座標
x=0
z=0
y=4

def c0():
  mc.setBlocks(x+1, y, z,  x+5, y, z,  block)
  print(0)

def c1():
  mc.setBlocks (x+1, y, z+1,  x+2, y, z+1,  block)
  mc.setBlocks (x+3, y, z+2,  x+4, y, z+2,  block)
  mc.setBlocks (x+5, y, z+3,  x+5, y, z+3,  block)
  print(1)

def c2():
  mc.setBlocks (x+1, y, z+1,  x+1, y, z+2,  block)
  mc.setBlocks (x+2, y, z+3,  x+2, y, z+4,  block)
  mc.setBlocks (x+3, y, z+5,  x+3, y, z+5,  block)
  print(2)

def c3():
  mc.setBlocks(z, y, x+1,  z, y, x+5,  block)
  print(0)

def c4():
  mc.setBlocks (x-1, y, z+1,  x-1, y, z+2,  block)
  mc.setBlocks (x-2, y, z+3,  x-2, y, z+4,  block)
  mc.setBlocks (x-3, y, z+5,  x-3, y, z+5,  block)
  print(2)

def c5():
  mc.setBlocks (x-1, y, z+1,  x-2, y, z+1,  block)
  mc.setBlocks (x-3, y, z+2,  x-4, y, z+2,  block)
  mc.setBlocks (x-5, y, z+3,  x-5, y, z+3,  block)
  print(1)

def c6():
  mc.setBlocks(x-1, y, z,  x-5, y, z,  block)
  print(0)

def c7():
  mc.setBlocks (x-1, y, z-1,  x-2, y, z-1,  block)
  mc.setBlocks (x-3, y, z-2,  x-4, y, z-2,  block)
  mc.setBlocks (x-5, y, z-3,  x-5, y, z-3,  block)
  print(1)

def c8():
  mc.setBlocks (x-1, y, z-1,  x-1, y, z-2,  block)
  mc.setBlocks (x-2, y, z-3,  x-2, y, z-4,  block)
  mc.setBlocks (x-3, y, z-5,  x-3, y, z-5,  block)
  print(2)

def c9():
  mc.setBlocks(z, y, x-1,  z, y, x-5,  block)
  print(0)

def c11():
  mc.setBlocks (x+1, y, z-1,  x+2, y, z-1,  block)
  mc.setBlocks (x+3, y, z-2,  x+4, y, z-2,  block)
  mc.setBlocks (x+5, y, z-3,  x+5, y, z-3,  block)
  print(1)

def c10():
  mc.setBlocks (x+1, y, z-1,  x+1, y, z-2,  block)
  mc.setBlocks (x+2, y, z-3,  x+2, y, z-4,  block)
  mc.setBlocks (x+3, y, z-5,  x+3, y, z-5,  block)
  print(2)

def air():
   
   mc.setBlocks (-5, y, -5,  +5, y+3, +5,  param.AIR)

for i in range(kaisu):
 y=4
 import datetime
 import time
 current_datetime = datetime.datetime.now()
 # 日付、時間、分、秒をそれぞれの変数に格納
 year = current_datetime.year
 month = current_datetime.month
 day = current_datetime.day
 hour = current_datetime.hour
 minute = current_datetime.minute
 second = current_datetime.second

 block=param.red_concrete
 y=y+2
 print(hour)
 # 時間
 if hour in(0,12):
  c0() 
  
 if hour in(1,13):
  c1()
 
 if hour in(2,14):
  c2()
 
 if hour in(3,15):
  c3()
  
 if hour in(4,16):
  c4() 
 
 if hour in(5,17):
  c5() 
 
 if hour in(6,18):
  c6()

 if hour in(7,19):
  c7()
 
 if hour in(8,20):
  c8()
 
 if hour in(9,21):
  c9()
  
 if hour in(10,22):
  c10()

 if hour in(11,23):
  c11() 
 block=param.blue_concrete
 y=y-1
 # 分
 

 if 0<minute<5:
  c0() 
  
 if 5<minute<10:
  c1() 
 
 if 10<minute<15:
  c2() 
 
 if 15<minute<20:
  c3() 
  
 if 20<minute<25:
  c4() 
 
 if 25<minute<30:
  c5()  
 
 if 30<minute<35:
  c6() 
  
 if 35<minute<40:
  c7() 
 
 if 40<minute<45:
  c8() 
 
 if 45<minute<50:
  c9() 
  
 if 50<minute<55:
  c10() 
 
 if 55<minute<60:
  c11() 

# 秒
 y=y-1
 block=param.green_concrete
 if 0<second<5:
  c0()  
 if 5<second<10:
  c1()  
 if 10<second<15:
  c2()  
 if 15<second<20:
  c3()   
 if 20<second<25:
  c4()  
 if 25<second<30:
  c5()  
 if 30<second<35:
  c6()   
 if 35<second<40:
  c7()  
 if 40<second<45:
  c8()  
 if 45<second<50:
  c9()   
 if 50<second<55:
  c10()  
 if 55<second<60:
  c11() 
 time.sleep(1)
 air()