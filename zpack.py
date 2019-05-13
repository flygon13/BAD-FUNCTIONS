import string
import random as ran
import pyautogui,time,os,winsound

# More functions soon!
 
__all__ = ["usable","ln","abscheck","shuffle","move","isint","keyPress","removedups","reverse","clear","osuser","countdown"]

## epic public variables ##
usable = string.digits + string.ascii_letters + string.punctuation
osuser = os.getlogin()
####################
        
def ln():
    print("")#built for from zogpack import *
    
def abscheck(x):
    if abs(x) == int(x):
        return False #It's positive
    elif abs(x) != int(x):
        return True #It's negative

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def move(x,y,table):
    removed = table[x]
    table.pop(x)
    table.insert(int(y),removed)

def isint(x):
    if type(x) == type(1):
        return True
    else:
        return False

def shuffle(x,table):
    try:
        if x == 0:
            print("Can't shuffle 0 times, it's pointless")
        else:
            for y in range(x):
                i = ran.randint(0,len(table)-1)
                p = ran.randint(0,len(table)-1)
                move(i,p,table)
    except TypeError:
        print("Invalid argument. X is required to be int, got {}".format(type(x)))

def removedups(mylist):
    return list(dict.fromkeys(mylist))

def reverse(s):
  e = "" 
  for i in s: 
    e = i + e
  return e

def countdown(minutes,seconds,soundtoggle):
    m = minutes * 60
    s = seconds + m
    print("countdown set for {} minutes and {} seconds".format(minutes,seconds))
    while s != 0:
        time.sleep(1)
        s -= 1
    if soundtoggle == True:
        winsound.beep(1,1000)
        print("COUNTDOWN COMPLETED")
    else:
        print("COUNTDOWN COMPLETED")
    


