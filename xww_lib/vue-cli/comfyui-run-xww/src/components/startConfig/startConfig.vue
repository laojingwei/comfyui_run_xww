<template>
    <show-page>
        <label class="title-bg">
            <span v-if="CHENFLAF">
                如果你有装sd-webUI，那么可以选择以下三种方式来让ComfyUI使用sd-webUI里的模型，这样不需要存两套模型了；选择哪种方式看你个人喜好；这里注意了，如果你配置了方式1，那么会优先使用方式1的，如果你想灵活使用，可以通过下方选项来切换你想要哪种方式；如果在输入内容时左边选项栏出现遮挡，可点击顶部锁定按钮锁定标题栏
            </span>
            <span v-else>
                If you have installed sd-webUI, you can choose one of three ways to use the models in ComfyUI's sd-webUI,
                instead of storing two sets of models. Which one you choose depends on your personal preference; Note that
                if you have mode 1 configured, Mode 1 will be preferred. If you want to use it flexibly, you can use the
                options below to switch which mode you want to use; If the left option bar is blocked while typing, click
                the lock button at the top to lock the title bar
            </span>
        </label>
        <div class="div-radio-box">
            <input type="radio" id="yaml" name="radio" :disabled="disabled" value="1" v-model="radioValue">
            <label for="yaml">
                <span v-if="CHENFLAF">
                    优先使用方式1
                </span>
                <span v-else>
                    Mode 1 is preferred
                </span>
            </label>
            <input type="radio" id="symlink" name="radio" :disabled="disabled" value="0" v-model="radioValue">
            <label for="symlink">
                <span v-if="CHENFLAF">
                    优先使用方式2或3
                </span>
                <span v-else>
                    Mode 2 or 3 is preferred
                </span>
            </label>
        </div>
        <br>
        <label>
            <span v-if="CHENFLAF">
                方式1--直接读取sd-webui里的模型：在这配置后，comfyUI启动时会直接通过路径读取sd-webui里的checkpoints、loras、vae、controlnet、embeddings、ESRGAN、SwinIR模型
            </span>
            <span v-else>
                Method 1-- Reading sd-webui models: After this configuration, comfyUI starts up using the checkpoints,
                loras, vae, controlnet, embeddings, ESRGAN and SwinIR models found on the sd-webui
            </span>
        </label>
        <textarea type="text" v-model="inputValue"
            :placeholder="CHENFLAF ? '请输入sd-webui的项目路径，如：F:/sd-webui' : 'Enter the project path of the sd-webui, for example:F:/sd-webui'" />
        <button @click="setModesPath" :disabled="modesDisabled">
            <span v-if="CHENFLAF">
                方式1
            </span>
            <span v-else>
                Mode 1
            </span>
        </button>
        <br>
        <br>
        <label>
            <span v-if="CHENFLAF">
                方式2--文件夹映射：在这配置后，comfyUI启动时会通过映射文件来读取sd-webui里的模型，这里只支持sd-webui里的checkpoints、loras、vae、controlnet、embeddings进行映射到comfyUI里，如需映射其它文件夹请使用下面的功能
            </span>
            <span v-else>
                Method 2-- Folder mapping: After this configuration, comfyUI startup reads the sd-webui models using a
                mapping file that I checkpoints, loras, vae, controlnet and embeddings in sd-webui. To map other folders,
                use the following functions
            </span>
        </label>
        <textarea type="text" v-model="inputValue0"
            :placeholder="CHENFLAF ? '请输入sd-webui的项目路径，如：F:/sd-webui' : 'Enter the project path of the sd-webui, for example:F:/sd-webui'" />
        <button @click="ok">
            <span v-if="CHENFLAF">
                方式2
            </span>
            <span v-else>
                Mode 2
            </span>
        </button>
        <br>
        <label>
            <span v-if="CHENFLAF">
                方式3--自定义创建映射
            </span>
            <span v-else>
                Method 3-- Create a custom mapping
            </span>
        </label>
        <textarea type="text" v-model="inputValue1"
            :placeholder="CHENFLAF ? '请输入源所在路径，如：F:/sd-webui' : 'Please enter the source path, for example:F:/sd-webui'" />
        <textarea type="text" v-model="inputValue2"
            :placeholder="CHENFLAF ? '请输入要创建映像的路径，如：F:/sd-webui' : 'Enter the path where you want to create the image, for example:F:/sd-webui'" />
        <button @click="ok1">
            <span v-if="CHENFLAF">
                方式3
            </span>
            <span v-else>
                Mode 3
            </span>
        </button>
    </show-page>
</template>

<script>

export default {
    props: {
        CHENFLAF: {
            type: Boolean,
            default: true,
        },
    },
    data() {
        return {
            isMounted: true,
            disabled: true,
            modesDisabled: false,
            radioValue: '',
            inputValue: '',
            inputValue0: '',
            inputValue1: '',
            inputValue2: '',
        };
    },

    watch: {
        radioValue(newVal) {
            if (!newVal || this.isMounted) {
                this.isMounted = false;
                return;
            }
            this.isMounted = false;
            this.disabled = true;
            this.$Xwwqt.useYmal(newVal);
            this.radioTimer = setTimeout(() => {
                clearTimeout(this.radioTimer)
                !this.$UseYmalFlag && (this.radioValue = '');
                this.disabled = false;
            }, 1500);
        }
    },

    mounted() {
        this.disabled = true;
        this.$Xwwqt.checkYmalFlag();
        this.mountedradioTimer = setTimeout(() => {
            clearTimeout(this.mountedradioTimer);
            this.disabled = false;
            this.radioValue = this.$UseYmalFlag;
        }, 1500);
    },

    methods: {
        setModesPath() {
            if (!this.inputValue) {
                this.$Toast.show(this.CHENFLAF ? '路径不能为空，请输入正确路径' : 'The path cannot be empty. Please enter the correct path');
            } else {
                this.modesPathTimer && clearTimeout(this.modesPathTimer);
                this.modesDisabled = true;
                // 给qt发送启动指令
                this.$Xwwqt.setModesPath(this.inputValue.trim());
                this.modesPathTimer = setTimeout(() => {
                    clearTimeout(this.modesPathTimer);
                    this.modesDisabled = false;
                    if (this.$ChangeModesPath === "1") {
                        this.$Xwwqt.py_alert(this.CHENFLAF ? '温馨提示' : 'tips', this.CHENFLAF ? '设置成功，可前往模型选项查看效果，ComfyUI生效需要重启' : 'After the setting is successful, you can go to the model option to view the effect. ComfyUI takes effect and needs to be restarted');
                    }
                }, 2000);
            }
        },
        ok() {
            if (!this.inputValue0) {
                this.$Toast.show(this.CHENFLAF ? '路径不能为空，请输入正确路径' : 'The path cannot be empty. Please enter the correct path');
            } else {
                // 给qt发送启动指令
                this.$Xwwqt.cread_symlink(this.inputValue0.trim());
            }
        },
        ok1() {
            if (!this.inputValue1 || !this.inputValue2) {
                this.$Toast.show(this.CHENFLAF ? '路径不能为空，请输入正确路径' : 'The path cannot be empty. Please enter the correct path');
            } else {
                this.$Xwwqt.cread_symlink_auto(this.inputValue1.trim(), this.inputValue2.trim());
            }
        },
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.title-bg {
    margin-top: 0;
    color: red;
    background: rgba(255, 255, 23, 0.8);
    ;
}

label {
    margin: 30px 0 0 0;
    padding: 10px;
    color: #45bb00;
    text-align: center;
    align-items: center;
    background: rgba(0, 0, 0, 0.8);
    border-radius: 5px;
}

.div-radio-box {
    display: flex;
    justify-content: center;
    background: rgba(0, 0, 0, 0.8);
    text-align: center;
    align-items: center;
}

.div-radio-box input {
    margin: 0 3px 0 10px;
}

.div-radio-box label {
    margin: 0;
    background-color: rgba(0, 0, 0, 0.8);
}

textarea {
    max-width: 99.8%;
    background: #000000;
    color: #ffffff;
    border-radius: 5px;
}

input {
    font-size: 20px;
    height: 50px;
    border: 1px solid #000000;
    border-radius: 2px;
    text-align: center;
    align-items: center;
}

button:hover {
    transform: scale(1.05);
}

button {
    font-size: 24px;
    margin: 10px 30%;
    width: 40%;
    /* background: #8d77d1; */
    background-image: linear-gradient(rgb(51, 51, 51), #fffdfd);
    border: 1px solid #000000;
    border-radius: 8px;
}

button:active {
    /* opacity: 0.8; */
    transform: scale(0.95);
    background-image: linear-gradient(rgb(80, 79, 79), rgb(255, 255, 255));
}
</style>
