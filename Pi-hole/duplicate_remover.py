import sys
import os
import inspect

user_input = raw_input("Enter the path of your file:\n")

assert os.path.exists(user_input), "\nI did not find the file at, "+str(user_input)

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