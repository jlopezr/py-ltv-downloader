import subprocess;
import sys;
import os.path;

if len(sys.argv)!=2+3:
    print("choose-audio-channels requires 3 parameters: [filename of input media] [left channel number] [right channel number]")
    print("   Ex: process choose-audio-channels input.mxf 6 7")
    sys.exit(-1)

input = sys.argv[2]
dir, file = os.path.split(input)
file = "chosen-"+file
output = os.path.join(dir, file)

left = sys.argv[3]
right = sys.argv[4]


#ffmpeg -i *Watermark.mov -map 0:v -c:v copy -filter_complex [0:a:6][0:a:7]join=inputs=2:channel_layout=stereo[a] -map [a] output.mov
#subprocess.run(["ffmpeg","-i",input,"-map","0:v","-c:v","copy","-filter_complex","[0:a:6][0:a:7]join=inputs=2:channel_layout=stereo[a]","-map","[a]",output])

#ffmpeg -i content.mxf -filter_complex "[0:a:6][0:a:7]amerge=inputs=2[a]" -map 0:v -map "[a]" -c:v copy -ac 2  output3.mxf
subprocess.run(["ffmpeg","-i",input,"-filter_complex",f"[0:a:{left}][0:a:{right}]amerge=inputs=2[a]","-map","0:v","-map","[a]","-c:v","copy","-ac","2",output])
