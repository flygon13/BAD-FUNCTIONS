import string
import random as ran
import pyautogui,time,os,winsound

# usable -- VAR -- All characters but whitespace. For passwords and crap.
# ln -- FN -- Prints an empty line. Supposed to cut down typing time for text based programs.
# abscheck -- FN -- Returns True or False depending if the abs() of x is the same as x. Intended to check if x is a negative to make adding different paths in programs easier.
# shuffle -- FN -- shuffles a table like a deck of cards. x = number of times a random item is moved to a random place.
# move -- FN -- moves the index,x, to index y in table.
# isint -- FN -- returns false is x is not an int, returns true if x is an int. Compares x to 1.
# keyPress -- FN -- Wrap for pyautogui's keyDown() and keyUp() like pyautogui's press function but key is held down for the interval parameter
# removedups -- FN -- remove duplicate items in a list
# reverse -- FN -- reverse a string
# clear -- FN -- clear the console
# osuser -- VAR -- easy access to the currently logged on user so you won't need to make a variable and can user it in paths
 
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

def keyPress(key,interval):
    py.keyDown(key)
    time.sleep(interval)
    py.keyUp(key)

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
    


