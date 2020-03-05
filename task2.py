#!/usr/bin/env python
# coding: utf-8


def is_polindrome(st, count):
    if (count < 0):
        raise TypeError
    for i in range(len(st) // 2):
        if st[i] == st[-(i + 1)]:
            count += 1
        else:
            break
    if count == len(st) // 2:
        return True


if __name__ == "__main__":
    my_string = input()
    count = 0
    print('yes') if is_polindrome(my_string, count) else print('no')
