# -*- coding: UTF-8 -*-
# filename:FoVTilesCompute.py
# Intro: this program convert the original 192x192 tile format into 480x480 format
# details can be found in "360 buffer update ProjDoc" Chapter II

import numpy as np
import os
import csv

TILE_TRACE_PATH = "./360dataset/sensory/tile/"
COMPUTED_TRACE_PATH = "./360dataset/sensory/computed_tiles/"

FRAME_SIZE = '3840x1920'
TILE_SIZE = '480x480'  # width x height

WIDTH_PIX = 3840
HEIGHT_PIX = 1920

TILE_NUM_W = 8
TILE_NUM_H = 4

BIT_LIST = ['200k', '400k', '600k', '800k', '1000k']

TRACE_LIST = ['diving_user']


def main():
    all_files = os.listdir(TILE_TRACE_PATH)

    # extract the file
    for trace_list in TRACE_LIST:
        files = [name for name in all_files if name.startswith(trace_list) and name.endswith('csv')]

    # all_fov_tiles = []
    # all_fov_num   = []
    # all_file_names = []
    # read line of trace csv file

    for file in files:

        with open(TILE_TRACE_PATH + file, 'r') as f_obj, open(COMPUTED_TRACE_PATH + file, 'w') as wf_obj:

            f_csv = csv.reader(f_obj)
            headers = next(f_csv)

            writer = csv.writer(wf_obj)
            writer.writerow(headers)
            fov_tiles = []
            fov_num = []

            for row in f_csv:
                fov_tiles = [int(i) for i in row[1:]]
                fov_num = int(row[0])
                tiles_pos = np.array(fov_tiles)
                raw_tiles_w = (tiles_pos - 1) % 20 + 1
                raw_tiles_h = np.floor((tiles_pos - 1) / 20) + 1

                # modified can not use round
                cur_tiles_w = np.floor((raw_tiles_w - 1) / 2.5) + 1
                cur_tiles_h = np.floor((raw_tiles_h - 1) / 2.5) + 1

                # print(cur_tiles_w)
                # print(cur_tiles_h)

                cur_pos = (cur_tiles_h - 1) * TILE_NUM_W + cur_tiles_w
                cur_pos_list = [fov_num]
                for i in list(cur_pos):
                    if i not in cur_pos_list:
                        cur_pos_list.append(i)
                    else:
                        pass

                # write to csv file
                writer.writerow(cur_pos_list)


if __name__ == '__main__':
    main()
