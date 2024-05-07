import sys
import os
import subprocess
import threading
import shutil
import requests
from io import BytesIO
from os import listdir
from os.path import isfile, join
import base64
import glob
from PIL import Image
import json
import imghdr
import io
import yaml
import webbrowser
    
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget, QHBoxLayout, QSizePolicy
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtCore import Signal, Slot, Property, QUrl, QObject, Qt
from PySide6.QtGui import QIcon
import download_project as dp
import models_config as mc
import psutil
import select_local_file as slf
import git_code as gc
import ch_en as ce
import image_data as imgd

def start():
    cwd = os.getcwd()
    run_xwwbk = os.path.join(cwd, "xww_lib", "run_xww")
    run_xww = os.path.join(cwd, "ComfyUI_windows_portable", "ComfyUI", "custom_nodes", "run_xww")
    checkPath = os.path.join(cwd, "ComfyUI_windows_portable","ComfyUI")

    if os.path.isdir(checkPath):
        if not os.path.isdir(run_xww):
            if ce.getCHEN() == "EN":
                print("----------start-------------The run xww folder was not found and is being processed。。。")
            else:
                print("----------start-------------未发现run_xww文件夹，正在处理。。。")
            shutil.copytree (run_xwwbk, run_xww)
            if ce.getCHEN() == "EN":
                print("-----------end------------The run xww folder is processed--------------")
            else:
                print("-----------end------------run_xww文件夹处理完成--------------")


    # import shutil
    # import glob
    # # 匹配以Pyside6开头的文件夹
    # dirs = glob.glob (pysidePath+"*")
    # # 遍历匹配到的文件夹
    # for dir in dirs: # 删除文件夹及其内容
    #     shutil.rmtree (dir)


    class MyWindow(QWidget):
        linkPath = ""
        linkPath1 = ""
        linkPath2 = ""
        # 初始化方法

        def __init__(self):
            # 调用父类的初始化方法
            super().__init__()
            # 设置窗口标题
            self.setWindowTitle("xww")
            # 设置窗口大小
            self.resize(1000, 700)
            # 设置窗口的背景颜色为黑色
            self.setStyleSheet("background-color: black;")
            # 设置窗口图标
            icon = os.path.join(cwd, "xww_lib", "dist", "xww.jpg")
            self.setWindowIcon(QIcon(icon))
            # 创建一个水平布局
            layout = QHBoxLayout()
            # 创建一个Qobj对象
            self.qobj = self.Qobj(self)
            # 传入self作为父对象 # 将QWebEngineView对象添加到布局中
            layout.addWidget(self.qobj.view)
            # 设置QWebEngineView对象的大小策略为自适应
            self.qobj.view.setSizePolicy(
                QSizePolicy.Expanding, QSizePolicy.Expanding)
            # 设置QWebEngineView对象的网页源为百度首页
            # self.qobj.view.load(QUrl("https://www.baidu.com")) # 将布局设置为窗口的主布局
            self.setLayout(layout)

        # 重载窗口关闭方法
        def closeEvent(self, event):
            self.setStyleSheet("QMessageBox { background-color: white; }" "QPushButton { color: black; }")  # 设置消息对话框和按钮的样式表
            # 弹出一个对话框，询问用户是否确定关闭窗口
            title = ""
            text = ""
            if ce.getCHEN() == "EN":
                title = "Don't mess with it"
                text = "Are you sure to close? Clicking OK will close Comfyui as well"
            else:
                title = "别乱点哦"
                text = "确定关闭吗？点击确定会同时关闭Comfyui"
            reply = QMessageBox.question(self, title,
                text, QMessageBox.Yes | 
                QMessageBox.No, QMessageBox.No)
            # 如果用户选择是，就接受关闭事件
            if reply == QMessageBox.Yes:
                if self.qobj.process:
                    if self.qobj.process.pid and psutil.Process(self.qobj.process.pid).children():
                        children = psutil.Process(self.qobj.process.pid).children()
                        print(children)
                        for child in children:
                            # 终止批处理文件
                            os.system('taskkill /F /PID ' + str(child.pid))
                        os.system('taskkill /F /PID ' + str(self.qobj.process.pid))
                os._exit(0)
            # 如果用户选择否，就忽略关闭事件
            else:
                event.ignore()
                # 设置窗口的背景颜色为黑色
                self.setStyleSheet("background-color: black;")

        class Qobj(QObject):
            # 定义一个信号
            mySignal = Signal(str)
            runStatData = Signal(str)
            # base64信号
            base64List = Signal(list)
            # modelsData信号
            modelsData = Signal(list)
            # saveData信号
            moreselect = Signal(list)
            layoutData = Signal(list)
            isHaveComfyUI = Signal(str)
            changeModesPath = Signal(str)
            useYmalFlag = Signal(str)
            changeImgBase64 = Signal(str)
            notTipsFlag = Signal(str)
            updateCuiBat = Signal(str)
            gitFlag = Signal(str)
            gitCloneFlag = Signal(str)
            gitData = Signal(list)
            gitComfyuiData = Signal(list)
            checkoutGitData = Signal(list)
            refreshData = Signal(list)
            chenFlag = Signal(str)
            imageData = Signal(list)
            saveFlag = Signal(str)
            customNodeLink = Signal(list)
            addModelList = Signal(list)
            downloadModelFlag = Signal(str)
            updateXwwV = Signal(list)
            updateXww = Signal(str)
            donloadFlag = Signal(str)
            threadList = Signal(list)
            # 进度
            progress = Signal(str)
            # 定义属性变化时的信号
            myPropertyChanged = Signal(str)

            def __init__(qobj, parent=None):
                super().__init__(parent)
                qobj.process = None
                # 初始化网页视图和 web 通道
                qobj.view = QWebEngineView()
                qobj.channel = QWebChannel()
                # setAttribute(QWebEngineSettings::ShowScrollBars, false);
                qobj.view.page().setBackgroundColor(Qt.black)
                # qobj.view.setStyleSheet("background-color: wite;")
                qobj.view.setStyleSheet(
                    "QMessageBox { background-color: white; }" "QPushButton { color: white; }")  # 设置消息对话框和按钮的样式表
                # 设置网页视图的大小和位置
                qobj.view.setWindowTitle("xww")
                # qobj.view.setGeometry(500,200,900,800)
                url = os.path.join(cwd, "xww_lib", "dist", "index.html")
                # 设置网页视图加载的网址，假设是 http://localhost:8080/index.html
                qobj.view.load(QUrl.fromLocalFile(url))  # 修改 load 函数的参数为 QUrl 对象
                # 设置 web 通道为网页视图的页面的 web 通道
                qobj.view.page().setWebChannel(qobj.channel)
                # 将自身对象发布到 web 通道中，并命名为 myObject
                qobj.channel.registerObject("xwwqt", qobj)
                qobj.mySignal.emit('{"stat":"555"}')  # 修改返回值为信号发送)


            # 检查url是否正常访问
            @Slot(str)
            def check_url(qobj, url):
                # 创建一个后台线程来执行bat文件
                thread = threading.Thread(
                    target=qobj.check_url_Thread, args=(url,))
                thread.start()

            def check_url_Thread(qobj, url):
                stat = False
                try:
                    response = requests.head(url)
                    stat = response.status_code == 200
                except:
                    stat = False
                stat_v = '404'
                if stat:
                    stat_v = '0'
                # print('{"stat":"'+stat_v+'"}')
                qobj.mySignal.emit('{"stat":"'+stat_v+'"}')  # 修改返回值为信号发送

            def run_bat(qobj, arg):
                # 使用subprocess.Popen代替os.system
                qobj.process = subprocess.Popen(os.path.join(cwd, "xww_lib", arg))
                # 保存子进程的pid
                qobj.pid = qobj.process.pid

            # 保存中英切换标志
            @Slot(str)
            def change_CHEN(qobj,str):
                qobj.chenFlag.emit(ce.change_CHEN(str))

            # 获取中英切换标志
            @Slot()
            def getCHEN(qobj):
                qobj.chenFlag.emit(ce.getCHEN())

            # 下载模型
            @Slot(list)
            def downloadModel(qobj,args):
                thread = threading.Thread(
                    target=qobj.downloadModel_, args=(args[0],))
                thread.start()
            def downloadModel_(qobj,args):
                args["self_"] = qobj
                mc.downloadModel(args)

            # 获取模型下载地址
            @Slot()
            def get_add_models_data(qobj):
                data = gc.check_installed_models()
                if not data:
                    data = []
                qobj.addModelList.emit(data)

            # 获取自定义节点下载地址
            @Slot()
            def getCustomNodeLink(qobj):
                thread = threading.Thread(
                    target=qobj.getCustomNodeLink_)
                thread.start()
            def getCustomNodeLink_(qobj):
                try:
                    qobj.customNodeLink.emit(gc.check_installed_nodes())
                except Exception as e:
                    print(e)
                    qobj.customNodeLink.emit([""])

            # 压缩图片
            @Slot()
            def imge_compression(qobj):
                qobj.imageData.emit(["start"])
                data = imgd.get_image_data()
                qobj.imageData.emit(data)

            # 获取图片里的信息
            @Slot()
            def get_image_data(qobj):
                qobj.imageData.emit(["start"])
                data = imgd.get_image_data()
                qobj.imageData.emit(data)

            # 不再提示
            @Slot()
            def notTips(qobj):
                path = os.path.join(cwd, "xww_lib", "savedata", "notTips.txt")
                with open(path, 'w', encoding='utf-8') as f:
                    f.write('notTips')
                    qobj.notTipsFlag.emit('notTips')

            # 获取提示标志
            @Slot()
            def getNotTips(qobj):
                path = os.path.join(cwd, "xww_lib", "savedata", "notTips.txt")
                try:
                    # 打开文件
                    f = open(path, "r", encoding='utf-8')
                    # 读取文件的全部内容
                    content = f.read()
                    # 关闭文件
                    f.close()
                    qobj.notTipsFlag.emit(content)
                except Exception:
                    qobj.notTipsFlag.emit("")

            def startUpdateCuiBat(qobj,path):
                qobj.updateCuiBat.emit('start')
                runPath = os.path.join(cwd, "xww_lib", path)

                if not os.path.isfile(runPath):
                    if path == "update_comfyui.bat":
                        runPath = os.path.join(cwd, "xww_lib", "update_comfyui_only.bat")
                    elif path == "update_comfyui_and_python_dependencies.bat":
                        runPath = os.path.join(cwd, "xww_lib", "update_all.bat")
                    else:
                        qobj.updateCuiBat.emit('finish')
                        if ce.getCHEN() == "EN":
                            print("Execution file not found...")
                        else:
                            print("未找到执行文件。。。")
                        return
                os.system(runPath)
                qobj.updateCuiBat.emit('finish')
                if ce.getCHEN() == "EN":
                    print("\n\nEnd of processing... , please try again if any error is reported, because access to gitHub in China often fails, please go to the corresponding address to download if necessary...\n")
                else:
                    print('\n\n处理结束。。。，如果报错请重新操作，因为国内gitHub经常会访问失败，如有必要请自行前往相应地址下载。。。\n')

            # 更新整合包
            @Slot(str)
            def updateCui(qobj,path):
                thread = threading.Thread(
                    target=qobj.startUpdateCuiBat, args=(path,))
                thread.start()

            #检查启动器版本
            @Slot()
            def check_xww_v(qobj):
                qobj.updateXwwV.emit(["start"])
                thread = threading.Thread(
                    target=qobj.check_xww_v_)
                thread.start()
            def check_xww_v_(qobj):
                qobj.updateXwwV.emit(gc.check_xww_v())

            # 更新启动器
            @Slot(str)
            def update_xww(qobj, hexsha):
                thread = threading.Thread(
                    target=qobj.update_xww_, args=(hexsha,))
                thread.start()
            def update_xww_(qobj, hexsha):
                print(hexsha)
                qobj.updateXww.emit("start")
                if ce.getCHEN() == "EN":
                    print("Please wait for a moment...")
                else:
                    print('正在更新，请稍等。。。')
                res = gc.git_checkout(cwd,hexsha)
                if res == ["success"]:
                    qobj.updateXww.emit("success")
                else:
                    qobj.updateXww.emit("error")

            # 检查是否有下载ComfyUI_windows_portable整合包
            @Slot()
            def check_confyui_package(qobj):
                checkPath = os.path.join(cwd, "ComfyUI_windows_portable")
                isHave = "0"
                if not os.path.isdir(checkPath):
                    isHave = "0"
                    if ce.getCHEN() == "EN":
                        print("ComfyUI_windows_portable project not found, please download...")
                    else:
                        print("未发现ComfyUI_windows_portable项目，请先下载。。。")
                else:
                    isHave = "1"
                qobj.isHaveComfyUI.emit(isHave)

            # 下载项目
            @Slot(int, int)
            def downloadProject(qobj,i,k):
                qobj.donloadFlag.emit("start")
                # 创建一个后台线程来执行文件下载
                thread = threading.Thread(target=qobj.downloadProject_, args=(i,k,))
                thread.start()
            def downloadProject_(qobj,i,k):
                flag = dp.dowload(int(i),int(k))
                if flag == "error":
                    qobj.donloadFlag.emit("error")
                    return
                # 更新项目状态
                qobj.check_confyui_package()
                qobj.donloadFlag.emit("success")

            # 使用 Slot 装饰器定义一个启动槽函数
            @Slot(str)
            def start(qobj, data): 
                if qobj.process:
                    if qobj.process.pid and psutil.Process(qobj.process.pid).children():
                        children = psutil.Process(qobj.process.pid).children()
                        print(children)
                        for child in children:
                            # 终止批处理文件
                            os.system('taskkill /F /PID ' + str(child.pid))
                        os.system('taskkill /F /PID ' + str(qobj.process.pid))
                        if ce.getCHEN() == "EN":
                            print(f'\nRestarting ing with {data}...\n')
                        else:
                            print(f'\n正在使用{data}重新启动ing。。。\n')
                # 创建一个后台线程来执行bat文件
                thread = threading.Thread(target=qobj.run_bat, args=(data,))
                # 设置线程为守护线程，防止退出主线程时，子线程仍在运行
                thread.setDaemon(True)
                thread.start()

            # 定义一个槽函数
            @Slot(str, result=str)
            def cread_symlink(self, linkPath):
                print(linkPath)
                if not os.path.isdir(linkPath):
                    if ce.getCHEN() == "EN":
                        mw.alert_show("tips", "The input path does not exist. Check whether the path is correct")
                    else:
                        mw.alert_show("温馨提示", "输入路径不存在，请检查路径是否正确")
                    return
                mw.linkPath = linkPath
                mw.cread_symlink_my()
            # 定义一个槽函数

            @Slot(str, str, result=str)
            def cread_symlink_auto(self, path1, path2):
                if not os.path.isdir(path1):
                    if ce.getCHEN() == "EN":
                        mw.alert_show("tips", "The input path does not exist. Check whether the path is correct")
                    else:
                        mw.alert_show("温馨提示", "输入路径不存在，请检查路径是否正确")
                    return
                # if not os.path.isdir(path2):
                #     mw.alert_show()
                #     return
                mw.linkPath1 = path1
                mw.linkPath2 = path2
                mw.cread_symlink_auto_my()

            # 获取图片数据
            @Slot(str, str, str, str, float)
            def set_img(qobj, type, img_path, out_path, rate):
                thread = threading.Thread(target=mw.get_local_img, args=(
                    qobj, type, img_path, out_path, rate,))
                thread.start()

            # 获取图片数据
            @Slot(list, int, int)
            def resize_img(qobj, path_list, w, h):
                thread = threading.Thread(
                    target=mw.resize_img_, args=(qobj, path_list, w, h,))
                thread.start()

            # 保存图片
            @Slot(str)
            def save_base64_2_img(qobj, bs64_data):
                qobj.saveFlag.emit("start")
                try:
                    img_data = base64.b64decode(bs64_data) # 把base64字符串转换为二进制数据
                    img = Image.open(io.BytesIO(img_data)) # 把二进制数据转换为图像对象
                    filename = slf.select_file("*.png;*.JPEG","保存图片",True)
                    if filename: # 如果选择了文件名
                        _,img_type = os.path.splitext(filename)
                        img_type = img_type.replace(".","")
                        if img_type == "jpg" or img_type == "JPG":
                            img_type = "JPEG"
                        img.save(filename, format=img_type, quality=100) # 保存图片，并指定数据格式和压缩质量
                        qobj.saveFlag.emit("success")
                        dir_path = filename.replace(os.path.basename(filename),'')
                        os.startfile(dir_path)
                    else:
                        qobj.saveFlag.emit("noselect")
                except Exception as e:
                    print(e)
                    qobj.saveFlag.emit("error")

            # 处理图片大小
            @Slot(int, int, str)
            def resize_img_select(qobj, w, h, path):
                qobj.base64List.emit(["start"])
                if path:
                    imagePath = path
                else:
                    imagePath = slf.select_file()
                if not imagePath:
                    qobj.base64List.emit(["noselect"])
                    return
                try:
                    f = open(imagePath, 'rb') # 第一个参数是图片的路径
                    join_list = [base64.b64encode(f.read()).decode()] # 将图片读取为二进制数据并编码为base64字符串
                    image = Image.open(f)
                    o_size = os.path.getsize(imagePath)/1024
                    size = image.size
                    img_data = [{"size": str(size), "kb": f"{o_size} kb", "path": imagePath}]
                    f.close()
                    path_list = [imagePath]
                    thread = threading.Thread(
                        target=mw.resize_img_, args=(qobj, path_list, w, h, join_list, img_data, True,))
                    thread.start()
                except Exception as e:
                    print(e)
                    qobj.base64List.emit(["error"])

            # 获取models数据
            @Slot(result=list)
            def get_models_data(qobj):
                dir_path = os.path.join(cwd, "ComfyUI_windows_portable", "ComfyUI", "models")
                thread = threading.Thread(
                    target=mw.get_dir_names, args=(qobj, dir_path))
                thread.start()

            # 更换图片
            @Slot(str)
            def change_img(qobj,filepath):
                qobj.changeImgBase64.emit('')
                filename = os.path.basename(filepath) # 获取文件名
                filepath = filepath.replace(filename,"")
                filepath = filepath + os.path.splitext(filename)[0]+".png" # 去掉后缀
                img_path = slf.select_file("*.png")
                if not img_path:
                    qobj.changeImgBase64.emit('NONE')
                    return
                # print(filepath,img_path)
                # 读取图片文件
                image = Image.open(img_path)
                # 压缩图片到指定大小
                image = image.resize((300, 300))
                # 创建一个字节流对象
                byte_data = BytesIO()
                # 将图片数据存入字节流对象，格式为JPEG
                image.save(byte_data, format="PNG")
                # 获取字节流对象的二进制数据
                byte_data = byte_data.getvalue()
                # 将二进制数据转为base64字符串
                base64_str = base64.b64encode(byte_data).decode("ascii")
                qobj.changeImgBase64.emit(base64_str)
                img = Image.open(io.BytesIO(byte_data)) # 用BytesIO对象创建一个图片对象
                img.save(filepath) # 保存图片到文件

            # 打印内容
            @Slot(str)
            def openUrl(qobj, url):
                webbrowser.open(url)

            # 打印内容
            @Slot(str)
            def py_print(qobj, data):
                print(data)
            
            # 检查使用了哪种model方式    
            @Slot()
            def checkYmalFlag(qobj):
                mc.checkYmalFlag(qobj)

            # 是否使用ymal文件路径
            @Slot(str)
            def useYmal(qobj,i):
                mc.useYmal(qobj,mw,i)

            # 设置models路径
            @Slot(str)
            def setModesPath(qobj, path):
                if not os.path.isdir(path):
                    if ce.getCHEN() == "EN":
                        mw.alert_show("tips", "The input path does not exist. Check whether the path is correct")
                    else:
                        mw.alert_show("温馨提示", "输入路径不存在，请检查路径是否正确")
                    return
                mc.setModesPath(qobj,path)

            # 弹框
            @Slot(str, str)
            def py_alert(qobj, title, text):
                mw.alert_show(title, text)

            # 启动状态
            @Slot(str)
            def run_stat(qobj, data):
                path = os.path.join(cwd, "xww_lib", "savedata", "runStat.txt")
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(data)

                qobj.runStatData.emit(data)

            # 获取save数据
            @Slot()
            def get_run_data(qobj):
                path = os.path.join(cwd, "xww_lib", "savedata", "runStat.txt")
                try:
                    # 打开文件
                    f = open(path, "r", encoding='utf-8')
                    # 读取文件的全部内容
                    content = f.read()
                    # 关闭文件
                    f.close()
                    qobj.runStatData.emit(content)
                except Exception:
                    qobj.runStatData.emit("")

            # 打开本地文件
            @Slot(str, str)
            def open_local_file(qobj, path, type):
                if type == 'file':
                    print('open_local_file:', path)
                    os.system('explorer /select,'+path)
                else:
                    if path == 'output':
                        path = os.path.join(cwd, "ComfyUI_windows_portable", "ComfyUI", "output")
                    elif path == 'ComfyUI':
                        path = os.path.join(cwd, "ComfyUI_windows_portable", "ComfyUI")
                    print('open_local_dir:', path)
                    os.startfile(path)

            # 获取save数据
            @Slot(str)
            def get_save_data(qobj, fileName):
                path = os.path.join(cwd, "xww_lib", "savedata", fileName)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        json_data = f.read()
                        data = json.dumps(json.loads(json_data))
                        # print (data)
                        if fileName == 'moreselect.json':
                            qobj.moreselect.emit([data, fileName])
                        else:
                            qobj.layoutData.emit([data, fileName])
                except Exception:
                    if fileName == 'moreselect.json':
                        qobj.moreselect.emit([[], fileName])
                    else:
                        qobj.layoutData.emit([[], fileName])

            # 保存数据(只支持json和txt)
            @Slot(str, str, str)
            def save_data(qobj, data, fileName, type):
                path = os.path.join(cwd, "xww_lib", "savedata", fileName)
                if type == "json":
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(data)
                elif type == "txt":
                    # ‘w’：写入模式，如果文件不存在，会创建一个新文件；如果文件存在，会覆盖原有内容。
                    # ‘a’：追加模式，如果文件不存在，会创建一个新文件；如果文件存在，会在末尾追加内容。
                    # ‘x’：独占模式，如果文件不存在，会创建一个新文件；如果文件存在，会抛出异常。
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(data)

            # 安装自定义节点
            @Slot(str, int, str)
            def clone_from(qobj, path, i, name):
                qobj.gitCloneFlag.emit(f"start#-#{name}")
                if ce.getCHEN() == "EN":
                    print("\nReady to download...\n")
                else:
                    print("\n准备下载中。。。\n")
                thread = threading.Thread(target=qobj.clone_from_, args=(qobj, path, i,name,))
                thread.start()
            def clone_from_(self, qobj, path, i,name):
                res = gc.clone_from(path, i)
                qobj.gitCloneFlag.emit(f"{res}#-#{name}")
            
            #获取comfyui版本信息
            @Slot(str)
            def git_comfyui_code(qobj,type):
                qobj.gitFlag.emit('start')
                qobj.gitComfyuiData.emit(['NONE'])
                thread = threading.Thread(target=qobj.git_comfyui_code_, args=(qobj, type,))
                thread.start()
            def git_comfyui_code_(slef,qobj,type):
                data = gc.git_comfyui_code(type,qobj)
                qobj.gitComfyuiData.emit(data)
                # print(data)
                qobj.gitFlag.emit('success')

            # 获取自定义节点列表
            @Slot()
            def get_node_data(qobj):
                qobj.gitData.emit(['NONE'])
                thread = threading.Thread(target=qobj.get_node_data_)
                thread.start()
            def get_node_data_(qobj):
                try:
                    qobj.gitData.emit(gc.get_node_data())
                except Exception as e:
                    print(e)
                    qobj.gitData.emit(['error'])

            # 切换自定义节点版本
            @Slot(str, str, str)
            def git_checkout(qobj, rep_path, hexsha, name):
                qobj.gitFlag.emit('start')
                qobj.checkoutGitData.emit(["NONE"])
                thread = threading.Thread(target=qobj.git_checkout_, args=(qobj, rep_path, hexsha, name,))
                thread.start()
            def git_checkout_(self, qobj, rep_path, hexsha, name):
                qobj.checkoutGitData.emit(gc.git_checkout(rep_path,hexsha, name))
                qobj.gitFlag.emit('success')

            # 切换comfyui版本
            @Slot(str, str)
            def git_checkout_cy(qobj, rep_path, hexsha):
                qobj.gitFlag.emit('start')
                thread = threading.Thread(target=qobj.git_checkout_cy_, args=(qobj, rep_path, hexsha,))
                thread.start()
            def git_checkout_cy_(self, qobj, rep_path, hexsha):
                qobj.gitFlag.emit(gc.git_checkout_cy(rep_path,hexsha))

            # 刷新获取最新github数据
            @Slot(str, str)
            def refresh_data(qobj, rep_path, name):
                qobj.gitFlag.emit('start')
                qobj.refreshData.emit(["NONE"])
                thread = threading.Thread(target=qobj.refresh_data_, args=(qobj, rep_path, name,))
                thread.start()
            def refresh_data_(self, qobj, rep_path, name):
                qobj.refreshData.emit(gc.refresh_data(rep_path, name))
                qobj.gitFlag.emit('success')

            # 设置节点启用状态
            @Slot(str, str)
            def file_stat(qobj, path, type):
                qobj.gitFlag.emit('')
                qobj.gitFlag.emit(gc.file_stat(path, type))


        def alert_show(self, title, text):
            self.setStyleSheet(
                "QMessageBox { background-color: white; }" "QPushButton { color: black; }")  # 设置消息对话框和按钮的样式表
            QMessageBox.information(self, title, text)
            # 设置窗口的背景颜色为黑色
            self.setStyleSheet("background-color: black;")
        # 定义一个槽函数

        def cread_symlink_my(self):
            self.setStyleSheet(
                "QMessageBox { background-color: white; }" "QPushButton { color: black; }")  # 设置消息对话框和按钮的样式表
            msg_box = QMessageBox(self)  # 创建一个消息对话框
            msg_box.setIcon(QMessageBox.Information)  # 设置图标为信息图标
            title = ""
            text = ""
            cancle = ""
            ok = ""
            if ce.getCHEN() == "EN":
                title = "tips"
                text = "If you have done soft connection operations for these folders before, this operation will clear the previous connection and rebind. Please confirm again whether your source path is this one?--> "
                cancle = "cancel"
                ok = "ok"
            else:
                title = "温馨提示"
                text = "如果你之前有对这些文件夹已经做了软连接操作，本次操作会清除之前的连接重新绑定，请再次确认你的源路径是这个吗？--> "
                cancle = "取消"
                ok = "确定"
            msg_box.setWindowTitle(title)
            msg_box.setText(
                text+mw.linkPath)  # 设置文本内容
            msg_box.setStandardButtons(
                QMessageBox.Ok | QMessageBox.Cancel)  # 设置按钮为确定和取消
            msg_box.setButtonText(QMessageBox.Ok, ok)  # 设置确定按钮的文本为中文
            msg_box.setButtonText(QMessageBox.Cancel, cancle)  # 设置取消按钮的文本为中文
            msg_box.buttonClicked.connect(self.symlink)
            # msg_box.setStyleSheet("QMessageBox { background-color: white; }" "QPushButton { color: black; }") # 设置消息对话框和按钮的样式表
            msg_box.show()  # 显示消息对话框

        # 定义一个槽函数
        def cread_symlink_auto_my(self):
            self.setStyleSheet(
                "QMessageBox { background-color: white; }" "QPushButton { color: black; }")  # 设置消息对话框和按钮的样式表
            msg_box = QMessageBox(self)  # 创建一个消息对话框
            msg_box.setIcon(QMessageBox.Information)  # 设置图标为信息图标

            title = ""
            text = ""
            cancle = ""
            ok = ""
            if ce.getCHEN() == "EN":
                title = "tips"
                text = "If you have done soft connection operations for these folders before, this operation will clear the previous connection and rebind. Please confirm again whether your source path is this one?--> "
                cancle = "cancel"
                ok = "ok"
            else:
                title = "温馨提示"
                text = "如果你之前有对这些文件夹已经做了软连接操作，本次操作会清除之前的连接重新绑定，请再次确认你的源路径是这个吗？--> "
                cancle = "取消"
                ok = "确定"

            msg_box.setWindowTitle(title)
            msg_box.setText(text +
                            mw.linkPath1+"  ----->   "+mw.linkPath2)  # 设置文本内容
            msg_box.setStandardButtons(
                QMessageBox.Ok | QMessageBox.Cancel)  # 设置按钮为确定和取消
            msg_box.setButtonText(QMessageBox.Ok, ok)  # 设置确定按钮的文本为中文
            msg_box.setButtonText(QMessageBox.Cancel,cancle)  # 设置取消按钮的文本为中文
            msg_box.buttonClicked.connect(self.symlink_auto)
            # msg_box.setStyleSheet("QMessageBox { background-color: white; }" "QPushButton { color: black; }") # 设置消息对话框和按钮的样式表
            msg_box.show()  # 显示消息对话框

        def symlink_auto(self, button):
            # 设置窗口的背景颜色为黑色
            self.setStyleSheet("background-color: black;")
            # 获取消息对话框对象
            msg_box = self.sender()
            # 获取用户点击的标准按钮
            result = msg_box.standardButton(button)
            if result == QMessageBox.Ok:  # 如果用户点击了确定
                try:
                    target = os.readlink(mw.linkPath2)
                    print(mw.linkPath2, "-> This is a symlink to", target)
                    flag = ""
                    if ce.getCHEN() == "EN":
                        flag = "modification"
                        print("Reestablishing the connection...")
                    else:
                        flag = "修改"
                        print("正在重新建立连接...")
                    os.unlink(mw.linkPath2)
                    mw.check_symlink(self, mw.linkPath2, flag, mw.linkPath1)
                except Exception:
                    print(mw.linkPath2, "-> This is not a symlink")
                    if os.path.isdir(mw.linkPath2):
                        if ce.getCHEN() == "EN":
                            print("Deleting folder...", mw.linkPath2)
                        else:
                            print("正在删除文件夹...", mw.linkPath2)
                        shutil.rmtree(mw.linkPath2)
                    flag = ""
                    if ce.getCHEN() == "EN":
                        flag = "add"
                        print("Adding a connection...")
                    else:
                        flag = "新增"
                        print("正在新增连接...")
                    mw.check_symlink(self, mw.linkPath2, flag, mw.linkPath1)
                self.setStyleSheet(
                    "QMessageBox { background-color: white; }" "QPushButton { color: black; }")  # 设置消息对话框和按钮的样式表
                title = ""
                text = ""
                if ce.getCHEN() == "EN":
                    title = "tips"
                    text = "The operation is complete. See the console log for details"
                else:
                    title = "温馨提示"
                    text = "操作完成，详情请看控制台日志"
                QMessageBox.information(self, title, text)
                # 设置窗口的背景颜色为黑色
                self.setStyleSheet("background-color: black;")

        def symlink(self, button):
            # 设置窗口的背景颜色为黑色
            self.setStyleSheet("background-color: black;")
            # 获取消息对话框对象
            msg_box = self.sender()
            # 获取用户点击的标准按钮
            result = msg_box.standardButton(button)
            if result == QMessageBox.Ok:  # 如果用户点击了确定
                # url = os.path.join(cwd, "xww_lib", "dist", "index.html")
                localPath = os.path.join(cwd, "ComfyUI_windows_portable", "ComfyUI", "models")
                modelsPath = self.linkPath
                # 判断是否已是符号连接
                # isLink = os.path.islink("F:/xxx/ComfyUI_windows_portable/ComfyUI/models")
                modelsList = [{"checkpoints": modelsPath+'\models\Stable-diffusion'}, {"loras": modelsPath+'\models\Lora'}, {"vae": modelsPath +
                                                                                                                            '\models\VAE'}, {"controlnet": modelsPath+'\extensions\sd-webui-controlnet\models'}, {"embeddings": modelsPath+'\embeddings'}]
                for d in modelsList:
                    for k, v in d.items():
                        print('kk--', k)
                        if os.path.isdir(v):
                            path = os.path.join(localPath, k)
                            try:
                                target = os.readlink(path)
                                print(k, "-> This is a symlink to", target)
                                flag = ""
                                if ce.getCHEN() == "EN":
                                    flag = "modification"
                                    print("Reestablishing the connection...")
                                else:
                                    flag = "修改"
                                    print("正在重新建立连接...")
                                os.unlink(path)
                                mw.check_symlink(self, path, flag, v)
                            except Exception:
                                print(k, "-> This is not a symlink")
                                if os.path.isdir(path):
                                    if ce.getCHEN() == "EN":
                                        flag = "modification"
                                        print("Deleting folder...", path)
                                    else:
                                        print("正在删除文件夹...", path)
                                    shutil.rmtree(path)
                                flag = ""
                                if ce.getCHEN() == "EN":
                                    flag = "add"
                                    print("Adding a connection...")
                                else:
                                    flag = "新增"
                                    print("正在新增连接...")
                                mw.check_symlink(self, path, flag, v)
                        else:
                            print('error:-->找不到路径：', v)
                title = ""
                text = ""
                if ce.getCHEN() == "EN":
                    title = "tips"
                    text = "Operation completed, please see console log for details, you can go to the model to see the effect, operation completed, please see console log for details, you can go to the model to see the effect, ComfyUI effective needs to restart"
                else:
                    title = "tips"
                    text = "操作完成，详情请看控制台日志，可前往模型查看效果，ComfyUI生效需要重启"
                self.setStyleSheet(
                    "QMessageBox { background-color: white; }" "QPushButton { color: black; }")  # 设置消息对话框和按钮的样式表
                QMessageBox.information(self, title, text)
                # 设置窗口的背景颜色为黑色
                self.setStyleSheet("background-color: black;")

        def check_symlink(self, path, type, v):
            try:
                print(path, '-------', type, '-------', v)
                os.symlink(v, path)
                newTo = os.readlink(path)
                if ce.getCHEN() == "EN":
                    print(type, "Successfully, the connection has been set up", path, ' ---> ', newTo, "\n")
                else:
                    print(type, "成功，已成功搭建连接", path, ' ---> ', newTo, "\n")
            except Exception as e:  # 捕获异常对象并命名为e
                print(e)  # 打印异常对象

        def get_local_img(type, img_path, out_path, rate):
            # mw.resize(img_path,100,100)
            # img_path = 'F:/临时文件夹/ComfyUI_windows_portable/xww_lib/logo.png'
            # out_path = 'F:/临时文件夹/ComfyUI_windows_portable/xww_lib/logo11.jpg' # 必须是 jpeg 类型
            img = mw.compress_image(img_path, out_path, rate)
            # img.save('logo11.jpg', quality=95) # 使用quality=95保证图像大小经过存储后不变

        def get_size(filename):
            # Obtain the file size: KB
            size = os.path.getsize(filename)
            return size / 1024

        def compress_image(qobj, img_path, out_path, rate=2, step=5, quality=100, dpi=(300, 300)):
            # dpi和一般分辨率的区别如下：
            # dpi是dots per inch的缩写，表示每英寸有多少个点，通常用于描述打印机或扫描仪的输出分辨率，也就是打印或扫描的精度。
            # 一般分辨率是指显示器或图像的分辨率，表示水平和垂直方向上的像素点的数量，也就是显示或图像的清晰度。
            # dpi和一般分辨率的联系如下：
            # dpi和一般分辨率都是表示分辨率的一个单位，但是dpi是针对输出设备而言，而一般分辨率是针对显示设备或图像而言。
            # dpi和一般分辨率之间有一个换算关系，即尺寸（英寸）=像素/分辨率（dpi），例如一张图片宽为600像素，分辨率为300dpi，那么实际打印宽度为600/300=2英寸
            """不改变图片尺寸压缩图像大小
            :param img_path: 压缩图像读取地址
            :param out_path: 压缩图像存储地址
            :param mb: 压缩目标，KB
            :param step: 每次调整的压缩比率
            :param quality: 初始压缩比率
            :param dpi: 图片的分辨率，元组形式
            :return: 压缩文件地址，压缩文件大小
            """
            mb = 50
            o_size = mw.get_size(img_path)
            mb = o_size/rate
            if o_size < mb:
                return Image.open(img_path)
            img = Image.open(img_path)
            while o_size > mb:
                img = Image.open(img_path)
                img = img.convert('RGB')
                img.save(out_path, format='JPEG', quality=quality, dpi=dpi)
                if quality - step < 0:
                    break
                quality -= step
                o_size = mw.get_size(out_path)
            print('File size: ' + str(o_size))
            return img

        def resize_img_(self,qobj, path_list, w, h, join_list=None,img_data=None,img_t=None):
            base64_list = []
            image_data = []
            for i in range(len(path_list)):
                img_type = "JPEG"
                # 如果使用png，压缩不是很明显，而且非常慢，这里默认使用JPEG
                if img_t:
                    _,img_type = os.path.splitext(path_list[i])
                    img_type = img_type.replace(".","")
                    if img_type == "jpg" or img_type == "JPG":
                        img_type = "JPEG"
                        
                # 读取图片文件
                image = Image.open(path_list[i])
                # 压缩图片到指定大小，这里假设为100*100
                image = image.resize((w, h))
                image_data.append({"size": str(image.size), "kb": f"{len(image.tobytes())/1024/6} kb"})
                # 创建一个字节流对象
                byte_data = BytesIO()
                # 将图片数据存入字节流对象，格式为JPEG
                image.save(byte_data, format=img_type)
                # 获取字节流对象的二进制数据
                byte_data = byte_data.getvalue()
                # 将二进制数据转为base64字符串
                base64_str = base64.b64encode(byte_data).decode("ascii")
                # # 打印base64字符串
                base64_list.append(base64_str)
            if join_list:
                image_data = img_data + image_data
                base64_list = join_list + base64_list + image_data
            qobj.base64List.emit(base64_list)

        def get_models_file(path):
            file = [f for f in listdir("your_path") if f.endswith(
                ".png") and isfile(join("your_path", f))]

        def get_models_img(path):
            png = [f for f in listdir("your_path") if f.endswith(
                ".png") and isfile(join("your_path", f))]

        def get_models_data():
            url = os.path.join(cwd, "xww_lib", "dist", "index.html")
            png_files = [f for f in listdir("your_path") if f.endswith(
                ".png") and isfile(join("your_path", f))]

        def get_all_img(self, path):
            return glob.glob("{path}/*.png")

        def get_all_paths(self, dir_path):
            # 创建一个空列表，用来存储所有的路径
            all_paths = []
            # 遍历指定目录下的所有文件和目录
            for file_or_dir in os.listdir(dir_path):
                # 拼接完整的路径
                full_path = os.path.join(dir_path, file_or_dir)
                # 如果是目录，就递归调用自己，将子目录下的路径添加到列表中
                if os.path.isdir(full_path):
                    all_paths.extend(self.get_all_paths(full_path))
                # 如果是文件，就直接添加到列表中
                else:
                    all_paths.append(full_path)
            # 返回所有的路径
            return all_paths

        def get_dir_names(self,qobj, dir_path):
            # 创建一个空列表，用来存储所有的文件夹名
            dir_names = []
            yp = mc.getYmalPath()
            if yp and len(yp) > 0:
                dir_names = yp
            else:
                # 遍历指定目录下的所有文件和目录
                for file_or_dir in os.listdir(dir_path):
                    # 拼接完整的路径
                    full_path = os.path.join(dir_path, file_or_dir)
                    # 如果是目录，就将目录名添加到列表中
                    if os.path.isdir(full_path):
                        dir_names.append({"name": file_or_dir, "path": full_path})
            # print(json.dumps(dir_names))
            # 返回所有的文件夹名
            qobj.modelsData.emit(
                mw.set_models_img_path_data(dir_names))

        def set_data(self, dir_path):
            result_models = []
            result_img = []
            all_files = glob.glob(dir_path['path']+"\\*.*")
            if all_files and len(all_files) > 0:
                for file_path in all_files:
                    file_type = imghdr.what(file_path)  # 获取文件的类型
                    file_name, file_ext = os.path.splitext(
                        os.path.basename(file_path))  # 分割文件名和扩展名
                    if file_type is None:  # 如果文件类型是None，说明不是图片类型
                        result_models.append(
                            {"models_name": file_name, "models_type": file_ext, "models_path": file_path})  # 将文件路径添加到结果列表中
                    else:
                        result_img.append(
                            {"img_name": file_name, "img_type": file_ext, "img_path": file_path})

                for models_path in result_models:
                    for img_path in result_img:
                        if img_path["img_name"].replace('.preview', '') == models_path["models_name"]:
                            models_path.update(img_path)

            return mw.set_models_img_path_data(result_models)

        def set_models_img_path_data(self, list):
            for dir in list:
                result_models = []
                result_img = []
                all_files = glob.glob(dir['path']+"\\*.*")
                if all_files and len(all_files) > 0:
                    for file_path in all_files:
                        file_type = imghdr.what(file_path)  # 获取文件的类型
                        file_name, file_ext = os.path.splitext(
                            os.path.basename(file_path))  # 分割文件名和扩展名
                        if file_type is None and file_ext != '.zip':  # 如果文件类型是None，说明不是图片类型
                            result_models.append(
                                {"models_name": file_name, "models_type": file_ext, "models_path": file_path})  # 将文件路径添加到结果列表中
                        else:
                            result_img.append({"img_name": file_name.replace(
                                '.preview', ''), "img_type": file_ext, "img_path": file_path})

                    for models_path in result_models:
                        for img_path in result_img:
                            if img_path["img_name"] == models_path["models_name"]:
                                models_path.update(img_path)

                dir["models"] = result_models
            # print(json.dumps(list))
            return list

        def get_sub_dir_names(self, dir_path):
            # 创建一个空列表，用来存储所有的文件夹名
            sub_dir_names = []
            # 遍历指定目录下的所有文件和目录
            for file_or_dir in os.listdir(dir_path):
                # 拼接完整的路径
                full_path = os.path.join(dir_path, file_or_dir)
                # 如果是目录，就将目录名添加到列表中
                if os.path.isdir(full_path):
                    sub_dir_names.append({"name": file_or_dir, "path": full_path})
            # 返回所有的文件夹名
            return sub_dir_names

        # 定义一个函数，接受一个文件夹路径作为参数，返回一个列表，包含所有非图片的文件路径
        def get_non_image_files(folder):
            result = []  # 创建一个空列表，用来存储结果
            for root, dirs, files in os.walk(folder):  # 遍历文件夹里的所有文件
                for file in files:  # 对每个文件进行判断
                    file_path = os.path.join(root, file)  # 获取文件的完整路径
                    file_type = imghdr.what(file_path)  # 获取文件的类型
                    if file_type is None:  # 如果文件类型是None，说明不是图片类型
                        result.append(file_path)  # 将文件路径添加到结果列表中
            return result  # 返回结果列表

    # 在主程序中，创建一个Qt应用对象
    app = QApplication(sys.argv)
    # 创建一个mywindowj对象
    mw = MyWindow()
    mw.show()
    # 启动Qt应用对象的事件循环
    sys.exit(app.exec())
