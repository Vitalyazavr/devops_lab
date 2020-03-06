#!/usr/bin/env python
# coding: utf-8

import os
import argparse

parser = argparse.ArgumentParser(description='Script for working with files')
group = parser.add_mutually_exclusive_group()
parser.add_argument('-v', '--version', action='version', version='v0.1_beta')
parser.add_argument('-p', '--parent', nargs='?', default='./', action="store",
                    dest='parent', help='set parent directory')
parser.add_argument('-r', '--recursive', action="store_true", dest='recursive',
                    help='show files recursively')
parser.add_argument('-e', '--extension', nargs='?', default=False,
                    action="store", dest='ext', help='sort by extention')
group.add_argument('-d', '--date', action="store_true", dest='date',
                   help='show files sorted by date')
group.add_argument('-f', '--filename', action="store_true", dest='name',
                   help='show files sorted filename')
args = parser.parse_args()

defpath = args.parent
key = args.ext


def out_par_files(path):
    files = []
    for file in os.listdir(path):
        if os.path.isfile(path + file):
          files.append([file, os.path.getctime(path + file)])
    return files


def list_files_recursively(path):
    files = []
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            fullpath = os.path.join(dirname, filename)
        files.append([fullpath[len(path):], os.path.getctime(fullpath)])
    return files


def filter_ext(list1, key):
    files = []
    for file in list1:
        if str(file[0].split('.')[-1:]).strip("['']") == key:
            files.append(file)
    return files


def list_sort(nst):
    if args.name:
        nst.sort()
    elif args.date:
        nst.sort(key=lambda x: x[1])
    return nst


if args.recursive:
    print('Show file recursively')
    if args.ext:
        st = filter_ext(list_files_recursively(defpath), key)
    elif not args.ext:
        st = list_files_recursively(defpath)
elif not args.recursive:
    print('Show file in directory')
    if args.ext:
        st = filter_ext(out_par_files(defpath), key)
    elif not args.ext:
        st = out_par_files(defpath)

st = list_sort(st)

for file in st:
    print(file[0])
