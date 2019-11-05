from module import add, even, hello

li = [i for i in range(add(4))]
print(hello("John {}".format(even(li)[2])))
