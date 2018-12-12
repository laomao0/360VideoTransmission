% x264已有重建YUV写成文件的接口，所以可以直接使用: ffmpeg -i INPUT ... -vcodec libx264 -x264opts dump-yuv=recon.yuv OUTPUT

% 设置总的传输码率为30000k
% ffmpeg -s 1920*960 -i input.yuv -b:v 600k -q 20 -r 30 -vframes 150 -bf 0 -g 15 -vcodec libx265 output.mp4

% srcFile = 'FrameTile_w%02d-h%02d.yuv';

% Processing a picture.yuv
% 每个分块的传输码率
% bitrate = 600;
% qp = 20;
fps = 30;
num_frames = 300;
% gopsize = 15;
Frame_size = '480*480';  % width * height

width_Tile_num = 8;
height_Tile_num = 4;
k=0;
% h=1;
% t=0;

cmd = sprintf('D:/ffmpeg/bin/ffmpeg -r 30 -s 480*480 -i D:/ffmpeg/bin/upsample_part1x1_abc_proposed.yuv -r 30 -vf pad=3840:1920:0:0:black D:/ffmpeg/bin/abc_8x4coded_0.yuv');
%unix(cmd);
cmd
for x = 1 : width_Tile_num
    for y = 1 : height_Tile_num
        cmd = sprintf('D:/ffmpeg/bin/ffmpeg -s 3840*1920 -r 30 -i D:/ffmpeg/bin/abc_8x4coded_%d.yuv  -s %s -r 30 -i D:/ffmpeg/bin/upsample_part%dx%d_abc_proposed.yuv -filter_complex "[0:v][1:v]overlay=480*%d:480*%d" D:/ffmpeg/bin/abc_8x4coded_%d.yuv',k,Frame_size,x, y, x-1,y-1,k+1);
        %unix(cmd);
        cmd
        if k>=1
            %delete (['D:/ffmpeg/bin/abc_8x4coded_',num2str(k),'.yuv']);
        end
        k=k+1;      
    end
end