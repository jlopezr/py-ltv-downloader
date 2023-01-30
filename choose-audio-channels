import subprocess;
import sys;
import os.path;

if len(sys.argv)!=3:
    print("choose-audio-channels requires 1 parameter: filename of input media")
    sys.exit(-1)

input = sys.argv[2]
dir, file = os.path.split(input)
file = "chosen-"+file
output = os.path.join(dir, file)

#ffmpeg -i *Watermark.mov -map 0:v -c:v copy -filter_complex [0:a:6][0:a:7]join=inputs=2:channel_layout=stereo[a] -map [a] output.mov
subprocess.run(["ffmpeg","-i",input,"-map","0:v","-c:v","copy","-filter_complex","[0:a:6][0:a:7]join=inputs=2:channel_layout=stereo[a]","-map","[a]",output])
