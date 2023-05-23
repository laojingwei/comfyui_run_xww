# 导入git模块
# import git
import os
import yaml
import models_config as mc
import random
import ch_en as ce
from datetime import datetime
import subprocess
import shutil
# import sys



cwd = os.getcwd()
global isUpdate
isUpdate = False

git_path = os.path.join(cwd, "xww_lib", ".venv", "Git","cmd")
git_exe = 'git'

loadingList = ['-','/','\\']

comfyuiPath = os.path.join(cwd, "ComfyUI_windows_portable", "ComfyUI")
nodePath = os.path.join(cwd, "ComfyUI_windows_portable", "ComfyUI", "custom_nodes")
webPath = os.path.join(cwd, "ComfyUI_windows_portable", "web", "extensions")
speed_up = ["https://github.com","https://kgithub.com","https://hub.njuu.cf"]
savedataPath = os.path.join(cwd, "xww_lib", "savedata")

def is_program_installed(program_name):
    """Check whether program_name is installed."""
    return shutil.which(program_name)

gitE = is_program_installed("git.exe")
if not gitE:
    # print(git_path)
    # 使用insert没法正常导入git，修改为创建系统环境变量映像来导入git
    # sys.path.insert(1, git_path)
    os.environ["PATH"] += os.pathsep + git_path # 在PATH变量后面追加git_path
    git_exe = os.path.join(git_path, "git.exe")
import git

# 克隆仓库
def clone_from(path, i):
    try:
        # 使用加速方式
        su = speed_up[i]
        path = path.replace("https://github.com",su)
        # 获取地址的文件名
        filename = os.path.splitext(os.path.basename(path))[0]
        node_path = os.path.join(nodePath,filename)
        if os.path.isdir(node_path):
            if ce.getCHEN() == "EN":
                print(f"\n\nThe node name already exists. Please confirm whether you want to install this node. If yes, please go to {node_path} and manually delete the node folder before installing\n\n")
            else:
                print(f"\n\n该节点名已存在，请确定你是否要安装此节点，如果是请前往{node_path}手动删除该节点文件夹再进行安装\n\n")
            return "warn"
        if ce.getCHEN() == "EN":
            print(f"\nDownloading {filename}...\n")
        else:
            print(f"\n正在下载{filename}...\n")
        # 克隆代码到本地
        # os.environ['PYTHONIOENCODING'] = 'utf-8'
        # git.Repo.clone_from(path, node_path)
        p = subprocess.Popen([git_exe, "clone", path, node_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        print(stdout.decode("utf-8"))
        print(stderr.decode("utf-8"))
        global isUpdate
        isUpdate = True
        if ce.getCHEN() == "EN":
            print(f"\n\nIf the user-defined node is installed successfully, go to {node_path} to check. Pay attention!! Since the author of some custom nodes packages the contents in a disorderly manner, including many.py nodes and.js nodes, if the node is.js nodes, please manually put the node containing.js into {webPath}, and restart ComfyUI to take effect after handling the problem.\n\n")
        else:
            print(f"\n\n自定义节点安装成功，可前往{node_path}查看；注意！！！由于某些自定义节点的作者打包的内容比较乱，里面包含了很多.py的节点和.js的节点，如果是.js的节点请自行手动把包含.js的节点放到{webPath}里面，处理好后需重启ComfyUI生效。。。\n\n")
        return "success"
    except Exception as e:
        print(e)
        return 'error'

# clone_from('https://github.com/laojingwei/comfy_translation_node.git',2)
# get the full path of git1.exe
# git_path = os.path.join(os.getcwd(), "xww_lib", ".venv", "git1.exe")
# # check if the file exists
# if os.path.isfile(git_path):
#     print("The file exists.")
# else:
#     print("The file does not exist.")
# # check if the file is executable
# if os.access(git_path, os.X_OK):
#     print("The file is executable.")
# else:
#     print("The file is not executable.")

# 获取节点信息
def get_node_data():
    node_rep = []
    global isUpdate
    # 获取目录信息
    for rep in os.listdir(nodePath):
        # 拼接完整的路径
        full_path = os.path.join(nodePath, rep)
        _git = os.path.join(full_path,".git")
        if os.path.isdir(_git):
            try:
                git.Repo(_git)
                # print(f"{_git}--This is a valid git repository")
                git_detail = get_git_data(full_path,rep,isUpdate)
                node_rep.append({"name": rep, "path": full_path, "git_detail": git_detail})
            except git.InvalidGitRepositoryError:
                print(f"{_git}--这不是一个有效的git存储库，可能git还在运行中，请稍等再重试(This is not a valid git repository and git may still be running. Please wait and try again)")
        elif os.path.isdir(full_path):
            # 判断该节点是否启用
            fileStat = file_stat(full_path, False)
            filename = os.path.splitext(os.path.basename(full_path))[0]
            git_detail = {"name": filename, "localHexsha": "", "localTime": "", "newHexsha": "", "newTime": "", "prevHexsha": "", "isNew": "", "fileStat": fileStat, "gitUrl": "", "noGit": "Y"}
            node_rep.append({"name": rep, "path": full_path, "git_detail": git_detail})
    
    if isUpdate:
        isUpdate = False
    return node_rep

# 获取git信息
def get_git_data(rep_path,rep,isUpdate):
    # 打开本地仓库
    repo = git.Repo(rep_path)
    # 获取当前分支名称
    name = repo.head.name
    # print(repo.git.fetch('--all'))
    # 当前哈希值
    localHexsha = repo.head.object.hexsha
    localTime = setTime(repo.head.object.authored_date)
    # 前一个版本
    commits = repo.iter_commits()
    # 当前版本
    next(commits)
    # 再执行一遍就是上一版本
    try: 
        prevHexsha = next(commits).hexsha
    except Exception as e:
        print(e)
        prevHexsha = ""

    # 最新哈希值
    new = next(repo.iter_commits(all=True))
    newHexsha = new.hexsha
    newTime = setTime(new.authored_date)

    # 判断该节点是否启用
    fileStat = file_stat(rep_path, False)

    gitUrl = None
    remotes = repo.remotes
    for remote in remotes:
        gitUrl = remote.url
        if gitUrl.endswith(".git"):
            gitUrl = gitUrl[:-4]
        gitUrl = gitUrl.replace(speed_up[1],speed_up[0]).replace(speed_up[2],speed_up[0])

    nh, t = None, None
    if isUpdate:
        nh, t = getNewHexsha(repo,rep,'0')
    isNew = '0'
    if nh and t:
        newHexsha = nh
        newTime = t
        isNew = '1'
    return {"name": name, "localHexsha": localHexsha, "localTime": localTime, "newHexsha": newHexsha, "newTime": newTime, "prevHexsha": prevHexsha, "isNew": isNew, "fileStat": fileStat, "gitUrl": gitUrl+"/commit/", "sourcePath": gitUrl}
    # git_detail = []
    # # 获取所有分支的提交信息
    # for commit in repo.iter_commits(all=True):
    #     git_detail.append({"name_rev":commit.name_rev.split()[1], "hexsha": commit.hexsha, "author": str(commit.author), "authored_datetime": commit.authored_datetime.isoformat(), "message": commit.message.replace('\n',"")})
    # return git_detail

def setTime(t):
    return datetime.fromtimestamp(t).isoformat().replace("T", " ")

# 切换到指定提交版本
def git_checkout(rep_path,hexsha,name=None):
    try:
        # 打开本地仓库
        repo = git.Repo(rep_path)
        repo.git.checkout(hexsha)
        if ce.getCHEN() == "EN":
            print(f"\nSwitched to branch:{hexsha}\n")
        else:
            print(f"\n已切换到分支：{hexsha}\n")
        if name:
            global isUpdate
            data = get_git_data(rep_path,name,isUpdate)
            return [data]
        else:
            return ['success']
    except Exception as e:
        print(e)
        return ['error']
    
# 切换到指定提交版本
def git_checkout_cy(rep_path,hexsha):
    try:
        # 打开本地仓库
        repo = git.Repo(rep_path)
        repo.git.checkout(hexsha)
        path = os.path.join(cwd, "xww_lib", "savedata", "comfyui-git.yaml")
        try:
            # 加载YAML文件
            with open(path, "r", encoding='utf-8') as stream:
                data = yaml.safe_load(stream)
                # 修改字段值
                for item in data:
                    # 如果不等于hexsha并且isLocal为1，需要重置为0
                    if item["hexsha"] != hexsha and item["isLocal"] == 1:
                        # 把isLocal改为0
                        item["isLocal"] = 0
                    if item["hexsha"] == hexsha:
                        # 把isLocal改为1
                        item["isLocal"] = 1
                # 写回YAML文件
                with open(path, "w", encoding='utf-8') as stream:
                    yaml.dump(data, stream)
        except Exception as e:
            if ce.getCHEN() == "EN":
                print("Cache update failure")
            else:
                print('更新缓存失败')
        if ce.getCHEN() == "EN":
            print(f"\nSwitched to branch:{hexsha}\n")
        else:
            print(f"\n已切换到分支：{hexsha}\n")
        return 'success'
    except Exception as e:
        print(e)
        return 'error'

# 获取最新内容
def refresh_data(rep_path,name):
    global isUpdate
    isUpdate = True
    data = get_git_data(rep_path,name,isUpdate)
    if isUpdate:
        isUpdate = False
    return [data]
# git_checkout("f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node","17bfe44d48a4dd194f764aa752745cd0311f13a4")

# print(get_node_data())

# fileStat
def file_stat(path,i):
    try:
        path = os.path.join(path,"__init__.py")
        if i == 'ban' and os.path.isfile(path):
            os.rename(path, path+'.bk')
            with open(path, 'w', encoding='utf-8') as f:
                f.write('pass')
            return "0"
        elif i == 'use' and os.path.isfile(path+'.bk'):
            if os.path.isfile(path):
                os.remove(path)
            os.rename(path+'.bk', path)
            return "1"
        else:
            if os.path.isfile(path+'.bk'):
                return "0"
            else:
                return "1"
    except Exception as e:
        print(e)
        return 'error'
    
def git_comfyui_code(type):
    try:
        # 打开本地仓库
        repo = git.Repo(comfyuiPath)
        # 当前哈希值
        localHexsha = repo.head.object.hexsha
        # # 最新哈希值
        # new = next(repo.iter_commits(all=True))
        # print(new)
        git_detail = []
        refList = None
        gitUrl = None
        remotes = repo.remotes
        for remote in remotes:
            gitUrl = remote.url
            if gitUrl.endswith(".git"):
                gitUrl = gitUrl[:-4]
        # 获取缓存
        if type != "refresh":
            refList = get_save_data("comfyui-git.yaml","yaml")
        if not refList:
            if ce.getCHEN() == "EN":
                print("Obtaining remote data may be slow, please wait...")
            else:
                print("正在获取远程数据，可能会比较慢，请稍等。。。")
            refList = getNewHexsha(repo,"ComfyUI",'1')
            # refList.extend(git_detail)
            
            # 获取本地所有分支的提交信息
            for commit in repo.iter_commits(all=True):
                if ce.getCHEN() == "EN":
                    print(f"In the process of acquiring---{random.choice(loadingList)}", end="\r")
                else:
                    print(f"正在获取中---{random.choice(loadingList)}", end="\r")
                isLocal = 0
                if localHexsha == commit.hexsha:
                    isLocal  = 1
                git_detail.append({"name":commit.name_rev.split()[1], "hexsha": commit.hexsha, "author": str(commit.author), "authored_datetime": commit.authored_datetime.isoformat().replace("T", " "), "message": commit.message.replace('\n',""), "isLocal": isLocal, "path": comfyuiPath, "gitUrl": gitUrl.replace(speed_up[1],speed_up[0]).replace(speed_up[2],speed_up[0])+"/commit/"+commit.hexsha})
            if ce.getCHEN() == "EN":
                print("Updated to the latest code submission record")
            else:
                print("已更新到最新代码提交记录")
            save_data(git_detail,"comfyui-git.yaml","yaml")
            refList = git_detail
        return refList
    except Exception as e:
        print(e)
        return []

# 获取最新哈希值，如果普通获取报错自动使用加速方式获取
def getNewHexsha(repo,rep,t):
    try: 
        repo_url = ""
        remotes = repo.remotes
        for remote in remotes:
            repo_url = remote.url.replace(speed_up[0],"").replace(speed_up[1],"").replace(speed_up[2],"")
            if remote.name == "speedUP1":
                suremote = repo.remote("speedUP1")
                repo.delete_remote(suremote)
            if remote.name == "speedUP2":
                suremote = repo.remote("speedUP2")
                repo.delete_remote(suremote)
        repo.create_remote("speedUP1", speed_up[1]+repo_url)
        repo.create_remote("speedUP2", speed_up[1]+repo_url)
        remotes = repo.remotes
        # print(remotes)
        # remotes.sort(key=lambda remote: remote.name) # 按升序排序
        # print(remotes)
        remotes.sort(key=lambda remote: remote.name, reverse=True) # 按降序排序
        # print(remotes)
        # 遍历远程仓库对象
        for remote in remotes:
            try: 
                if ce.getCHEN() == "EN":
                    print(f"\nGet the latest information about the {rep} code... {remote}")
                else:
                    print(f"\n获取{rep}代码最新信息。。。{remote}")
                remote = repo.remote(remote.name)
                remote.fetch()
                refList = []
                for ref in remote.refs:
                    if ce.getCHEN() == "EN":
                        print(f"\nThe latest remote repository changes for {rep} have been successfully obtained as follows: ------- :")
                    else:
                        print(f"已成功获取{rep}最新远程仓库变更，详情如下-------：")
                    print(ref.name, ref.commit.hexsha, ref.commit.authored_datetime, ref.commit.message,'\n')
                    remoteurl = remote.url
                    if remoteurl.endswith(".git"):
                        remoteurl = remoteurl[:-4]
                    gitUrl = remoteurl.replace(speed_up[1],speed_up[0]).replace(speed_up[2],speed_up[0])+"/commit/"+ref.commit.hexsha
                    if t == "0":
                        return ref.commit.hexsha, ref.commit.authored_datetime.isoformat()
                    refList.append({"name": ref.name, "hexsha": ref.commit.hexsha, "authored_datetime": ref.commit.authored_datetime.isoformat().replace("T", " "), "message": ref.commit.message.replace('\n',""), "isLocal": 0, "path": comfyuiPath, "gitUrl": gitUrl})
                return refList
            except Exception as e:
                print(e)
                if ce.getCHEN() == "EN":
                    print(f"\nObtaining the latest information of {rep} node is enabled...")
                else:
                    print(f"\n普通方式获取失败，正在启用加速获取{rep}节点最新信息。。。\n")
        if t == "0":
            return None, None
        return []
    except Exception as e:
        print(e)
        if ce.getCHEN() == "EN":
            print("Failed to get the latest remote changes, please try again...")
        else:
            print("获取远程最新变更失败，请重试。。。")
        if t == "0":
            return None, None
        return []
    
 # 获取save数据
def get_save_data(fileName,type):
    path = os.path.join(cwd, "xww_lib", "savedata", fileName)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            if type == "yaml":
                data = yaml.safe_load(f)
            else:
                data = f.read()
            return data
    except Exception as e:
        print(e)
        if ce.getCHEN() == "EN":
            print("No cached data was found")
        else:
            print('未发现缓存数据')
        return None

# 保存数据
def save_data(data, fileName, type):
    path = os.path.join(savedataPath, fileName)
    
    # ‘w’：写入模式，如果文件不存在，会创建一个新文件；如果文件存在，会覆盖原有内容。
    # ‘a’：追加模式，如果文件不存在，会创建一个新文件；如果文件存在，会在末尾追加内容。
    # ‘x’：独占模式，如果文件不存在，会创建一个新文件；如果文件存在，会抛出异常。
    if type == "json":
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data)
    elif type == "txt":
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data)
    elif type == "yaml":
        with open(path, "w", encoding='utf-8') as file:
            yaml.dump(data, file)
    else:
        if ce.getCHEN() == "EN":
            print("This file type is not supported for saving")
        else:
            print("暂不支持该文件类型保存")


def check_installed_models():
    modelData = get_save_data("model.yaml","yaml")
    allModels = mc.get_all_models(True)
    keyList = []
    for k in modelData[0].keys():
       if k:
        keyList.append(k)
    
    for item in keyList:
        if modelData[0][item] and len(modelData[0][item])>0:
            for item_sub in modelData[0][item]:
                if f"{item}-{item_sub['name']}" in allModels:
                    item_sub["installed"] = "1"
                else:
                    item_sub["installed"] = "0"
    return modelData

def check_installed_nodes():
    cnData = get_save_data("cutomNodeData.yaml","yaml")
    nodeData = get_node_data()
    keyList = []
    for item in cnData:
        a = False
        for item_sub in nodeData:
            if item["name"] == item_sub["name"]:
                item["installed"] = "1"
                a = True
                break
        if not a:   
            item["installed"] = "0"
    return cnData

# 检查启动器版本
def check_xww_v():
    try:
        # print(cwd)
        # 打开本地仓库
        repo = git.Repo(cwd)
        # print(repo)
        global isUpdate
        isUpdate = True
        data = get_git_data(cwd,'comfyui_run_xww',isUpdate)
        return [data]
    except Exception as e:
        print(e)
        return ['error']
    
# print(check_xww_v())
# print(check_installed_nodes())
# print(check_installed_models())
# print(git_comfyui_code('refresh'))
# print(get_node_data())

# 整理数据
# import requests 
# url = "https://huggingface.co/yehiaserag/anime-pencil-diffusion/resolve/b52ffef86adeaa55ecb75017ec6be9adcb1bff59/anime-pencil-diffusion-v1.ckpt" 
# r = requests.get(url, stream=True) # 使用stream参数，可以分块下载
# total_size = int(r.headers.get("content-length")) # 获取文件的总大小
# print(f"文件大小 total_size: {total_size / 1024 / 1024:.4f}MB  {total_size / 1024 / 1024 / 1024:.4f}GB")
# print (r.headers)

# modelData = get_save_data("model.yaml","yaml")
# modelDataNew = {"checkpoints":[],"configs":[],"controlnet":[],"embeddings":[],"hypernetworks":[],"loras":[],"upscale_models":[]}
# for k in modelDataNew.keys():
#     for item in modelData:
#         if k == item["type"]:
#             modelDataNew[k].append(item)
# print ([modelDataNew])
# save_data([modelDataNew], "model1.yaml","yaml")

# print(get_save_data("model1.yaml","yaml"))

# # 修改字段值
# for item in modelData:
#     filename = os.path.basename(item["url"])
#     url_sub_l = item["url"].replace("https://huggingface.co/","").replace("swl-models/","").split("/")
#     if url_sub_l:
#         if not item["author"] or item["author"] == '':
#             item["author"] = url_sub_l[0].split("-")[0].split("_")[0]
#         if not item["name"] or item["name"] == '':
#             item["name"] = filename
# print (modelData)
# save_data(modelData, "model.yaml","yaml")

# import requests 
# modelData = get_save_data("model.yaml","yaml")
# l = len(modelData)
# print(l)
# a = 0
# # 修改字段值
# for item in modelData:
#     try:
#         a = a + 1
#         print(f'{a/l*100:.2f}%', item["url"])
#         r = requests.get(item["url"], stream=True) # 使用stream参数，可以分块下载
#         lastModified = r.headers.get("Last-Modified")
#         total_size = int(r.headers.get("content-length")) # 获取文件的总大小
#         M = total_size / 1024 / 1024
#         G = total_size / 1024 / 1024 / 1024
#         size = ""
#         if M < 1000:
#             size = f'{M:.4f} MB'
#         else:
#             size = f'{G:.4f} GB'
#         print(f"文件大小 total_size: {M}MB  {G}GB  {size} {lastModified}")
#         item["size"] = size
#         item["lastModified"] = lastModified
#     except Exception as e:
#         print(e)
# print (modelData)
# save_data(modelData, "model.yaml","yaml")


# import requests 
# modelData = get_save_data("model1.yaml","yaml")
# print(modelData)
# def getUrlData(l):
#     for item in l:
#         r = requests.get(item["url"], stream=True) # 使用stream参数，可以分块下载
#         lastModified = r.headers.get("Last-Modified")
#         total_size = int(r.headers.get("content-length")) # 获取文件的总大小
#         M = total_size / 1024 / 1024
#         G = total_size / 1024 / 1024 / 1024
#         size = ""
#         if M < 1000:
#             size = f'{M:.4f} MB'
#         else:
#             size = f'{G:.4f} GB'
#         item["size"] = size
#         item["lastModified"] = lastModified
# getUrlData(modelData['vae'])
# save_data(modelData, "model2.yaml","yaml")