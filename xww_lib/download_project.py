import requests
import time
import subprocess
import ch_en as ce
import os

def dowload(i,k):
    try:
        speed_up = ["https://github.com","https://huggingface.co"]
        path = ["/comfyanonymous/ComfyUI/releases/download/latest/ComfyUI_windows_portable_nvidia_cu118_or_cpu.7z","/comfyanonymous/ComfyUI/releases/download/latest/ComfyUI_windows_portable_nvidia_cu121_or_cpu.7z","/xww/xww_comfyui_resource/resolve/main/ComfyUI_windows_portable_nvidia_cu118_or_cpu.7z"]
        if i != 0:
            k = 2
        path_ = f"{speed_up[i]}{path[k]}"
        
        file_name = os.path.basename(path[k])
        print(f"file_name: {file_name}")
        if not os.path.exists(file_name):
            # 不存在压缩包，开始下载
            if ce.getCHEN() == "EN":
                print("\n is downloading the integration package of the original author, please wait...")
                print(f"\n You can go to this link to download the ComfyUI project:\n{path_}\n")
            else:
                print("\n正在下载整合包，请稍等。。。")
                print(f"\n如有需要可前往该链接自行下载，ComfyUI项目链接：\n{path_}\n")
            # 下载zip文件
            r = requests.get(path_, stream=True) # 使用stream参数，可以分块下载
            total_size = int(r.headers.get("content-length")) # 获取文件的总大小
            if ce.getCHEN() == "EN":
                print(f"File szie total_size: {total_size / 1024 / 1024:.4f}MB  {total_size / 1024 / 1024 / 1024:.4f}GB")
            else:
                print(f"文件大小 total_size: {total_size / 1024 / 1024:.4f}MB  {total_size / 1024 / 1024 / 1024:.4f}GB")

            r = requests.get(path_, stream=True)  # 使用stream参数，可以分块下载
            total_size = int(r.headers.get("content-length"))  # 获取文件的总大小
            start = time.time()  # 获取开始下载的时间
            chunk_size = 1024  # 每次读取的字节数
            downloaded_size = 0  # 已经下载的字节数
            # 下载
            with open(file_name, "wb") as f: # 以二进制写入模式打开文件
                print("Downloading %s" % file_name)
                for chunk in r.iter_content(chunk_size=chunk_size): # 使用iter_content方法，可以迭代地获取每一块内容
                    if chunk: # 如果块不为空
                        f.write(chunk) # 写入文件
                        downloaded_size += len(chunk) # 更新已下载的大小，注意不一定等于chunk_size
                        progress = downloaded_size / total_size * 100 # 计算下载进度百分比
                        bar = "█" * int(progress / 2) + " " * (50 - int(progress / 2)) # 绘制进度条，长度为50个字符
                        speed = downloaded_size // (time.time() - start) # 计算下载速度，单位是字节每秒
                        speed_KB = speed / 1024
                        speed_MB = speed / 1024 / 1024
                        # 1 kB = 1000 B，1 KB = 1024 B。1 Mb = 1000 kb，1 MB = 1024 kb。
                        # 1MB=1024KB=1024*1024B
                        # kb/s = B/s * 8 / 1000
                        # kb/s = M/s * 8000
                        # M/s = B/s/1048576
                        # 速度单位时 1KB/s=8Kb/s 1MB/s=8Mb/s 1GB/s=8Gb/s
                        if ce.getCHEN() == "EN":
                            print(f"[{bar}] {progress:.2f}%  {speed_KB:.4f}KB/s  {speed_MB:.4f}MB/s  anticipated:{(total_size-downloaded_size)/speed_MB/1024/1024/60 :.2f}minute  ", end="\r") # 显示进度条、百分比和速度
                        else:
                            print(f"[{bar}] {progress:.2f}%  {speed_KB:.4f}KB/s  {speed_MB:.4f}MB/s  预计:{(total_size-downloaded_size)/speed_MB/1024/1024/60 :.2f}分钟  ", end="\r") # 显示进度条、百分比和速度
            if ce.getCHEN() == "EN":
                print(f"\n\n Download time:{time.time() - start :.4f}s  {(time.time() - start)/60 :.2f}minute\n")
            else:
                print(f"\n\n下载耗时：{time.time() - start :.4f}s  {(time.time() - start)/60 :.2f}分钟\n")
        else:
            if ce.getCHEN() == "EN":
                print("Check found the integrated package has been downloaded, no need to download again, start to decompress...")
            else:
                print("检查发现已下载整合包，无需再次下载，开始解压。。。")
        start = time.time()
        # 解压
        if ce.getCHEN() == "EN":
            print(f"Unzipping {file_name}, the unzipping process may be slow, please be patient...")
        else:
            print(f"正在解压 {file_name} ,解压过程可能会比较慢，请耐心等待。。。")
        extract_folder = "ComfyUI_windows_portable2"
        # # 由于py7zr不支持bcj2算法，这里只能使用第三方软件来解压
        subprocess.run(['./xww_lib/.venv/7z/7-Zip/7z.exe','x', file_name, '-o./','-bsp1'])
        # 执行文件重命名操作
        os.rename(file_name.replace(".7z",""), extract_folder)
        if ce.getCHEN() == "EN":
            print(f"\n Decompression time:{time.time() - start}s\n")
            print("The ComfyUI project is unpacked, and now you can use the features in the launcher. Have fun...\n\n")
        else:
            print(f"\n解压耗时：{time.time() - start}s\n")
            print("ComfyUI项目解压完成，现在可以使用启动器里的功能了，祝你玩的愉快。。。\n\n")
        # for i in range(10, 0, -1):
        #     print("\\r {}秒后会自动关闭本窗口".format(i), end="", flush=True)
        #     time.sleep(1)
        # print("\\r倒计时结束！")
        # # 删除.7z文件
        # os.remove(file_name)
        # # 打印删除完成
        # print("删除完成")
        return "success"
    except Exception as e:
        # 打印错误信息
        print("error:", e)
        return "error"


    # 等待用户输入
    # input("\`n按回车键或点击右上角关闭按钮退出程序")

# dowload(1)