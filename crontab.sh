#!/bin/bash

crontab -l > tempfile
echo "$3 $4 $5 $6 $7 python scraper.py $1 $2" >> tempfile
crontab tempfile
rm tempfile