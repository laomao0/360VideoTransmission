#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filename：VideoCrop.py
# Intro: this program crop a 360 video into WxH tiles video
# The input video is YUV video and output video is multiple tiled YUV videos, names ”w[i]h[i].yuv“
# Dependence：ffmpeg

# author: shenwang@sjtu.edu.cn
# date: 2018/7/17


import os

V_PATH = 'rawvideo1920.yuv'
frame_size = '3840x1920'

Width_pix = 3840
Height_pix = 1920

TileNum_w = 8
TileNum_h = 4


def main():
    tile_w = Width_pix / TileNum_w
    tile_h = Height_pix / TileNum_h

    # get current work directory
    start_dir = os.getcwd()
    print("here is the current work dir: " + '\n' + start_dir)

    tmp_w = 0
    tmp_h = 0
    for x in range(TileNum_w):
        tmp_w = x * tile_w
        for y in range(TileNum_h):
            tmp_h = y * tile_h
            os.system("ffmpeg -f rawvideo -vcodec rawvideo -s {0} -r 30 -i {1} -filter:v \
\"crop={2}:{3}:{4}:{5}\" {6}.yuv ".format(frame_size, V_PATH, tile_w, tile_h, tmp_w, tmp_h,
                                          'w' + str(x + 1) + 'h' + str(y + 1)))


if __name__ == '__main__':
    main()
