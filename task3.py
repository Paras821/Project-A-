x =" Enter Your Marks According To Following Subjects: "
print(x)

y = int(input(" Science \n "))
print(y)

z = int(input(" SS \n "))
print(z)

a = int(input(" English \n "))
print(a)

b = int(input(" Maths \n "))
print(b)

c = int(input(" Gujrati \n "))
print(c)

q = str(input(" Total Marks " )), int(input( y + z + a + b + c ))
print(q)

r = float(input(" Enter Your % \n "))
print(q / 500 * 100)
print(r)


if r > 90 :
    print(" Grade A ")
    
elif r > 80 or r < 90 :
    print(" Grade B ")

elif r > 70 or r < 80 :
    print(" Grade C ")

elif r > 55 or r < 70 :
    print(" Grade D ")

elif r > 45 or r < 55 :
    print(" Grade E ")

else :
    print(" Failed ")


