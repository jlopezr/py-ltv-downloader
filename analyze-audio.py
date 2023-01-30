#!/usr/bin/env python3

import subprocess;
import sys;
import os.path;
import json

if len(sys.argv)!=3:
    print("analyze-audio requires 1 parameter: filename of input media")
    sys.exit(-1)

input = sys.argv[2]

#ffprobe -show_streams -show_format -print_format json cut-\*Watermark.mov
txt = subprocess.run(['ffprobe','-hide_banner','-show_streams','-show_format','-print_format','json',input], stdout=subprocess.PIPE).stdout.decode('utf-8')
#print(txt)

print()
print()
print()

data = json.loads(txt)
streams = data["streams"]

for stream in streams:
    if stream["codec_type"]=="audio":
        if "channel_layout" in stream:
            layout = stream["channel_layout"]
        else:
            layout = "?"
        if stream["codec_long_name"]!="unknown":
            codec = stream["codec_long_name"]
        else:
            codec = stream["codec_name"]
        if "language" in stream["tags"]:
            lang = stream["tags"]["language"]
        else:
            lang = "?"
        print(str(stream["index"])+") Channels:",stream["channels"],codec, stream["sample_rate"],"Hz Lang:",lang,"-",layout)
