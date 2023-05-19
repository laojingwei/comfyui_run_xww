from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def select_file(img_type="*.png;*.JPEG;*.WEBP",title="选择图片",save_type=None):
    Tk().withdraw() # 隐藏根窗口
    if save_type:
        filename = asksaveasfilename(title=title, filetypes=[("Image files", img_type)])
    else:
        filename = askopenfilename(title=title, filetypes=[("Image files", img_type)])
    return filename