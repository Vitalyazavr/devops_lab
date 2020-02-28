#!/bin/bash

SH=$(echo $SHELL | awk -F "/" '{print $3}')

PA_TH=$(echo "$HOME/.$SH""rc")

COND=$(grep 'pyenv' $PA_TH)

if [[ -z $COND ]] ; then
  echo "Need to add"
  echo 'export PATH="/home/andrushkevich_vitaliy/.pyenv/bin:$PATH"' >> $PA_TH
  echo 'eval "$(pyenv init -)"' >> $PA_TH
  echo 'eval "$(pyenv virtualenv-init -)"' >>$PA_TH
  source $PA_TH
else
 echo "Path already added"
fi

pyenv install 2.7.9
pyenv install 3.7.2
pyenv virtualenv 2.7.9 env1
pyenv virtualenv 3.7.2 env2
pyenv activate env2
