x =float(input(" Enter Your Units \n"))
print(x)


if x <= 200:
    print("Rs.", x*1)

elif x > 200 and x <= 300:
    print( "Rs.", x*1.5)

elif x > 300 and x <= 400:
    print("Rs.", x*2)


y = x * 5/100         #duty tax
print("Rs.", y)

z= x + y              #duty tax + units expenses
print("Rs.", z)

u = z * 8/100         #GST
print("Rs.", u)

v= z + u              #Total Expenses
print("Rs.", v)
