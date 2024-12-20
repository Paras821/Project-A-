x = int(input(" Enter Your Weight \n"))
print(x)

y= x - 60

if x <= 60:
    print("Rs.",200)

elif x > 60 and x <= 80:
    print( "Rs.", 200 + 100*y)

elif x > 80 and x <= 100:
    print("Rs.", 200 + 150*y)

else:
    print("Not Eligible")
