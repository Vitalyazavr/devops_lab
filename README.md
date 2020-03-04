#### DevOps Lab 2020 (January-April)
##### Homework3: Vitali Andrushkevich

**_Description:_** <br>
This app makes snapshots of next system information: 
- % of CPU load
- % of disk usage
- % of usage virtual memory
- % input/outup count
- sent and recieved bytes(network)

And redirect information to json/txt (info.<json/txt>) file in your current directory.

**_How it works:_** <br>
Application recieves two parameters:<br>
- type of output file (default: txt, you may choose: txt/help)
- delay (in seconds) (by default 300 seconds)

```bash
# for help
snapshot -h

# for run by default
snapshot 

# takes snaphosts every 30 second and put it into json file
snapshot json 30

# takes snaphosts every 15 second and put it into  txt file
snapshot txt 15

```

**_How to setup:_** <br>
Clone the repo and navigate to this folder.

```bash
# to install
 pip install .
 snapshot
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
