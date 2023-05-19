<template>
    <div>
        <div ref="versionControl" class="version-control" :style="style">
            <div class="vc-box-div-top">
                <div>ComfyUI Code</div>
                <button class="sub-button" @click="goBranch">
                    <span v-if="CHENFLAF">
                        所在分支
                    </span>
                    <span v-else>
                        location branch
                    </span>
                </button>
                <button class="sub-button" @click="opendir">
                    <span v-if="CHENFLAF">
                        打开本地
                    </span>
                    <span v-else>
                        Open local
                    </span>
                </button>
                <button class="sub-button" @click="getComfyuiData">
                    <span v-if="CHENFLAF" @mouseenter="refreshTips(1)" @mouseleave="refreshTips(0)">
                        刷新
                    </span>
                    <span v-else @mouseenter="refreshTips(1)" @mouseleave="refreshTips(0)">
                        refresh
                    </span>
                </button>
                <button class="sub-button" @click="hide">
                    <span v-if="CHENFLAF">
                        关闭
                    </span>
                    <span v-else>
                        close
                    </span>
                </button>
            </div>
            <div class="vc-box-div">
                <div class="vc-box-div-sub">
                    <span v-if="CHENFLAF">
                        版本哈希值
                    </span>
                    <span v-else>
                        Version hash value
                    </span>
                </div>
                <div class="vc-box-div-sub">
                    <span v-if="CHENFLAF">
                        更新日志
                    </span>
                    <span v-else>
                        update log
                    </span>
                </div>
                <div class="vc-box-div-sub">
                    <span v-if="CHENFLAF">
                        所在版本
                    </span>
                    <span v-else>
                        version
                    </span>
                </div>
            </div>
            <div id="vcBox" class="vc-box">
                <div v-for="(item, index) in ComfyUIgitData" :key="index + item.name">
                    <div :id="index + item.hexsha + item.name"
                        :class="item.isLocal == 1 ? 'vc-box-div selected-bg' : 'vc-box-div'">
                        <div class="vc-box-div-sub">
                            <span class="blue text-dec" @click="openUrl(item)">{{ subStringF(item.hexsha, 15) }}</span>
                        </div>
                        <div class="vc-box-div-sub">
                            <span>{{ item.authored_datetime }}</span>
                            <span class="scale08 text-dec" @click="openUrl(item)">{{ subStringF(item.message, 30) }}</span>
                        </div>
                        <div class="vc-box-div-sub raido-an">
                            <input type="radio" :checked="item.isLocal == 1 ? true : false" :id="item.hexsha + index"
                                name="radioVC" :value="index" class="center" @click="checkoutcy(item, index)" />
                            <label class="center" :for="item.hexsha + index">
                                {{ ComfyUIgitData.length - index }}
                                <span v-if="CHENFLAF">
                                    {{ item.isLocal == 1 ? "你所在分支" : "切换" }}
                                </span>
                                <span v-else>
                                    {{ item.isLocal == 1 ? "Your branch" : "switch to" }}
                                </span>
                            </label>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>

export default {
    name: 'vc-div',
    components: {},
    data() {
        return {
            selectedId: '',
            isSelectedIndex: '',
            CHENFLAF: true,
            isShow: false,
            style: '',
            ComfyUIgitData: [],
            emoji: ['(≧∇≦)ﾉ', '(+.+)(-.-)(_ _) ..zzZZ もうだめ', 'ヾ(≧O≦)〃嗷~', '٩(๑òωó๑)۶', '( *￣▽￣)((≧︶≦*)', '（*＾-＾*）', '...(*￣０￣)ノ[等等我…]', 'n(*≧▽≦*)n', '(～o￣▽￣)～o 。。。滚来滚去……o～(＿△＿o～) ~。。。', '不＞(￣ε￣ = ￣3￣)<要', '.....((/- -)/', '-________-', '(*￣▽￣)(￣▽:;.…::;.:.:::;..::;.:...', '『家』 ～o(▽｀ o) =3 =3 =3', '＼（＾∀＾）メ（＾∀＾）ノ', '(*/ω＼*)/p.', '◕ฺ‿◕ฺ✿ฺ)', 'Ψ(￣∀￣)Ψ', '( *^-^)ρ(^0^* )', '↑↑↓↓←→←→ＢＡ...┗( -o-)┛', '（￣ー￣）ノ~~マ☆’.・.・:★', '．《{=．．．．（嘎~嘎~嘎~）'],
        };
    },
    mounted() {
        // TODO: test
        // this.ComfyUIgitData = [{ 'name': 'comfy_translation_node', 'path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node', 'hexsha': '4ef4cf913f587600b8349e65c0a03f5afcbead0e', 'authored_datetime': '2023-04-24T20:59:04', 'message': '为撒服务如风无非是打发儿童反反复复反反复复反反复复方法', "isLocal": 0, 'gitUrl': 'https://github.com/comfyanonymous/ComfyUI/commit/4ef4cf913f587600b8349e65c0a03f5afcbead0e' }];
        // for (let i = 0; i < 5; i++) {
        //     this.ComfyUIgitData = [...this.ComfyUIgitData, ...this.ComfyUIgitData];
        // }
        // let tt = [{ 'name': 'comfy_translation_node', 'path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node', 'hexsha': '4ef4cf913f587600b8349e65c0a03f5afcbead0e', 'authored_datetime': '2023-04-24T20:59:04', 'message': '为撒服务如风无非是打发儿童反反复复反反复复反反复复方法', "isLocal": 1, 'gitUrl': 'https://github.com/comfyanonymous/ComfyUI/commit/4ef4cf913f587600b8349e65c0a03f5afcbead0e' }];
        // this.ComfyUIgitData = [...this.ComfyUIgitData, ...tt];
        // console.log(this.ComfyUIgitData.length)
        // this.$nextTick(() => {
        //     setTimeout(() => {
        //         this.selectedId = '324ef4cf913f587600b8349e65c0a03f5afcbead0ecomfy_translation_node';
        //         let targetbox = document.getElementById(this.selectedId);
        //         document.getElementById("vcBox").scrollTop = targetbox.offsetTop;
        //     })
        // })

    },
    methods: {
        opendir() {
            this.$Xwwqt.open_local_file('ComfyUI', 'dir');
        },
        openUrl(item) {
            item.gitUrl && this.$Xwwqt.openUrl(item.gitUrl)
        },
        refreshTips(i) {
            if (i) {
                this.$Toast.show(this.CHENFLAF ? '如果刷新时间超过5分钟，可以重新点击刷新；当发现刷新回来的内容不全时，也可以重新点击刷新' : 'If the refresh time exceeds 5 minutes, click refresh again. If you find that the content is not complete, you can click refresh again', 30000);
            } else {
                this.$Toast.hide();
            }
        },
        set_chen(v) {
            this.CHENFLAF = v;
        },
        goBranch() {
            if (this.selectedId) {
                let targetbox = document.getElementById(this.selectedId);
                document.getElementById("vcBox").scrollTop = targetbox.offsetTop;
            }
        },
        setCyData() {
            if (this.$GitComfyuiData && this.$GitComfyuiData[0] !== "NONE") {
                this.ComfyUIgitData = this.$GitComfyuiData;
                for (let i = 0; i < this.ComfyUIgitData.length; i++) {
                    if (this.ComfyUIgitData[i].isLocal == 1) {
                        this.isSelectedIndex = i;
                        this.selectedId = i + this.ComfyUIgitData[i].hexsha + this.ComfyUIgitData[i].name;
                        break;
                    }
                }
                this.$nextTick(() => {
                    setTimeout(() => {
                        if (this.selectedId) {
                            let targetbox = document.getElementById(this.selectedId);
                            document.getElementById("vcBox").scrollTop = targetbox.offsetTop;
                        }
                    })
                })
            }
        },
        show() {
            if (!this.isShow) {
                // 使用finish会出现无法再次打开问题，这里使用两个动画来实现快速点击效果
                // this.$velocity(this.$refs.versionControl, "finish");
                this.$velocity(this.$refs.versionControl, { translateY: "-100vh", opacity: 0.5 }, { duration: 100 });
                // this.$Xwwqt.py_print(JSON.stringify(this.$GitComfyuiData))
                this.setCyData();
                this.isShow = true;
                this.$velocity(this.$refs.versionControl, { translateY: "100vh", opacity: 1 }, { duration: 1000, delay: 110 });
            } else {
                this.hide();
            }
        },
        hide() {
            if (!this.isShow) {
                return;
            }
            this.isShow = false;
            // this.$velocity(this.$refs.versionControl, { translateY: "100vh", opacity: 1 }, { duration: 100 });
            this.$velocity(this.$refs.versionControl, { translateY: "-100vh", opacity: 0.5 }, { duration: 1000, delay: 110 });
        },
        chenflag(v) {
            this.CHENFLAF = v;
        },
        checkoutcy(item, i) {
            if (item.isLocal) {
                return;
            }
            this.$Toast.show(this.CHENFLAF ? '切换中。。。' : 'Switching...');
            this.$Xwwqt.git_checkout_cy(item.path, item.hexsha);
            this.checkoutcyTime(i);
        },
        checkoutcyTime(i) {
            this.checkoutcyTimer && clearTimeout(this.checkoutcyTimer);
            this.checkoutcyTimer = setTimeout(() => {
                clearTimeout(this.checkoutcyTimer);
                if (this.$GitFlag && this.$GitFlag !== "start") {
                    if (this.$GitFlag === "error") {
                        this.$Toast.show(this.CHENFLAF ? '切换失败' : 'Switchover failure', 3000);
                    } else {
                        if (this.isSelectedIndex !== '') {
                            this.ComfyUIgitData[this.isSelectedIndex].isLocal = 0;
                        }
                        this.isSelectedIndex = i;
                        this.ComfyUIgitData[this.isSelectedIndex].isLocal = 1;
                        this.$Toast.show(this.CHENFLAF ? '切换成功' : 'Successful switchover', 3000);
                    }
                } else {
                    this.$Toast.show((this.CHENFLAF ? '努力切换中。。。' : 'Trying to switch...') + this.emoji[Math.floor(Math.random() * 20)]);
                    this.checkoutcyTime(i);
                }
            }, 1000);
        },
        subStringF(str, i) {
            if (!str) {
                return '';
            }
            return str.substring(0, i) + '...';
        },
        getComfyuiDataTime() {
            this.getComfyuiDataTimer && clearTimeout(this.getComfyuiDataTimer);
            this.getComfyuiDataTimer = setTimeout(() => {
                clearTimeout(this.getComfyuiDataTimer);
                // this.$Xwwqt.py_print(this.$GitFlag)
                if (this.$GitFlag && this.$GitFlag === "success") {
                    this.setCyData();
                    this.$Toast.show(this.CHENFLAF ? '刷新完成' : 'Refresh complete');
                } else if (this.$GitFlag === "error") {
                    this.$Toast.show(this.CHENFLAF ? '刷新失败' : 'Refresh failure');
                } else {
                    this.tip = this.CHENFLAF ? ['正在获取自定义节点最新信息。。。', '这么慢？嗯，是有点慢。。。', '努力加载中，请稍等。。。', '国内gitHub环境就这样。。。', '有时稍微等会也是一种放松。。。'] : ['Getting updates on custom nodes... ', ' so slow? Well, a little slow... ', 'trying to load, please wait... ', ' the domestic gitHub environment is like this... ', 'sometimes waiting a little is a kind of relaxation... ']
                    this.$Toast.show(this.tip[Math.floor(Math.random() * 5)] + this.emoji[Math.floor(Math.random() * 20)]);
                    this.getComfyuiDataTime();
                }
            }, 1000);
        },
        getComfyuiData() {
            this.$Toast.show(this.CHENFLAF ? '正在刷新ComfyUI版本信息，请稍等' : 'Please wait while refreshing ComfyUI version information');
            this.$Xwwqt.git_comfyui_code('refresh');
            this.getComfyuiDataTime();
        },
    },
};
</script>

<style scoped>
.version-control {
    position: fixed;
    top: -100vh;
    left: 30%;
    width: 60%;
    background-color: rgb(51, 51, 51, 0.8);
    color: #fff;
    padding: 10px;
    border-radius: 5px;
    word-wrap: break-word;
    word-break: break-all;
    z-index: 990;
    opacity: 0.5;
}

.empty-div {
    width: 100%;
    height: 30vh;
    /* background-color: red; */
}

.vc-box {
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
    height: 80vh;
    overflow-x: scroll;
}

.vc-tab {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: auto;
}

.vc-tab .button:hover {
    color: #55ff00;
    transform: scale(1.1);
    background-image: linear-gradient(to right, rgb(0, 0, 0), rgb(129, 128, 128));
}

.vc-tab .button {
    margin: 30px 20px;
    padding: 10px;
    font-size: 14px;
    color: #ffffff;
    border-radius: 8px;
    opacity: 1;
    background-image: linear-gradient(to right, rgb(0, 0, 0), rgb(183, 183, 183));
}

.vc-tab .button:active {
    /* opacity: 0.8; */
    transform: scale(0.95);
    background-image: linear-gradient(to right, rgb(63, 75, 62), rgb(0, 255, 34));
}

.vc-list {
    position: absolute;
    top: 100px;
    left: 0;
    right: 0;
    width: 100%;
    height: 100%;
    padding: 10px 10px;
    overflow-x: scroll;
    color: #FFFFFF;
    transform: 1;
    /* background-color: #55ff00; */
}

.vc-load {
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 100px;
    left: 200%;
    right: 0;
    width: 100%;
    height: 100%;
    padding: 10px 10px;
    overflow-x: scroll;
    color: #FFFFFF;
    transform: 1;
}

.vc-load label {
    padding: 10px;
    color: #45bb00;
    text-align: center;
    align-items: center;
    background: rgba(0, 0, 0, 0.8);
    ;
    border-radius: 5px;
}

.vc-load textarea {
    background: #000000;
    color: #ffffff;
    border-radius: 5px;
}

.vc-load input {
    font-size: 20px;
    height: 50px;
    border: 1px solid #000000;
    border-radius: 2px;
    text-align: center;
    align-items: center;
}

.vc-load button:hover {
    transform: scale(1.05);
}

.vc-load button {
    font-size: 24px;
    margin: 10px 30%;
    width: 40%;
    /* background: #8d77d1; */
    background-image: linear-gradient(rgb(51, 51, 51), #fffdfd);
    border: 1px solid #000000;
    border-radius: 8px;
}

.vc-load button:active {
    /* opacity: 0.8; */
    transform: scale(0.95);
    background-image: linear-gradient(rgb(80, 79, 79), rgb(255, 255, 255));
}

.selected-bg {
    background: rgba(24, 97, 1, 0.8) !important;
}

.selected-bg:hover {
    background: rgba(32, 129, 2, 0.8) !important;
}

.vc-box-div:hover {
    background: rgb(10 40 1 / 80%);
}

.vc-box-div {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    width: 99%;
    height: auto;
    /* padding: 10px; */
    border: 1px solid #FFFFFF;
    background: rgb(0, 0, 0, 0.8);
}

.vc-box-div-top {
    display: flex;
    justify-content: space-between;
    width: 100%;
    height: auto;
    border-right-style: solid;
    /* font-size: 14px; */
}

.raido-an:hover {
    color: #42a211;
    transform: scale(1.2);
}

.vc-box-div-sub {
    display: flex;
    align-items: center;
    flex-direction: column;
    font-size: 12px;
    /* justify-content: flex-start; */
    padding: 3px;
    width: 33.3%;
    height: auto;
    border-right-style: solid;
}

.vc-box-div-sub:last-child {
    width: 33.3%;
    border-right-style: none;
}

.sub-vc-box-div-detail {
    border: 1px solid #FFFFFF;
}

.center {
    width: 100%;
    text-align: center;
}

.scale08 {
    transform: scale(0.8);
}

.text-dec {
    text-decoration: underline
}

.text-dec:hover {
    transform: scale(1.2);
}

.blue {
    color: #0000ff;
}

.green {
    color: #55ff00;
}

.green1 {
    color: #42a211;
}

.red {
    color: red;
}

.sub-button {
    margin: 5px 5px;
    border: 1px solid #000000;
    border-radius: 5px;
    font-size: 14px;
}

.sub-button:hover {
    transform: scale(1.2);
    background-color: rgb(193, 213, 191);
    color: #38a302 !important;
}

.sub-button:active {
    transform: scale(0.9);
}
</style>
