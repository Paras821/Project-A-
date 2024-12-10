#read

f = open("expo.txt", "r")
print(f.read())


f = open("D:\Paras Python 2.00\expo.txt", "r")
print(f.read())


f = open("expo.txt", "r")
print(f.read(5))


f = open("expo.txt", "r")
print(f.readline())
print(f.readline())


f = open("expo.txt", "r")
for x in f:
    print(x)


f = open("expo.txt", "r")
print(f.readline())
print(f.readline())
f.close()



#write/create

f = open("expo.txt", "a")                     #appending
f.write("Now this file has more content!")
f.close()

f = open("expo.txt", "r")
print(f.read())


f = open("expo.txt", "w")                     #overwrite
f.write("the file has no content anymore!")
f.close()

f = open("expo.txt", "r")
print(f.read())


f = open("exp.txt", "x")
print(f.read())



#delete

import os
os.remove("D:\Paras Python 2.00\exp.txt")


import os
if os.path.exists("exp.txt"):
    os.remove("expo.txt")
else:
    print("the file does not exist")


import os
os.rmdir("D:\Paras Python 2.00\exp")
