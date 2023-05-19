import yaml
import os
import requests
import time
import glob
import imghdr
import ch_en as ce

cwd = os.getcwd()
basePath = os.path.join(cwd, "ComfyUI_windows_portable","ComfyUI")
modelsyamlPath = os.path.join(basePath,"extra_model_paths.yaml")
modelsyamlPathBk = os.path.join(basePath,"extra_model_paths.yaml.bk")

def checkIsFirst():
    if not os.path.isfile(modelsyamlPath) and not os.path.isfile(modelsyamlPathBk):
        return True
    else:
        return False

def checkYmalFlag(qobj=None):
    flag = ""
    if os.path.isfile(modelsyamlPath):
        flag = "1"
    elif os.path.isfile(modelsyamlPathBk):
        flag = "0"
    else:
        flag = ""
    if qobj:
        qobj.useYmalFlag.emit(flag)
    return flag

def useYmal(qobj,mw,i):
    if checkIsFirst():
        if ce.getCHEN() == "EN":
            mw.alert_show("tips", "Please set mode 1 first, and then switch mode")
        else:
            mw.alert_show("温馨提示", "请先设置方式1，再进行方式切换")
        qobj.useYmalFlag.emit('')
        return
    text = ""
    if i == "1":
        if not os.path.isfile(modelsyamlPath):
            os.rename(modelsyamlPathBk, modelsyamlPath)
        if ce.getCHEN() == "EN":
            text = "The switch is successful, you have used the model of mode 1, you can go to the model option to see the effect, ComfyUI to take effect requires a restart"
        else:
            text = "切换成功，你已使用方式1的模型，可前往模型选项查看效果，ComfyUI生效需要重启"
    else:
        if not os.path.isfile(modelsyamlPathBk):
            os.rename(modelsyamlPath, modelsyamlPathBk)
        if ce.getCHEN() == "EN":
            text = "The switch is successful, you have used mode 2 or 3 model, can go to the model option to see the effect, ComfyUI to take effect needs to restart"
        else:
            text = "切换成功，你已使用方式2或3的模型，可前往模型选项查看效果，ComfyUI生效需要重启"
    qobj.useYmalFlag.emit(i)
    if ce.getCHEN() == "EN":
        mw.alert_show("tips", text)
    else:
        mw.alert_show("温馨提示", text)

def createYaml(self,path):
    data = {
        "a111": {
            "base_path": path,
            "checkpoints": "models/Stable-diffusion",
            "configs": "models/Stable-diffusion",
            "vae": "models/VAE",
            "loras": "models/Lora",
            "upscale_models": "models/ESRGAN\nmodels/SwinIR\n",
            "embeddings": "embeddings",
            "hypernetworks": "models/hypernetworks",
            "controlnet": "models/ControlNet"
        }
    }

    with open(modelsyamlPath, "w") as file:
        yaml.dump(data, file)
    self.changeModesPath.emit('1')

def getYmalPath():
    if os.path.isfile(modelsyamlPath):
        with open(modelsyamlPath) as file:
            data = yaml.safe_load(file) # 把YAML文件加载成字典
            base_path = data["a111"]["base_path"]
            if base_path [-1] == "\\": # 检查最后一个字符是否是"\\"
                base_path = base_path [:-1] # 取出除了最后一个字符之外的所有字符
            if base_path [-1] == "/": # 检查最后一个字符是否是"/"
                base_path = base_path [:-1] # 取出除了最后一个字符之外的所有字符
            if base_path [-1] == "\\/": # 检查最后一个字符是否是"\\/"
                base_path = base_path [:-1] # 取出除了最后一个字符之外的所有字符
            if base_path [-1] == "//": # 检查最后一个字符是否是"//"
                base_path = base_path [:-1] # 取出除了最后一个字符之外的所有字符
            return [
                {"name": "checkpoints", "path": os.path.join(base_path,data["a111"]["checkpoints"]).replace("/","\\")},
                {"name": "configs", "path":os.path.join(base_path,data["a111"]["configs"]).replace("/","\\")},
                {"name": "vae", "path": os.path.join(base_path,data["a111"]["vae"]).replace("/","\\")},
                {"name": "loras", "path": os.path.join(base_path,data["a111"]["loras"]).replace("/","\\")},
                {"name": "upscale_models", "path": os.path.join(base_path,"models/ESRGAN").replace("/","\\")},
                {"name": "upscale_models2", "path": os.path.join(base_path,"models/SwinIR").replace("/","\\")},
                {"name": "embeddings", "path": os.path.join(base_path,data["a111"]["embeddings"]).replace("/","\\")},
                {"name": "hypernetworks", "path": os.path.join(base_path,data["a111"]["hypernetworks"]).replace("/","\\")},
                {"name": "controlnet", "path": os.path.join(base_path,data["a111"]["controlnet"]).replace("/","\\")}]
    else:
        return []

def changeYaml(self,path):
    ymalPath = ""
    if os.path.isfile(modelsyamlPath):
        ymalPath = modelsyamlPath
    elif os.path.isfile(modelsyamlPathBk):
        ymalPath = modelsyamlPathBk
        
    with open(ymalPath) as file:
        data = yaml.safe_load(file) # 把YAML文件加载成字典
        data["a111"]["base_path"] = path # 修改字典中的值
        print(data)

    with open(ymalPath, "w") as file:
        yaml.dump(data, file) # 把字典写回YAML文件
    
    self.changeModesPath.emit('1')


def setModesPath(self,path):
    if (checkIsFirst()):
        createYaml(self,path)
    else:
        changeYaml(self,path)

def downloadModel(args):
    try:
        url,typ,path,emitValue,self_ = args.get("url"),args.get("typ"),args.get("path"),args.get("emitValue"),args.get("self_")
        if emitValue and self_:
            self_.downloadModelFlag.emit(f"{emitValue}#-#start")
        file_name = os.path.basename(url)
        downloadSavePath = ''
        if path:
            downloadSavePath = path
        else:
            if checkYmalFlag() == "1":
                yamlPath = getYmalPath()
                for k in yamlPath:
                    if typ == k["name"]:
                        downloadSavePath = os.path.join(k["path"],file_name)
            else:
                downloadSavePath = os.path.join(basePath,"models",typ,file_name)
        if not downloadSavePath:
            if ce.getCHEN() == "EN":
                print("The saved address path is incorrect. Please check if the path exists")
            else:
                print("保存地址路径有误，请检查路径是否存在")
            if emitValue and self_:
                self_.downloadModelFlag.emit(f"{emitValue}#-#error")
            return "error"
        if ce.getCHEN() == "EN":
            print(f"\nPlease wait while verifying that the {downloadSavePath} link is correct...")
        else:
            print(f"\n正在校验链接{downloadSavePath}是否正确，请稍等。。。")
        r = requests.get(url, stream=True) # 使用stream参数，可以分块下载
        total_size = int(r.headers.get("content-length")) # 获取文件的总大小
        if ce.getCHEN() == "EN":
            print(f"Verification success, file size total_size: {total_size / 1024 / 1024:.4f}MB  {total_size / 1024 / 1024 / 1024:.4f}GB")
        else:
            print(f"校验成功，文件大小 total_size: {total_size / 1024 / 1024:.4f}MB  {total_size / 1024 / 1024 / 1024:.4f}GB")
        start = time.time()  # 获取开始下载的时间
        chunk_size = 1024  # 每次读取的字节数
        downloaded_size = 0  # 已经下载的字节数
        # 下载
        with open(downloadSavePath, "wb") as f: # 以二进制写入模式打开文件
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
            print("Download completed, you can go to the corresponding model options to see the details...")
        else:
            print(f"\n\n下载耗时：{time.time() - start :.4f}s  {(time.time() - start)/60 :.2f}分钟\n")
            print("下载完成，你可到对应模型选项查看详情。。。")
        if emitValue and self_:
            self_.downloadModelFlag.emit(f"{emitValue}#-#success")
        return "success"
    except Exception as e:
        # 打印错误信息
        print("error：", e)
        if emitValue and self_:
            self_.downloadModelFlag.emit(f"{emitValue}#-#error")
        return "error"

# url = "https://huggingface.co/yehiaserag/anime-pencil-diffusion/resolve/b52ffef86adeaa55ecb75017ec6be9adcb1bff59/anime-pencil-diffusion-v1.ckpt" 
# downloadModel(url,"loras")

# aa = [{'name': 'checkpoints', 'path': 'F:\\miaoshouai-sd-webui-v230315full\\models\\Stable-diffusion'}, {'name': 'configs', 'path': 'F:\\miaoshouai-sd-webui-v230315full\\models\\Stable-diffusion'}, {'name': 'vae', 'path': 'F:\\miaoshouai-sd-webui-v230315full\\models\\VAE'}, {'name': 'loras', 'path': 'F:\\miaoshouai-sd-webui-v230315full\\models\\Lora'}, {'name': 'upscale_models', 'path': 'F:\\miaoshouai-sd-webui-v230315full\\models\\ESRGAN'}, {'name': 'upscale_models2', 'path': 'F:\\miaoshouai-sd-webui-v230315full\\models\\SwinIR'}, {'name': 'embeddings', 'path': 'F:\\miaoshouai-sd-webui-v230315full\\embeddings'}, {'name': 'hypernetworks', 'path': 'F:\\miaoshouai-sd-webui-v230315full\\models\\hypernetworks'}, {'name': 'controlnet', 'path': 'F:\\miaoshouai-sd-webui-v230315full\\models\\ControlNet'}]
# for k in aa:
#     print(k["name"])

def get_all_models(typ=None):
    # 创建一个空列表，用来存储所有的文件夹名
    dir_names = []
    models_str_list = []
    dir_path = os.path.join(cwd, "ComfyUI_windows_portable", "ComfyUI", "models")
    yp = getYmalPath()
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
    
    for dir in dir_names:
        result_models = []
        all_files = glob.glob(dir['path']+"\\*.*")
        if all_files and len(all_files) > 0:
            for file_path in all_files:
                file_type = imghdr.what(file_path)  # 获取文件的类型
                basename = os.path.basename(file_path)
                file_name, file_ext = os.path.splitext(basename)  # 分割文件名和扩展名
                if file_type is None and file_ext != '.zip':  # 如果文件类型是None，说明不是图片类型
                    result_models.append(
                        {"models_name": basename, "models_path": file_path})  # 将文件路径添加到结果列表中
                    if typ:
                        models_str_list.append(f"{dir['name']}-{basename}")

        dir["models"] = result_models
    
    if typ:
        return models_str_list
    else:
        return dir_names

# print(get_all_models(True))