<template>
    <div id="main-page">
        <!-- grid-layout属性说明
        属性名称	属性说明
        col-num	画布占几列,默认12列
        row-height	每行的高度，默认150px
        is-draggable	是否允许拖拽布局中的单元格，默认true
        is-resizable	是否允许缩放布局中的单元格，默认true
        max-rows	定义最大行数,你把它设置成1拖拽试试就知道它的作用了
        margin	布局中单元格之间的间距，如果[10,10]
        responsive	是否是响应式布局，比如大屏下显示5列，小屏幕下将会根据屏幕大小显示多少列。默认为false
        is-mirrored	镜像反转，就是布局是从左到右还是从右到左
        auto-size	布局的容器是否自动自动大小
        vertical-compact	是否开启垂直压缩，设置true或false试试看
        prevent-collision	防止碰撞，设置为ture时，单元格只能拖动到空白处
        use-css-transforms	否使用CSS属性 transition-property: transform
        breakpoints	为响应式布局设置断点,默认为 { lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0 }，里面的单位为像素px
        cols	设置每个断点对应的列数,默认{ lg: 12, md: 10, sm: 6, xs: 4, xxs: 2 }。
        use-style-cursor	是否使用动态鼠标指针样式，当拖动出现卡顿时，将此值设为 false也许可以缓解布局问题。
        
        ---------

        grid-item属性说明
        属性名称	属性说明
        i	单元格的id,字符串类型
        x	单元格起始列
        y	单元格起始行
        w	单元格占几列
        h	单元格占几行
        min-w	单元格最小宽度占几列，缩放单元格时起作用
        min-h	单元格最小宽度占几行，缩放单元格时起作用
        max-w	单元格最大宽度占几列，缩放单元格时起作用
        max-h	单元格最大宽度占几行，缩放单元格时起作用
        is-draggable	单元格是否允许拖拽，如果为 null 取决父容器
        is-resizable	单元格是否允许缩放，如果为 null 取决父容器
        static	单元格是否是静态的，默认为false,如果是那么无法缩放、拖动、被其他元素影响
        drag-ignore-from	css 筛选器，设置那些元素无法触发拖拽事件，比如'a, button'
        drag-allow-from	css 筛选器，那些元素可以触发拖拽事件，默认为null,全部元素
        resize-ignore-from	css 筛选器，那些元素无法触发调整大小事件
    -->
        <div class="inner-div">
            <button id="lockBtn" class="lock-button" @click="lock">{{ lockText }}</button>
            <button id="changeChEn" class="chen-button" @click="changeChEn"><span v-if="CHENFLAF">{{ chenText }}</span><span
                    v-else>{{ chenTextEn }}</span></button>
            <button id="VCbtn" class="vc-button" :disabled="vcDisabled" @click="changeVC"><span
                    v-if="CHENFLAF">版本管理</span><span v-else>Versioning</span></button>
            <!-- 左侧布局 -->
            <!-- 禁止浏览器在用户拖动元素时进行平移，元素添加touch-action: none样式，这样拖动grid-item时就不会一直报错了 -->
            <div ref="leftLayout" class="left-layout" @mouseenter="moseLeftLayout">
                <div class="left-layout-box">
                    <grid-layout :prevent-collision="false" :layout.sync="layout" :col-num="2" :row-height="15">
                        <grid-item v-for="item in layout" :x="item.x" :y="item.y" :w="item.w" :h="item.h" :i="item.i"
                            :key="item.i" :is-resizable="false" style="touch-action: none;border-radius: 8px;"
                            drag-allow-from=".drag-allow-div">
                            <div class="grid-div" :id="'grid-div' + item.i" @mouseenter="gridDiv([1.2, '#00ff0d'], item.i)"
                                @mouseleave="gridDiv([1, '#ffffff'], item.i)">
                                <button v-if="item.path === 'run'" class="grid-button" @click="clinkBtn(item)">
                                    <span>
                                        {{
                                            openStart ? CHENFLAF ? item.name1 : item.nameEn1 : CHENFLAF ? item.name :
                                            item.nameEn
                                        }}
                                    </span>
                                </button>
                                <button v-else class="grid-button" @click="clinkBtn(item)">
                                    <span v-if="CHENFLAF">
                                        {{ item.name }}
                                    </span>
                                    <span v-else>
                                        {{ item.nameEn }}
                                    </span>
                                </button>
                                <div class="drag-allow-div">
                                    <!-- <span :id="'showdrag-text' + item.i">{{ '拖动' }}</span> -->
                                </div>
                            </div>
                        </grid-item>
                    </grid-layout>
                </div>
            </div>
            <!-- 路由 -->
            <router-view v-if="isRouterAlive" :CHENFLAF="CHENFLAF"></router-view>
        </div>
    </div>
</template>

<script>
export default {
    name: "main-page",
    components: {},
    provide() {
        return {
            reload: this.reload
        }
    },
    props: {
        msg: String,
    },
    data() {
        return {
            vcDisabled: false,
            CHENFLAF: true,
            chenText: "中文",
            chenTextEn: "English",
            isRouterAlive: true,
            layout: [
                { "x": 0, "y": 0, "w": 2, "h": 2, "i": "0", disabled: false, id: 'gpu', name: "使用Gpu启动", nameEn: "Booting with Gpu", path: 'run_nvidia_gpu.bat' },
                { "x": 0, "y": 0, "w": 2, "h": 2, "i": "1", disabled: false, id: 'cpu', name: "使用Cpu启动", nameEn: "Booting with Cpu", path: 'run_cpu.bat' },
                { "x": 0, "y": 0, "w": 2, "h": 2, "i": "2", name: "不启动ComfyUI", name1: "自动起ComfyUI", nameEn: "ComfyUI do not start", nameEn1: "Automatic ComfyUI", path: 'run' },
                { "x": 0, "y": 0, "w": 2, "h": 2, "i": "3", name: "启动前配置", nameEn: "Pre-startup configuration", path: '/start_config' },
                { "x": 0, "y": 0, "w": 2, "h": 2, "i": "4", name: "模型", nameEn: "model", path: '/molelsShow' },
                { "x": 0, "y": 0, "w": 2, "h": 2, "i": "5", id: "custom_node", name: "自定义节点", nameEn: "Custom node", path: '/customNode' },
                { "x": 0, "y": 0, "w": 2, "h": 2, "i": "6", id: "tools", name: "懒得起标题", nameEn: "Too lazy to title", path: '/tools' },
                { "x": 0, "y": 0, "w": 2, "h": 2, "i": "7", id: "download", name: "更新下载", nameEn: "Update download", path: '/upDownload' },
                { "x": 0, "y": 0, "w": 2, "h": 2, "i": "8", id: "home", name: "首页", nameEn: "home", path: '/' },
            ],
            time: 1000,
            isShowdragText: false,
            setTimeouter: null,
            startFlag: 0,
            gpu_id: 'gpu',
            cpu_name: 'cpu',
            isLock: false,
            lockText: '未锁',
            openStart: false,
            emoji: ['(≧∇≦)ﾉ', '(+.+)(-.-)(_ _) ..zzZZ もうだめ', 'ヾ(≧O≦)〃嗷~', '٩(๑òωó๑)۶', '( *￣▽￣)((≧︶≦*)', '（*＾-＾*）', '...(*￣０￣)ノ[等等我…]', 'n(*≧▽≦*)n', '(～o￣▽￣)～o 。。。滚来滚去……o～(＿△＿o～) ~。。。', '不＞(￣ε￣ = ￣3￣)<要', '.....((/- -)/', '-________-', '(*￣▽￣)(￣▽:;.…::;.:.:::;..::;.:...', '『家』 ～o(▽｀ o) =3 =3 =3', '＼（＾∀＾）メ（＾∀＾）ノ', '(*/ω＼*)/p.', '◕ฺ‿◕ฺ✿ฺ)', 'Ψ(￣∀￣)Ψ', '( *^-^)ρ(^0^* )', '↑↑↓↓←→←→ＢＡ...┗( -o-)┛', '（￣ー￣）ノ~~マ☆’.・.・:★', '．《{=．．．．（嘎~嘎~嘎~）'],
        };
    },
    watch: {
        time(newVal, oldVal) {
            if (newVal !== oldVal && newVal === 0) {
                this.$velocity(this.$refs.leftLayout, { opacity: 0.3, translateX: [0, [100, 10]] }, { duration: 1000 });
                this.setTimeouter && clearTimeout(this.setTimeouter);
                this.time = 1000;
            }
        }
    },
    async mounted() {
        // test TODO:
        // this.$IsHaveComfyUI = "1";

        // main
        this.$nextTick(function () {
            this.$Toast.hide()
            this.check_web_stat_timer && clearTimeout(this.check_web_stat_timer);
            this.check_web_stat(3000);
            setTimeout(async () => {
                try {
                    this.$Xwwqt.getCHEN();
                    this.$Xwwqt.check_confyui_package();
                    this.$Xwwqt.get_run_data();
                    this.$Xwwqt.getNotTips();
                } catch (error) {
                    console.log(error)
                }
                setTimeout(async () => {
                    this.CHENFLAF = this.$ChenFlag === "EN" ? false : true;
                    this.$Vc.chenflag(this.CHENFLAF);
                    this.lockText = this.CHENFLAF ? '未锁' : 'unlocked';
                    if (this.$RunStatData && this.$RunStatData == "1") {
                        this.$Xwwqt.start("run_nvidia_gpu.bat");
                        this.openStart = true;
                    } else {
                        this.openStart = false;
                    }
                    if (this.$IsHaveComfyUI && this.$IsHaveComfyUI === "1") {
                        this.getComfyuiData();
                    }
                }, 200);
                if (this.$RunStatData && this.$RunStatData == "1") {
                    this.$Xwwqt.start("run_nvidia_gpu.bat");
                    this.openStart = true;
                } else {
                    this.openStart = false;
                }
            }, 500);
        })
    },
    methods: {
        getComfyuiDataTime() {
            this.CHENFLAF = this.$ChenFlag === "EN" ? false : true;
            this.getComfyuiDataTimer && clearTimeout(this.getComfyuiDataTimer);
            this.getComfyuiDataTimer = setTimeout(() => {
                clearTimeout(this.getComfyuiDataTimer);
                // this.$Xwwqt.py_print(this.$GitFlag)
                if (this.$GitFlag && this.$GitFlag === "success") {
                    this.$Toast.show(this.CHENFLAF ? '获取完成' : 'End of data');
                } else {
                    this.tip = this.CHENFLAF ? ['正在获取自定义节点最新信息。。。', '这么慢？嗯，是有点慢。。。', '努力加载中，请稍等。。。', '国内gitHub环境就这样。。。', '有时稍微等会也是一种放松。。。'] : ['Getting updates on custom nodes... ', ' so slow? Well, a little slow... ', 'trying to load, please wait... ', ' the domestic gitHub environment is like this... ', 'sometimes waiting a little is a kind of relaxation... ']
                    this.$Toast.show(this.tip[Math.floor(Math.random() * 5)] + this.emoji[Math.floor(Math.random() * 20)]);
                    this.getComfyuiDataTime();
                }
            }, 1000);
        },
        getComfyuiData() {
            this.$Toast.show(this.CHENFLAF ? '正在获取ComfyUI版本信息，请稍等' : 'Please wait for ComfyUI version information');
            this.$Xwwqt.git_comfyui_code('');
            this.getComfyuiDataTime();
        },
        changeVC() {
            if (!this.$IsHaveComfyUI || this.$IsHaveComfyUI === "0") {
                this.$Toast.show('未发现<label style="color: red">ComfyUI_windows_portable</label>项目，如没下载过，请先下载或在左侧选项栏里找到<label style="color: blue">更新下载</label>按钮进行下载；如果你下载过但修改了包名或是自行配置的python项目本启动器将不生效，如需使用请保证你的ComfyUI项目放在<label style="color: green">ComfyUI_windows_portable</label>这个文件夹里', { time: 30000, closeBtn: true });
                return;
            }
            this.vcDisabled = true;
            setTimeout(() => {
                this.vcDisabled = false;
            }, 1000);
            this.$Vc.show();
        },
        changeChEn() {
            if (this.CHENFLAF) {
                this.$Toast.show('正在切换，请稍等');
                this.$Xwwqt.change_CHEN("EN");
            } else {
                this.$Toast.show('Switching, please wait a moment');
                this.$Xwwqt.change_CHEN("CH");
            }
            setTimeout(() => {
                // this.$Xwwqt.py_print(this.$ChenFlag)
                if (this.$ChenFlag === "error") {
                    if (this.CHENFLAF) {
                        this.$Toast.show('切换失败，请重试');
                    } else {
                        this.$Toast.show('Switchover failed, please try again');
                    }
                } else {
                    this.CHENFLAF = this.$ChenFlag === "EN" ? false : true;
                    if (this.isLock) {
                        this.lockText = this.CHENFLAF ? '已锁' : 'LOCK';
                    } else {
                        this.lockText = this.CHENFLAF ? '未锁' : 'unlocked';
                    }
                }
                this.$Vc.chenflag(this.CHENFLAF);
            }, 1000);
        },
        lock() {
            this.isLock = !this.isLock;
            let btn = document.getElementById('lockBtn');
            if (this.isLock) {
                this.lockText = this.CHENFLAF ? '已锁' : 'LOCK';
                btn.style.color = 'red';
            } else {
                this.lockText = this.CHENFLAF ? '未锁' : 'unlocked';
                btn.style.color = '#55ff00';
            }
        },
        reload() {
            this.isRouterAlive = false
            this.$nextTick(function () {
                this.isRouterAlive = true
            })
        },
        setTimeout() {
            this.setTimeouter && clearTimeout(this.setTimeouter);
            this.setTimeouter = setTimeout(() => {
                this.time = 0;
                clearTimeout(this.setTimeouter);
            }, this.time);
        },
        moseLeftLayout() {
            if (this.isLock) {
                return;
            }
            this.$velocity(this.$refs.leftLayout, { opacity: 1, translateX: [100, [100, 10]] }, { duration: 800 });
            this.setTimeout();
        },
        gridDiv(v, i) {
            if (this.isLock) {
                return;
            }
            let gd = document.getElementById('grid-div' + i);
            let gdbtn = gd.querySelector('button');
            // gd.style.scale = v[0];
            // gdbtn.style.color = v[1];
            this.$velocity(gd, "finish");
            this.$velocity(gdbtn, "finish");
            this.$velocity(gd, { scale: v[0] }, { duration: 200 });
            this.$velocity(gdbtn, { color: v[1] }, { duration: 200 });
            if (v[0] === 1) {
                this.setTimeout();
            } else {
                this.time = 1000;
                this.setTimeouter && clearTimeout(this.setTimeouter);
            }

        },
        async clinkBtn(item) {
            this.$Vc.hide();
            this.$Toast.hide()
            if (this.isLock) {
                return;
            }
            if ((!this.$IsHaveComfyUI || this.$IsHaveComfyUI === "0") && item.id !== "download" && item.id !== "home") {
                this.$Toast.show('未发现<label style="color: red">ComfyUI_windows_portable</label>项目，如没下载过，请先下载或在左侧选项栏里找到<label style="color: blue">更新下载</label>按钮进行下载；如果你下载过但修改了包名或是自行配置的python项目本启动器将不生效，如需使用请保证你的ComfyUI项目放在<label style="color: green">ComfyUI_windows_portable</label>这个文件夹里', { time: 30000, closeBtn: true });
                return;
            }
            let path = item.path;
            if (item.id && (item.id === "gpu" || item.id === "cpu")) {
                let text = '已在启动中，请勿重复点击。。。';
                if (!this.CHENFLAF) {
                    text = 'Already being started, Do not click repeatedly...'
                }
                if (this.startFlag === 1) {
                    this.$Toast.show(text);
                    return;
                }
                this.check_web_stat_timer && clearTimeout(this.check_web_stat_timer);
                this.startFlag = 1;
                // 给qt发送启动指令
                this.$Xwwqt.start(path);
                // 检查状态
                this.check_web_stat(1000);
                this.clicksetTimeouter = setTimeout(() => {
                    this.startFlag = 0;
                    clearTimeout(this.clicksetTimeouter);
                }, 5000);
                return;
            }
            if (path === 'run') {
                if (this.$RunStatData && this.$RunStatData == "1") {
                    this.$Xwwqt.run_stat("0");
                } else {
                    this.$Xwwqt.run_stat("1");
                }
                setTimeout(async () => {
                    if (this.$RunStatData && this.$RunStatData == "1") {
                        this.$Toast.show(this.CHENFLAF ? "下次打开启动器时自动使用GPU模式启动ComfyUI" : "The next time you open the initiator, ComfyUI is automatically started in GPU mode", { time: 10000, closeBtn: true });
                        this.openStart = true;
                    } else {
                        this.$Toast.show(this.CHENFLAF ? "下次打开启动器时不会自动启动ComfyUI" : "ComfyUI will not start automatically the next time you open the initiator", { time: 10000, closeBtn: true });
                        this.openStart = false;
                    }
                }, 400);
                return;
            }
            if (path === this.$route.path) {
                // 如果已经在当前页面，则不做跳转，注意，这里使用的是$route，和$router不是同一个
                return;
            }
            this.$router.push({ path: path });
        },
        setLayoutdisable(name_list, v) {
            let gtext = "使用Gpu启动"
            let ctext = "使用Cpu启动"
            let grtext = "使用Gpu重启"
            let crtext = "使用Cpu重启"
            if (!this.CHENFLAF) {
                gtext = "Booting with Gpu"
                ctext = "Booting with Cpu"
                grtext = "Restart using Gpu"
                crtext = "Restart using Cpu"
            }
            for (let i = 0; i < this.layout.length; i++) {
                for (let j = 0; j < name_list.length; j++) {
                    if (this.layout[i].id == name_list[j]) {
                        this.layout[i].disabled = v;
                        if (v) {
                            this.layout[i].name = this.layout[i].id === 'gpu' ? grtext : crtext;
                        } else if (this.layout[i].id === 'gpu') {
                            this.layout[i].name = gtext;
                        } else if (this.layout[i].id === 'cpu') {
                            this.layout[i].name = ctext;
                        }
                    }
                }
            }
        },
        async check_web_stat(t) {
            this.check_web_stat_timer = setTimeout(async () => {
                try {
                    if (this.$IsHaveComfyUI && this.$IsHaveComfyUI === "1") {
                        // 设置按钮状态 不清楚为何qt那边调用js的fetch时一直无法连接，所以这里只能在qt那边去检查url是否可以访问，再根据qt返回的信号字段判断服务是否已起成功
                        this.$Xwwqt.check_url('http://127.0.0.1:8188/');
                        let xwwsignal = this.$Xwwsignal && JSON.parse(this.$Xwwsignal);
                        let runStat = xwwsignal.stat === '0' ? true : false;
                        this.setLayoutdisable([this.gpu_id, this.cpu_name], runStat)
                    }
                } catch (error) {
                    console.log(error)
                }
                this.check_web_stat(3000);
            }, t);
        }
    },
};
</script>
<style scoped>
#main-page {
    width: 100%;
    height: 96vh;
    position: relative;
    overflow: hidden;
}

.lock-button {
    position: fixed;
    top: 0;
    left: 140px;
    z-index: 999;
    /* width: 30px; */
    /* height: 30px; */
    color: #55ff00;
    border-radius: 10px;
    text-align: center;
    opacity: 0.3;
    transform-origin: top center;
    background-image: linear-gradient(to right, rgb(0, 0, 0), rgb(255, 255, 255));
}

.lock-button:hover {
    transform: scale(1.3);
    opacity: 1;
}

.vc-button {
    position: fixed;
    top: 0;
    right: 10px;
    z-index: 999;
    /* width: 30px; */
    /* height: 30px; */
    color: #55ff00;
    border-radius: 10px;
    text-align: center;
    opacity: 0.3;
    transform-origin: top center;
    background-image: linear-gradient(to left, rgb(0, 0, 0), rgb(255, 255, 255));
}

.vc-button:hover {
    transform: scale(1.3);
    opacity: 1;
}

.chen-button {
    position: fixed;
    top: 0;
    left: 220px;
    z-index: 999;
    /* width: 30px; */
    /* height: 30px; */
    color: #55ff00;
    border-radius: 10px;
    text-align: center;
    opacity: 0.3;
    transform-origin: top center;
    background-image: linear-gradient(to right, rgb(0, 0, 0), rgb(255, 255, 255));
}

.chen-button:hover {
    transform: scale(1.3);
    opacity: 1;
}


.inner-div {
    position: absolute;
    left: 0;
    top: 0;
    right: -17px;
    bottom: 0;
    overflow-x: hidden;
    overflow-y: scroll;
}

.left-layout {
    position: fixed;
    display: flex;
    flex-direction: row-reverse;
    top: 0;
    z-index: 999;
    left: -180px;
    width: 200px;
    opacity: 0.3;
    /* background-color: aquamarine; */
}

.left-layout-box {
    position: relative;
    right: 0;
    width: 120px;
    /* background-color: aquamarine; */
}

.drag-allow-div {
    display: flex;
    flex-direction: row-reverse;
    justify-content: flex-end;
    width: 10%;
    height: 100%;
    display: 1;
    border-end-end-radius: 8px;
    /* background-color: #282222; */
    transform-origin: bottom center;
}

.drag-allow-div span {
    color: #ffffff;
    margin-top: 5px;
    font-size: 12px;
    /* text-align: right; */
}

.grid-div {
    display: flex;
    /* justify-content: center; */
    flex-direction: row-reverse;
    width: 100%;
    height: 100%;
    text-align: center;
    align-items: center;
    color: black;
    border-radius: 8px;
    background-image: linear-gradient(to right, rgb(7, 7, 7), rgb(244, 10, 10));
    transform-origin: left center;
}

.grid-button:hover {
    background-image: linear-gradient(to right, rgb(0, 0, 0), rgb(150, 147, 147));
}

.grid-button {
    width: 90%;
    height: 100%;
    font-size: 14px;
    color: #ffffff;
    border-radius: 8px;
    opacity: 1;
    background-image: linear-gradient(to right, rgb(0, 0, 0), rgb(255, 255, 255));
}

.vue-grid-layout {
    color: red;
    padding-right: 6px;
    cursor: pointer;

}

.vue-grid-item {
    touch-action: none;
}

.vue-grid-item:not(.vue-grid-placeholder) {
    /* background-color: rgba(0, 0, 0, 0);
    border: 1px solid black;
    border-radius: 8px; */
    /* touch-action: none; */
    border-radius: 8px;
}

.vue-grid-item .resizing {
    opacity: 0.9;
}

.vue-grid-item .static {
    background: #cce;
}

.vue-grid-item .text {
    font-size: 24px;
    text-align: center;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
    height: 100%;
    width: 100%;
}

.vue-grid-item .no-drag {
    height: 100%;
    width: 100%;
}

.vue-grid-item .minMax {
    font-size: 12px;
}

.vue-grid-item .add {
    cursor: pointer;
}

.vue-draggable-handle {
    position: absolute;
    width: 20px;
    height: 20px;
    top: 0;
    left: 0;
    padding: 0 8px 8px 0;
    background-repeat: no-repeat;
    background-origin: content-box;
    box-sizing: border-box;
    cursor: pointer;
}
</style>