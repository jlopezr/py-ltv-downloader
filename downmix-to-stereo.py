import subprocess;
import sys;
import os.path;

if len(sys.argv)!=3:
    print("downmix-to-stereo requires 1 parameter: filename of input media")
    sys.exit(-1)

input = sys.argv[2]
dir, file = os.path.split(input)
file = "stereo-"+file
output = os.path.join(dir, file)

subprocess.run(["ffmpeg","-i",input,"-c:v","copy","-ac","2",output])
