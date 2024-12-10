
def weight(x):
    y = (x - 25)
    z = (x - 100)
    o = (x - 200)
    print("Weight")

    if x <= 25:
        result = x * 0.50
        print(result)

    elif x <= 100:
        result = (25 * 0.50) + (y * 1)
        print(result)

    elif x <= 200:
        result = (25 * 0.50) + (75 * 1) + (z * 1.5)
        print(result)

    elif x > 200:
        result = (25 * 0.50) + (75 * 1) + (100 * 1.5) + (o * 2)
        print(result)

weight(250)
