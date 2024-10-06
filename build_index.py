#!/usr/bin/env python

import argparse
import glob
import os


parser = argparse.ArgumentParser()
parser.add_argument('--glob', type='str', default='**/*')
args = parser.parse_args()


filepaths = list()

for filepath in glob.glob(args.glob, recursive=True):

    # Only accept files from sub-directories (only static files are top-level)
    if os.path.isfile(filepath) and '/' in filepath:
        filepaths.append(filepath)

html = """
<html>
<body>
<ul>
""" + '\n'.join(f'<li><a href="{filepath}">{filepath}</a></li>' for filepath in sorted(filepaths)) + """
</ul>
</body>
"""

with open('index.html', 'w') as fout:
    fout.write(html)
