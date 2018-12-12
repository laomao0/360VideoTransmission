#!/usr/bin/python
# -*- coding: UTF-8 -*-

# VideoMultiBitRate.py 
# Introduction: this program convert each tiled YUV video(480x480,30fps) to multi bitrate 
# 200k, 400k, 600k, 800k, 1000k
# the output video container is mp4,with gop:30, total frames:1800, frame rate:30, codec:h.265
# Tips: if you want take a look at the command line, just replace the os.system with print

# author: shenwang@sjtu.edu.cn
# date: 2018/7/18
# modify: change -g from 15 to 30. want set segment length 1s（videoset 1: 15  video set 2:30）

import os

V_PATH = 'C:\Users\Wangshen\Desktop\video'
frame_size = '3840x1920'
tile_size = '480x480'  # width x height

Width_pix = 3840
Height_pix = 1920

TileNum_w = 8
TileNum_h = 4

BitNum = ['200k', '400k', '600k', '800k', '1000k']


def main():
    tile_w = Width_pix / TileNum_w
    tile_h = Height_pix / TileNum_h

    # get current work directory
    start_dir = os.getcwd()
    print("here is the current work dir: " + '\n' + start_dir)

    tmp_w = 0
    tmp_h = 0

    # use for loop to add other tiles
    for x in range(1, TileNum_w + 1):
        for y in range(1, TileNum_h + 1):
            for bitv in BitNum:
                os.system(
                    "ffmpeg -f rawvideo -s {0} -r 30 -i {1} -b:v {2} -q 1 -r 30 -vframes 1800 -g 30 -c:v libx265 {3}".format \
                        (tile_size, \
                         "w" + str(x) + "h" + str(y) + ".yuv", \
                         bitv, \
                         "tiled_" + "w" + str(x) + "h" + str(y) + "_" + bitv + ".mp4"))


if __name__ == '__main__':
    main()
