#!/usr/bin/env python3

import subprocess;
import sys;
import os.path;
import json
from urllib import request;

if len(sys.argv)!=2:
    print("list-commands require no arguments")
    sys.exit(-1)

URL='https://api.github.com/repos/jlopezr/py-ltv-downloader/git/trees/main?recursive=1'

 
data = code = request.urlopen(URL).read().decode("utf-8")
data = json.loads(data)

files=data["tree"]
result=[]

for file in files:
    path=file["path"]
    if path.endswith(".py") :
        result.append((path[:len(path) - 3]))

result.sort()
print(*result, sep = "\n")
