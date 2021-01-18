#!/usr/bin/env python3

import sys
import datetime

if len(sys.argv) != 2:
    print('Usage: ./gen_md_doc.py title')
    sys.exit(-1)
 

title = sys.argv[1]
today = datetime.date.today().strftime('%Y-%m-%d')
filename = today + "-" + title

with open(filename +  ".md", 'a') as f:
    f.write('---\n')
    f.write('layout: post\n')
    f.write('title: ' + title + '\n') 
    f.write('---\n')

