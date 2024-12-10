for x in range(6):
    print(x)

for y in range(2,6):
    print(y)

for m in range(2,30,2):
    print(m)                 #even numbers

for n in range(1,30,2):
    print(n)                 #odd numbers


for a in range(6):
    print(a)
    if a == 3 :
        break

for b in range(6):
    if b == 3 :
        break
    print(b)


for p in range(6):
    print(p)
    if p == 3 :
        break
else:
    print("The Loop is Over")

for r in range(6):
    if r == 6 :
        break
    print(r)
else:
    print("Finally, Loop is Over")


vegs = ["Potato", "Tomato", "Chana", "Bit"]
fruits = ["Apple", "Banana", "Kiwi"]

for i in vegs:
    for j in fruits:
        print(i,j)
