#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filename VideoClassify.py
# Intro: creat multi directory then classify video files

# author: shenwang@sjtu.edu.cn
# date: 2018/7/18

import os

V_PATH = 'C:\Users\Wangshen\Desktop\\video\\'
videoname = "tiled_w{0}h{1}"
dir_name = "tiled_w{0}h{1}"
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
    num = 0

    files = os.listdir(V_PATH)

    # use for loop to make dir for each tiled video
    for x in range(1, TileNum_w + 1):
        for y in range(1, TileNum_h + 1):
            if not os.path.exists(V_PATH + "tiled_w" + str(x) + "h" + str(y)):
                os.system("mkdir " + V_PATH + "tiled_w" + str(x) + "h" + str(y))
                for file in files:
                    if videoname.format(x, y) in file:
                        os.system("copy {0} {1}".format(V_PATH + file, V_PATH + dir_name.format(x, y)))


if __name__ == '__main__':
    main()
