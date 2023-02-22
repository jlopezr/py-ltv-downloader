import subprocess;
import sys;
import os.path;

if len(sys.argv)!=3:
    print("cut-two-minutes requires 1 parameter: filename of input media")
    sys.exit(-1)

input = sys.argv[2]
dir, file = os.path.split(input)
file = "cut-"+file
output = os.path.join(dir, file)

subprocess.run(["ffmpeg","-i",input,"-ss","0","-t","120","-c","copy","-map","0",output])
