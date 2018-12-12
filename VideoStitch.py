#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filename：VideoStitch.py
# Introduction: this program stich multiple tiles [8x4] each pixel 480x480 into a 3840x1920 whole vidoe 
# information: need to cd into the video directory and put this .py here
# TIP：this ffmpeg prog runs very slow, you can use yuvplayer to
# playback then temp video to check if it is stitched correctly.

# author: shenwang@sjtu.edu.cn
# date: 2018/7/17

import os

V_PATH = 'rawvideo1920.yuv'
frame_size = '3840x1920'
tile_size = '480x480'  # width x height

Width_pix = 3840
Height_pix = 1920

TileNum_w = 8;
TileNum_h = 4;


def main():
    tile_w = Width_pix / TileNum_w
    tile_h = Height_pix / TileNum_h

    # get current work directory
    start_dir = os.getcwd()
    print("here is the current work dir: " + '\n' + start_dir)

    # create a 3840x1920 video then add one 480x480 video
    print("ffmpeg -f rawvideo -vcodec rawvideo -r 30 -s 480*480 -i {0} -r 30 -vf pad=3840:1920:0:0:black {1}".format(
        'w1h1.yuv', 'tempvideo0.yuv'))
    os.system(
        "ffmpeg -f rawvideo -vcodec rawvideo -r 30 -s 480*480 -i {0} -r 30 -vf pad=3840:1920:0:0:black {1}".format(
            'w1h1.yuv', 'tempvideo0.yuv'))

    tmp_w = 0
    tmp_h = 0
    num = 0

    # use for loop to add other tiles
    for x in range(1, TileNum_w + 1):
        for y in range(1, TileNum_h + 1):
            os.system(
                "ffmpeg -f rawvideo -vcodec rawvideo -s {0} -r 30 -i {1} -f rawvideo -vcodec rawvideo -s {2} -r 30 -i {3} -filter_complex \"[0:v][1:v]overlay=480*{4}:480*{5}\" {6}".format(
                    frame_size, "tempvideo" + str(num) + ".yuv", tile_size, "w" + str(x) + "h" + str(y) + ".yuv",
                    str(x - 1), str(y - 1), "tempvideo" + str(num + 1) + ".yuv"))
            print(
                "ffmpeg -f rawvideo -vcodec rawvideo -s {0} -r 30 -i {1} -f rawvideo -vcodec rawvideo -s {2} -r 30 -i {3} -filter_complex \"[0:v][1:v]overlay=480*{4}:480*{5}\" {6}".format(
                    frame_size, "tempvideo" + str(num) + ".yuv", tile_size, "w" + str(x) + "h" + str(y) + ".yuv",
                    str(x - 1), str(y - 1), "tempvideo" + str(num + 1) + ".yuv"))

            if num >= 1:
                os.remove("tempvideo" + str(num) + ".yuv")
                print("tempvideo" + str(num) + ".yuv")
            else:
                pass

            num = num + 1

    # remove the first temp video
    os.remove("tempvideo0.yuv")


if __name__ == '__main__':
    main()
