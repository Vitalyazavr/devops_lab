#!/usr/bin/python3

str1 = input()
for word in str1.split():
    str1 = str1.replace(word[::], word[::-1])

print(str1)
