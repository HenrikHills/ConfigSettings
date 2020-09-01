import os, inspect
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
user_input = askopenfilename()

with open(user_input, encoding="utf-8") as f:
     oldList = f.readlines()

bad_words = [' ', ';', ':']

oldList = [x for x in oldList if not x.startswith('#')]

decision = input("Remove \"0.0.0.0\" and spaces from list? Y/N \n")
if decision.upper() == "Y":
    print("Removing ... ")
    oldList = [w.replace("0.0.0.0 ", "").replace('\t', "").replace("127.0.0.1 ", "") for w in oldList]
else:
    print("Not removing \"0.0.0.0\"")



# Make new clean list
newList = list(dict.fromkeys(oldList))
newList.sort()

filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

with open(path + '\\no_duplicates.txt', 'w', encoding="utf-8") as filehandle:
    for line in newList:

        # Remove all lines with spaces in them (many are duplicate...)
        if not any(bad_words in line for bad_words in bad_words):
            filehandle.write('%s' % line)

print("Saved file with no duplicates here: \t"+ path +"\\no_duplicates.txt")