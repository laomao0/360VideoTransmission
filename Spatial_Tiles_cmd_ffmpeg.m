
% ffmpeg -s 3840x1920 -i Frame_0.yuv -filter:v "crop=1280:1920:0:0" FrameTiles.yuv

% srcFile = 'E:/campare_test/testing/PoleVault_le_3840x1920_30fps_8bit_420_erp.yuv';
Frame_size = '3840*1920'; % width * height 

Width = 3840;
Height = 1920;

tileNum_Width = 8;
tileNum_Height = 4;

tile_Width = Width / tileNum_Width;
tile_Height = Height / tileNum_Height;

x = 0;
y = 0;

for w = 0 : tileNum_Width - 1
	x = w * tile_Width;
    for h = 0 : tileNum_Height - 1
		y = h * tile_Height;
        cmd = sprintf('D:/ffmpeg/bin/ffmpeg -s %s -i D:/ffmpeg/bin/abc.yuv -filter:v "crop=%d:%d:%d:%d" D:/ffmpeg/bin/abc_w%02d-h%02d.yuv', Frame_size, tile_Width, tile_Height, x, y, w+1, h+1);%原始视频分辨率 分块视频的分辨率 x y表示相对位置
        cmd
        unix(cmd);
	end
end
