# -*- coding:utf-8 -*-
import tkinter as tk
from PIL import Image, ImageTk
# 调用Tk()创建主窗口


def res_position_button():
    pass


def main():
    root_window = tk.Tk()
    # 给主窗口起一个名字，也就是窗口的名字
    root_window.title('智能选址选线程序：')
    # 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
    root_window.geometry('1800x1200')
    # 更改左上角窗口的的icon图标,加载C语言中文网logo标
    root_window.iconbitmap('./icons8-earth-planet-48.ico')
    # 设置主窗口的背景颜色,颜色值可以是英文单词，或者颜色值的16进制数,除此之外还可以使用Tk内置的颜色常量
    root_window["background"] = "#C9C9C9"
    # 添加文本内,设置字体的前景色和背景色，和字体类型、大小
    text = tk.Label(root_window, text="智能选址选线程序", bg="white", fg="blue",
                    font=('Times', 60, ),
                    )
    # 将文本内容放置在主窗口内
    text.pack()
    #
    canvas = tk.Canvas(root_window, height=100, width=400)
    img = Image.open('./icons8-earth-planet-48.png')
    pimg = ImageTk.PhotoImage(img)
    canvas.create_image(500, 500, image=pimg)
    # label = tk.Label(root_window, image=pimg)
    # label.pack()
    # 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
    position_button = tk.Button(root_window, text="位置筛选", font=('Times', 30, 'bold italic'),
                                command=root_window.quit, height=1, width=20)
    position_button.pack(side='top', expand='yes')
    path_button = tk.Button(root_window, text="线路规划", font=('Times', 30, 'bold italic'),
                            command=root_window.quit, height=1, width=20)
    path_button.pack(side='top', expand='yes')
    # button = tk.Button(root_window, text="关闭", command=root_window.quit)
    # # 将按钮放置在主窗口内
    # button.grid()
    # 进入主循环，显示主窗口
    root_window.mainloop()


if __name__ == "__main__":
    main()