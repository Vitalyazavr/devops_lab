#!/usr/bin/python3

inpt = key = int(input())
list1 = []

for i in range(9, 1, -1):
    if key < 10 and key == i:
        i -= 1
    else:
        while inpt % i == 0:
            inpt /= i
            list1.append(str(i))

if len(list1) <= 1:
    print('-1')
    quit()

print(''.join(list1[::-1]))
