<template>
    <show-page>
        <img ref="errImg" class="err-img" src="@/assets/error.png" />
        <label>
            <span v-if="CHENFLAF">
                ComfyUI整合包更新：一般只需要更新ComfyUI代码就可以了，如果更新ComfyUI后没法使用，那说明作者新增了python依赖，这时可以使用“更新ComfyUI代码和python依赖”按钮进行全部更新。
            </span>
            <span v-else>
                ComfyUI integration package update: Generally, you only need to update the ComfyUI code. If the ComfyUI
                update cannot be used, it means that the author has added python dependencies. In this case, you can use the
                "Update ComfyUI code and python dependencies" button for all updates.
            </span>
        </label>
        <button @click="updateCui('update_comfyui.bat')">
            <span v-if="CHENFLAF">
                只更新ComfyUI代码
            </span>
            <span v-else>
                Update ComfyUI code only
            </span>
        </button>
        <button @click="updateCui('update_comfyui_and_python_dependencies.bat')">
            <span v-if="CHENFLAF">
                更新ComfyUI代码和python依赖
            </span>
            <span v-else>
                Update ComfyUI code and python dependencies
            </span>
        </button>
        <br>
        <br>
        <label>
            <span v-if="CHENFLAF">
                项目下载：没下载过项目的可选择下面按钮进行下载，项目大小在1.34G左右，如果你下载下来的压缩包小于1.34G，请重新下载或更换其它方式下载；如果你的网络访问gitHub比较快，推荐使用第一个下载，如果比较慢，可以去我的百度网盘下载，解压即用
            </span>
            <span v-else>
                Project Download: If you haven't downloaded the project before, you can choose the button below to start the download. The project size is around 1.34GB. If the size of the downloaded compressed file is less than 1.34GB, please download it again or use another method for downloading. If your network accesses GitHub quickly, it is recommended to use the first download option. If it's slow, you can download from my Baidu Netdisk and use it after extracting.
            </span>
        </label>
        <button @click="downLoad(0,1)">
            <span v-if="CHENFLAF">
                项目下载（github）-新版
            </span>
            <span v-else>
                Project download (github)-New version
            </span>
        </button>
        <button @click="openUrl_('https://pan.baidu.com/s/1jH67y')">
            <span v-if="CHENFLAF">
                项目下载（百度云）-新版
            </span>
            <span v-else>
                Project download (Baidu cloud)-New version
            </span>
        </button>
        <!-- <button @click="downLoad(1)">
            <span v-if="CHENFLAF">
                项目下载（huggingface）-旧版
            </span>
            <span v-else>
                Project download (huggingface)
            </span>
        </button>
        <br>
        <button @click="downLoad(0,0)">
            <span v-if="CHENFLAF">
                项目下载（github）-旧版
            </span>
            <span v-else>
                Project download (github)
            </span>
        </button> -->
        <br>
        <!-- <button @click="downLoad(1)">
            <span v-if="CHENFLAF">
                项目下载（国内加速1下载）
            </span>
            <span v-else>
                Project download (Domestic accelerated 1 download)
            </span>
        </button>
        <br>
        <button @click="downLoad(2)">
            <span v-if="CHENFLAF">
                项目下载（国内加速2下载）
            </span>
            <span v-else>
                Project download (Domestic accelerated 2 download)
            </span>
        </button> -->
        <br>
        <br>
        <label>
            <span v-if="CHENFLAF">
                启动器版本更新：点击可更新最新版（进入该页面会自动校验是否为最新版，如何你开了代理请关闭代理再进入，要不然可能会一直卡着）
            </span>
            <span v-else>
                Initiator version update: Click to update the latest version (Entering this page will automatically check
                whether it is the latest version. If you have opened the proxy, please close the proxy before entering,
                otherwise it may be stuck.)
            </span>
        </label>
        <button v-if="isLatestVersion">
            <span v-if="CHENFLAF">
                已是最新
            </span>
            <span v-else>
                It's the latest version
            </span>
        </button>
        <button v-else @click="updateXww">
            <span v-if="CHENFLAF">
                更新
            </span>
            <span v-else>
                update
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
            isLatestVersion: true,
            isShowErrImg: false,
            emoji: ['(≧∇≦)ﾉ', '(+.+)(-.-)(_ _) ..zzZZ もうだめ', 'ヾ(≧O≦)〃嗷~', '٩(๑òωó๑)۶', '( *￣▽￣)((≧︶≦*)', '（*＾-＾*）', '...(*￣０￣)ノ[等等我…]', 'n(*≧▽≦*)n', '(～o￣▽￣)～o 。。。滚来滚去……o～(＿△＿o～) ~。。。', '不＞(￣ε￣ = ￣3￣)<要', '.....((/- -)/', '-________-', '(*￣▽￣)(￣▽:;.…::;.:.:::;..::;.:...', '『家』 ～o(▽｀ o) =3 =3 =3', '＼（＾∀＾）メ（＾∀＾）ノ', '(*/ω＼*)/p.', '◕ฺ‿◕ฺ✿ฺ)', 'Ψ(￣∀￣)Ψ', '( *^-^)ρ(^0^* )', '↑↑↓↓←→←→ＢＡ...┗( -o-)┛', '（￣ー￣）ノ~~マ☆’.・.・:★', '．《{=．．．．（嘎~嘎~嘎~）'],
            inputValue: '',
            inputValue1: '',
            inputValue2: '',
            updateStart: '',
            updateStart1: '',
        };
    },

    mounted() {
        this.$Xwwqt.check_xww_v();
        this.check_xww_vTime();

    },

    methods: {
        openUrl_(url) {
            url && this.$Xwwqt.openUrl(url)
        },
        check_xww_vTime() {
            this.check_xww_vTimer && clearTimeout(this.check_xww_vTimer);
            this.check_xww_vTimer = setTimeout(() => {
                clearTimeout(this.check_xww_vTimer)
                if (this.$UpdateXwwV && this.$UpdateXwwV[0] === "start") {
                    // let text = this.CHENFLAF ? "正在检查启动器版本，请稍等。。。" : "Checking launcher version, please wait...";
                    // this.$Toast.show(text + this.emoji[Math.floor(Math.random() * 20)]);
                    // this.check_xww_vTime();
                } else if (this.$UpdateXwwV && this.$UpdateXwwV[0] === "error") {
                    // let text = this.CHENFLAF ? "无法获取启动器最新版本信息" : "Unable to get the latest version information of the launcher";
                    // this.$Toast.show(text);
                } else if (this.$UpdateXwwV && this.$UpdateXwwV[0]) {
                    let v = this.$UpdateXwwV[0];
                    if (v["localHexsha"] !== v["newHexsha"]) {
                        this.isLatestVersion = false;
                        let text = this.CHENFLAF ? "启动器有更新，你可点击最下面启动器更新按钮进行更新" : "The launcher has updated, you can click the launcher update button at the bottom to update";
                        this.$Toast.show(text, 5000);
                    } else {
                        this.isLatestVersion = true;
                    }
                }
            }, 500);
        },
        randomString(len, chars) {
            let str = "";
            for (let i = 0; i < len; i++) {
                // 随机生成一个索引
                let index = Math.floor(Math.random() * chars.length);
                // 从chars中取出对应的字符
                let char = chars.charAt(index);
                // 拼接到str中
                str += char;
            }
            return str;
        },
        updateTimer(i, t) {
            this.updateAllTimer && clearTimeout(this.updateAllTimer);
            this.updateAllTimer = setTimeout(() => {
                this.$Toast.hide();
                clearTimeout(this.updateAllTimer)
                if (this.$UpdateCuiBat !== "finish") {
                    this.tip = this.CHENFLAF ? "正在努力处理中，请勿退出或进行其它操作。。。(进度请看控制台)" : "Please do not exit or perform other operations while trying to process... (Please refer to the console for progress)";
                    let strL = [this.tip, this.randomString(this.tip.length, this.tip)]
                    this.$Toast.show(strL[Math.floor(Math.random() * 2)] + this.emoji[Math.floor(Math.random() * 20)], 5000);
                    this.updateTimer(i, 5000);
                }
            }, t);
        },
        updateCui(i) {
            if (this.$DonloadFlag === "start" || this.$UpdateCuiBat === "start" || this.$UpdateXww === "start") {
                this.$Toast.show(this.CHENFLAF ? '已有其它任务正在下载中，请稍等。。。' : 'Other tasks are downloading, please wait...', 3000);
                return;
            }
            this.$velocity(this.$refs.errImg, "finish");
            this.$velocity(this.$refs.errImg, { height: 400, opacity: 1 }, { duration: 3000 });
            this.$velocity(this.$refs.errImg, { height: 0, opacity: 0 }, { duration: 3000, delay: 20000 });
            this.$Xwwqt.updateCui(i);
            this.updateTimer(i, 100);
        },
        updateXwwTime() {
            this.updateXwwTimer && clearTimeout(this.updateXwwTimer);
            this.updateXwwTimer = setTimeout(() => {
                clearTimeout(this.updateXwwTimer);
                if (this.$UpdateXww === "start") {
                    this.$Toast.show(this.CHENFLAF ? `正在更新，请稍等。。。${this.emoji[Math.floor(Math.random() * 20)]}` : `Updating, please wait...${this.emoji[Math.floor(Math.random() * 20)]}`);
                    this.updateXwwTime();
                } else if (this.$UpdateXww === "error") {
                    this.isLatestVersion = false;
                    this.$Toast.show(this.CHENFLAF ? '更新失败' : 'Update failed', 3000);
                } else if (this.$UpdateXww === "success") {
                    this.$Toast.show(this.CHENFLAF ? '更新成功，如果有些功能无法使用时，请退出启动器重新启动' : 'The update was successful. If some functions are not available, please exit the launcher and start again', 3000);
                    this.isLatestVersion = true;
                }
            }, 1000);
        },
        updateXww() {
            if (this.$DonloadFlag === "start" || this.$UpdateCuiBat === "start" || this.$UpdateXww === "start") {
                this.$Toast.show(this.CHENFLAF ? '已有其它任务正在下载中，请稍等。。。' : 'Other tasks are downloading, please wait...', 3000);
                return;
            }
            this.$Toast.show(this.CHENFLAF ? '正在更新，请稍等。。。' : 'Updating, please wait...');
            let v = this.$UpdateXwwV[0];
            this.$Xwwqt.update_xww(v.newHexsha);
            this.updateXwwTime();
        },
        downLoad(i,k) {
            if (this.$DonloadFlag === "start" || this.$UpdateCuiBat === "start" || this.$UpdateXww === "start") {
                this.$Toast.show(this.CHENFLAF ? '已有其它任务正在下载中，请稍等。。。' : 'Other tasks are downloading, please wait...', 3000);
                return;
            }
            this.$Toast.show(this.CHENFLAF ? "正在下载项目，请耐心等待，可前往控制台查看下载进度" : "Downloading the project, please wait patiently, you can go to the console to check the download progress", 3000);
            this.$Xwwqt.downloadProject(i,k);
            this.downLoadTime();
        },
        downLoadTime() {
            this.downLoadTimer && clearTimeout(this.downLoadTimer);
            this.downLoadTimer = setTimeout(() => {
                clearTimeout(this.downLoadTimer);
                let progress = this.$Progress || '请稍等';
                if (this.$DonloadFlag === "start") {
                    let text = this.CHENFLAF ? `${progress}<br>正在努力下载中。。。${this.emoji[Math.floor(Math.random() * 20)]}` : `${progress}<br>Working on downloading...${this.emoji[Math.floor(Math.random() * 20)]}`;
                    this.$Toast.show(text);
                    this.downLoadTime();
                } else if (this.$DonloadFlag === "error") {
                    this.$Toast.show(this.CHENFLAF ? '操作失败' : 'Download failed', 3000);
                } else if (this.$DonloadFlag === "success") {
                    this.$Toast.show(this.CHENFLAF ? '操作成功' : 'Download successfully', 3000);
                }
            }, 2000);
        },
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.err-img {
    height: 0;
    opacity: 0;
}

label {
    margin: 30px;
    padding: 10px;
    color: #45bb00;
    text-align: center;
    align-items: center;
    background: rgba(0, 0, 0, 0.8);
    ;
    border-radius: 5px;
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
