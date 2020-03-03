#!/usr/bin/python3

key = int(input())
list1 = []
sum1 = 0
sum2 = 0

for line in range(key):
    list1.append((input()).split())

for i in range(len(list1)):
<<<<<<< HEAD
    sum1 += int(list1[i][i])
    sum2 += int(list1[i][-1 * (i + 1)])
=======
    sum1 = sum1 + int(list1[i][i])
    sum2 = sum2 + int(list1[i][-1 * (i + 1)])
>>>>>>> a2aa397b14db1dea09602c03135efeaf890629c2

print(abs(sum1 - sum2))
