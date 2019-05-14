# ZPACK
zpack is a collection of simple functions that I use commonly.
It's a few very small homemade functions to cut down on typing time and line usage.
Nothing fancy all the functions are extremely basic and can be improved upon.
No idea how github works and hopes this allows me to use my functions on school computers.

## Installation and usage
Currently there isn't a setup file but it's really easy to use.
You can either put it in the same folder as the script your writing is in or you can put it in the Lib folder.
Just find the python folder and put in the Lib folder. Pretty simple.
Importing in a script should be just like this:
```python
import zpack
```
Unless you changed the script name of course.

# Functions and Variables

usable = All characters from strings lib but whitespace.

osuser = Easy access to the currently logged on user so you won't need to make a variable and can user it in paths.

ln = Prints an empty line. Supposed to cut down typing time for text based programs.

abscheck = Returns true if int/float is negative returns false if positive.

shuffle = Shuffles a list using random. X parameter is the number of times the function takes an item and moves it.
```python
import zpack as z
list = [1,2,3,4,5]
print(z.shuffle(list))
```
output would be a scrambled version of the list var

move = Moves the index x to index y in list.

isint = Compares x to 1 and returns true if x is an int.

isnum = Returns true if an int or a float, return false if neither.

removedups = Remove duplicate items in a list.

reverse = Reverse a string.

clear = Clear the console. Doesn't work in some cases like running the script in IDLE.

listgen = Generates a new list from random items in the parent parameter and has the length of the length parameter.
```python
import zogpack as z
import random
items = ["sword","potion","rock","stick","shield"]

chest = z.listgen(items,random.choice([2,3,4]))
print(chest)
```

# Notes
Pull requests are welcome :D
Obviously more functions are coming soon.
Thanks for looking!
