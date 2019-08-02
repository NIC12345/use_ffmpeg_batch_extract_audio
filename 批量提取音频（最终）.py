# -*- coding: utf-8 -*-
import os
from tkinter import *
import tkinter.filedialog

root = Tk()

def window48():
    filenames = tkinter.filedialog.askopenfilenames()
    if len(filenames) != 0:
        for i in range(0, len(filenames)):
            path = filenames[i]
            print(path)
            cmd48 = '''ffmpeg -i "''' + path + '''" -acodec copy -vn "''' + os.path.splitext(path)[0] + '''.aac"'''
            # print(cmd48)#'ffmpeg -i "D:/video/维棠下载/48/方琪vlog/video/【小番茄】tomato’s vlog 1 下午吃广式早茶点都德 让少女偶像绝望的大油条.mp4" -acodec copy -vn "D:/video/维棠下载/48/方琪vlog/video/【小番茄】tomato’s vlog 1 下午吃广式早茶点都德 让少女偶像绝望的大油条.aac"'
            # os.system('ffmpeg -i "D:/video/维棠下载/48/方琪vlog/video/【小番茄】tomato’s vlog 1 下午吃广式早茶点都德 让少女偶像绝望的大油条.mp4" -acodec copy -vn "D:/video/维棠下载/48/方琪vlog/video/【小番茄】tomato’s vlog 1 下午吃广式早茶点都德 让少女偶像绝望的大油条.mp4.aac"')
            os.system('%s' % (cmd48))
        print('完成了'+os.path.dirname(filenames[0]))
    else:
        lb.config(text = "You did not select any files")

def center_window(w, h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


center_window(425, 210)



lb = Label(root, text='please install ffmpeg before use')
lb.pack()
btn = Button(root, text="please select video file", command=window48)
btn.pack()
root.mainloop()