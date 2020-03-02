#!/usr/bin/python3

my_string = input()
count = 0
delim = len(my_string)//2

for i in range(delim):
    if my_string[i] == my_string[-(i+1)]:
        count = count+1
    else:
        print('No')
        break

if count == delim:
    print('Yes')
