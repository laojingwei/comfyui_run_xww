# 备注：这个功能使用了receyuki大佬在sd-webui写的一个脚本文件image_data_reader.py，本人只是针对ComfyUI的图片处理做了些修改，有兴趣可以前往他的个人github查看，如使用到他的插件或代码可以的话给他一个小星星
# https://github.com/receyuki/stable-diffusion-prompt-reader/blob/master/sd_prompt_reader/image_data_reader.py
# -*- encoding:utf-8 -*-
# __author__ = 'receyuki'
# __filename__ = 'image_data_reader.py'
# __copyright__ = 'Copyright 2023'
# __email__ = 'receyuki@gmail.com'

import json
import base64
import piexif
import piexif.helper
from PIL import Image

import select_local_file as slf

# comfyui node types
KSAMPLER_TYPES = ["KSampler", "KSamplerAdvanced"]
VAE_ENCODE_TYPE = ["VAEEncode", "VAEEncodeForInpaint"]
CHECKPOINT_LOADER_TYPE = ["CheckpointLoader", "CheckpointLoaderSimple"]

# import os

# cwd = os.getcwd()

class ImageDataReader:
    def __init__(self, file):
        self._height = None
        self._width = None
        self._info = {}
        self._positive = ""
        self._negative = ""
        self._setting = ""
        self._raw = ""
        self._tool = ""
        self._upscale_model = ""
        self.read_data(file)

    def read_data(self, file):
        with Image.open(file) as f:
            self._width = f.width
            self._height = f.height
            self._info = f.info
            # a1111 png format
            if "parameters" in self._info and f.format == "PNG":
                self._tool = "A1111-sd-webUI"
                self._sd_png()
            # a1111 jpeg and webp format
            elif "exif" in self._info and (f.format == "JPEG" or f.format == "WEBP"):
                self._tool = "A1111-sd-webUI"
                self._sd_jpg()
            # novelai format
            elif self._info.get("Software") == "NovelAI" and f.format == "PNG":
                self._tool = "NovelAI"
                self._nai_png()
            # comfyui format
            elif self._info.get("prompt") and f.format == "PNG":
                self._tool = "ComfyUI"
                self._comfy_png()

    def _sd_png(self):
        self._raw = self._info.get("parameters")
        self._sd_format()

    def _sd_jpg(self):
        exif = piexif.load(self._info.get("exif")) or {}
        try:
            self._raw = piexif.helper.UserComment.load(exif.get("Exif").get(piexif.ExifIFD.UserComment))
        except Exception:
            pass
        else:
            self._sd_format()

    def _sd_format(self):
        if self._raw and "\nSteps:" in self._raw:
            if "Negative prompt:" in self._raw:
                prompt_index = [self._raw.index("\nNegative prompt:"),
                                self._raw.index("\nSteps:")]
            else:
                prompt_index = [self._raw.index("\nSteps:"),
                                self._raw.index("\nSteps:")]
            self._positive = self._raw[:prompt_index[0]]
            self._negative = self._raw[prompt_index[0] + 1 + len("Negative prompt: "):prompt_index[1]]
            self._setting = self._raw[prompt_index[1] + 1:]
        else:
            self._raw = ""

    def _nai_png(self):
        self._positive = self._info.get("Description")
        self._raw += self._positive
        comment = self._info.get("Comment") or {}
        comment_json = json.loads(comment)
        self._negative = comment_json.get("uc")
        self._raw += "\n" + self.negative
        self._raw += "\n" + comment
        self._setting = (
            f"Steps: {comment_json.get('steps')}"
            f", Sampler: {comment_json.get('sampler')}"
            f", CFG scale: {comment_json.get('scale')}"
            f", Seed: {comment_json.get('seed')}"
            f", Size: {self._width}x{self._height}"
            f", Denoising strength: {comment_json.get('Denoise')}"
            f", Hires upscale: {comment_json.get('Upscale method')}"
            f", Hires upscaler: {comment_json.get('Upscale model')}"
        )
        if "strength" in comment_json:
            self._setting += f", Strength: {comment_json.get('strength')}"
        if "noise" in comment_json:
            self._setting += f", Noise: {comment_json.get('noise')}"
        if "scale" in comment_json:
            self._setting += f", Scale: {comment_json.get('scale')}"
        if self._setting:
            self._setting += ", Clip skip: 2, ENSD: 31337"

    def _comfy_png(self):
        prompt = self._info.get("prompt") or {}
        workflow = self._info.get("workflow") or {}
        prompt_json = json.loads(prompt)

        # find end node of each flow
        longest_flow = {}
        keys = [i for i in prompt_json if prompt_json[i]["class_type"]=="SaveImage"] # 获取所有满足条件的键
        max_key = str(max(int(i) for i in keys)) # 获取最大的键
        
        longest_flow = self._comfy_traverse(prompt_json, max_key,'images')

        self._positive = self.remove_quotes(longest_flow.get('positive'))
        self._negative = self.remove_quotes(longest_flow.get('negative'))


        self._raw += self._positive
        self._raw += "\n" + self._negative
        self._raw += "\n" + str(prompt)
        if workflow:
            self._raw += "\n" + str(workflow)
        self._setting = (
            f"Seed: {longest_flow.get('seed')}"
            f", Steps: {longest_flow.get('steps')}"
            f", CFG scale: {longest_flow.get('cfg')}"
            f", Sampler: {self.remove_quotes(longest_flow.get('sampler_name'))}"
            f", Scheduler: {self.remove_quotes(longest_flow.get('scheduler'))}"
            f", Size: {self._width}x{self._height}"
            f", Model: {self.remove_quotes(longest_flow.get('model'))}"
        )
        
        if "denoise" in longest_flow:
            self._setting += f", Denoising strength: {longest_flow.get('denoise')}"
        if "upscale_method" in longest_flow:
            self._setting += f", Hires upscale: {self.remove_quotes(longest_flow.get('upscale_method'))}"
        if "upscaler" in longest_flow:
            self._setting += f", Hires upscaler: {self.remove_quotes(longest_flow.get('upscale_model'))}"

    def _comfy_traverse(self, prompt, cy_key, dataType):
        images_data = {}
        # try:
        inputs = prompt[cy_key]["inputs"]
        if dataType == "images" or dataType == "image":
            if inputs.get("upscale_model"):
                self._upscale_model = self._comfy_traverse(prompt, inputs["upscale_model"][0],'upscale_model').get("model_name")
            if inputs.get("samples"):
                dataType = "samples"
            elif inputs.get("image"):
                dataType = "image"
        
        type_value = inputs.get(dataType)
        if type_value and type(type_value) is list:
            if dataType == "positive" or dataType == "negative":
                dataType = "text"
            elif dataType == "model":
                dataType = "ckpt_name"
            return self._comfy_traverse(prompt, type_value[0], dataType)
        else:
            if dataType == "samples" or dataType == "image":
                images_data = {
                    "seed": inputs.get("seed"), 
                    "steps": inputs.get("steps"), 
                    "cfg": inputs.get("cfg"), 
                    "sampler_name": inputs.get("sampler_name"), 
                    "scheduler": inputs.get("scheduler"), 
                    "denoise": inputs.get("denoise"), 
                    "upscaler": inputs.get("upscaler"),
                    "upscale_model": self._upscale_model
                }
                images_data["model"] = self._comfy_traverse(prompt, inputs["model"][0],'model').get("ckpt_name")
                latent_image = self._comfy_traverse(prompt, inputs["latent_image"][0],'latent_image')
                images_data["width"] = latent_image.get("width")
                images_data["height"] = latent_image.get("height")
                images_data["upscale_method"] = latent_image.get("upscale_method")
                images_data["positive"] = self._comfy_traverse(prompt, inputs["positive"][0],'text').get("text")
                images_data["negative"] = self._comfy_traverse(prompt, inputs["negative"][0],'text').get("text")
                # print(images_data["model"],'--\n',latent_image,'--\n',images_data["positive"],'--\n',images_data["negative"])
                # print('=============',images_data["width"],images_data["height"],images_data["positive"])
            else:
                # print(type_value,'................')
                return inputs
        # except:
        #     print("node error")
        return images_data

    @staticmethod
    def remove_data(image_file):
        with Image.open(image_file) as f:
            image_data = list(f.getdata())
            image_without_exif = Image.new(f.mode, f.size)
            image_without_exif.putdata(image_data)
            return image_without_exif

    @staticmethod
    def merge_str_to_tuple(item1, item2):
        if not isinstance(item1, tuple):
            item1 = (item1,)
        if not isinstance(item2, tuple):
            item2 = (item2,)
        return item1 + item2

    def merge_dict(self, dict1, dict2):
        dict3 = dict1.copy()
        for k, v in dict2.items():
            dict3[k] = self.merge_str_to_tuple(v, dict3[k]) if k in dict3 else v
        return dict3

    @staticmethod
    def remove_quotes(string):
        return str(string).replace('"', '').replace("'", "")

    @property
    def positive(self):
        return self._positive

    @property
    def negative(self):
        return self._negative

    @property
    def setting(self):
        return self._setting

    @property
    def raw(self):
        return self._raw

    @property
    def tool(self):
        return self._tool
    
def get_image_data():
    try:
        imagePath = slf.select_file()
        if not imagePath:
            return ["noselect"]
        ls_f = "NONE"
        try:
            f = open(imagePath, 'rb') # 第一个参数是图片的路径
            ls_f = base64.b64encode(f.read()).decode() # 将图片读取为二进制数据并编码为base64字符串
            f.close()
        except Exception:
            pass
        imgData = ImageDataReader(imagePath)
        return [{"_tool": imgData._tool, "_setting": imgData._setting, "_positive": imgData._positive, "_negative": imgData._negative, "imgBase64": ls_f}]
    except Exception as e:
        print(e)
        return ['error']

# print(get_image_data())
# get_image_data()