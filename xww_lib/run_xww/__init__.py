
from nodes import CheckpointLoader
from nodes import CheckpointLoaderSimple
from nodes import VAELoader
from nodes import LoraLoader
from nodes import CLIPLoader
from nodes import ControlNetLoader
from nodes import DiffControlNetLoader
from nodes import StyleModelLoader
from nodes import CLIPVisionLoader
from comfy_extras.nodes_upscale_model import UpscaleModelLoader
import json
import os

cwd = os.getcwd().replace('ComfyUI_windows_portable','')
# Define a decorator
def CheckpointLoaderDec(func):
    def wrapper (*args, **kwargs):
        result = func (*args, **kwargs)
        try:
            ckpt_name = list(result.get('required').get('ckpt_name')[0])
            
            path = os.path.join(cwd, "xww_lib", "savedata",'checkpointslayout.json')
            data = []
            file_name = []
            with open (path, 'r') as f:
                json_data = f.read ()
                data = json.loads(json_data)
        except OSError:
            data = []
        if len(data) > 0:
            for lt in data['layout']:
                for cn in ckpt_name:
                    if cn == lt['models_name']+lt['models_type']:
                        file_name.append(cn)
                        ckpt_name.remove(cn)
        ckpt_name_new = file_name + ckpt_name
        result['required']['ckpt_name'] = tuple([ckpt_name_new])
        return result
    return wrapper

CheckpointLoader.INPUT_TYPES = CheckpointLoaderDec(CheckpointLoader.INPUT_TYPES)


def CheckpointLoaderSimplerDec(func):
    def wrapper (*args, **kwargs):
        result = func (*args, **kwargs)
        try:
            ckpt_name = list(result.get('required').get('ckpt_name')[0])
            path = os.path.join(cwd, "xww_lib", "savedata",'checkpointslayout.json')
            data = []
            file_name = []
            with open (path, 'r') as f:
                json_data = f.read ()
                data = json.loads(json_data)
        except OSError:
            data = []
        if len(data) > 0:
            for lt in data['layout']:
                for cn in ckpt_name:
                    if cn == lt['models_name']+lt['models_type']:
                        file_name.append(cn)
                        ckpt_name.remove(cn)
        ckpt_name_new = file_name + ckpt_name
        result['required']['ckpt_name'] = tuple([ckpt_name_new])
        return result
    return wrapper

CheckpointLoaderSimple.INPUT_TYPES = CheckpointLoaderSimplerDec(CheckpointLoaderSimple.INPUT_TYPES)



def VAELoaderrDec(func):
    def wrapper (*args, **kwargs):
        result = func (*args, **kwargs)
        try:
            vae_name = list(result.get('required').get('vae_name')[0])
            
            path = os.path.join(cwd, "xww_lib", "savedata",'vaelayout.json')
            data = []
            file_name = []
            with open (path, 'r') as f:
                json_data = f.read ()
                data = json.loads(json_data)
        except OSError:
            data = []
        if len(data) > 0:
            for lt in data['layout']:
                for cn in vae_name:
                    if cn == lt['models_name']+lt['models_type']:
                        file_name.append(cn)
                        vae_name.remove(cn)
        vae_name_new = file_name + vae_name
        result['required']['vae_name'] = tuple([vae_name_new])
        return result
    return wrapper

VAELoader.INPUT_TYPES = VAELoaderrDec(VAELoader.INPUT_TYPES)



def LoraLoaderDec(func):
    def wrapper (*args, **kwargs):
        result = func (*args, **kwargs)
        try:
            lora_name = list(result.get('required').get('lora_name')[0])
            
            path = os.path.join(cwd, "xww_lib", "savedata",'loraslayout.json')
            data = []
            file_name = []
            with open (path, 'r') as f:
                json_data = f.read ()
                data = json.loads(json_data)
        except OSError:
            data = []
        if len(data) > 0:
            for lt in data['layout']:
                for cn in lora_name:
                    if cn == lt['models_name']+lt['models_type']:
                        file_name.append(cn)
                        lora_name.remove(cn)
        lora_name_new = file_name + lora_name
        result['required']['lora_name'] = tuple([lora_name_new])
        return result
    return wrapper

LoraLoader.INPUT_TYPES = LoraLoaderDec(LoraLoader.INPUT_TYPES)


def CLIPLoaderDec(func):
    def wrapper (*args, **kwargs):
        result = func (*args, **kwargs)
        try:
            clip_name = list(result.get('required').get('clip_name')[0])
            
            path = os.path.join(cwd, "xww_lib", "savedata",'cliplayout.json')
            data = []
            file_name = []
            with open (path, 'r') as f:
                json_data = f.read ()
                data = json.loads(json_data)
        except OSError:
            data = []
        if len(data) > 0:
            for lt in data['layout']:
                for cn in clip_name:
                    if cn == lt['models_name']+lt['models_type']:
                        file_name.append(cn)
                        clip_name.remove(cn)
        clip_name_new = file_name + clip_name
        result['required']['clip_name'] = tuple([clip_name_new])
        return result
    return wrapper

CLIPLoader.INPUT_TYPES = CLIPLoaderDec(CLIPLoader.INPUT_TYPES)




def ControlNetLoaderDec(func):
    def wrapper (*args, **kwargs):
        result = func (*args, **kwargs)
        try:
            control_net_name = list(result.get('required').get('control_net_name')[0])
            
            path = os.path.join(cwd, "xww_lib", "savedata",'controlnetlayout.json')
            data = []
            file_name = []
            with open (path, 'r') as f:
                json_data = f.read ()
                data = json.loads(json_data)
        except OSError:
            data = []
        if len(data) > 0:
            for lt in data['layout']:
                for cn in control_net_name:
                    if cn == lt['models_name']+lt['models_type']:
                        file_name.append(cn)
                        control_net_name.remove(cn)
        control_net_name_new = file_name + control_net_name
        result['required']['control_net_name'] = tuple([control_net_name_new])
        return result
    return wrapper

ControlNetLoader.INPUT_TYPES = ControlNetLoaderDec(ControlNetLoader.INPUT_TYPES)



def DiffControlNetLoaderDec(func):
    def wrapper (*args, **kwargs):
        result = func (*args, **kwargs)
        try:
            control_net_name = list(result.get('required').get('control_net_name')[0])
            
            path = os.path.join(cwd, "xww_lib", "savedata",'controlnetlayout.json')
            data = []
            file_name = []
            with open (path, 'r') as f:
                json_data = f.read ()
                data = json.loads(json_data)
        except OSError:
            data = []
        if len(data) > 0:
            for lt in data['layout']:
                for cn in control_net_name:
                    if cn == lt['models_name']+lt['models_type']:
                        file_name.append(cn)
                        control_net_name.remove(cn)
        control_net_name_new = file_name + control_net_name
        result['required']['control_net_name'] = tuple([control_net_name_new])
        return result
    return wrapper

DiffControlNetLoader.INPUT_TYPES = DiffControlNetLoaderDec(DiffControlNetLoader.INPUT_TYPES)




def StyleModelLoaderDec(func):
    def wrapper (*args, **kwargs):
        result = func (*args, **kwargs)
        try:
            style_model_name = list(result.get('required').get('style_model_name')[0])
            
            path = os.path.join(cwd, "xww_lib", "savedata",'style_modelslayout.json')
            data = []
            file_name = []
            with open (path, 'r') as f:
                json_data = f.read ()
                data = json.loads(json_data)
        except OSError:
            data = []
        if len(data) > 0:
            for lt in data['layout']:
                for cn in style_model_name:
                    if cn == lt['models_name']+lt['models_type']:
                        file_name.append(cn)
                        style_model_name.remove(cn)
        style_model_name_new = file_name + style_model_name
        result['required']['style_model_name'] = tuple([style_model_name_new])
        return result
    return wrapper

StyleModelLoader.INPUT_TYPES = StyleModelLoaderDec(StyleModelLoader.INPUT_TYPES)


def CLIPVisionLoaderDec(func):
    def wrapper (*args, **kwargs):
        result = func (*args, **kwargs)
        try:
            clip_name = list(result.get('required').get('clip_name')[0])
            
            path = os.path.join(cwd, "xww_lib", "savedata",'clip_visionlayout.json')
            data = []
            file_name = []
            with open (path, 'r') as f:
                json_data = f.read ()
                data = json.loads(json_data)
        except OSError:
            data = []
        if len(data) > 0:
            for lt in data['layout']:
                for cn in clip_name:
                    if cn == lt['models_name']+lt['models_type']:
                        file_name.append(cn)
                        clip_name.remove(cn)
        clip_name_new = file_name + clip_name
        result['required']['clip_name'] = tuple([clip_name_new])
        return result
    return wrapper

CLIPVisionLoader.INPUT_TYPES = CLIPVisionLoaderDec(CLIPVisionLoader.INPUT_TYPES)



def UpscaleModelLoaderDec(func):
    def wrapper (*args, **kwargs):
        result = func (*args, **kwargs)
        try:
            model_name = list(result.get('required').get('model_name')[0])
            
            path = os.path.join(cwd, "xww_lib", "savedata",'upscale_modelslayout.json')
            data = []
            file_name = []
            with open (path, 'r') as f:
                json_data = f.read ()
                data = json.loads(json_data)
        except OSError:
            data = []
        if len(data) > 0:
            for lt in data['layout']:
                for cn in model_name:
                    if cn == lt['models_name']+lt['models_type']:
                        file_name.append(cn)
                        model_name.remove(cn)
        model_name_new = file_name + model_name
        result['required']['model_name'] = tuple([model_name_new])
        return result
    return wrapper

UpscaleModelLoader.INPUT_TYPES = UpscaleModelLoaderDec(UpscaleModelLoader.INPUT_TYPES)
NODE_CLASS_MAPPINGS = {}
# __all__ = ['NODE_CLASS_MAPPINGS']