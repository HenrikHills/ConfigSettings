import os, inspect
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
user_input = askopenfilename()

with open(user_input) as f:
     content = f.readlines()

clean = list(dict.fromkeys(content))
clean.sort()

filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

with open(path + '\\no_duplicates.txt', 'w') as filehandle:
    for listitem in clean:
        filehandle.write('%s' % listitem)

print("Saved file with no duplicates here: "+ path +"\\no_duplicates.txt")