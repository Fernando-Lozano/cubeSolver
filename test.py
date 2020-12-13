import itertools
counter = 0
for count in range(1, 10):
        print(count)
        for characters1 in itertools.product("rRdDbB", repeat=count):
            counter += 1
            print(counter)