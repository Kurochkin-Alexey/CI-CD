#!/bin/bash

config=$(python3 config.py)

IP=$(echo $config | cut -d' ' -f3)

scp cat/s21_cat rosscome@$IP:/usr/local/bin
scp grep/s21_grep rosscome@$IP:/usr/local/bin