# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import splitpdf

#定义点击事件
def butonck():
    # input_path = label_path_input.get().strip()
    input_path = select_file()
    start_num = int(label_start_input.get().strip())
    end_num = int(label_end_input.get().strip())

    splitpdf.split_pdf(input_path, start_num ,end_num)

def on_closing():
    messagebox.showinfo("成功", "程序已成功结束！")
    top.destroy()

def select_file():
    # top.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename()  # 打开文件选择对话框
    if file_path:
        log_text.insert(tk.END, "选择的文件是:"+file_path+ '\n')
    # top.destroy()  # 关闭程序
    return  file_path
top = tk.Tk()
# 标题
top.title("pdf分割工具")
# 窗口大小 长高用小写x隔开
top.geometry("500x400")
# 窗口基于屏幕的坐标 +x轴+y轴
top.geometry("+500+200")
# input_dir_text = Entry(top)
log_text = tk.Text(top, height=10, width=50)
log_text.grid(row=6, column=1, padx=6, pady=10)
# 添加说明文字标签
label = tk.Label(top, text="这是说明文字")
label.grid(row=5, column=1, padx=6, pady=10)

# # 创建lab标签 填写文件的输入路径
# label_path = Label(top, text="excle文件路径:", fg="red", font=("宋体", 12))
# # 显示lab标签 网格布局 sticky=W #左对齐 E为右对齐 默认为中间对齐
# label_path.grid(row=0, column=0, padx=6, pady=10)
#
# # # 创建输入框，填写文件路径
# label_path_input = Entry(top, font=("宋体", 12))
#
# # 显示输入框
# label_path_input.grid(row=0, column=1)

#起始页
label_start = Label(top, text="起始页:", fg="red", font=("宋体", 12))
# 显示lab标签 网格布局 sticky=W #左对齐 E为右对齐 默认为中间对齐
label_start.grid(row=1, column=0)

# 创建输入框，填写文件路径
label_start_input = Entry(top, font=("宋体", 12))

# 显示输入框
label_start_input.grid(row=1, column=1)


#起始页
label_end = Label(top, text="结束页:", fg="red", font=("宋体", 12))
# 显示lab标签 网格布局 sticky=W #左对齐 E为右对齐 默认为中间对齐
label_end.grid(row=2, column=0)

# 创建输入框，填写文件路径
label_end_input = Entry(top, font=("宋体", 12))

# 显示输入框
label_end_input.grid(row=2, column=1)

# 创建按钮
button = Button(top, text="选择pdf文件", font=("宋体", 15), command=butonck)
# 显示按钮
button.grid(row=3, column=1, padx=6, pady=10)

button1 = tk.Button(top, text="退出", command=on_closing)
button1.grid(row=4, column=1, padx=6, pady=10)


top.protocol("WM_DELETE_WINDOW", on_closing)

# 进入消息循环
top.mainloop()
