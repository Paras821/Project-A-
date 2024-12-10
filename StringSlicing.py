a="HELLOW, WORLD"
print(a[2:5])
print(a[:5])
print(a[2:])
print(a[-5:-2])


#modified string

b=" HELLOW, JARVIS "
print(b.strip())

print(a.replace("H", "J"))
print(b.replace("H", "J"))

print(a.split(","))
print(b.split(" ,"))


x="HELLOW"
y="WORLD"
z=x+y
print(z)
z=x+" "+y
print(z)



#formatstring
age=23
name=f"My name is Paras. I am {age} years old."
print(name)

price=75
value=f"the price is {price : .2f} $"
print(value)


text="Python is so called \" Vikings \" of Python"
print(text)
