#!/bin/bash

greeting=`python simple.py` 

if [ $1 ]; then
  echo $greeting $1!
else
  echo $greeting World!
fi
