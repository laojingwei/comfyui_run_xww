import os

cwd = os.getcwd()

global isUpdateCE
isUpdateCE = True
global CEFLAG
CEFLAG = "EN"

# 保存中英切换标志
def change_CHEN(str):
    try:
        path = os.path.join(cwd, "xww_lib", "savedata", "ChineseEnglish.txt")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str)
            global CEFLAG
            CEFLAG = str
            return str
    except Exception as e:
        print(e)
        return "error"

# 获取中英切换标志
def getCHEN():
    global isUpdateCE
    if not isUpdateCE:
        global CEFLAG
        return CEFLAG
    path = os.path.join(cwd, "xww_lib", "savedata", "ChineseEnglish.txt")
    try:
        # 打开文件
        f = open(path, "r")
        # 读取文件的全部内容
        content = f.read()
        # 关闭文件
        f.close()
        return content
    except Exception as e:
        # print(e)
        return "CH"