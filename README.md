#### DevOps Lab 2020 (January-April)
##### Homework4: Vitali Andrushkevich

**_Descriptions:_** <br>

TASK 1

I have created a script which lists files in directory with the following options:

- by default (without options it' shows only files in current directory)

- output files only from the parent directory (option, -p)

- list files recursively (-r, list files not only in parent directory)

- filter by file extension (-e, optinos, list files with specific extension)

- order output by filename (-f, sort by filename)

- order output by date of creation (-d, sort by creation date)

**_Examples:_** <br>
```bash
# run without arguments (show file in current directory)
$./get_files.py
Show file in directory
.gitignore
README.md
requirements.txt
tox.ini
task2.py
test.py
get_files.py
```

```bash

# recursively in parent directory (set with -p parametr) and show only .py files
$./get_files.py -r -p ~/python/ -e py
Show file recursively
day2/task5.py
day3/snapshot.py
day4/setup.py
day4/setup.py
day4/git/devops_lab/setup.py
day5/temp.py
day5/01/temp.py
day5/git_send/devops_lab/get_files.py

```
```
# the same with sorting by date
$./get_files.py -r -p ~/gcp/ -e tf  -d
Show file recursively
classwork/variables.tf
Day2/variables.tf
Day2/variables.tf
Day2/variables.tf
github/google-cloud-module/classwork/variables.tf
github/google-cloud-module/Day3/variables.tf
Day3-2/main.tf
Day3-2/main.tf
Day3-2/main.tf
Day4/terraform-v.0.1/var.tf
Day4/terraform-v0.2/var.tf
Day4/Day4-terraform/backed_db.tf
Day4/Day4-terraform/backed_db.tf

```


```
# help
$./get_files.py -h                  
usage: get_files.py [-h] [-v] [-p [PARENT]] [-r] [-e [EXT]] [-d | -f]

Script for working with files

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -p [PARENT], --parent [PARENT]
                        set parent directory
  -r, --recursive       show files recursively
  -e [EXT], --extension [EXT]
                        sort by extention
  -d, --date            show files sorted by date
  -f, --filename        show files sorted filename
```

TASK 2

Created unit tests for 2task from homework 2.
```
$nosetests test.py --with-coverage --cover-erase 

Name       Stmts   Miss  Cover
------------------------------
task2.py      13      3    77%
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```
