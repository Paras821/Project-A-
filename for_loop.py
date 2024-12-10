#for loop = iterating a code for specific times.
#for loop key address = "for"   for() :
#for loop can be used in multiple ways;
#list, tuple, set, dict


fruits = ["Apple", "Banana", "Kiwi"]
#print(fruits)
#print(type(fruits))

for x in fruits :
    print(x)


veg = ["Potato", "Tomato", "Chana", "Cabbage"]

for y in veg :
    print(y)
    if y == "Chana" :
        break
    
vegs = ["Potato", "Tomato", "Chana", "Cabbage"]

for z in vegs :
    if z == "Chana" :
        break
    print(z)


veggy = ["Potato", "Tomato", "Chana", "Cabbage", "Bit"]

for X in veggy :
    print(X)
    if X == "Cabbage" :
        continue                                #no change in output
    
veggs = ["Potato", "Tomato", "Chana", "Cabbage", "Bit"]

for Z in veggs :
    if Z == "Cabbage" :
        continue
    print(Z)


tuple1= ("JARVIS", "FRIDAY", "ATOMS", "RICHIE")


for A in tuple1 :
    if A == "FRIDAY" :
        break
    print(A)

for A in tuple1 :
    if A == "FRIDAY" :
        continue
    print(A)
