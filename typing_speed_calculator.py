
from time import *
import random as r
def mistake(partest,usertest):
  error=0
  for a in range(len(partest)):
    try:
        if partest[a]!=usertest[a]:
            error=error+1
    except:
          error=error+1
  return error
def speed_time(time_s,time_e,userinput):
  time_d=time_e-time_s
  time_r=round(time_d,2)
  speed=(len(userinput))/time_r
  return round(speed,2)
while True:
  ck=input("ready to test:yes/no:")
  if ck=="yes":


   test=["A paragraph is a self-contained unit of discourage in windows","this is our python class", " welcome to python universe"]
   test1=r.choice(test)
   print("*****Typing speed***")
   print(test1)
   time_1=time()
   testinput=input("enter:")
   time_2=time()
   print("speed:",speed_time(time_1,time_2,testinput))
   print("error:",mistake(test1,testinput))
  elif ck=="no":
    print("thank you")
    break
  else:
    print("invalid input")
