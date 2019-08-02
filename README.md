# use_ffmpeg_batch_extract_audio
使用前需要安装ffmpeg。参考安装教程https://blog.csdn.net/qq_39516859/article/details/81843419  。
使用ffmpeg批量提取音频，不转码，非常快，一秒提取一个
按照我上传的图片image.png将下列内容填入excel
start 	cmd /k ffmpeg -i 	"	D:\视频\维棠下载\48\方琪vlog\video\【小番茄】tomato’s vlog 1 下午吃广式早茶点都德 让少女偶像绝望的大油条.mp4	"	 -acodec copy -vn 	"	output	.aac	"	start cmd /k ffmpeg -i "D:\视频\维棠下载\48\方琪vlog\video\【小番茄】tomato’s vlog 1 下午吃广式早茶点都德 让少女偶像绝望的大油条.mp4" -acodec copy -vn =$A$1&$B$1&$C$1&D1&$E$1&$F$1&$G$1&SUBSTITUTE(D1,".flv","")&$I$1&$J$1
