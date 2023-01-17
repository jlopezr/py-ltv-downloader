import subprocess;
import sys;

if len(sys.argv)!=3:
    print("downmix-to-stereo requires 1 parameter: filename of input media")
    sys.exit(-1)

input = sys.argv[2]
output = "stereo-"+input

subprocess.run(["ffmpeg","-i",input,"-c:v","copy","-ac","2",output])
