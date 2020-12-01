#!/bin/bash

echo "--PYTHON--"
time python code.py
echo "--C--"
gcc code.c -o code && time ./code && rm code 
