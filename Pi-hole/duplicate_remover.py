dirty=open("C:\Users\henri\Desktop\list.txt", "r")
fugly = dirty.read()

with open("C:\Users\henri\Desktop\list.txt") as f:
     content = f.readlines()

clean = list(dict.fromkeys(content))
clean.sort()

with open('C:\Users\henri\Desktop\\no_duplicates.txt', 'w') as filehandle:
    for listitem in clean:
        filehandle.write('%s' % listitem)