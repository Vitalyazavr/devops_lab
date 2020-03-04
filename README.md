#### DevOps Lab 2020 (January-April)
##### Homework4: Vitali Andrushkevich

**_Description:_** <br>

This script following information using GitHub API:
- info about user (Name, E-mail, Work place, count of public repos)
- info about repository (Full name, date of last push, basic language, default branch, number of forks)
- time where they created
- links for fast clone repo and open repo link via browser.

**_How to install:_** <br>
Clone the repo and navigate to this folder.

```bash
# to install
 pip install .
 snapshot
```

**_How it works:_** <br>

Use -h options for help. (if you run it without options, script will show information about your login profile)

```bash
$pr-stats -h
usage: pr-stats [-h] [-v] [-o [OWNER]] [-r REPO] [--info] [--date] [--link]
                [--all]

Script for working with GitHub

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -o [OWNER], --owner [OWNER]
                        set username
  -r REPO, --repo REPO  set repository name
  --info                information about user/repo
  --date                date of user/repo activity
  --link                show links for clone repo
  --all, -a             show all info
```

**_Examples of usage:_** <br>

```bash
# take information from alenaPy/devops_lab
$pr-stats --owner alenaPy --repo devops_lab --info --link
Please input GitHub credentials
Username: vitalyazavr
Password: 

# OUTPUT

SSH:  git@github.com:alenaPy/devops_lab.git
GIT:  git://github.com/alenaPy/devops_lab.git
HTTPS:  https://github.com/alenaPy/devops_lab.git
Full name:  alenaPy/devops_lab
Last push:  2020-03-04T17:08:35Z
Basic language:  None
Default branch:  master
Forks:  14
```

```bash
# take information about alenaPy
$pr-stats --owner alenaPy -a       
Please input GitHub credentials
Username: vitalyazavr
Password:

# OUTPUT

Name:  Alena Sheshko
EMAIL:  None
Work for:  @epam
Public repos:  5
Registered:  2016-02-25T12:21:44Z
Last actions:  2020-02-28T08:39:31Z

```

