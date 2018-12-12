#!/usr/bin/python
# -*- coding: UTF-8 -*-

# VideoMultiChunk.py
# This program segment each tiled video into 0.5s segment with different quality
# 试验失败：不能先将视频转为帧内编码，再chunk化，正在尝试其他的集成切割方法
# 目前尝试使用的是 MP4Box

# author: shenwang@sjtu.edu.cn
# date: 2018/7/18
# run On MAC OS

import os
import numpy as np

V_PATH = "./diving_video"
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
    out_video_path = './chunked_tiled_video'
    if not os.path.exists(out_video_path):
        os.makedirs(out_video_path)

    # tiled_w1h1 DIR
    all_files_dir = os.listdir(V_PATH)
    if '.DS_Store' in all_files_dir:
        all_files_dir.remove('.DS_Store')

    all_files_dir = [i for i in all_files_dir if i.startswith('tiled')]


    tmp_w = 0
    tmp_h = 0

    # One step
    # use for loop to create dir and remove files

    # for file in all_files_dir:
    #
    #     cpath = V_PATH + '/' + file
    #     videofiles = os.listdir(cpath)
    #
    #     # remove the trash DS_Store
    #     if '.DS_Store' in videofiles:
    #         videofiles.remove('.DS_Store')
    #
    #     for videofile in videofiles:
    #         dirname = videofile[0:-4] + '_chunked'
    #         if not os.path.exists(cpath + '/' + dirname):
    #             os.system("mkdir {0}/{1}".format(cpath, dirname))
    #             os.system("mv {0} {1}".format(cpath+'/'+videofile, cpath+'/'+dirname))

    count = 0
    for file in all_files_dir:

        out_tile_path = out_video_path + '/' + file
        if not os.path.exists(out_tile_path):
            os.makedirs(out_tile_path)

        cpath = V_PATH + '/' + file
        videofiles = os.listdir(cpath)

        # remove the trash DS_Store
        if '.DS_Store' in videofiles:
            videofiles.remove('.DS_Store')
        videofiles = [i for i in videofiles if i.startswith('tiled')]

        for videofile in videofiles:
            # convert all video to Intra coded
            intra_video_name = 'intra_' + videofile[0:-4] + '.mp4'
            bitstr = videofile[11:]
            bitstr = bitstr[:-4]
            raw_video_path = cpath + '/' + videofile
            intra_video_path = cpath  + '/' +intra_video_name
            out_video_path = out_tile_path + '/' + 'chunked_'+ videofile[0:-4]
            if not os.path.exists(out_video_path):
                os.makedirs(out_video_path)
            if not os.path.isfile(intra_video_path):
                os.system("ffmpeg -i {0} -strict -2 -qscale 0 -intra {1}".format(raw_video_path, intra_video_path))
            count = count + 1

            i = np.arange(0, 60, 1, int)
            j = i + 1
            for t in range(0, 60):
                if t == 59:
                    #os.system("ffmpeg -i {0} -vcodec copy -ss 00:00:{1} -to 00:01:00 {2} -y".format
                    #          (intra_video_path, str(i[t]),
                    #           out_video_path + '/'+ file[-4:] + '_' + str(t) + '.mp4'))
                    print("ffmpeg -i {0} -vcodec copy -b:v {1} -r 30 -vframes 1800 -g 30"
                              " -ss 00:00:{2} -to 00:01:00 {3} -c:v libx265".format
                              (intra_video_path,
                               bitstr,
                               str(i[t]),
                               out_video_path + '/' + file[-4:] + '_' + str(t) + '.mp4'))
                    os.system("ffmpeg -i {0} -vcodec copy -b:v {1} -r 30 -vframes 1800 -g 30"
                              " -ss 00:00:{2} -to 00:01:00 {3} -c:v libx265".format
                              (intra_video_path,
                               bitstr,
                               str(i[t]),
                               out_video_path + '/' + file[-4:] + '_' + str(t) + '.mp4'))
                else:
                    #os.system("ffmpeg -i {0} -vcodec copy -ss 00:00:{1} -to 00:00:{2} {3} -y".format
                    #          (intra_video_path, str(i[t]), str(j[t]),
                    #           out_video_path + '/'+ file[-4:] + '_' +str(t) + '.mp4'))
                    print("ffmpeg -i {0} -vcodec copy -b:v {1} -r 30 -vframes 1800 -g 30"
                              " -ss 00:00:{2} -to 00:00:{3} {4} -c:v libx265".format
                              (intra_video_path,
                               bitstr,
                               str(i[t]),
                               str(j[t]),
                               out_video_path + '/' + file[-4:] + '_' + str(t) + '.mp4'))
                    os.system("ffmpeg -i {0} -vcodec copy -b:v {1} -r 30 -vframes 1800 -g 30"
                              " -ss 00:00:{2} -to 00:00:{3} {4} -c:v libx265".format
                              (intra_video_path,
                               bitstr,
                               str(i[t]),
                               str(j[t]),
                               out_video_path + '/' + file[-4:] + '_' + str(t) + '.mp4'))


    print(count)




if __name__ == '__main__':
    main()
