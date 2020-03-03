#!/usr/bin/python3

my_string = input()
count = 0
delim = len(my_string) // 2

for i in range(delim):
    if my_string[i] == my_string[-(i + 1)]:
<<<<<<< HEAD
        count += 1
=======
        count = count + 1
>>>>>>> a2aa397b14db1dea09602c03135efeaf890629c2
    else:
        print('No')
        break

if count == delim:
    print('Yes')
