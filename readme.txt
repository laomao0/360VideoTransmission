# read.me
# This temp generated video record of 360 video file set_1
# Gop=15, duration = 60s
# multi bitrate 200k, 400k, 600k, 800k, 1000k

// raw video: about 4 mins duration

SharkShipwreck720p.mp4:	downloaded raw 720p 360 video with audio;
SharkShipwreck2160p.mp4:	downloaded raw 2160p 360 video without audio;
SharkShipwreck2160p.webm: 	downloaded raw 2160p 360 video without audio;
Sahrk.mp4:  		downloaded raw 2160p 360 video with audio;

// Key frame video(OPTIONAL)
>ffmpeg -i SharkShipwreck2160p.mp4 -strict -2 -qscale 0 -intra keyoutput.mp4
keyoutput.mp4:		generated from SharkShipwreck2160p.mp4, intra code video;

//duration 1min video
>ffmpeg -i keyoutput.mp4 -vcodec copy -acodec copy -ss 00:00:30 每to 00:01:30 output.mp4 每y
output.mp4: 		generated from keyoutput.mp4, 2160p, without audio, 1800frames, 30fps;
output1.mp4: 		generated from keyoutput.mp4, 2160p, with audio, 1800frames, 30fps;

//change 3840x2048 -> 3840x1920(optional)
>ffmpeg 每I output.mp4 每s 3840x1920 SharkShipwreck.mp4
 SharkShipwreck.mp4:	generated from output.mp4, framesize 3840x1920, duration 1min, without audio;
 SharkShipwreck1.mp4:	generated from output.mp4, framesize 3840x1920, duration 1min, with audio;

//change mp4 to yuv, to get 3840x1920 yuv
>ffmpeg -i output.mp4 -f rawvideo -vcodec rawvideo -pix_fmt yuv420p -s 3840x1920 -r 30 rawvideo1920.yuv
rawvideo1920.yuv		yuv file generated from output.mp4, framesize 3840x1920, 30fps, without audio;

//tile the yuv, 3840x1920, tile size: 480x480, [8x4]tiles
>ffmpeg -f rawvideo -vcodec rawvideo -s 3840x1920 -r 30 -i rawvideo1920.yuv -filter:v "crop=480:480:0:0" w01-h01.yuv 
//use VideoCrop.py 
i from 1~8, j from 1~4
w[i]h[j].yuv		tiled video, frame size 480x480, 1800 frames, 30fps

//multi bitrate multi bitrate 200k, 400k, 600k, 800k, 1000k
// >ffmpeg -f rawvideo -s 480x480 -r 30 -i w1h1.yuv -b:v 300k -q 1 -r 30 -vframes 1800 -g 15 -c:v libx265 w1h1.mp4
//use VideoMultiBitRate.py
i from 1~8, j from 1~4 , k from [200k, 400k, 600k, 800k, 1000k]
tiled_w[i]h[i]_[k].mp4

//DO NOT chunked
//actually, in dataset one we do not chunked the tiled video(tiled_w[i]h[i]_[k].mp4), it is a duration 1min mp4, with
different video bitrate, we use a classify prog to classify the file into different directory
use VideoClassify.py


