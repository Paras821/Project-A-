my_set = {1,2,3,4,5}
print(my_set)


my_set = set([1,2,3,4,5])
print(my_set)


my_set = {1,2,2,3,3,4,5,5}
print(my_set)


mixed_set = {1, 'hello' , (1,2,3)}
print(mixed_set)


my_set = {1,2,3,3}
my_set.add(4)
print(my_set)


my_set = {1,2,3,4}
my_set.remove(3)
print(my_set)


my_set = {1,2,3,4,5}
my_set.discard(5)
print(my_set)


my_set = {1,2,3,4}
if 5 in my_set:
    print(" is present in the set ")
else:
    print(" is Not present in the set ")
