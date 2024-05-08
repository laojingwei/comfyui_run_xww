# import json
import yaml

# jsonPath = ''
# # 以二进制模式打开文件
# with open(jsonPath, 'rb') as json_file:
#     # 使用utf-8编码读取json数据
#     json_data = json_file.read().decode('utf-8')

# # 将数据转换为JSON
# parsed_json = json.loads(json_data)
# custom_nodes = parsed_json.get('custom_nodes', [])
# node_list = []
# for node in custom_nodes:
#     gitUrl = ''
#     civitaiUrl = ''
#     if "https://civitai.com" in node.get('reference'):
#         civitaiUrl = node.get('reference')
#     if "https://github.com" in node.get('reference'):
#         gitUrl = node.get('reference')

#     node_list.append({
#         "author":node.get('author'),
#         "name":node.get('title'),
#         "gitUrl":gitUrl,
#         "civitaiUrl":civitaiUrl,
#         "description":node.get('description'),
#     })

# # # 将 JSON 数据转换为 YAML
# yaml_data = yaml.dump(node_list)

# # 将转换后的 YAML 数据写入文件
# with open('cutome-node-list.yaml', 'w', encoding='utf-8') as yaml_file:
#     yaml_file.write(yaml_data)

import sys
print(sys.path)

from PyDeepLx import PyDeepLx

# 创建 PyDeepLx 实例
deepL = PyDeepLx()

# 使用 translate 方法来进行翻译
result = deepL.translate("Hello", "en", "zh")
print(result)


# def translate_text(text):
#     # 创建翻译器对象
#     translator = Translator()

#     # 要翻译的英文文本
#     english_text = text

#     # 将英文翻译成中文
#     translated = translator.translate(english_text, dest='zh-cn')
#     return translated.text


# with open('D:/comfyui-xwwrun/comfyui_run_xww/xww_lib/savedata/cutomNodeData.yaml', "r", encoding='utf-8') as stream:
#     data = yaml.safe_load(stream)
#     # 修改字段值
#     i = 0
#     for item in data:
#         text = item.get('description')
#         i += 1
#         if i == 1:
#             if text:
#                 text = translate_text(text)
#             print(text,'\n')