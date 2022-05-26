#f = open("new.txt", "r")
#print(f.read())
#print(f.readline())

#for x in f:
    #print (x)

#f.close()

import os
if os.path.exists("new.txt"):
    os.remove("new.txt")
else:  
    print("File does not exist")