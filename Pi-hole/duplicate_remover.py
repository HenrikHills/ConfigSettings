import os, inspect
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
user_input = askopenfilename()

with open(user_input, encoding="utf-8") as f:
     content = f.readlines()


content = [x for x in content if not x.startswith('#')]

decision = input("Remove \"0.0.0.0\" from list? Y/N\n")
if decision.upper() == "Y":
    print("Removing ... ")
    content = [w.replace("0.0.0.0", "").replace('\t', "").replace("127.0.0.1", "") for w in content]
else:
    print("Not removing \"0.0.0.0\"")

clean = list(dict.fromkeys(content))
clean.sort()

filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))

with open(path + '\\no_duplicates.txt', 'w', encoding="utf-8") as filehandle:
    for listitem in clean:
        filehandle.write('%s' % listitem)

print("Saved file with no duplicates here: \t"+ path +"\\no_duplicates.txt")