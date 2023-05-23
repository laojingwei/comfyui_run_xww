<template>
    <show-page>
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
        <div class="more-select-div">
            <div class="img-tip" v-if="this.modelsName" @click="moreaddshow()">
                <div>
                    <span v-if="CHENFLAF">
                        名称：
                    </span>
                    <span v-else>
                        name
                    </span>
                    {{ this.modelsName }}
                </div>
                <div>
                    <span v-if="CHENFLAF">
                        models路径：
                    </span>
                    <span v-else>
                        models Path:
                    </span>
                    {{ this.modelsPath }}
                </div>
                <div>
                    <span v-if="CHENFLAF">
                        图片路径：
                    </span>
                    <span v-else>
                        Picture path:
                    </span>
                    {{ this.imgPath }}
                </div>
            </div>
            <div ref="safeTip" class="safe-tip" @click="moreaddshow()">
                <span v-if="CHENFLAF">
                    ！如果你使用本脚本打开本地具体某个文件时，系统安全软件提示阻止，请点击同意；因为有些安全软件会检测某些应用去使用本地数据行为，本脚本所有操作行为均为安全操作，不涉及任何危险行为，请放心使用
                </span>
                <span v-else>
                    ! If you use this script to open a specific local file, the system security software prompts to block,
                    please click agree; Because some security software will detect the use of local data by some
                    applications, all operations of this script are safe operations and do not involve any dangerous
                    behaviors. Please feel free to use it
                </span>
                <button ref="noTips" @click="noTips">
                    <span v-if="CHENFLAF">
                        不再提示
                    </span>
                    <span v-else>
                        No more prompt
                    </span>
                </button>
            </div>
            <div class="select-layout" @click="moreaddshow()">
                <grid-layout :prevent-collision="false" :layout.sync="typtList" :col-num="12" :row-height="30">
                    <grid-item v-for="item in typtList" :x="item.x" :y="item.y" :w="item.w" :h="item.h" :i="item.i"
                        :key="item.i" :is-resizable="false" style="touch-action: none;box-sizing: border-box"
                        drag-allow-from=".grid-item-div-move">
                        <div class="grid-item-div-select">
                            <div class="grid-item-div-move"></div>
                            <button :id="item.name + item.i" class="grid-item-div-name" @click="clickItem(item)">{{
                                setStrLen(item.name, 20) }}</button>
                        </div>
                    </grid-item>
                </grid-layout>
            </div>
            <div class="util-class" @click="moreaddshow()">
                <button @click="reSort(0)">
                    <span v-if="CHENFLAF">
                        重置类型
                    </span>
                    <span v-else>
                        Reset type
                    </span>
                    <span class="span">↑</span></button>
                <button @click="reSort(1)">
                    <span v-if="CHENFLAF">
                        重置图片
                    </span>
                    <span v-else>
                        Reset picture
                    </span>
                    <span class="span">↓</span></button>
                <button @click="openLocalDir(localDirPath)">
                    <span v-if="CHENFLAF">
                        打开文件夹
                    </span>
                    <span v-else>
                        Open Folder
                    </span>
                </button>
                <button @click="openLocalDir('output')">
                    <span v-if="CHENFLAF">
                        打开生成图片文件夹
                    </span>
                    <span v-else>
                        Open the Generate Img folder
                    </span>
                </button>
                <button @click="save_data" @mouseenter="saveToast($event, 1)" @mouseleave="saveToast($event, 0)">
                    <span v-if="CHENFLAF">
                        记住排序更改
                    </span>
                    <span v-else>
                        Remember sort changes
                    </span>
                </button>
                <button @click="clear_save_data" @mouseenter="clearToast($event, 1)" @mouseleave="clearToast($event, 0)">
                    <span v-if="CHENFLAF">
                        清空排序更改
                    </span>
                    <span v-else>
                        Clear sort changes
                    </span>
                </button>
                <button @click="reloadPage">
                    <span v-if="CHENFLAF">
                        刷新页面
                    </span>
                    <span v-else>
                        refresh the page
                    </span>
                </button>
            </div>
            <div class="image-layout" @click="moreaddshow()">
                <!-- <button @click="zipImg">压缩图片</button>
                <button @click="addItem">添加单元格</button> -->
                <grid-layout :prevent-collision="false" :layout.sync="layout" :col-num="12" :row-height="30"
                    :margin="[15, 15]" :vertical-compact="true">
                    <grid-item v-for="(item, key) in layout" :x="item.x" :y="item.y" :w="item.w" :h="item.h" :i="item.i"
                        :key="item.i" style="touch-action: none;box-sizing: border-box" :static="item.static"
                        drag-ignore-from=".change-img">
                        <div class="grid-item-div">
                            <img v-if="item.static" class="lock-img" src="@/assets/lock.png"
                                @mouseenter="showLockText($event, 1)" @mouseleave="showLockText($event)"
                                @click="lockImgClick(false, key)" />
                            <img v-else class="lock-img" src="@/assets/nolock.png" @mouseenter="showLockText($event, 1)"
                                @mouseleave="showLockText($event)" @click="lockImgClick(true, key)" />
                            <span class="grid-item-span">
                                <button class="grid-item-span-btn" @click="openLocalFile(item)"
                                    @mouseenter="showOpenText($event, 1)" @mouseleave="showOpenText($event)">i</button>
                                <span @mouseenter="showTipText(item)" @mouseleave="hideTipText()">
                                    {{
                                        setStrLen(item.models_name, 20)
                                    }}
                                </span>
                            </span>
                            <img class="change-img" src="@/assets/img-change.png" @mouseenter="showCimgText($event, 1)"
                                @mouseleave="showCimgText($event)" @click="changeImg(item, key)" />
                            <img class="grid-item-img" v-bind:src="'data:image/jpge;base64,' + item.base64" />
                        </div>
                    </grid-item>
                </grid-layout>

                <div class="empty-div"></div>
            </div>

            <!-- 模型添加 -->
            <div ref="addBtn" class="center-div">
                <button class="add-btn show-btn" @click="moreaddshow(1)">{{ CHENFLAF ? '添加模型' : 'Add Model' }}</button>
            </div>
            <div ref="moreAddDiv" class="more-add-div">
                <div class="search-div">
                    <input type="text" v-model="searchValue"
                        :placeholder="CHENFLAF ? '模型太多不好找？试试输入内容精确查找吧' : 'Too many model to find? Try entering content for precise search.'">
                    <button class="show-btn clear-btn" @click="clear">{{ CHENFLAF ? '清空' : 'clear' }}</button>
                    <button class="show-btn" @click="moreaddshow()">{{ CHENFLAF ? '关闭' : 'close' }}</button>
                </div>
                <div class="more-add-show-tab" v-for="(item, i) in addModelList" :key="i + 'tab'">
                    <button :class="selectModelIndex == i ? 'more-add-tab select-bg' : 'more-add-tab'"
                        @click="click_add_tab(i)">{{ i }}</button>
                </div>
                <div ref="moreAddModel" class="more-add-show-detail" v-if="selectModelIndex">
                    <div class="detail-div-title">
                        <div class="detail-div-div">
                            {{ CHENFLAF ? '模型名称' : 'Model name' }}
                        </div>
                        <div class="detail-div-div">
                            {{ CHENFLAF ? '作者/发布者' : 'Author/publisher' }}
                        </div>
                        <div class="detail-div-div">
                            {{ CHENFLAF ? '最后修改时间' : 'Last modified time' }}
                        </div>
                        <div class="detail-div-div">
                            {{ CHENFLAF ? '大小' : 'Size' }}
                        </div>
                        <div class="detail-div-div">
                            {{ CHENFLAF ? '操作' : 'execute' }}
                        </div>
                    </div>
                    <div class="detail-div" v-for="(item_sub, k) in addModelList[selectModelIndex]" :key="k + 'detalis'"
                        :ref="k + refEnd">
                        <div class="detail-div-div">
                            <div v-html="item_sub.name"></div>
                        </div>
                        <div class="detail-div-div">
                            <div v-html="item_sub.author"></div>
                        </div>
                        <div class="detail-div-div">
                            {{ format_time(item_sub.lastModified) }}
                        </div>
                        <div class="detail-div-div">
                            {{ item_sub.size }}
                        </div>
                        <div class="detail-div-div">
                            <button v-if="item_sub.installed && item_sub.installed == 1" :ref="k + refEnd + 'btn'"
                                :disabled="true" :style="'background-color:#787878;color:#000000;'">
                                {{
                                    CHENFLAF ? '已安装' : 'Installed'
                                }}
                            </button>
                            <button v-else :ref="k + refEnd + 'btn'" @click="downloadModel(item_sub, k + refEnd + 'btn')">
                                {{
                                    CHENFLAF ? '安装' : 'Install'
                                }}
                            </button>
                        </div>
                    </div>
                    <div class="empty-div"></div>
                </div>
            </div>
        </div>
    </show-page>
</template>

<script>

export default {
    inject: ['reload'],
    name: "HelloWorld",
    props: {
        CHENFLAF: {
            type: Boolean,
            default: true,
        },
    },
    data() {
        return {
            typtList: [],
            saveTypeList: [],
            baseTyptList: { "x": 0, "y": 0, "w": 2, "h": 1, "i": "0", name: '' },
            layout: [],
            saveLayout: [],
            baseLayout: { "x": 0, "y": 0, "w": 2, "h": 3, "i": "0", base64: "", static: false },
            addModelList: [],
            addModelListBk: [],
            selectModelIndex: "checkpoints",
            index: 0,
            isSelectBtn: '',
            isSelectName: '',
            modelsName: '',
            modelsPath: '',
            imgPath: '',
            localDirPath: '',
            searchValue: '',
            refEnd: 'moreAddModel',
            emoji: ['(≧∇≦)ﾉ', '(+.+)(-.-)(_ _) ..zzZZ もうだめ', 'ヾ(≧O≦)〃嗷~', '٩(๑òωó๑)۶', '( *￣▽￣)((≧︶≦*)', '（*＾-＾*）', '...(*￣０￣)ノ[等等我…]', 'n(*≧▽≦*)n', '(～o￣▽￣)～o 。。。滚来滚去……o～(＿△＿o～) ~。。。', '不＞(￣ε￣ = ￣3￣)<要', '.....((/- -)/', '-________-', '(*￣▽￣)(￣▽:;.…::;.:.:::;..::;.:...', '『家』 ～o(▽｀ o) =3 =3 =3', '＼（＾∀＾）メ（＾∀＾）ノ', '(*/ω＼*)/p.', '◕ฺ‿◕ฺ✿ฺ)', 'Ψ(￣∀￣)Ψ', '( *^-^)ρ(^0^* )', '↑↑↓↓←→←→ＢＡ...┗( -o-)┛', '（￣ー￣）ノ~~マ☆’.・.・:★', '．《{=．．．．（嘎~嘎~嘎~）'],

        };
    },
    watch: {
        searchValue() {
            if (this.searchValue && this.searchValue.length > 0) {
                this.search();
            } else {
                this.addModelList = JSON.parse(JSON.stringify(this.addModelListBk))
            }
        }
    },
    filters: {
        // formatTime(time) {
        //     if (!time) {
        //         return "--";
        //     }
        //     return this.format_time(time);
        // },
    },
    mounted() {
        // this.ciBase64 = this.$ChangeImgBase64 || '';

        // test TODO:
        // let x = 0;
        // let y = 0;
        // let bl = this.baseTyptList;
        // for (let i = 0; i < 10; i++) {
        //     bl["i"] = i;
        //     bl["name"] = i;
        //     if (x < 12) {
        //         bl["x"] = x;
        //         x = x + 2;
        //     } else {
        //         x = 0;
        //         bl["x"] = x;
        //         x = x + 2;
        //         y = y + 1;
        //     }
        //     bl["y"] = y;
        //     this.typtList.push({ ...bl })
        // }

        // let x1 = 0;
        // let y1 = 0;
        // let bl1 = this.baseLayout;
        // for (let i = 0; i < 50; i++) {
        //     bl1["i"] = i;
        //     bl1["name"] = i;
        //     if (x1 < 12) {
        //         bl1["x"] = x1;
        //         x1 = x1 + 2;
        //     } else {
        //         x1 = 0;
        //         bl1["x"] = x1;
        //         x1 = x1 + 2;
        //         y1 = y1 + 3;
        //     }
        //     bl1["y"] = y;
        //     this.layout.push({ ...bl1 })
        // }
        // this.saveTypeList = JSON.parse(JSON.stringify(this.typtList))
        // this.saveLayout = JSON.parse(JSON.stringify(this.layout))
        // this.getAddModel();

        // main
        if (!this.$NotTipsFlag) {
            this.$velocity(this.$refs.safeTip, {
                opacity: 1, height: 50,
            }, { duration: 2000, delay: 5000 });
            this.$velocity(this.$refs.safeTip, {
                opacity: 0, height: 0,
            }, { duration: 2000, delay: 60000 });
            this.$velocity(this.$refs.noTips, {
                opacity: 1,
            }, { duration: 2000, delay: 20000 });
        }
        this.index = this.layout.length;
        this.$Xwwqt.get_models_data();
        this.$Xwwqt.get_save_data('moreselect.json');
        this.$Xwwqt.get_add_models_data();
        this.init();
    },
    methods: {
        downloadModelTime(refName) {
            try {
                this[refName] && clearTimeout(this[refName]);
                this[refName] = setTimeout(() => {
                    clearTimeout(this[refName]);
                    if (this.$DownloadModelFlag && this.$DownloadModelFlag === refName + "#-#success") {
                        this.$Toast.show(this.CHENFLAF ? '安装成功' : 'Install successfully', 3000);
                        if (this.$refs[refName] && this.$refs[refName][0]) {
                            this.$refs[refName][0].innerText = this.CHENFLAF ? "已安装" : "Installed";
                        }
                    } else if (this.$DownloadModelFlag && this.$DownloadModelFlag === refName + "#-#error") {
                        if (this.$refs[refName] && this.$refs[refName][0]) {
                            this.$refs[refName][0].disabled = false;
                            this.$refs[refName][0].innerText = this.CHENFLAF ? "安装" : "Install";
                            this.$refs[refName][0].style.backgroundColor = "";
                            this.$refs[refName][0].style.color = "";
                        }
                        this.$Toast.show(this.CHENFLAF ? '安装失败' : 'Installation failed', 3000);
                    } else {
                        this.$Toast.show(this.CHENFLAF ? `正在安装中，请耐心等待。。。${this.emoji[Math.floor(Math.random() * 20)]}` : `Installation underway, please be patient...${this.emoji[Math.floor(Math.random() * 20)]}`);
                        this.downloadModelTime(refName);
                    }
                }, 1000);

            } catch (error) {
                console.log(error);
            }
        },
        downloadModel(item, refName) {
            let url = item.url;
            if (url) {
                this.$Toast.show(this.CHENFLAF ? '正在安装中，请耐心等待。。。' : 'Installation underway, please be patient...');
                if (this.$refs[refName] && this.$refs[refName][0]) {
                    this.$refs[refName][0].disabled = true;
                    this.$refs[refName][0].innerText = this.CHENFLAF ? "安装中..." : "Installation in progress";
                    this.$refs[refName][0].style.backgroundColor = "#787878";
                    this.$refs[refName][0].style.color = "#000000";
                }
                this.$Xwwqt.downloadModel([{ url: url, typ: this.selectModelIndex, path: "", emitValue: refName }]);
                this.downloadModelTime(refName);
            }
        },
        more_add_model_time() {
            this.more_add_model_timer = setTimeout(() => {
                clearTimeout(this.customNodeLinkTimer);
                // this.$Xwwqt.py_print(JSON.stringify(this.$AddModelList))
                if (this.$AddModelList) {
                    let list = [];
                    this.$AddModelList[0] && (list = this.$AddModelList[0]);
                    this.addModelList = list;
                    this.addModelList && (this.addModelListBk = JSON.parse(JSON.stringify(this.addModelList)))
                } else {
                    this.more_add_model_time();
                }
            }, 500);
        },
        click_add_tab(i) {
            this.selectModelIndex = i;
            this.clear();
        },
        clear() {
            this.searchValue = "";
        },
        search() {
            if (this.searchValue && this.addModelList) {
                let reg = new RegExp(this.searchValue, "gi")
                this.addModelList = JSON.parse(JSON.stringify(this.addModelListBk));
                let list = this.addModelList[this.selectModelIndex];
                let list1 = [];
                for (let i = 0; i < list.length; i++) {
                    let name = list[i].name;
                    let author = list[i].author;
                    let m = 0;
                    if (name.match(reg)) {
                        list[i].name = name.replace(reg, function (match) {
                            return `<span style="background-color: #55ff00;">${match}</span>`;
                        });
                        m = 1;
                    }
                    if (author.match(reg)) {
                        list[i].author = author.replace(reg, function (match) {
                            return `<span style="background-color: #55ff00;">${match}</span>`;
                        });
                        m = 1;
                    }
                    if (m == 1) {
                        list1.push(list[i])
                    }
                }
                this.addModelList[this.selectModelIndex] = list1;
            }
        },
        moreaddshow(i) {
            if (!i) {
                if (this.$refs.moreAddDiv.style.opacity == 1) {
                    this.$refs.addBtn.style.display = "inline-flex";
                    this.$velocity(this.$refs.moreAddDiv, { opacity: 1, translateY: '-90vh' }, { duration: 50 });
                    this.$velocity(this.$refs.moreAddDiv, { opacity: 0, translateY: '90vh' }, { duration: 1000, delay: 100 });
                }
            } else if (this.$refs.moreAddDiv.style.opacity == 1) {
                this.$refs.addBtn.style.display = "inline-flex";
                this.$velocity(this.$refs.moreAddDiv, { opacity: 1, translateY: '-90vh' }, { duration: 50 });
                this.$velocity(this.$refs.moreAddDiv, { opacity: 0, translateY: '90vh' }, { duration: 1000, delay: 100 });
            } else {
                this.$refs.addBtn.style.display = "none";
                this.$velocity(this.$refs.moreAddDiv, { opacity: 0, translateY: '90vh' }, { duration: 50 });
                this.$velocity(this.$refs.moreAddDiv, { opacity: 1, translateY: '-90vh' }, { duration: 1000, delay: 100 });
            }
        },
        format_time(time) {
            if (!time) {
                return "--";
            }
            if (this.CHENFLAF) {
                let timeFormat = this.$Com.format_time(time);
                return timeFormat;
            } else {
                return time;
            }
        },
        getAddModel() {
            let list = [{ 'checkpoints': [{ 'author': 'yehiaserag', 'lastModified': 'Sat, 03 Dec 2022 04:19:12 GMT', 'name': 'anime-pencil-diffusion-v1.ckpt', 'size': '3.8166 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/yehiaserag/anime-pencil-diffusion/resolve/b52ffef86adeaa55ecb75017ec6be9adcb1bff59/anime-pencil-diffusion-v1.ckpt' }, { 'author': 'yehiaserag', 'lastModified': 'Sat, 03 Dec 2022 08:58:54 GMT', 'name': 'anime-pencil-diffusion-v2.ckpt', 'size': '3.8166 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/yehiaserag/anime-pencil-diffusion/resolve/b52ffef86adeaa55ecb75017ec6be9adcb1bff59/anime-pencil-diffusion-v2.ckpt' }, { 'author': 'swl-models?', 'lastModified': 'Fri, 30 Dec 2022 16:16:50 GMT', 'name': 'anything-V2.1-pruned-bf16.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/anything-v2.1/resolve/main/anything-V2.1-pruned-bf16.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Mon, 27 Mar 2023 01:47:12 GMT', 'name': 'Anything-v3.0-For-Tachie.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/Anything-v3.0-For-Tachie/resolve/153fe4da2aca45bea3adb59249db91367f3ac9c8/Anything-v3.0-For-Tachie.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Tue, 31 Jan 2023 13:47:34 GMT', 'name': 'Anything-V3.0-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/anything-v3.0/resolve/727ab3550690ab8cfefc2daccc2b57bb86ff9d8e/Anything-V3.0-non-ema-fp32.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Wed, 01 Feb 2023 01:05:57 GMT', 'name': 'Anything-V3.0.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/anything-v3.0/resolve/727ab3550690ab8cfefc2daccc2b57bb86ff9d8e/Anything-V3.0.safetensors' }, { 'author': 'andite', 'lastModified': 'Fri, 13 Jan 2023 14:41:43 GMT', 'name': 'anything-v4.0-pruned-fp16.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/andite/anything-v4.0/resolve/8eb1055fba5a23bf1b60d52cdc620f84b25ca054/anything-v4.0-pruned-fp16.safetensors' }, { 'author': 'andite', 'lastModified': 'Fri, 13 Jan 2023 14:28:23 GMT', 'name': 'anything-v4.0.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/andite/anything-v4.0/resolve/main/anything-v4.0.ckpt' }, { 'author': 'andite', 'lastModified': 'Sun, 15 Jan 2023 15:15:53 GMT', 'name': 'anything-v4.5-pruned-fp16.ckpt', 'size': '1.9864 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/andite/anything-v4.0/resolve/8eb1055fba5a23bf1b60d52cdc620f84b25ca054/anything-v4.5-pruned-fp16.ckpt' }, { 'author': 'andite', 'lastModified': 'Fri, 13 Jan 2023 18:14:00 GMT', 'name': 'anything-v4.5-pruned.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/andite/anything-v4.0/resolve/main/anything-v4.5-pruned.ckpt' }, { 'author': 'andite', 'lastModified': 'Fri, 13 Jan 2023 19:48:36 GMT', 'name': 'anything-v4.5-pruned.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/andite/anything-v4.0/resolve/main/anything-v4.5-pruned.safetensors' }, { 'author': 'andite', 'lastModified': 'Sun, 15 Jan 2023 15:05:00 GMT', 'name': 'anything-v4.5.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/andite/anything-v4.0/resolve/8eb1055fba5a23bf1b60d52cdc620f84b25ca054/anything-v4.5.ckpt' }, { 'author': 'swl-models?', 'lastModified': 'Tue, 28 Mar 2023 02:57:50 GMT', 'name': 'Anything-v5.0-PRT-RE.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/Anything-v5.0-PRT/resolve/8f4143c96d5a9a9869061b5c3ea71a1d962790be/Anything-v5.0-PRT-RE.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Mon, 27 Mar 2023 04:10:07 GMT', 'name': 'Anything-v5.0-PRT.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/Anything-v5.0-PRT/resolve/8f4143c96d5a9a9869061b5c3ea71a1d962790be/Anything-v5.0-PRT.safetensors' }, { 'author': 'Crosstyan', 'lastModified': 'Tue, 20 Dec 2022 19:13:03 GMT', 'name': 'bp_1024_with_vae_te.ckpt', 'size': '2.1422 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/Crosstyan/BPModel/resolve/dea2172f2fa1858444b14cc948c8cf0146592604/bp_1024_with_vae_te.ckpt' }, { 'author': 'EK12317', 'lastModified': 'Tue, 17 Jan 2023 10:53:07 GMT', 'name': 'Ekmix-gen3-fp16-pruned.safetensors', 'size': '1.6011 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/a650b7f46ea7249de8e810bca945186c324dbd08/Ekmix-gen3-fp16-pruned.safetensors' }, { 'author': 'EK12317', 'lastModified': 'Sun, 18 Dec 2022 09:38:57 GMT', 'name': 'Ekmix-gen3.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/e8489459acdfdbbd52ec5be5d9277748c2ad7d4e/Ekmix-gen3.ckpt' }, { 'author': 'EK12317', 'lastModified': 'Sun, 22 Jan 2023 03:00:02 GMT', 'name': 'Ekmix-gen4.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/31fae1bf719fe6c58b847bb9b1f1d6ff5b6f0bf3/Ekmix-gen4.ckpt' }, { 'author': 'nitrosocke', 'lastModified': 'Wed, 05 Oct 2022 23:03:18 GMT', 'name': 'eldenring-v1-pruned.ckpt', 'size': '1.9864 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/nitrosocke/elden-ring-diffusion/resolve/240e4f59150a998492ab41c8233c535084d64377/eldenring-v1-pruned.ckpt' }, { 'author': 'nitrosocke', 'lastModified': 'Sat, 22 Oct 2022 12:53:53 GMT', 'name': 'eldenring-v2-pruned.ckpt', 'size': '1.9864 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/nitrosocke/elden-ring-diffusion/resolve/240e4f59150a998492ab41c8233c535084d64377/eldenring-v2-pruned.ckpt' }, { 'author': 'nitrosocke', 'lastModified': 'Tue, 01 Nov 2022 15:09:44 GMT', 'name': 'eldenRing-v3-pruned.ckpt', 'size': '1.9864 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/nitrosocke/elden-ring-diffusion/resolve/240e4f59150a998492ab41c8233c535084d64377/eldenRing-v3-pruned.ckpt' }, { 'author': 'haor', 'lastModified': 'Sun, 20 Nov 2022 21:37:43 GMT', 'name': 'evt_v2-ema-pruned.ckpt', 'size': '2.3714 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/haor/Evt_V2/resolve/main/evt_v2-ema-pruned.ckpt' }, { 'author': 'haor', 'lastModified': 'Sat, 26 Nov 2022 14:18:31 GMT', 'name': 'Evt_V3_ema.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/haor/Evt_V3/resolve/main/Evt_V3_ema.ckpt' }, { 'author': 'xiaolxl', 'lastModified': 'Thu, 02 Feb 2023 00:35:28 GMT', 'name': 'GuoFeng3_Fix-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v3-fix/resolve/4d11f5b8470f73140ee45d78d6fa4e5d4bc911bf/GuoFeng3_Fix-non-ema-bf16.safetensors' }, { 'author': 'hans', 'lastModified': 'Wed, 01 Feb 2023 07:32:03 GMT', 'name': 'hans-v4.4-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/hans-v4.4/resolve/568deba7c897575e98ab659788f7f7f68aa21aae/hans-v4.4-ema-fp32.safetensors' }, { 'author': 'MeinaMix', 'lastModified': 'Fri, 14 Apr 2023 14:11:33 GMT', 'name': 'Meina V8 baked VAE.safetensors', 'size': '3.2185 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MeinaMix/resolve/478e265654aedb91c246cb2e84faa57b5619ea27/Meina V8 baked VAE.safetensors' }, { 'author': 'andite', 'lastModified': 'Tue, 24 Jan 2023 19:03:56 GMT', 'name': 'pastelmix-fp16.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/andite/pastel-mix/resolve/7f691d69c0a348b183f15630005ec96b672458ed/pastelmix-fp16.safetensors' }, { 'author': 'MistyOrange', 'lastModified': 'Sun, 26 Feb 2023 08:31:13 GMT', 'name': 'MistyOrange-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MistyOrange/resolve/bb5747bd502be81824a7dee0bc47caf0745ebaf6/MistyOrange-non-ema-fp16.safetensors' }, { 'author': 'MistyOrange', 'lastModified': 'Sun, 26 Feb 2023 08:31:13 GMT', 'name': 'MistyOrange.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MistyOrange/resolve/bb5747bd502be81824a7dee0bc47caf0745ebaf6/MistyOrange.safetensors' }, { 'author': 'runwayml', 'lastModified': 'Mon, 17 Oct 2022 02:54:53 GMT', 'name': 'sd-v1-5-inpainting.ckpt', 'size': '3.9725 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/runwayml/stable-diffusion-inpainting/resolve/caac1048f28756b68042add4670bec6f4ae314f8/sd-v1-5-inpainting.ckpt' }, { 'author': 'runwayml', 'lastModified': 'Thu, 20 Oct 2022 00:39:45 GMT', 'name': 'v1-5-pruned-emaonly.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt' }, { 'author': 'runwayml', 'lastModified': 'Thu, 20 Oct 2022 12:04:48 GMT', 'name': 'v1-5-pruned.ckpt', 'size': '7.1747 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.ckpt' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Wed, 01 Feb 2023 07:01:13 GMT', 'name': 'WhiteDistance-v1.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v1/resolve/517c0e7422ec457aa9a40eec4cc0b86060db6355/WhiteDistance-v1.ckpt' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Sat, 04 Feb 2023 17:12:07 GMT', 'name': 'WhiteDistance-v2.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v2/resolve/a8272c98444dbd4ff7d5e9c5c4e0db83f080a65d/WhiteDistance-v2.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Sat, 04 Feb 2023 17:46:42 GMT', 'name': 'WhiteDistance-v3.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v3/resolve/f1bac5b36aae88e05d93a5741edc435ed9559fc7/WhiteDistance-v3.ckpt' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Tue, 28 Feb 2023 09:52:00 GMT', 'name': 'WhiteDistance.Ver4.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v4/resolve/2ff49b9ebbb30654ee358a4b948df16dfc37e050/WhiteDistance.Ver4.ckpt' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Tue, 28 Feb 2023 09:30:11 GMT', 'name': 'WhiteDistance2.5.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v2.5/resolve/c41e1b627e04859ee2e6e3b06f54ff5f93f962e0/WhiteDistance2.5.safetensors' }, { 'author': 'zuzhe', 'lastModified': 'Tue, 07 Feb 2023 08:42:23 GMT', 'name': '机甲v3.0AY.ckpt', 'size': '3.8166 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/zuzhe/Mecha-model/resolve/27ae72a130b5e712dedbaa6d9c7e60c64c0642f5/机甲v3.0AY.ckpt' }, { 'author': 'zuzhe', 'lastModified': 'Wed, 08 Feb 2023 17:02:40 GMT', 'name': '机甲v3.0AY.safetensors', 'size': '3.8164 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/zuzhe/Mecha-model/resolve/bc070a33da74aad4cfa1ca8ed1e1c501788a1cac/机甲v3.0AY.safetensors' }, { 'author': 'WarriorMama777', 'lastModified': 'Sun, 08 Jan 2023 05:08:02 GMT', 'name': 'AbyssOrangeMix2_sfw.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/WarriorMama777/OrangeMixs/resolve/5b4e578501349950ea8d06da78113590a01006df/Models/AbyssOrangeMix2/AbyssOrangeMix2_sfw.ckpt' }, { 'author': 'Crosstyan', 'lastModified': 'Mon, 02 Jan 2023 06:28:34 GMT', 'name': 'bp_mk3.safetensors', 'size': '1.6011 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/Crosstyan/BPModel/resolve/dea2172f2fa1858444b14cc948c8cf0146592604/bp_mk3.safetensors' }, { 'author': 'syaimu', 'lastModified': 'Tue, 27 Dec 2022 06:12:27 GMT', 'name': 'Abyss_7th_layer.ckpt', 'size': '5.5736 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_layer/Abyss_7th_layer.ckpt' }, { 'author': 'JosephusCheung', 'lastModified': 'Tue, 13 Dec 2022 18:20:16 GMT', 'name': 'ACertainThing.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/JosephusCheung/ACertainThing/resolve/f29dbc8b2737fa20287a7ded5c47973619b5c012/ACertainThing.ckpt' }, { 'author': 'xiaolxl', 'lastModified': 'Tue, 31 Jan 2023 15:46:12 GMT', 'name': 'GuoFeng3.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v3/resolve/aa8d62cae717b89cb6689717f3d69c665373b818/GuoFeng3.ckpt' }, { 'author': 'xiaolxl', 'lastModified': 'Thu, 02 Feb 2023 00:50:28 GMT', 'name': 'GuoFeng3_Fix.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v3-fix/resolve/4d11f5b8470f73140ee45d78d6fa4e5d4bc911bf/GuoFeng3_Fix.safetensors' }, { 'author': 'xiaolxl', 'lastModified': 'Thu, 02 Feb 2023 00:35:28 GMT', 'name': 'GuoFeng3_Fix-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v3-fix/resolve/4d11f5b8470f73140ee45d78d6fa4e5d4bc911bf/GuoFeng3_Fix-non-ema-fp16.safetensors' }, { 'author': 'xiaolxl', 'lastModified': 'Fri, 07 Apr 2023 05:18:41 GMT', 'name': 'GuoFeng3.3.safetensors', 'size': '3.9526 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/xiaolxl/GuoFeng3/resolve/main/GuoFeng3.3.safetensors' }, { 'author': 'WarriorMama777', 'lastModified': 'Sat, 24 Dec 2022 13:48:57 GMT', 'name': 'AbyssOrangeMix.safetensors', 'size': '5.5733 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/WarriorMama777/OrangeMixs/resolve/5b4e578501349950ea8d06da78113590a01006df/Models/AbyssOrangeMix/AbyssOrangeMix.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Tue, 31 Jan 2023 07:30:09 GMT', 'name': 'Anything-V3.0.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/anything-v3.0/resolve/main/Anything-V3.0.ckpt' }, { 'author': 'JosephusCheung', 'lastModified': 'Mon, 12 Dec 2022 17:41:40 GMT', 'name': 'ACertainModel.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/JosephusCheung/ACertainModel/resolve/02fc9a2dccf7ebce834fb17f53a304dc77d679ba/ACertainModel.ckpt' }, { 'author': 'JosephusCheung', 'lastModified': 'Mon, 12 Dec 2022 18:24:52 GMT', 'name': 'ACertainModel-half.ckpt', 'size': '1.9864 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/JosephusCheung/ACertainModel/resolve/02fc9a2dccf7ebce834fb17f53a304dc77d679ba/ACertainModel-half.ckpt' }, { 'author': 'JosephusCheung', 'lastModified': 'Tue, 13 Dec 2022 18:41:18 GMT', 'name': 'ACertainThing-half.ckpt', 'size': '1.9864 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/JosephusCheung/ACertainThing/resolve/f29dbc8b2737fa20287a7ded5c47973619b5c012/ACertainThing-half.ckpt' }, { 'author': 'Crosstyan', 'lastModified': 'Tue, 20 Dec 2022 17:40:17 GMT', 'name': 'bp_1024_e10.ckpt', 'size': '1.6012 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/Crosstyan/BPModel/resolve/dea2172f2fa1858444b14cc948c8cf0146592604/bp_1024_e10.ckpt' }, { 'author': 'DanMix', 'lastModified': 'Sat, 25 Feb 2023 09:09:23 GMT', 'name': 'DanMix-v2-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2/resolve/afc7d3168cb6a2690ba152b81ce058b593e66d17/DanMix-v2-non-ema-bf16.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Sat, 25 Feb 2023 08:14:36 GMT', 'name': 'DanMix-v2.2-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.2/resolve/051d38948e26246139437dcee4b1ce89eaac69bd/DanMix-v2.2-non-ema-bf16.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Wed, 01 Feb 2023 01:37:21 GMT', 'name': 'YaguruMagiku-v3.1-AnyBased.ckpt', 'size': '3.8166 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v3-dreambooth/resolve/c94ef9feb7b34c5e2137a7b088b5c584d18eb0ea/YaguruMagiku-v3.1-AnyBased.ckpt' }, { 'author': 'toooajk', 'lastModified': 'Wed, 01 Feb 2023 01:47:20 GMT', 'name': 'YaguruMagiku-v3.1-AnyBased-non-ema-bf16.safetensors', 'size': '2.2154 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v3-dreambooth/resolve/c94ef9feb7b34c5e2137a7b088b5c584d18eb0ea/YaguruMagiku-v3.1-AnyBased-non-ema-bf16.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Wed, 01 Feb 2023 01:40:31 GMT', 'name': 'YaguruMagiku-v3.1-AnyBased.safetensors', 'size': '3.8164 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v3-dreambooth/resolve/c94ef9feb7b34c5e2137a7b088b5c584d18eb0ea/YaguruMagiku-v3.1-AnyBased.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Wed, 01 Feb 2023 01:46:39 GMT', 'name': 'YaguruMagiku-v3.1-AnyBased-non-ema-fp16.safetensors', 'size': '2.2154 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v3-dreambooth/resolve/c94ef9feb7b34c5e2137a7b088b5c584d18eb0ea/YaguruMagiku-v3.1-AnyBased-non-ema-fp16.safetensors' }, { 'author': 'monx', 'lastModified': 'Tue, 28 Feb 2023 10:00:16 GMT', 'name': 'monx 1_10000.safetensors', 'size': '3.8164 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/monx/resolve/d33cbc848f69aae38926d31f2d649eb671a64823/monx 1_10000.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Sat, 25 Feb 2023 08:14:35 GMT', 'name': 'DanMix-v2.2-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.2/resolve/051d38948e26246139437dcee4b1ce89eaac69bd/DanMix-v2.2-non-ema-fp32.safetensors' }, { 'author': 'andite', 'lastModified': 'Tue, 24 Jan 2023 18:58:59 GMT', 'name': 'pastelmix.safetensors', 'size': '5.5733 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/andite/pastel-mix/resolve/7f691d69c0a348b183f15630005ec96b672458ed/pastelmix.safetensors' }, { 'author': 'Icarus', 'lastModified': 'Thu, 09 Feb 2023 08:04:12 GMT', 'name': 'Icarus-ver7.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/Icarus-v7/resolve/9471f7dbc9f5294d5cf89bca8a58977ee9f6dfd0/Icarus-ver7.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Sat, 11 Feb 2023 16:07:32 GMT', 'name': 'DanMix-v2.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2/resolve/afc7d3168cb6a2690ba152b81ce058b593e66d17/DanMix-v2.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Sat, 25 Feb 2023 08:04:46 GMT', 'name': 'DanMix-v2.1-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.1/resolve/0f58c4f6698e1a196fa743ab8830a15f59b49105/DanMix-v2.1-non-ema-fp32.safetensors' }, { 'author': 'bailocat', 'lastModified': 'Thu, 09 Feb 2023 08:46:55 GMT', 'name': 'bailocat.safetensors', 'size': '7.1743 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/bailocat/resolve/84bdf9bb5d6db24d29cc4aa6e5b372a858e59021/bailocat.safetensors' }, { 'author': 'scabbard', 'lastModified': 'Fri, 10 Feb 2023 04:28:39 GMT', 'name': '刀鞘V2.0.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/scabbard-v2.0/resolve/026d148a068a1d818b1c330e7b8d455addcd57fc/刀鞘V2.0.ckpt' }, { 'author': 'syaimu', 'lastModified': 'Sat, 14 Jan 2023 16:46:33 GMT', 'name': '7th_anime_v3_A.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v3/7th_anime_v3_A.safetensors' }, { 'author': 'AnythingMix', 'lastModified': 'Sat, 25 Feb 2023 07:35:26 GMT', 'name': 'AnythingMix-V1.1-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/AnythingMix-v1.1/resolve/38f9f8225c41fdd62c67aa0acfd3cc442cb07a5f/AnythingMix-V1.1-non-ema-fp16.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Sat, 25 Feb 2023 09:09:23 GMT', 'name': 'DanMix-v2-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2/resolve/afc7d3168cb6a2690ba152b81ce058b593e66d17/DanMix-v2-non-ema-fp32.safetensors' }, { 'author': 'syaimu', 'lastModified': 'Sat, 14 Jan 2023 16:46:34 GMT', 'name': '7th_anime_v3_B.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v3/7th_anime_v3_B.ckpt' }, { 'author': 'syaimu', 'lastModified': 'Sat, 14 Jan 2023 16:46:31 GMT', 'name': '7th_anime_v3_A.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v3/7th_anime_v3_A.ckpt' }, { 'author': 'syaimu', 'lastModified': 'Mon, 02 Jan 2023 17:32:11 GMT', 'name': '7th_anime_v2_C.ckpt', 'size': '5.5736 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v2/7th_anime_v2_C.ckpt' }, { 'author': 'syaimu', 'lastModified': 'Sat, 14 Jan 2023 16:17:45 GMT', 'name': '7th_anime_v2_B.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v2/7th_anime_v2_B.safetensors' }, { 'author': 'syaimu', 'lastModified': 'Mon, 02 Jan 2023 17:32:11 GMT', 'name': '7th_anime_v2_B.ckpt', 'size': '5.5736 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v2/7th_anime_v2_B.ckpt' }, { 'author': 'syaimu', 'lastModified': 'Sat, 14 Jan 2023 15:51:27 GMT', 'name': '7th_anime_v2_A.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v2/7th_anime_v2_A.safetensors' }, { 'author': 'syaimu', 'lastModified': 'Mon, 02 Jan 2023 17:32:11 GMT', 'name': '7th_anime_v2_A.ckpt', 'size': '5.5736 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v2/7th_anime_v2_A.ckpt' }, { 'author': 'DanMix', 'lastModified': 'Sat, 25 Feb 2023 09:09:23 GMT', 'name': 'DanMix-v2-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2/resolve/afc7d3168cb6a2690ba152b81ce058b593e66d17/DanMix-v2-non-ema-fp16.safetensors' }, { 'author': 'AnythingMix', 'lastModified': 'Sat, 25 Feb 2023 07:33:16 GMT', 'name': 'AnythingMix-V1.1-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/AnythingMix-v1.1/resolve/38f9f8225c41fdd62c67aa0acfd3cc442cb07a5f/AnythingMix-V1.1-non-ema-bf16.safetensors' }, { 'author': 'wind', 'lastModified': 'Wed, 01 Feb 2023 00:48:03 GMT', 'name': 'wind-v4-12000.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/wind-v4/resolve/9bc39169bd292e8e744b6ce15e47265ce8096eae/wind-v4-12000.safetensors' }, { 'author': 'xiaolxl', 'lastModified': 'Wed, 01 Feb 2023 00:58:10 GMT', 'name': 'Gf_style-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v1/resolve/9f20e292d80db9ae7c5bdae2485fa1dba6db941d/Gf_style-non-ema-bf16.safetensors' }, { 'author': 'xiaolxl', 'lastModified': 'Tue, 31 Jan 2023 15:44:01 GMT', 'name': 'Gf_style.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v1/resolve/9f20e292d80db9ae7c5bdae2485fa1dba6db941d/Gf_style.safetensors' }, { 'author': 'xiaolxl', 'lastModified': 'Wed, 01 Feb 2023 00:57:15 GMT', 'name': 'Gf_style-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v1/resolve/9f20e292d80db9ae7c5bdae2485fa1dba6db941d/Gf_style-non-ema-fp16.safetensors' }, { 'author': 'syaimu', 'lastModified': 'Sat, 14 Jan 2023 15:51:26 GMT', 'name': '7th_anime_v1.1.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v1/7th_anime_v1.1.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Wed, 01 Feb 2023 07:01:14 GMT', 'name': 'WhiteDistance-v1.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v1/resolve/517c0e7422ec457aa9a40eec4cc0b86060db6355/WhiteDistance-v1.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Wed, 01 Feb 2023 07:01:13 GMT', 'name': 'WhiteDistance-v1-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v1/resolve/517c0e7422ec457aa9a40eec4cc0b86060db6355/WhiteDistance-v1-non-ema-bf16.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Wed, 01 Feb 2023 07:18:35 GMT', 'name': 'WhiteDistance-v1-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v1/resolve/517c0e7422ec457aa9a40eec4cc0b86060db6355/WhiteDistance-v1-non-ema-fp32.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Wed, 01 Feb 2023 07:01:13 GMT', 'name': 'WhiteDistance-v1-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v1/resolve/517c0e7422ec457aa9a40eec4cc0b86060db6355/WhiteDistance-v1-non-ema-fp16.safetensors' }, { 'author': 'hans', 'lastModified': 'Wed, 01 Feb 2023 07:32:03 GMT', 'name': 'hans-v4.4-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/hans-v4.4/resolve/568deba7c897575e98ab659788f7f7f68aa21aae/hans-v4.4-non-ema-fp16.safetensors' }, { 'author': 'hans', 'lastModified': 'Wed, 01 Feb 2023 07:32:03 GMT', 'name': 'hans-v4.4.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/hans-v4.4/resolve/568deba7c897575e98ab659788f7f7f68aa21aae/hans-v4.4.ckpt' }, { 'author': 'hans', 'lastModified': 'Wed, 01 Feb 2023 07:32:03 GMT', 'name': 'hans-v4.4.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/hans-v4.4/resolve/568deba7c897575e98ab659788f7f7f68aa21aae/hans-v4.4.safetensors' }, { 'author': 'hans', 'lastModified': 'Wed, 01 Feb 2023 07:32:03 GMT', 'name': 'hans-v4.4-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/hans-v4.4/resolve/568deba7c897575e98ab659788f7f7f68aa21aae/hans-v4.4-non-ema-fp32.safetensors' }, { 'author': 'NullMix', 'lastModified': 'Sat, 25 Feb 2023 10:39:32 GMT', 'name': 'NullMix-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/NullMix/resolve/33aba85a1da7eb9709b86e0113b4de44f3f1bdf9/NullMix-non-ema-fp32.safetensors' }, { 'author': 'AnythingMix', 'lastModified': 'Sat, 25 Feb 2023 07:33:16 GMT', 'name': 'AnythingMix-V1.1-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/AnythingMix-v1.1/resolve/38f9f8225c41fdd62c67aa0acfd3cc442cb07a5f/AnythingMix-V1.1-non-ema-fp32.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Sat, 25 Feb 2023 09:26:15 GMT', 'name': 'cornflower_v9.safetensors', 'size': '5.1882 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v9/resolve/ad3295475da0a0022d65a2a2ebe186369c5df9b6/cornflower_v9.safetensors' }, { 'author': 'AnythingMix', 'lastModified': 'Thu, 16 Feb 2023 18:23:59 GMT', 'name': 'AnythingMix-V1.1.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/AnythingMix-v1.1/resolve/38f9f8225c41fdd62c67aa0acfd3cc442cb07a5f/AnythingMix-V1.1.safetensors' }, { 'author': 'syaimu', 'lastModified': 'Thu, 29 Dec 2022 07:51:16 GMT', 'name': '7th_anime_v1.1.ckpt', 'size': '5.5737 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v1/7th_anime_v1.1.ckpt' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:01:08 GMT', 'name': 'Null-v1.2-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v1.2/resolve/d178c9222828a428210b950b432c43cea5e56769/Null-v1.2-non-ema-fp16.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:18:32 GMT', 'name': 'Null-v2.0-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v2.0/resolve/bcb234b72565769d81704cd51621405a37cd537b/Null-v2.0-non-ema-bf16.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:18:32 GMT', 'name': 'Null-v2.0-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v2.0/resolve/bcb234b72565769d81704cd51621405a37cd537b/Null-v2.0-ema-bf16.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:18:32 GMT', 'name': 'Null-v2.0-ema-fp32.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v2.0/resolve/bcb234b72565769d81704cd51621405a37cd537b/Null-v2.0-ema-fp32.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:18:32 GMT', 'name': 'Null-v2.0.safetensors', 'size': '5.5733 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v2.0/resolve/bcb234b72565769d81704cd51621405a37cd537b/Null-v2.0.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:18:32 GMT', 'name': 'Null-v2.0-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v2.0/resolve/bcb234b72565769d81704cd51621405a37cd537b/Null-v2.0-non-ema-fp32.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:18:32 GMT', 'name': 'Null-v2.0-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v2.0/resolve/bcb234b72565769d81704cd51621405a37cd537b/Null-v2.0-non-ema-fp16.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:55:11 GMT', 'name': 'Null-v2.2.safetensors', 'size': '5.5733 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v2.2/resolve/284edaade2a16b4a249a5fb1f0b7a762f62ae49a/Null-v2.2.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:55:11 GMT', 'name': 'Null-v2.2-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v2.2/resolve/284edaade2a16b4a249a5fb1f0b7a762f62ae49a/Null-v2.2-non-ema-fp32.safetensors' }, { 'author': 'hans', 'lastModified': 'Wed, 01 Feb 2023 07:32:03 GMT', 'name': 'hans-v4.4-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/hans-v4.4/resolve/568deba7c897575e98ab659788f7f7f68aa21aae/hans-v4.4-ema-bf16.safetensors' }, { 'author': 'hans', 'lastModified': 'Wed, 01 Feb 2023 07:32:03 GMT', 'name': 'hans-v4.4-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/hans-v4.4/resolve/568deba7c897575e98ab659788f7f7f68aa21aae/hans-v4.4-non-ema-bf16.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:55:11 GMT', 'name': 'Null-v2.2-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v2.2/resolve/284edaade2a16b4a249a5fb1f0b7a762f62ae49a/Null-v2.2-non-ema-bf16.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:55:11 GMT', 'name': 'Null-v2.2-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v2.2/resolve/284edaade2a16b4a249a5fb1f0b7a762f62ae49a/Null-v2.2-ema-bf16.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:55:11 GMT', 'name': 'Null-v2.2-ema-fp32.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v2.2/resolve/284edaade2a16b4a249a5fb1f0b7a762f62ae49a/Null-v2.2-ema-fp32.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:55:12 GMT', 'name': 'Null-v2.2-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v2.2/resolve/284edaade2a16b4a249a5fb1f0b7a762f62ae49a/Null-v2.2-non-ema-fp16.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Sat, 25 Feb 2023 09:26:15 GMT', 'name': 'cornflower_v9-non-ema-fp32.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v9/resolve/ad3295475da0a0022d65a2a2ebe186369c5df9b6/cornflower_v9-non-ema-fp32.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Sun, 26 Feb 2023 10:40:16 GMT', 'name': 'cornflower_v8-non-ema-fp32.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v8/resolve/9664dab9d69ec13be9078f0a77274c1d3d6ae6d3/cornflower_v8-non-ema-fp32.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Fri, 30 Dec 2022 17:29:17 GMT', 'name': 'anything-V2.1-fp16.safetensors', 'size': '3.5872 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/anything-v2.1/resolve/main/anything-V2.1-fp16.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Thu, 02 Feb 2023 01:08:29 GMT', 'name': 'DanMix-v1-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v1/resolve/96f360b2bdde9854aa5146fe317f3fa6f8171103/DanMix-v1-non-ema-bf16.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Thu, 02 Feb 2023 01:08:29 GMT', 'name': 'DanMix-v1.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v1/resolve/96f360b2bdde9854aa5146fe317f3fa6f8171103/DanMix-v1.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Thu, 02 Feb 2023 01:08:28 GMT', 'name': 'DanMix-v1-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v1/resolve/96f360b2bdde9854aa5146fe317f3fa6f8171103/DanMix-v1-non-ema-fp16.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Sat, 25 Feb 2023 09:26:15 GMT', 'name': 'cornflower_v9-non-ema-bf16.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v9/resolve/ad3295475da0a0022d65a2a2ebe186369c5df9b6/cornflower_v9-non-ema-bf16.safetensors' }, { 'author': 'WarriorMama777', 'lastModified': 'Sun, 01 Jan 2023 21:12:43 GMT', 'name': 'EerieOrangeMix2.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/WarriorMama777/OrangeMixs/resolve/641d5be1a5f89a040e58f769cac02b328a277467/Models/EerieOrangeMix/EerieOrangeMix2.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Sun, 26 Feb 2023 10:37:30 GMT', 'name': 'cornflower_v8-non-ema-bf16.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v8/resolve/9664dab9d69ec13be9078f0a77274c1d3d6ae6d3/cornflower_v8-non-ema-bf16.safetensors' }, { 'author': '9527', 'lastModified': 'Thu, 02 Feb 2023 01:28:32 GMT', 'name': '9527-ema-bf16.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/9527/resolve/50426dd1c4acdde6a421d0aacd6d619da08b4e7c/9527-ema-bf16.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Thu, 29 Dec 2022 12:31:21 GMT', 'name': 'anything-V2.1.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/anything-v2.1/resolve/main/anything-V2.1.ckpt' }, { 'author': 'swl-models?', 'lastModified': 'Fri, 30 Dec 2022 16:51:56 GMT', 'name': 'anything-V2.1.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/anything-v2.1/resolve/main/anything-V2.1.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Tue, 31 Jan 2023 13:57:44 GMT', 'name': 'Anything-V3.0-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/anything-v3.0/resolve/727ab3550690ab8cfefc2daccc2b57bb86ff9d8e/Anything-V3.0-non-ema-bf16.safetensors' }, { 'author': '9527', 'lastModified': 'Thu, 02 Feb 2023 01:28:32 GMT', 'name': '9527-ema-fp16.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/9527/resolve/50426dd1c4acdde6a421d0aacd6d619da08b4e7c/9527-ema-fp16.safetensors' }, { 'author': '9527', 'lastModified': 'Thu, 02 Feb 2023 01:42:59 GMT', 'name': '9527-ema-fp32.safetensors', 'size': '3.5871 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/9527/resolve/50426dd1c4acdde6a421d0aacd6d619da08b4e7c/9527-ema-fp32.safetensors' }, { 'author': '9527', 'lastModified': 'Thu, 02 Feb 2023 01:28:32 GMT', 'name': '9527-non-ema-bf16.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/9527/resolve/50426dd1c4acdde6a421d0aacd6d619da08b4e7c/9527-non-ema-bf16.safetensors' }, { 'author': '9527', 'lastModified': 'Thu, 02 Feb 2023 01:28:32 GMT', 'name': '9527-non-ema-fp32.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/9527/resolve/50426dd1c4acdde6a421d0aacd6d619da08b4e7c/9527-non-ema-fp32.safetensors' }, { 'author': 'yehiaserag', 'lastModified': 'Sun, 25 Dec 2022 11:10:47 GMT', 'name': 'anime-pencil-diffusion-v4.safetensors', 'size': '3.8164 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/yehiaserag/anime-pencil-diffusion/resolve/b52ffef86adeaa55ecb75017ec6be9adcb1bff59/anime-pencil-diffusion-v4.safetensors' }, { 'author': 'yehiaserag', 'lastModified': 'Mon, 12 Dec 2022 16:10:38 GMT', 'name': 'anime-pencil-diffusion-v3.safetensors', 'size': '3.8164 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/yehiaserag/anime-pencil-diffusion/resolve/b52ffef86adeaa55ecb75017ec6be9adcb1bff59/anime-pencil-diffusion-v3.safetensors' }, { 'author': 'EK12317', 'lastModified': 'Sun, 22 Jan 2023 03:12:12 GMT', 'name': 'Ekmix-gen4-fp16-no-ema.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/31fae1bf719fe6c58b847bb9b1f1d6ff5b6f0bf3/Ekmix-gen4-fp16-no-ema.safetensors' }, { 'author': 'EK12317', 'lastModified': 'Tue, 31 Jan 2023 15:23:23 GMT', 'name': 'Ekmix-pastel-fp16.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/31fae1bf719fe6c58b847bb9b1f1d6ff5b6f0bf3/Ekmix-pastel-fp16.safetensors' }, { 'author': 'NullMix', 'lastModified': 'Sat, 25 Feb 2023 10:39:32 GMT', 'name': 'NullMix.safetensors', 'size': '5.5733 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/NullMix/resolve/33aba85a1da7eb9709b86e0113b4de44f3f1bdf9/NullMix.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Tue, 31 Jan 2023 13:53:35 GMT', 'name': 'Anything-V3.0-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/anything-v3.0/resolve/727ab3550690ab8cfefc2daccc2b57bb86ff9d8e/Anything-V3.0-non-ema-fp16.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Sun, 26 Feb 2023 10:44:39 GMT', 'name': 'Anything-v1.0.ckpt', 'size': '1.9864 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/Anything-v1.0/resolve/d1881a9d11555f64dad4483817d475a7d7441fc9/Anything-v1.0.ckpt' }, { 'author': 'SKACO', 'lastModified': 'Thu, 02 Feb 2023 07:12:30 GMT', 'name': 'SKACO-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/SKACO/resolve/8b30e7718768ec1eaa23a6ff7e5d3935c4d1d7fa/SKACO-ema-bf16.safetensors' }, { 'author': 'JinXiao', 'lastModified': 'Thu, 02 Feb 2023 07:26:44 GMT', 'name': '1号.safetensors', 'size': '5.1882 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/JinXiao-Mix/resolve/2ad936068cfb85f1c31d01d9bada465702d5c03e/1号.safetensors' }, { 'author': 'SKACO', 'lastModified': 'Thu, 02 Feb 2023 07:12:30 GMT', 'name': 'SKACO-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/SKACO/resolve/8b30e7718768ec1eaa23a6ff7e5d3935c4d1d7fa/SKACO-ema-fp16.safetensors' }, { 'author': 'SKACO', 'lastModified': 'Thu, 02 Feb 2023 07:12:30 GMT', 'name': 'SKACO-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/SKACO/resolve/8b30e7718768ec1eaa23a6ff7e5d3935c4d1d7fa/SKACO-ema-fp32.safetensors' }, { 'author': 'SKACO', 'lastModified': 'Thu, 02 Feb 2023 07:12:30 GMT', 'name': 'SKACO-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/SKACO/resolve/8b30e7718768ec1eaa23a6ff7e5d3935c4d1d7fa/SKACO-non-ema-bf16.safetensors' }, { 'author': 'SKACO', 'lastModified': 'Thu, 02 Feb 2023 07:12:30 GMT', 'name': 'SKACO-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/SKACO/resolve/8b30e7718768ec1eaa23a6ff7e5d3935c4d1d7fa/SKACO-non-ema-fp16.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Sat, 04 Feb 2023 17:12:07 GMT', 'name': 'WhiteDistance-v2.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v2/resolve/a8272c98444dbd4ff7d5e9c5c4e0db83f080a65d/WhiteDistance-v2.ckpt' }, { 'author': 'NullMix', 'lastModified': 'Sat, 25 Feb 2023 10:39:33 GMT', 'name': 'NullMix-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/NullMix/resolve/33aba85a1da7eb9709b86e0113b4de44f3f1bdf9/NullMix-non-ema-fp16.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Sat, 04 Feb 2023 17:12:07 GMT', 'name': 'WhiteDistance-v2-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v2/resolve/a8272c98444dbd4ff7d5e9c5c4e0db83f080a65d/WhiteDistance-v2-non-ema-bf16.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Sat, 04 Feb 2023 17:33:02 GMT', 'name': 'WhiteDistance-v2-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v2/resolve/a8272c98444dbd4ff7d5e9c5c4e0db83f080a65d/WhiteDistance-v2-non-ema-fp32.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Sat, 04 Feb 2023 17:12:07 GMT', 'name': 'WhiteDistance-v2-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v2/resolve/a8272c98444dbd4ff7d5e9c5c4e0db83f080a65d/WhiteDistance-v2-non-ema-fp16.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Sat, 04 Feb 2023 17:46:43 GMT', 'name': 'WhiteDistance-v3.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v3/resolve/f1bac5b36aae88e05d93a5741edc435ed9559fc7/WhiteDistance-v3.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Sat, 04 Feb 2023 17:46:43 GMT', 'name': 'WhiteDistance-v3-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v3/resolve/f1bac5b36aae88e05d93a5741edc435ed9559fc7/WhiteDistance-v3-non-ema-bf16.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Sat, 04 Feb 2023 17:46:42 GMT', 'name': 'WhiteDistance-v3-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v3/resolve/f1bac5b36aae88e05d93a5741edc435ed9559fc7/WhiteDistance-v3-non-ema-fp32.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Sat, 04 Feb 2023 17:48:52 GMT', 'name': 'WhiteDistance-v3-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v3/resolve/f1bac5b36aae88e05d93a5741edc435ed9559fc7/WhiteDistance-v3-non-ema-fp16.safetensors' }, { 'author': 'NullMix', 'lastModified': 'Sat, 25 Feb 2023 10:39:33 GMT', 'name': 'NullMix-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/NullMix/resolve/33aba85a1da7eb9709b86e0113b4de44f3f1bdf9/NullMix-non-ema-bf16.safetensors' }, { 'author': '9527', 'lastModified': 'Thu, 02 Feb 2023 01:28:32 GMT', 'name': '9527.ckpt', 'size': '5.1886 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/9527/resolve/50426dd1c4acdde6a421d0aacd6d619da08b4e7c/9527.ckpt' }, { 'author': 'wind', 'lastModified': 'Wed, 01 Feb 2023 00:43:32 GMT', 'name': 'wind-v2-12000.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/wind-v2/resolve/a7ba486df6c6f371db5ff41972b3d7b10eddb8f5/wind-v2-12000.safetensors' }, { 'author': 'Crosstyan', 'lastModified': 'Tue, 20 Dec 2022 19:28:17 GMT', 'name': 'bp_1024_e10_ema.ckpt', 'size': '3.2022 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/Crosstyan/BPModel/resolve/dea2172f2fa1858444b14cc948c8cf0146592604/bp_1024_e10_ema.ckpt' }, { 'author': 'SKACO', 'lastModified': 'Thu, 02 Feb 2023 07:12:30 GMT', 'name': 'SKACO-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/SKACO/resolve/8b30e7718768ec1eaa23a6ff7e5d3935c4d1d7fa/SKACO-non-ema-fp32.safetensors' }, { 'author': 'SKACO', 'lastModified': 'Thu, 02 Feb 2023 07:12:30 GMT', 'name': 'SKACO.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/SKACO/resolve/8b30e7718768ec1eaa23a6ff7e5d3935c4d1d7fa/SKACO.safetensors' }, { 'author': 'SKACO', 'lastModified': 'Thu, 02 Feb 2023 07:12:30 GMT', 'name': 'SKACO.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/SKACO/resolve/8b30e7718768ec1eaa23a6ff7e5d3935c4d1d7fa/SKACO.ckpt' }, { 'author': '9527', 'lastModified': 'Thu, 02 Feb 2023 01:28:32 GMT', 'name': '9527.safetensors', 'size': '5.1882 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/9527/resolve/50426dd1c4acdde6a421d0aacd6d619da08b4e7c/9527.safetensors' }, { 'author': 'syaimu', 'lastModified': 'Sat, 14 Jan 2023 17:17:28 GMT', 'name': '7th_anime_v3_C.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v3/7th_anime_v3_C.safetensors' }, { 'author': 'syaimu', 'lastModified': 'Sat, 14 Jan 2023 16:46:33 GMT', 'name': '7th_anime_v3_C.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v3/7th_anime_v3_C.ckpt' }, { 'author': 'syaimu', 'lastModified': 'Sat, 14 Jan 2023 16:46:33 GMT', 'name': '7th_anime_v3_B.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v3/7th_anime_v3_B.safetensors' }, { 'author': 'syaimu', 'lastModified': 'Sat, 14 Jan 2023 16:17:40 GMT', 'name': '7th_anime_v2_G.safetensors', 'size': '4.4306 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v2/7th_anime_v2_G.safetensors' }, { 'author': 'xiaolxl', 'lastModified': 'Tue, 31 Jan 2023 15:44:56 GMT', 'name': 'Gf_style2.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v2/resolve/86fb9ef75ed9e988447e18dfbf38e8470795878d/Gf_style2.ckpt' }, { 'author': 'xiaolxl', 'lastModified': 'Wed, 01 Feb 2023 01:12:51 GMT', 'name': 'Gf_style2-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v2/resolve/86fb9ef75ed9e988447e18dfbf38e8470795878d/Gf_style2-non-ema-bf16.safetensors' }, { 'author': 'xiaolxl', 'lastModified': 'Wed, 01 Feb 2023 01:05:25 GMT', 'name': 'Gf_style2.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v2/resolve/86fb9ef75ed9e988447e18dfbf38e8470795878d/Gf_style2.safetensors' }, { 'author': 'xiaolxl', 'lastModified': 'Wed, 01 Feb 2023 01:12:07 GMT', 'name': 'Gf_style2-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v2/resolve/86fb9ef75ed9e988447e18dfbf38e8470795878d/Gf_style2-non-ema-fp16.safetensors' }, { 'author': 'zoirun', 'lastModified': 'Thu, 09 Feb 2023 08:09:13 GMT', 'name': 'zoirun%2B.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/zoirun-plus/resolve/4497a794a363e7d39008a132504e91fca94d6b99/zoirun%2B.safetensors' }, { 'author': 'koushake', 'lastModified': 'Thu, 09 Feb 2023 08:39:11 GMT', 'name': 'koushake.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/koushake/resolve/691d6598c556c75582b2dd92824c8fe4df8497e9/koushake.safetensors' }, { 'author': 'syaimu', 'lastModified': 'Thu, 12 Jan 2023 18:11:03 GMT', 'name': '7th_anime_v2_G.ckpt', 'size': '7.6331 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v2/7th_anime_v2_G.ckpt' }, { 'author': 'xiaolxl', 'lastModified': 'Thu, 02 Feb 2023 00:35:28 GMT', 'name': 'GuoFeng3_Fix.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v3-fix/resolve/4d11f5b8470f73140ee45d78d6fa4e5d4bc911bf/GuoFeng3_Fix.ckpt' }, { 'author': 'xiaolxl', 'lastModified': 'Wed, 01 Feb 2023 01:24:48 GMT', 'name': 'GuoFeng3-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v3/resolve/aa8d62cae717b89cb6689717f3d69c665373b818/GuoFeng3-non-ema-bf16.safetensors' }, { 'author': 'xiaolxl', 'lastModified': 'Wed, 01 Feb 2023 01:20:32 GMT', 'name': 'GuoFeng3.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v3/resolve/aa8d62cae717b89cb6689717f3d69c665373b818/GuoFeng3.safetensors' }, { 'author': 'xiaolxl', 'lastModified': 'Wed, 01 Feb 2023 01:25:32 GMT', 'name': 'GuoFeng3-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v3/resolve/aa8d62cae717b89cb6689717f3d69c665373b818/GuoFeng3-non-ema-fp16.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Wed, 01 Feb 2023 14:03:01 GMT', 'name': 'AnyJrny90.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v4/resolve/7be3d76c2add0abebabc6f3a69007a2181e30eb7/AnyJrny90.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Wed, 01 Feb 2023 14:32:46 GMT', 'name': 'AJ-Mai80.ckpt', 'size': '1.9864 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v5/resolve/431fe8feca1c0ce4ea811595477c8e8099e268ee/AJ-Mai80.ckpt' }, { 'author': 'toooajk', 'lastModified': 'Wed, 01 Feb 2023 14:32:46 GMT', 'name': 'AJ-Mai80.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v5/resolve/431fe8feca1c0ce4ea811595477c8e8099e268ee/AJ-Mai80.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Wed, 01 Feb 2023 14:41:13 GMT', 'name': 'YaguruMagiku_v6.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v6/resolve/d3c1a07c817f315b9402d30a0f22c8d623837624/YaguruMagiku_v6.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Wed, 01 Feb 2023 14:43:10 GMT', 'name': 'cornflower_v7.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v7/resolve/f85b3e494e29cbec94c8b259f4e6e9a95ecf3fa9/cornflower_v7.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Thu, 09 Feb 2023 01:47:13 GMT', 'name': 'cornflower_v8.safetensors', 'size': '3.5872 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v8/resolve/main/cornflower_v8.safetensors' }, { 'author': 'JinXiao', 'lastModified': 'Thu, 02 Feb 2023 07:26:44 GMT', 'name': 'JinXiaoMix-H.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/JinXiao-Mix/resolve/2ad936068cfb85f1c31d01d9bada465702d5c03e/JinXiaoMix-H.safetensors' }, { 'author': 'JinXiao', 'lastModified': 'Thu, 02 Feb 2023 07:26:44 GMT', 'name': 'JinXiaoMix-K-Mod.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/JinXiao-Mix/resolve/2ad936068cfb85f1c31d01d9bada465702d5c03e/JinXiaoMix-K-Mod.safetensors' }, { 'author': 'JinXiao', 'lastModified': 'Thu, 02 Feb 2023 07:26:44 GMT', 'name': 'JinXiaoMix-M.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/JinXiao-Mix/resolve/2ad936068cfb85f1c31d01d9bada465702d5c03e/JinXiaoMix-M.safetensors' }, { 'author': 'JinXiao', 'lastModified': 'Thu, 02 Feb 2023 07:26:44 GMT', 'name': 'JinXiaoMix-M-Mod.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/JinXiao-Mix/resolve/2ad936068cfb85f1c31d01d9bada465702d5c03e/JinXiaoMix-M-Mod.safetensors' }, { 'author': 'syaimu', 'lastModified': 'Sat, 14 Jan 2023 16:17:37 GMT', 'name': '7th_anime_v2_C.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/syaimu/7th_Layer/resolve/3ed51a9efa1b7f7386aafb94049617d4de8c50b9/7th_anime_v2/7th_anime_v2_C.safetensors' }, { 'author': 'EK12317', 'lastModified': 'Sun, 18 Dec 2022 06:50:38 GMT', 'name': 'Ekmix-gen1.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/e8489459acdfdbbd52ec5be5d9277748c2ad7d4e/Ekmix-gen1.ckpt' }, { 'author': 'andite', 'lastModified': 'Sun, 15 Jan 2023 15:16:30 GMT', 'name': 'anything-v4.5.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/andite/anything-v4.0/resolve/8eb1055fba5a23bf1b60d52cdc620f84b25ca054/anything-v4.5.safetensors' }, { 'author': 'JinXiao', 'lastModified': 'Thu, 02 Feb 2023 07:26:44 GMT', 'name': 'JinXiaoMix-O.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/JinXiao-Mix/resolve/2ad936068cfb85f1c31d01d9bada465702d5c03e/JinXiaoMix-O.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:01:08 GMT', 'name': 'Null-v1.2.ckpt', 'size': '5.5736 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v1.2/resolve/d178c9222828a428210b950b432c43cea5e56769/Null-v1.2.ckpt' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:01:08 GMT', 'name': 'Null-v1.2-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v1.2/resolve/d178c9222828a428210b950b432c43cea5e56769/Null-v1.2-ema-bf16.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:01:08 GMT', 'name': 'Null-v1.2-ema-fp32.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v1.2/resolve/d178c9222828a428210b950b432c43cea5e56769/Null-v1.2-ema-fp32.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:01:08 GMT', 'name': 'Null-v1.2.safetensors', 'size': '5.5733 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v1.2/resolve/d178c9222828a428210b950b432c43cea5e56769/Null-v1.2.safetensors' }, { 'author': 'andite', 'lastModified': 'Tue, 24 Jan 2023 17:41:11 GMT', 'name': 'pastelmix.ckpt', 'size': '5.5736 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/andite/pastel-mix/resolve/7f691d69c0a348b183f15630005ec96b672458ed/pastelmix.ckpt' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:01:08 GMT', 'name': 'Null-v1.2-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v1.2/resolve/d178c9222828a428210b950b432c43cea5e56769/Null-v1.2-non-ema-bf16.safetensors' }, { 'author': 'EK12317', 'lastModified': 'Tue, 31 Jan 2023 15:00:24 GMT', 'name': 'Ekmix-pastel.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/31fae1bf719fe6c58b847bb9b1f1d6ff5b6f0bf3/Ekmix-pastel.safetensors' }, { 'author': 'null', 'lastModified': 'Wed, 01 Feb 2023 08:01:08 GMT', 'name': 'Null-v1.2-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/null-v1.2/resolve/d178c9222828a428210b950b432c43cea5e56769/Null-v1.2-non-ema-fp32.safetensors' }, { 'author': 'gsdf', 'lastModified': 'Fri, 13 Jan 2023 14:37:50 GMT', 'name': 'Counterfeit-V2.0fp16.safetensors', 'size': '3.5872 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/gsdf/Counterfeit-V2.0/resolve/7e4b174f12b9f1b301540df3ef85148231c7414a/Counterfeit-V2.0fp16.safetensors' }, { 'author': 'gsdf', 'lastModified': 'Fri, 13 Jan 2023 14:37:46 GMT', 'name': 'Counterfeit-V2.0.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/gsdf/Counterfeit-V2.0/resolve/7e4b174f12b9f1b301540df3ef85148231c7414a/Counterfeit-V2.0.safetensors' }, { 'author': 'gsdf', 'lastModified': 'Fri, 13 Jan 2023 09:38:27 GMT', 'name': 'Counterfeit-V2.0.ckpt', 'size': '7.1746 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/gsdf/Counterfeit-V2.0/resolve/7e4b174f12b9f1b301540df3ef85148231c7414a/Counterfeit-V2.0.ckpt' }, { 'author': 'gsdf', 'lastModified': 'Sat, 04 Feb 2023 04:53:59 GMT', 'name': 'Counterfeit-V2.1.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/gsdf/Counterfeit-V2.5/resolve/af6f56fe239d0aed0621969aad1d55d7b6db412e/Counterfeit-V2.1.safetensors' }, { 'author': 'gsdf', 'lastModified': 'Sat, 04 Feb 2023 04:54:01 GMT', 'name': 'Counterfeit-V2.2.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/gsdf/Counterfeit-V2.5/resolve/af6f56fe239d0aed0621969aad1d55d7b6db412e/Counterfeit-V2.2.safetensors' }, { 'author': 'gsdf', 'lastModified': 'Thu, 02 Feb 2023 14:44:59 GMT', 'name': 'Counterfeit-V2.5.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/gsdf/Counterfeit-V2.5/resolve/5c62b30f2c4ff4bb1cd29b4db76e60fb879337a0/Counterfeit-V2.5.safetensors' }, { 'author': 'timbrooks', 'lastModified': 'Fri, 20 Jan 2023 05:00:21 GMT', 'name': 'instruct-pix2pix-00-22000.safetensors', 'size': '7.1744 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/timbrooks/instruct-pix2pix/resolve/93224554bd65f19b6f0c99cbcce3a4ac59bb6382/instruct-pix2pix-00-22000.safetensors' }, { 'author': 'MistyOrange', 'lastModified': 'Sun, 26 Feb 2023 08:31:13 GMT', 'name': 'MistyOrange-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MistyOrange/resolve/bb5747bd502be81824a7dee0bc47caf0745ebaf6/MistyOrange-non-ema-bf16.safetensors' }, { 'author': 'yehiaserag', 'lastModified': 'Sun, 25 Dec 2022 05:40:01 GMT', 'name': 'anime-pencil-diffusion-v4.ckpt', 'size': '3.8166 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/yehiaserag/anime-pencil-diffusion/resolve/b52ffef86adeaa55ecb75017ec6be9adcb1bff59/anime-pencil-diffusion-v4.ckpt' }, { 'author': 'yehiaserag', 'lastModified': 'Tue, 06 Dec 2022 20:40:53 GMT', 'name': 'anime-pencil-diffusion-v3.ckpt', 'size': '3.8166 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/yehiaserag/anime-pencil-diffusion/resolve/b52ffef86adeaa55ecb75017ec6be9adcb1bff59/anime-pencil-diffusion-v3.ckpt' }, { 'author': 'MistyOrange', 'lastModified': 'Sun, 26 Feb 2023 08:31:13 GMT', 'name': 'MistyOrange-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MistyOrange/resolve/bb5747bd502be81824a7dee0bc47caf0745ebaf6/MistyOrange-non-ema-fp32.safetensors' }, { 'author': 'WarriorMama777', 'lastModified': 'Wed, 14 Dec 2022 05:10:19 GMT', 'name': 'ElyOrangeMix.ckpt', 'size': '3.9724 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/WarriorMama777/OrangeMixs/resolve/641d5be1a5f89a040e58f769cac02b328a277467/Models/ElyOrangeMix/ElyOrangeMix.ckpt' }, { 'author': 'yehiaserag', 'lastModified': 'Mon, 12 Dec 2022 16:10:38 GMT', 'name': 'anime-pencil-diffusion-v2.safetensors', 'size': '3.8164 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/yehiaserag/anime-pencil-diffusion/resolve/b52ffef86adeaa55ecb75017ec6be9adcb1bff59/anime-pencil-diffusion-v2.safetensors' }, { 'author': 'yehiaserag', 'lastModified': 'Mon, 12 Dec 2022 16:10:38 GMT', 'name': 'anime-pencil-diffusion-v1.safetensors', 'size': '3.8164 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/yehiaserag/anime-pencil-diffusion/resolve/b52ffef86adeaa55ecb75017ec6be9adcb1bff59/anime-pencil-diffusion-v1.safetensors' }, { 'author': 'zuzhe', 'lastModified': 'Wed, 08 Feb 2023 17:25:33 GMT', 'name': 'Ancient-Chinese-head-portrait-AY.safetensors', 'size': '3.8164 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/zuzhe/Ancient-Chinese-head-portrait/resolve/c6452d2e248f0d5b9b8fa88c04aff4f1cb98f9d5/Ancient-Chinese-head-portrait-AY.safetensors' }, { 'author': 'zuzhe', 'lastModified': 'Tue, 31 Jan 2023 05:54:46 GMT', 'name': 'Ancient-Chinese-head-portrait-AY.ckpt', 'size': '3.8166 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/zuzhe/Ancient-Chinese-head-portrait/resolve/d4faefe31921b8e0e3e45c58d6ebc7d8ecca374f/Ancient-Chinese-head-portrait-AY.ckpt' }, { 'author': 'zuzhe', 'lastModified': 'Wed, 08 Feb 2023 17:17:48 GMT', 'name': 'Chinese weddingAY.safetensors', 'size': '3.8164 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/zuzhe/Chinese-wedding/resolve/a652b48d1ffd9d3701d491aad2e92aef72cfa29a/Chinese weddingAY.safetensors' }, { 'author': 'zuzhe', 'lastModified': 'Fri, 03 Feb 2023 17:04:11 GMT', 'name': 'Chinese wedding v2.0 AY.ckpt', 'size': '5.5736 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/zuzhe/Chinese-wedding/resolve/e5fb4586bc04a34e80e4a8064ff70e42c5713bd8/Chinese wedding v2.0 AY.ckpt' }, { 'author': 'xiaolxl', 'lastModified': 'Tue, 28 Feb 2023 08:55:41 GMT', 'name': 'GuoFeng3.2.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v3.2/resolve/e1e42973de0f10e64fbb3706f8e108751a69ebee/GuoFeng3.2.safetensors' }, { 'author': 'scabbard', 'lastModified': 'Fri, 10 Feb 2023 04:28:39 GMT', 'name': '刀鞘V2.0-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/scabbard-v2.0/resolve/026d148a068a1d818b1c330e7b8d455addcd57fc/刀鞘V2.0-non-ema-bf16.safetensors' }, { 'author': 'scabbard', 'lastModified': 'Fri, 10 Feb 2023 04:28:39 GMT', 'name': '刀鞘V2.0-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/scabbard-v2.0/resolve/026d148a068a1d818b1c330e7b8d455addcd57fc/刀鞘V2.0-non-ema-fp16.safetensors' }, { 'author': 'scabbard', 'lastModified': 'Fri, 10 Feb 2023 04:28:39 GMT', 'name': '刀鞘V2.0-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/scabbard-v2.0/resolve/026d148a068a1d818b1c330e7b8d455addcd57fc/刀鞘V2.0-non-ema-fp32.safetensors' }, { 'author': 'scabbard', 'lastModified': 'Fri, 10 Feb 2023 04:28:39 GMT', 'name': '刀鞘V2.0.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/scabbard-v2.0/resolve/026d148a068a1d818b1c330e7b8d455addcd57fc/刀鞘V2.0.safetensors' }, { 'author': 'Crosstyan', 'lastModified': 'Mon, 02 Jan 2023 06:28:42 GMT', 'name': 'bp_mk5.safetensors', 'size': '1.6011 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/Crosstyan/BPModel/resolve/dea2172f2fa1858444b14cc948c8cf0146592604/bp_mk5.safetensors' }, { 'author': 'ProllyMix', 'lastModified': 'Tue, 28 Feb 2023 08:41:33 GMT', 'name': 'ZoiProllyMix-v1.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/ProllyMix/resolve/5faaacec2bd82910e57d367d4a89d10e726dafbb/ZoiProllyMix-v1.safetensors' }, { 'author': 'ProllyMix', 'lastModified': 'Tue, 28 Feb 2023 08:41:33 GMT', 'name': 'IceProllyMix-v1.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/ProllyMix/resolve/5faaacec2bd82910e57d367d4a89d10e726dafbb/IceProllyMix-v1.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Tue, 28 Feb 2023 09:52:00 GMT', 'name': 'WhiteDistance.Ver4-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v4/resolve/2ff49b9ebbb30654ee358a4b948df16dfc37e050/WhiteDistance.Ver4-non-ema-bf16.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Tue, 28 Feb 2023 09:52:00 GMT', 'name': 'WhiteDistance.Ver4-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v4/resolve/2ff49b9ebbb30654ee358a4b948df16dfc37e050/WhiteDistance.Ver4-non-ema-fp16.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Tue, 28 Feb 2023 09:52:00 GMT', 'name': 'WhiteDistance.Ver4-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v4/resolve/2ff49b9ebbb30654ee358a4b948df16dfc37e050/WhiteDistance.Ver4-non-ema-fp32.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Tue, 28 Feb 2023 09:52:00 GMT', 'name': 'WhiteDistance.Ver4.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v4/resolve/2ff49b9ebbb30654ee358a4b948df16dfc37e050/WhiteDistance.Ver4.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Tue, 28 Feb 2023 09:30:11 GMT', 'name': 'WhiteDistance2.5-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v2.5/resolve/c41e1b627e04859ee2e6e3b06f54ff5f93f962e0/WhiteDistance2.5-non-ema-bf16.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Tue, 28 Feb 2023 09:30:11 GMT', 'name': 'WhiteDistance2.5-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v2.5/resolve/c41e1b627e04859ee2e6e3b06f54ff5f93f962e0/WhiteDistance2.5-non-ema-fp16.safetensors' }, { 'author': 'WhiteDistanceMix', 'lastModified': 'Tue, 28 Feb 2023 09:44:19 GMT', 'name': 'WhiteDistance2.5-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/WhiteDistanceMix-v2.5/resolve/c41e1b627e04859ee2e6e3b06f54ff5f93f962e0/WhiteDistance2.5-non-ema-fp32.safetensors' }, { 'author': 'MoonTea', 'lastModified': 'Tue, 28 Feb 2023 10:43:12 GMT', 'name': 'MoonTea_V2.0-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MoonTea-v2/resolve/f4526acf82a6c87a6a6ed83c53a36df9e2591417/MoonTea_V2.0-non-ema-bf16.safetensors' }, { 'author': 'MoonTea', 'lastModified': 'Tue, 28 Feb 2023 10:45:22 GMT', 'name': 'MoonTea_V2.0-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MoonTea-v2/resolve/f4526acf82a6c87a6a6ed83c53a36df9e2591417/MoonTea_V2.0-non-ema-fp16.safetensors' }, { 'author': 'MoonTea', 'lastModified': 'Tue, 28 Feb 2023 10:43:12 GMT', 'name': 'MoonTea_V2.0.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MoonTea-v2/resolve/f4526acf82a6c87a6a6ed83c53a36df9e2591417/MoonTea_V2.0.safetensors' }, { 'author': 'diamond', 'lastModified': 'Tue, 28 Feb 2023 10:23:48 GMT', 'name': 'diamond-half.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/diamond/resolve/3e15b0a030125a2f8ad64c325f8a544d5b625d4b/diamond-half.safetensors' }, { 'author': 'diamond', 'lastModified': 'Tue, 28 Feb 2023 10:23:51 GMT', 'name': 'crystal-half.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/diamond/resolve/3e15b0a030125a2f8ad64c325f8a544d5b625d4b/crystal-half.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Mon, 27 Mar 2023 03:02:54 GMT', 'name': 'Anything-v3.0-For-Tachie-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/Anything-v3.0-For-Tachie/resolve/153fe4da2aca45bea3adb59249db91367f3ac9c8/Anything-v3.0-For-Tachie-non-ema-fp32.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Mon, 27 Mar 2023 01:47:12 GMT', 'name': 'Anything-v3.0-For-Tachie-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/Anything-v3.0-For-Tachie/resolve/153fe4da2aca45bea3adb59249db91367f3ac9c8/Anything-v3.0-For-Tachie-non-ema-fp16.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Mon, 27 Mar 2023 01:47:12 GMT', 'name': 'Anything-v3.0-For-Tachie-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/Anything-v3.0-For-Tachie/resolve/153fe4da2aca45bea3adb59249db91367f3ac9c8/Anything-v3.0-For-Tachie-non-ema-bf16.safetensors' }, { 'author': 'QteaMix', 'lastModified': 'Mon, 27 Mar 2023 01:37:10 GMT', 'name': 'QteaMix-gamma.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/QteaMix/resolve/50f927feb0f44b82c50ee78a0297d3981d31094f/QteaMix-gamma.safetensors' }, { 'author': 'QteaMix', 'lastModified': 'Mon, 27 Mar 2023 01:37:10 GMT', 'name': 'QteaMix-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/QteaMix/resolve/50f927feb0f44b82c50ee78a0297d3981d31094f/QteaMix-fp16.safetensors' }, { 'author': 'BY_A_RE', 'lastModified': 'Tue, 28 Mar 2023 02:54:51 GMT', 'name': 'BY_A_RE-1.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/BY_A_RE-1/resolve/10755874905b5ea4ff2427025f6caeca59495855/BY_A_RE-1.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Mon, 27 Mar 2023 08:15:24 GMT', 'name': 'DanMix-V2.3-alpha-non-ema-bf16.safetensors', 'size': '2.6876 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.3-alpha/resolve/c6d28786fc081bd649c5c8331ecee4f667cbce4d/DanMix-V2.3-alpha-non-ema-bf16.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Mon, 27 Mar 2023 08:15:24 GMT', 'name': 'DanMix-V2.3-alpha-non-ema-fp16.safetensors', 'size': '2.6876 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.3-alpha/resolve/c6d28786fc081bd649c5c8331ecee4f667cbce4d/DanMix-V2.3-alpha-non-ema-fp16.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Mon, 27 Mar 2023 11:15:59 GMT', 'name': 'DanMix-V2.3-alpha-non-ema-fp32.safetensors', 'size': '5.2832 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.3-alpha/resolve/c6d28786fc081bd649c5c8331ecee4f667cbce4d/DanMix-V2.3-alpha-non-ema-fp32.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Mon, 27 Mar 2023 08:15:24 GMT', 'name': 'DanMix-V2.3-alpha.safetensors', 'size': '5.2832 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.3-alpha/resolve/c6d28786fc081bd649c5c8331ecee4f667cbce4d/DanMix-V2.3-alpha.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Mon, 27 Mar 2023 04:34:18 GMT', 'name': 'DanMix-V2.3-non-ema-fp16.safetensors', 'size': '2.6876 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.3/resolve/42190ad4938d1720e3c4e2c65accd34b240f678a/DanMix-V2.3-non-ema-fp16.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Mon, 27 Mar 2023 06:53:30 GMT', 'name': 'DanMix-V2.3-non-ema-fp32.safetensors', 'size': '5.2832 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.3/resolve/42190ad4938d1720e3c4e2c65accd34b240f678a/DanMix-V2.3-non-ema-fp32.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Mon, 27 Mar 2023 06:53:30 GMT', 'name': 'DanMix-V2.3.safetensors', 'size': '5.2832 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.3/resolve/42190ad4938d1720e3c4e2c65accd34b240f678a/DanMix-V2.3.safetensors' }, { 'author': 'ariamix', 'lastModified': 'Tue, 28 Mar 2023 03:01:21 GMT', 'name': 'Ariamix-v1.0-non-ema-bf16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/ariamix/resolve/426026101cd04b6d7e9c6155fccf82c30d2a8e95/Ariamix-v1.0-non-ema-bf16.safetensors' }, { 'author': 'ariamix', 'lastModified': 'Tue, 28 Mar 2023 03:01:21 GMT', 'name': 'Ariamix-v1.0-non-ema-fp16.safetensors', 'size': '2.3712 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/ariamix/resolve/426026101cd04b6d7e9c6155fccf82c30d2a8e95/Ariamix-v1.0-non-ema-fp16.safetensors' }, { 'author': 'ariamix', 'lastModified': 'Tue, 28 Mar 2023 03:01:22 GMT', 'name': 'Ariamix-v1.0-non-ema-fp32.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/ariamix/resolve/426026101cd04b6d7e9c6155fccf82c30d2a8e95/Ariamix-v1.0-non-ema-fp32.safetensors' }, { 'author': 'ariamix', 'lastModified': 'Tue, 28 Mar 2023 03:01:21 GMT', 'name': 'Ariamix-v1.0.safetensors', 'size': '7.1742 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/ariamix/resolve/426026101cd04b6d7e9c6155fccf82c30d2a8e95/Ariamix-v1.0.safetensors' }, { 'author': 'gsdf', 'lastModified': 'Thu, 02 Feb 2023 14:44:58 GMT', 'name': 'Counterfeit-V2.5_fp16.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/gsdf/Counterfeit-V2.5/resolve/5c62b30f2c4ff4bb1cd29b4db76e60fb879337a0/Counterfeit-V2.5_fp16.safetensors' }, { 'author': 'gsdf', 'lastModified': 'Thu, 02 Feb 2023 14:45:10 GMT', 'name': 'Counterfeit-V2.5_pruned.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/gsdf/Counterfeit-V2.5/resolve/5c62b30f2c4ff4bb1cd29b4db76e60fb879337a0/Counterfeit-V2.5_pruned.safetensors' }, { 'author': 'Icarus', 'lastModified': 'Fri, 14 Apr 2023 13:24:30 GMT', 'name': 'Icarus-ver15.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/Icarus-v15/resolve/45196339cf27f8e9a10cd626b3b1c5a798e5a1d7/Icarus-ver15.safetensors' }, { 'author': 'IceFantasy', 'lastModified': 'Fri, 14 Apr 2023 12:56:01 GMT', 'name': 'IceFantasy_v1.5.safetensors', 'size': '3.9384 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/IceFantasy/resolve/c3f18fb688617fb885df0876eb3ee68d92fa9ca4/IceFantasy_v1.5.safetensors' }, { 'author': 'IceFantasy', 'lastModified': 'Fri, 14 Apr 2023 12:56:01 GMT', 'name': 'IceFantasy-v1.0.safetensors', 'size': '5.2737 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/IceFantasy/resolve/c3f18fb688617fb885df0876eb3ee68d92fa9ca4/IceFantasy-v1.0.safetensors' }, { 'author': 'Butter', 'lastModified': 'Tue, 28 Feb 2023 10:20:51 GMT', 'name': 'Butter.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/Butter/resolve/38c85fcf22551e4435261db1104edfd5126afba0/Butter.safetensors' }, { 'author': 'MeinaPastel', 'lastModified': 'Fri, 14 Apr 2023 14:11:51 GMT', 'name': 'MeinaPastelV4 - Without VAE.safetensors', 'size': '3.0431 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MeinaPastel/resolve/c595a1200e4231375b6f6acf2934e18731dadeea/MeinaPastelV4 - Without VAE.safetensors' }, { 'author': 'MeinaPastel', 'lastModified': 'Fri, 14 Apr 2023 14:11:51 GMT', 'name': 'MeinaPastelV3 - Without VAE.safetensors', 'size': '3.5873 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MeinaPastel/resolve/c595a1200e4231375b6f6acf2934e18731dadeea/MeinaPastelV3 - Without VAE.safetensors' }, { 'author': 'MeinaMix', 'lastModified': 'Fri, 14 Apr 2023 14:11:33 GMT', 'name': 'MeinaPastelV2 - baked VAE- pruned.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MeinaMix/resolve/478e265654aedb91c246cb2e84faa57b5619ea27/MeinaPastelV2 - baked VAE- pruned.safetensors' }, { 'author': 'MeinaMix', 'lastModified': 'Fri, 14 Apr 2023 14:11:33 GMT', 'name': 'MeinaPastel - baked VAE.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MeinaMix/resolve/478e265654aedb91c246cb2e84faa57b5619ea27/MeinaPastel - baked VAE.safetensors' }, { 'author': 'MeinaMix', 'lastModified': 'Fri, 14 Apr 2023 14:11:33 GMT', 'name': 'Meina Version 3.0 - baked VAE.safetensors', 'size': '3.5873 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MeinaMix/resolve/478e265654aedb91c246cb2e84faa57b5619ea27/Meina Version 3.0 - baked VAE.safetensors' }, { 'author': 'MeinaMix', 'lastModified': 'Fri, 14 Apr 2023 14:11:33 GMT', 'name': 'Meina Version 2.1 .safetensors', 'size': '3.5873 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MeinaMix/resolve/478e265654aedb91c246cb2e84faa57b5619ea27/Meina Version 2.1 .safetensors' }, { 'author': 'MeinaMix', 'lastModified': 'Fri, 14 Apr 2023 14:11:33 GMT', 'name': 'Meina V7 - Baked VAE ckpt.ckpt', 'size': '3.2187 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MeinaMix/resolve/478e265654aedb91c246cb2e84faa57b5619ea27/Meina V7 - Baked VAE ckpt.ckpt' }, { 'author': 'MeinaMix', 'lastModified': 'Fri, 14 Apr 2023 14:11:33 GMT', 'name': 'Meina V6 - Baked VAE.safetensors', 'size': '2.8935 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MeinaMix/resolve/478e265654aedb91c246cb2e84faa57b5619ea27/Meina V6 - Baked VAE.safetensors' }, { 'author': 'MeinaMix', 'lastModified': 'Fri, 14 Apr 2023 14:11:33 GMT', 'name': 'Meina V5.1 - Baked VAE.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MeinaMix/resolve/478e265654aedb91c246cb2e84faa57b5619ea27/Meina V5.1 - Baked VAE.safetensors' }, { 'author': 'MeinaMix', 'lastModified': 'Fri, 14 Apr 2023 14:11:33 GMT', 'name': 'Meina V5 - Baked VAE.safetensors', 'size': '3.5873 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MeinaMix/resolve/478e265654aedb91c246cb2e84faa57b5619ea27/Meina V5 - Baked VAE.safetensors' }, { 'author': 'MeinaMix', 'lastModified': 'Fri, 14 Apr 2023 14:11:33 GMT', 'name': 'Meina V4.1 - Baked VAE.safetensors', 'size': '3.5873 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MeinaMix/resolve/478e265654aedb91c246cb2e84faa57b5619ea27/Meina V4.1 - Baked VAE.safetensors' }, { 'author': 'MeinaMix', 'lastModified': 'Fri, 14 Apr 2023 14:11:33 GMT', 'name': 'Meina V4- Baked Vae.safetensors', 'size': '3.5873 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/MeinaMix/resolve/478e265654aedb91c246cb2e84faa57b5619ea27/Meina V4- Baked Vae.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Tue, 11 Apr 2023 03:26:00 GMT', 'name': 'DanMix V2.2-S-non-ema-bf16.safetensors', 'size': '2.6876 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.2-S/resolve/b6d7f76186c3409527ac889e28a3c8543e32556c/DanMix V2.2-S-non-ema-bf16.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Tue, 11 Apr 2023 04:59:30 GMT', 'name': 'DanMix V2.2-S-non-ema-fp16.safetensors', 'size': '2.6876 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.2-S/resolve/b6d7f76186c3409527ac889e28a3c8543e32556c/DanMix V2.2-S-non-ema-fp16.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Tue, 11 Apr 2023 03:26:00 GMT', 'name': 'DanMix V2.2-S-non-ema-fp32.safetensors', 'size': '5.2832 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.2-S/resolve/b6d7f76186c3409527ac889e28a3c8543e32556c/DanMix V2.2-S-non-ema-fp32.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Fri, 14 Apr 2023 12:01:24 GMT', 'name': 'DanMix V2.2-S-re.safetensors', 'size': '4.9667 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.2-S/resolve/b6d7f76186c3409527ac889e28a3c8543e32556c/DanMix V2.2-S-re.safetensors' }, { 'author': 'DanMix', 'lastModified': 'Tue, 11 Apr 2023 03:26:00 GMT', 'name': 'DanMix V2.2-S.safetensors', 'size': '8.4852 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/DanMix-v2.2-S/resolve/b6d7f76186c3409527ac889e28a3c8543e32556c/DanMix V2.2-S.safetensors' }, { 'author': 'toooajk', 'lastModified': 'Sat, 15 Apr 2023 01:14:19 GMT', 'name': 'cornflower-x.safetensors', 'size': '3.5872 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-x/resolve/4513bed401a9cdcb7de09c0d3075c9cbbc56e03a/cornflower-x.safetensors' }, { 'author': 'corneo', 'lastModified': 'Sat, 15 Apr 2023 01:03:28 GMT', 'name': 'coreno-7th-heaven-mix-v1.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/corneo-7th-heaven-mix-v1/resolve/5a3e09ae0867090c55f3435e4080b8c9573211f8/coreno-7th-heaven-mix-v1.safetensors' }, { 'author': 'HomoMix', 'lastModified': 'Fri, 14 Apr 2023 14:23:44 GMT', 'name': 'HomoMix_RE.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/HomoMix-v1.0/resolve/bbb1254b4d4a7dd906b5304c7afb938293135652/HomoMix_RE.safetensors' }, { 'author': 'HomoMix', 'lastModified': 'Fri, 14 Apr 2023 13:43:47 GMT', 'name': 'HomoMix_beta_v1.0-fp16-no-ema.safetensors', 'size': '1.8303 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/HomoMix-v1.0/resolve/bbb1254b4d4a7dd906b5304c7afb938293135652/HomoMix_beta_v1.0-fp16-no-ema.safetensors' }, { 'author': 'HomoMix', 'lastModified': 'Fri, 14 Apr 2023 13:43:47 GMT', 'name': 'HomoMix_beta_v1.0.safetensors', 'size': '7.1743 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/HomoMix-v1.0/resolve/bbb1254b4d4a7dd906b5304c7afb938293135652/HomoMix_beta_v1.0.safetensors' }, { 'author': 'three', 'lastModified': 'Thu, 20 Apr 2023 14:25:58 GMT', 'name': 'three-delicacy-wonton-v2.0.safetensors', 'size': '4.1084 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/three-delicacy-wonton-v2.0/resolve/main/three-delicacy-wonton-v2.0.safetensors' }, { 'author': 'AC_H-3', 'lastModified': 'Mon, 17 Apr 2023 01:56:41 GMT', 'name': 'AC_H-3-RD-half.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/AC_H-3/resolve/27e6faf16950664a11acd6f0e1e99c7cc88d98fc/AC_H-3-RD-half.safetensors' }, { 'author': 'AC_H-3', 'lastModified': 'Mon, 17 Apr 2023 01:56:41 GMT', 'name': 'AC_H-3-half.safetensors', 'size': '1.9862 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/AC_H-3/resolve/27e6faf16950664a11acd6f0e1e99c7cc88d98fc/AC_H-3-half.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Thu, 20 Apr 2023 14:48:35 GMT', 'name': 'Anything-V2.1-RE.safetensors', 'size': '2.1420 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/anything-v2.1/resolve/main/Anything-V2.1-RE.safetensors' }, { 'author': 'swl-models?', 'lastModified': 'Thu, 20 Apr 2023 14:42:16 GMT', 'name': 'Anything-V3.0-RE.safetensors', 'size': '3.9722 GB', 'type': 'checkpoints', 'url': 'https://huggingface.co/swl-models/anything-v3.0/resolve/main/Anything-V3.0-RE.safetensors' }], 'configs': [], 'controlnet': [], 'embeddings': [{ 'author': 'toooajk', 'lastModified': 'Wed, 01 Feb 2023 01:34:45 GMT', 'name': 'yaguru magiku.pt', 'size': '0.0068 MB', 'type': 'embeddings', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v3-hypernet/resolve/b8468979e2cdfa081c0cb2f6a37dc6c5eaf3df17/yaguru magiku.pt' }], 'hypernetworks': [{ 'author': 'toooajk', 'lastModified': 'Wed, 01 Feb 2023 14:43:10 GMT', 'name': 'cornflower_v7_phantom.pt', 'size': '83.7037 MB', 'type': 'hypernetworks', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v7/resolve/f85b3e494e29cbec94c8b259f4e6e9a95ecf3fa9/hypernetworks/cornflower_v7_phantom.pt' }, { 'author': 'EK12317', 'lastModified': 'Tue, 20 Dec 2022 12:45:49 GMT', 'name': 'ekmix-style1-35000.pt', 'size': '1.0167 GB', 'type': 'hypernetworks', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/e8489459acdfdbbd52ec5be5d9277748c2ad7d4e/hypernetworks/ekmix-style1-35000.pt' }, { 'author': 'EK12317', 'lastModified': 'Tue, 20 Dec 2022 12:45:50 GMT', 'name': 'ekmix-style1-47500.pt', 'size': '1.0167 GB', 'type': 'hypernetworks', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/e8489459acdfdbbd52ec5be5d9277748c2ad7d4e/hypernetworks/ekmix-style1-47500.pt' }, { 'author': 'EK12317', 'lastModified': 'Tue, 20 Dec 2022 13:17:25 GMT', 'name': 'ekmix-style2-45000.pt', 'size': '1.0175 GB', 'type': 'hypernetworks', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/e8489459acdfdbbd52ec5be5d9277748c2ad7d4e/hypernetworks/ekmix-style2-45000.pt' }, { 'author': 'EK12317', 'lastModified': 'Wed, 21 Dec 2022 12:18:43 GMT', 'name': 'ekmix-style2-67500.pt', 'size': '1.0175 GB', 'type': 'hypernetworks', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/a650b7f46ea7249de8e810bca945186c324dbd08/hypernetworks/ekmix-style2-67500.pt' }, { 'author': 'EK12317', 'lastModified': 'Mon, 16 Jan 2023 07:13:38 GMT', 'name': 'ekmix-style2-81000.pt', 'size': '1.0175 GB', 'type': 'hypernetworks', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/a650b7f46ea7249de8e810bca945186c324dbd08/hypernetworks/ekmix-style2-81000.pt' }, { 'author': 'EK12317', 'lastModified': 'Wed, 18 Jan 2023 05:55:17 GMT', 'name': 'ekmix-style3-16000.pt', 'size': '752.9444 MB', 'type': 'hypernetworks', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/a650b7f46ea7249de8e810bca945186c324dbd08/hypernetworks/ekmix-style3-16000.pt' }, { 'author': 'EK12317', 'lastModified': 'Wed, 18 Jan 2023 05:55:18 GMT', 'name': 'ekmix-style3-54500.pt', 'size': '752.9444 MB', 'type': 'hypernetworks', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/a650b7f46ea7249de8e810bca945186c324dbd08/hypernetworks/ekmix-style3-54500.pt' }, { 'author': 'EK12317', 'lastModified': 'Wed, 18 Jan 2023 07:17:53 GMT', 'name': 'ekmix-style4-37000.pt', 'size': '752.9444 MB', 'type': 'hypernetworks', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/a650b7f46ea7249de8e810bca945186c324dbd08/hypernetworks/ekmix-style4-37000.pt' }, { 'author': 'EK12317', 'lastModified': 'Wed, 18 Jan 2023 07:17:53 GMT', 'name': 'ekmix-style4-57500.pt', 'size': '752.9444 MB', 'type': 'hypernetworks', 'url': 'https://huggingface.co/EK12317/Ekmix-Diffusion/resolve/a650b7f46ea7249de8e810bca945186c324dbd08/hypernetworks/ekmix-style4-57500.pt' }, { 'author': 'toooajk', 'lastModified': 'Wed, 01 Feb 2023 01:34:43 GMT', 'name': 'YaguruMagiku-v3.pt', 'size': '83.7033 MB', 'type': 'hypernetworks', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v3-hypernet/resolve/b8468979e2cdfa081c0cb2f6a37dc6c5eaf3df17/YaguruMagiku-v3.pt' }, { 'author': 'toooajk', 'lastModified': 'Wed, 01 Feb 2023 14:32:46 GMT', 'name': 'Yaguru_Magiku_v5.pt', 'size': '83.7037 MB', 'type': 'hypernetworks', 'url': 'https://huggingface.co/swl-models/toooajk-yagurumagiku-v5/resolve/431fe8feca1c0ce4ea811595477c8e8099e268ee/hypernetworks/Yaguru_Magiku_v5.pt' }], 'loras': [{ 'author': 'loras', 'lastModified': 'Tue, 28 Feb 2023 08:58:25 GMT', 'name': 'GuoFeng2_Lora.safetensors', 'size': '288.1097 MB', 'type': 'loras', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v2/resolve/acf9ab8deb1331f8f2c767fed8d2d8d9677d1360/GuoFeng2_Lora.safetensors' }, { 'author': 'xiaolxl', 'lastModified': 'Tue, 28 Feb 2023 08:57:32 GMT', 'name': 'GuoFeng3.2_Lora.safetensors', 'size': '288.1097 MB', 'type': 'loras', 'url': 'https://huggingface.co/swl-models/xiaolxl-guofeng-v3.2/resolve/e1e42973de0f10e64fbb3706f8e108751a69ebee/GuoFeng3.2_Lora.safetensors' }, { 'author': 'lora', 'lastModified': 'Wed, 19 Apr 2023 01:49:35 GMT', 'name': '15365-30796-hanfu-v3.0-ming.safetensors', 'size': '225.1184 MB', 'type': 'loras', 'url': 'https://huggingface.co/swl-models/lora-pub/resolve/c77704af1b9cd8ead4e9916299566467a7126b76/15365-hanfu/15365-30796-hanfu-v3.0-ming.safetensors' }, { 'author': 'lora', 'lastModified': 'Tue, 28 Feb 2023 12:18:33 GMT', 'name': '12597-14856-MoXin-1.0.safetensors', 'size': '144.1390 MB', 'type': 'loras', 'url': 'https://huggingface.co/swl-models/lora-pub/resolve/09ba6cdb03135ffc594a8857d750ec20a06b8a4c/12597-MoXin/12597-14856-MoXin-1.0.safetensors' }, { 'author': 'lora', 'lastModified': 'Thu, 02 Feb 2023 05:45:18 GMT', 'name': '吴带ribbon1.safetensors', 'size': '36.0748 MB', 'type': 'loras', 'url': 'https://huggingface.co/swl-models/lora-pub/resolve/73b1f4ad7ce16d1ae2f6e1d6d630d67ba0a59b7b/吴带ribbon1.safetensors' }, { 'author': 'lora', 'lastModified': 'Sat, 15 Apr 2023 00:59:20 GMT', 'name': '28205-33811-RainbowLinesStyle-linev1.safetensors', 'size': '36.1073 MB', 'type': 'loras', 'url': 'https://huggingface.co/swl-models/lora-pub/resolve/0e2866afbcc17f1190f553b43058c5b4d15ab389/28205-33811-RainbowLinesStyle-linev1.safetensors' }, { 'author': 'lora', 'lastModified': 'Sat, 15 Apr 2023 02:22:46 GMT', 'name': '12597-20143-Shukezouma-v1.1.safetensors', 'size': '144.1147 MB', 'type': 'loras', 'url': 'https://huggingface.co/swl-models/lora-pub/resolve/0e2866afbcc17f1190f553b43058c5b4d15ab389/12597-MoXin/12597-20143-Shukezouma-v1.1.safetensors' }, { 'author': 'lora', 'lastModified': 'Tue, 28 Feb 2023 12:18:33 GMT', 'name': '12597-16075-Shukezouma.safetensors', 'size': '144.1120 MB', 'type': 'loras', 'url': 'https://huggingface.co/swl-models/lora-pub/resolve/0e2866afbcc17f1190f553b43058c5b4d15ab389/12597-MoXin/12597-16075-Shukezouma.safetensors' }, { 'author': 'lora', 'lastModified': 'Wed, 19 Apr 2023 02:06:51 GMT', 'name': '17727-20957-guizhong-v1.safetensors', 'size': '144.1134 MB', 'type': 'loras', 'url': 'https://huggingface.co/swl-models/lora-pub/resolve/c77704af1b9cd8ead4e9916299566467a7126b76/17727-guizhong-genshin-impact-lora/17727-20957-guizhong-v1.safetensors' }, { 'author': 'lora', 'lastModified': 'Wed, 19 Apr 2023 01:53:51 GMT', 'name': '15365-27946-hanfu-v2.9.safetensors', 'size': '72.1158 MB', 'type': 'loras', 'url': 'https://huggingface.co/swl-models/lora-pub/resolve/c77704af1b9cd8ead4e9916299566467a7126b76/15365-hanfu/15365-27946-hanfu-v2.9.safetensors' }, { 'author': 'lora', 'lastModified': 'Wed, 19 Apr 2023 01:46:35 GMT', 'name': '15365-39043-hanfu-v3.0-song.safetensors', 'size': '144.1190 MB', 'type': 'loras', 'url': 'https://huggingface.co/swl-models/lora-pub/resolve/c77704af1b9cd8ead4e9916299566467a7126b76/15365-hanfu/15365-39043-hanfu-v3.0-song.safetensors' }, { 'author': 'lora', 'lastModified': 'Wed, 19 Apr 2023 01:57:25 GMT', 'name': '11177-28609-anime-tarot-card-art-style-lora-v3.1.safetensors', 'size': '36.1072 MB', 'type': 'loras', 'url': 'https://huggingface.co/swl-models/lora-pub/resolve/c77704af1b9cd8ead4e9916299566467a7126b76/11177-anime-tarot-card-art-style-lora/11177-28609-anime-tarot-card-art-style-lora-v3.1.safetensors' }, { 'author': 'lora', 'lastModified': 'Tue, 28 Feb 2023 09:01:25 GMT', 'name': '5175-6004-guizhong-v1.safetensors', 'size': '36.0748 MB', 'type': 'loras', 'url': 'https://huggingface.co/swl-models/lora-pub/resolve/c77704af1b9cd8ead4e9916299566467a7126b76/5175-guizhong/5175-6004-guizhong-v1.safetensors' }], 'upscale_models': [] }]
            this.addModelList = list[0];
            this.addModelListBk = JSON.parse(JSON.stringify(this.addModelList))
        },
        noTips() {
            this.$Xwwqt.notTips();
        },
        changeTimer(i) {
            this.changeImgTimer && clearTimeout(this.changeImgTimer);
            this.changeImgTimer = setTimeout(() => {
                clearTimeout(this.changeImgTimer)
                if (this.$ChangeImgBase64 === "NONE") {
                    return;
                }
                if (this.$ChangeImgBase64) {
                    this.layout[i]["base64"] = this.$ChangeImgBase64;
                    this.saveLayout[i]["base64"] = this.$ChangeImgBase64;
                } else {
                    this.changeTimer(i);
                }
            }, 500);
        },
        changeImg(item, i) {
            if (item && item.models_path) {
                this.$Xwwqt.change_img(item.models_path);
                this.changeTimer(i);
            }
        },
        showCimgText(e, i) {
            this.showCimgTextTimer && clearTimeout(this.showCimgTextTimer);
            if (i) {
                this.showCimgTextTimer = setTimeout(() => {
                    clearTimeout(this.showCimgTextTimer);
                    this.$Toast.show(this.CHENFLAF ? '更换图片' : 'Change the picture', 30000, e.clientX, e.clientY);
                }, 800);
            } else {
                this.$Toast.hide();
            }
        },
        reloadPage() {
            this.reload();
        },
        showOpenText(e, i) {
            this.showwOpenTextTimer && clearTimeout(this.showwOpenTextTimer);
            if (i) {
                this.showwOpenTextTimer = setTimeout(() => {
                    clearTimeout(this.showwOpenTextTimer);
                    this.$Toast.show(this.CHENFLAF ? '打开本地位置' : 'Open local location', 30000, e.clientX, e.clientY);
                }, 800);
            } else {
                this.$Toast.hide();
            }
        },
        showLockText(e, i) {
            this.showwLockTextTimer && clearTimeout(this.showwLockTextTimer);
            if (i) {
                this.showwLockTextTimer = setTimeout(() => {
                    clearTimeout(this.showwLockTextTimer);
                    this.$Toast.show(this.CHENFLAF ? '锁定图片' : 'Lock picture', 30000, e.clientX, e.clientY);
                }, 800);
            } else {
                this.$Toast.hide();
            }
        },
        lockImgClick(i, key) {
            this.layout[key].static = i;
        },
        clearToast(e, i) {
            this.showwClearTextTimer && clearTimeout(this.showwClearTextTimer);
            if (i) {
                this.showwClearTextTimer = setTimeout(() => {
                    clearTimeout(this.showwClearTextTimer);
                    this.$Toast.show(this.CHENFLAF ? '注意！！！该操作会清空所有你之前保存的记录，请谨慎操作！' : 'Pay attention!! This operation will clear all your previously saved records, please exercise caution!', 30000, e.clientX, e.clientY + 100);
                }, 800);
            } else {
                this.$Toast.hide();
            }
        },
        saveToast(e, i) {
            this.showwSaveTextTimer && clearTimeout(this.showwSaveTextTimer);
            if (i) {
                this.showwSaveTextTimer = setTimeout(() => {
                    clearTimeout(this.showwSaveTextTimer);
                    this.$Toast.show(this.CHENFLAF ? '点击记住后，以后进来会记住你目前模型的顺序和是否锁定效果，其它效果并不会记住；同时，在comfyui界面去选择对应模型时，会优先展示你目前设置的模型顺序，方便在茫茫models里快速找到你想要的选项（点击记住后，浏览器里刷新一下就可以看到你配置的模型顺序了）' : 'After clicking Remember, you will remember the order of your current model and whether to lock the effect, other effects will not remember; At the same time, when selecting the corresponding model in comfyui interface, the current model order will be displayed first, so that you can quickly find the options you want in the vast models (click Remember, refresh the browser to see the model order you configured).', 30000, e.clientX, e.clientY + 100);
                }, 800);
            } else {
                this.$Toast.hide();
            }
        },
        reSort(i) {
            if (i == 0) {
                this.typtList = JSON.parse(JSON.stringify(this.saveTypeList));
            } else {
                this.layout = JSON.parse(JSON.stringify(this.saveLayout));
            }
        },
        clear_save_data() {
            // this.$Xwwqt.py_alert('温馨提示', '该操作会删除你之前保存的记录，是否确定删除？');
            this.$Xwwqt.save_data(JSON.stringify({ "typtList": '' }), "moreselect.json", "json");
            let jsonName = `${this.isSelectName}layout.json`;
            this.$Xwwqt.save_data(JSON.stringify({ "layout": '' }), jsonName, "json");
            this.reload();
            this.$Toast.hide();
        },
        save_data() {
            let tl = this.typtList;
            // console.log(this.layout)
            let saveTl = []
            for (let i = 0; i < tl.length; i++) {
                saveTl[i] = {}
                saveTl[i]["x"] = tl[i]["x"]
                saveTl[i]["y"] = tl[i]["y"]
                saveTl[i]["w"] = tl[i]["w"]
                saveTl[i]["h"] = tl[i]["h"]
                saveTl[i]["name"] = tl[i]["name"]
                saveTl[i]["position"] = `${tl[i]["y"]}${tl[i]["x"]}`
            }
            if (saveTl) {
                saveTl.sort(function (a, b) {
                    return a.position - b.position;
                });
            }
            let lt = this.layout;
            let saveLt = []
            for (let i = 0; i < this.layout.length; i++) {
                saveLt[i] = {}
                saveLt[i]["x"] = lt[i]["x"]
                saveLt[i]["y"] = lt[i]["y"]
                saveLt[i]["w"] = lt[i]["w"]
                saveLt[i]["h"] = lt[i]["h"]
                saveLt[i]["static"] = lt[i]["static"]
                saveLt[i]["models_name"] = lt[i]["models_name"]
                saveLt[i]["models_type"] = lt[i]["models_type"]
                saveLt[i]["position"] = `${lt[i]["y"]}${lt[i]["x"]}`
            }
            if (saveLt) {
                saveLt.sort(function (a, b) {
                    return a.position - b.position;
                });
            }
            // console.log(saveLt)
            this.$Xwwqt.save_data(JSON.stringify({ "typtList": saveTl }), "moreselect.json", "json");
            let jsonName = `${this.isSelectName}layout.json`;
            this.$Xwwqt.save_data(JSON.stringify({ "layout": saveLt }), jsonName, "json");
        },
        openLocalDir(path) {
            if (path) {
                this.$Xwwqt.open_local_file(path, 'dir');
            }
        },
        openLocalFile(item) {
            if (item && item.models_path) {
                this.$Xwwqt.open_local_file(item.models_path, 'file');
            }
        },
        hideTipText() {
            this.showtiptextTimer && clearTimeout(this.showtiptextTimer);
            this.modelsName = "";
            this.modelsPath = "";
            this.imgPath = "";
        },
        showTipText(item) {
            this.showtiptextTimer && clearTimeout(this.showtiptextTimer);
            this.showtiptextTimer = setTimeout(() => {
                clearTimeout(this.showtiptextTimer);
                // this.$Xwwqt.py_print(JSON.stringify(item))
                if (item && item.models_name) {
                    this.modelsName = item.models_name + item.models_type
                } else {
                    this.modelsName = this.CHENFLAF ? "无" : "not"
                }
                if (item && item.models_path) {
                    this.modelsPath = item.models_path
                } else {
                    this.modelsPath = this.CHENFLAF ? "无" : "not"
                }
                if (item && item.img_path) {
                    this.imgPath = item.img_path
                } else {
                    this.imgPath = this.CHENFLAF ? "无" : "not"
                }
            }, 800);
        },
        setStrLen(str, len) {
            if (str && str.length > len) {
                str = str.substr(0, len) + '...'
            }
            return str;
        },
        init() {
            this.typtList = [];
            clearTimeout(this.initTimer);
            this.initTimer = setTimeout(() => {
                let mdd = this.$ModelsData;
                this.Ms = this.$Moreselect;
                let md = [];
                if (mdd && this.Ms) {
                    this.more_add_model_time();
                    clearTimeout(this.initTimer);
                    let ms = this.Ms[0];
                    let tl = [];
                    if (ms && ms.length > 0) {
                        tl = JSON.parse(ms).typtList;
                    }
                    let h = [];
                    if (tl && tl.length > 0) {
                        // this.$Xwwqt.py_print(JSON.stringify(tl))
                        for (let k = 0; k < tl.length; k++) {
                            for (let m = 0; m < mdd.length; m++) {
                                if (mdd[m].name === tl[k].name) {
                                    h.push({ ...mdd[m] });
                                    mdd.splice(m, 1);
                                    break;
                                }
                            }
                        }
                    }
                    md = [...h, ...mdd];
                    // this.$Xwwqt.py_print(JSON.stringify(h[0].name))
                    let x = 0;
                    let y = 0;
                    let bl = this.baseTyptList;
                    for (let i = 0; i < md.length; i++) {
                        bl["i"] = `${i}${md[i].name}`;
                        if (x < 12) {
                            bl["x"] = x;
                            x = x + 2;
                        } else {
                            x = 0;
                            bl["x"] = x;
                            x = x + 2;
                            y = y + 1;
                        }
                        bl["y"] = y;
                        this.typtList.push({ ...bl, ...md[i] })
                        this.saveTypeList = JSON.parse(JSON.stringify(this.typtList))

                    }
                    // 默认展示第一个选项
                    this.$nextTick(function () {
                        document.getElementById(this.typtList[0].name + this.typtList[0].i).click()
                    });
                } else {
                    this.init()
                }
            }, 200);
        },

        get_save_data_(item, jsonName) {
            this.layoutSaveTimer && clearTimeout(this.layoutSaveTimer);
            this.layoutSaveTimer = setTimeout(() => {
                let id = item.name + item.i;
                let ld = this.$LayoutData[0];
                if (ld && this.$LayoutData[1] == jsonName) {
                    this.localDirPath = item.path;
                    let selectbtn = document.getElementById(id);
                    // selectbtn.style.color = "green";
                    // selectbtn.style.backgroundImage = "linear-gradient(to right, rgb(255 255 255), rgb(175 223 155))";
                    // 无法删除伪类效果，这里只能进行样式更换来实现
                    // selectbtn.classList.remove("hover"); // 移除hover类名
                    selectbtn.classList.add("grid-item-div-name-selected");
                    selectbtn.classList.remove("grid-item-div-name");
                    if (this.isSelectBtn) {
                        let isb = document.getElementById(this.isSelectBtn);
                        isb.classList.remove("grid-item-div-name-selected");
                        isb.classList.add("grid-item-div-name");
                        // isb.classList.add("hover");
                        // isb.style.color = "#fff";
                        // isb.style.backgroundImage = "linear-gradient(to right, rgb(38, 37, 37), rgb(195, 188, 188))";
                    }
                    this.isSelectBtn = item.name + item.i;
                    this.layout = [];
                    let path_list = [];
                    let name_list = [];
                    for (let i = 0; i < item.models.length; i++) {
                        if (item.models[i].img_path) {
                            path_list.push(item.models[i].img_path);
                            name_list.push(item.models[i].models_name);
                        }

                    }
                    let models = JSON.parse(JSON.stringify(item.models))
                    if (path_list.length > 0) {
                        this.$Xwwqt.resize_img(path_list, 320, 320);
                        this.set_layout(name_list, models);
                    } else {
                        this.set_layout_img(name_list, models, []);
                    }
                } else {
                    this.get_save_data_(item, jsonName);
                }
            }, 200);
        },

        clickItem(item) {
            this.isSelectName = item.name;
            let id = item.name + item.i;
            if (id === this.isSelectBtn) {
                return;
            }
            let jsonName = `${this.isSelectName}layout.json`;
            this.$Xwwqt.get_save_data(jsonName);
            this.get_save_data_(item, jsonName);
        },
        set_layout(name_list, models) {
            clearTimeout(this.layoutTimer);
            this.layoutTimer = setTimeout(() => {
                let base64List = this.$Base64List;
                if (base64List) {
                    clearTimeout(this.layoutTimer);
                    this.set_layout_img(name_list, models, base64List);
                } else {
                    this.set_layout(name_list, models)
                }
            }, 1000);
        },
        set_layout_img(name_list, models, base64List) {
            let ld = this.$LayoutData[0];
            let tl = [];
            let mds = [];
            if (ld && ld.length > 0) {
                tl = JSON.parse(ld).layout;
            }
            let h = [];
            if (tl && tl.length > 0) {
                // this.$Xwwqt.py_print(JSON.stringify(tl))
                for (let k = 0; k < tl.length; k++) {
                    for (let m = 0; m < models.length; m++) {
                        if (`${models[m].models_name}${tl[k].models_type}` === `${tl[k].models_name}${tl[k].models_type}`) {
                            models[m]["static"] = tl[k]["static"];
                            h.push({ ...models[m] });
                            models.splice(m, 1);
                            break;
                        }
                    }
                }
            }
            // this.$Xwwqt.py_print(JSON.stringify(h))
            mds = [...h, ...models];
            let x = 0;
            let y = 0;
            let bl = this.baseLayout;
            for (let i = 0; i < mds.length; i++) {
                for (let j = 0; j < base64List.length; j++) {
                    if (name_list[j] === mds[i].models_name) {
                        mds[i]['base64'] = base64List[j];
                    }
                }
                bl["i"] = `${i}${mds[i].models_name}`;
                if (x < 12) {
                    bl["x"] = x;
                    x = x + 2;
                } else {
                    x = 0;
                    bl["x"] = x;
                    x = x + 2;
                    y = y + 3;
                }
                bl["y"] = y;
                this.layout.push({ ...bl, ...mds[i] })
                this.saveLayout = JSON.parse(JSON.stringify(this.layout))
            }
        },
        // 添加一个单元格
        addItem: function () {
            this.layout.push({
                x: (this.layout.length * 2) % (this.colNum || 12),
                y: this.layout.length + (this.colNum || 12),
                w: 2,
                h: 2,
                i: this.index,
            });
            // Increment the counter to ensure key is always unique.    
            this.index++;
        },
        // 删除单元格  
        removeItem: function (val) {
            const index = this.layout.map(item => item.i).indexOf(val);
            this.layout.splice(index, 1);
        },
    },
};
</script>
<style scoped>
.empty-div {
    width: 100%;
    height: 40vh;
    /* background-color: red; */
}

.safe-tip {
    background-color: rgba(255, 255, 0, 0.8);
    padding: 2px 10px;
    opacity: 0;
    height: 0;
    width: 96%;
    font-size: 12px;
    /* line-height: 0; */
    word-wrap: break-word;
    word-break: break-all;
}

.safe-tip button {
    /* position: absolute;
    top: 3px;
    left: 46%; */
    opacity: 0;
}

.change-img {
    position: absolute;
    right: 0;
    top: 0;
    width: 15px;
    z-index: 10;
    opacity: 0.5;
}

.change-img:hover {
    transform: rotateZ(180deg);
    width: 25px;
    opacity: 1;
    /* transform: scale(1.2); */
}

.img-tip {
    position: absolute;
    top: 30px;
    left: 0;
    z-index: 99;
    max-width: 100%;
    height: auto;
    padding: 30px;
    border-radius: 10px;
    color: #FFFFFF;
    text-align: left;
    word-wrap: break-word;
    word-break: break-all;
    background-color: rgb(0 0 0 / 80%);
}

.more-select-div {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 95vh;
    overflow: hidden;
}

.search-div {
    display: flex;
}

.search-div input {
    width: 40%;
    margin: 10px 10px 10px 30%;
    border-radius: 4px;
}

.clear-btn {
    margin-right: 10% !important;
}

.center-div {
    width: 100%;
    display: flex;
    justify-content: center;
}

.add-btn {
    position: absolute;
    bottom: 0;
    padding: 10px !important;
    z-index: 101;
    border-radius: 10px;
    opacity: 0.3;
    display: inline;
    color: #FFFFFF;
    background: #000000;
}

.more-add-div {
    position: absolute;
    bottom: -90vh;
    left: 5%;
    width: 90%;
    height: 90%;
    z-index: 100;
    border-radius: 10px;
    opacity: 0;
    background-color: rgba(0, 0, 0, 0.8);
}

.more-add-div button {
    border-radius: 4px;
    color: #FFFFFF;
    background: #000000;
}

.more-add-div button:hover {
    border-radius: 4px;
    color: #84f04e;
    transform: scale(1.1);
}

.more-add-div button:active {
    transform: scale(0.9);
}

.show-btn {
    margin: 10px 10px;
    transform-origin: bottom center;
}

.show-btn:hover {
    transform: scale(1.2);
    opacity: 1;
}

.show-btn:active {
    transform: scale(1);
    opacity: 1;
    margin: 10px 10px;
}

.more-add-show-tab {
    display: inline;
    width: 100%;
}

.more-add-tab {
    margin: 0 5px;
}

.more-add-show-detail {
    height: 87%;
    overflow: scroll;
    margin-top: 1%;
}

.detail-div {
    width: 100%;
    display: flex;
    justify-content: center;
    border-radius: 4px;
    color: #FFFFFF;
}

.detail-div:hover {
    color: #444cea;
    background-color: rgb(31, 42, 26);
}

.detail-div-title {
    width: 100%;
    display: flex;
    justify-content: center;
    border-radius: 4px;
    color: #FFFFFF;
}

.detail-div-div {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 5px;
    width: 20%;
    border: 1px solid #FFFFFF;
    word-wrap: break-word;
    word-break: break-all;
}

.select-bg {
    background-color: #235e06 !important;
}

.select-layout {
    position: relative;
    top: 0;
    left: 0;
    z-index: 5;
    width: 100%;
}

.image-layout {
    position: relative;
    /* top: 30px; */
    left: 0;
    overflow-x: scroll;
    z-index: 1;
    width: 100%;
    height: 100%;
}

.image-layout::-webkit-scrollbar {
    display: none;
}

.grid-item-div-select {
    display: flex;
    flex-direction: row;
    width: 100%;
    height: 100%;
    border-radius: 8px;
    /* background-image: linear-gradient(to right, rgb(38, 37, 37), rgb(195, 188, 188)); */
}

.grid-item-div-name-selected {
    width: 90%;
    height: 100%;
    margin: 0;
    padding: 0;
    border: 1px solid #000000;
    font-size: 16px;
    line-height: 0.8;
    text-align: center;
    word-wrap: break-word;
    word-break: break-all;
    transform-origin: right center;
    border-top-right-radius: 8px;
    border-bottom-right-radius: 8px;
    color: rgb(66, 0, 164) !important;
    background-image: linear-gradient(to right, rgb(255 255 255), rgb(74, 211, 15)) !important;
}

.grid-item-div-name:hover {
    transform: scaleY(1.5);
    border-radius: 8px;
    color: #55ff00;
    background-image: linear-gradient(to right, rgb(38, 37, 37), rgb(76, 75, 75)) !important;
    ;
}

.grid-item-div-name:active {
    transform: scale(0.9);
}

.grid-item-div-name {
    width: 90%;
    height: 100%;
    margin: 0;
    padding: 0;
    border: 1px solid #000000;
    color: rgb(255, 255, 255);
    font-size: 16px;
    line-height: 0.8;
    text-align: center;
    word-wrap: break-word;
    word-break: break-all;
    transform-origin: right center;
    border-top-right-radius: 8px;
    border-bottom-right-radius: 8px;
    background-image: linear-gradient(to right, rgb(38, 37, 37), rgb(195, 188, 188));

    /* background-image: linear-gradient(to right, rgb(98, 96, 96), rgb(149, 108, 108)); */
}

.grid-item-div-move:hover {
    background-image: linear-gradient(to right, rgb(255, 255, 255), rgb(38, 37, 37)) !important;
    ;
}

.grid-item-div-move {
    width: 10%;
    height: 100%;
    border-top-left-radius: 8px;
    border-bottom-left-radius: 8px;
}

.util-class {
    width: 100%;
    padding: 3px;
}

.util-class button .span {
    color: gold;
}

.util-class button {
    margin: 0 3px;
    color: #FFFFFF;
    border-radius: 4px;
    background-color: rgba(0, 0, 0, 0.6);
}

.util-class button:hover {
    color: #55ff00;
    transform: scale(1.1);
    background-color: rgba(0, 0, 0, 1);
}

.util-class button:active {
    color: #55ff00;
    transform: scale(1);
    background-color: rgba(0, 0, 0, 1);
}

.vue-grid-layout {
    width: 100%;
    /* background: #eee; */
}

.vue-grid-layout span {
    display: flex;
    justify-content: space-between;
}

/* .vue-grid-layout span>label {
    color: red;
    padding-right: 6px;
    cursor: pointer;

} */

.vue-grid-item {
    border-radius: 8px;
    background: #ccc;
}

.vue-grid-item:not(.vue-grid-placeholder) {
    border: 1px solid black;
}

.vue-grid-item .resizing {
    opacity: 0.9;
}

/* .vue-grid-item .static {
    background: rgb(25, 25, 76);
} */

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

.lock-img:hover {
    opacity: 1;
    /* transform: scale(1.3); */
    width: 20px;
    transform: rotateY(180deg);
}

.lock-img {
    position: absolute;
    left: 0;
    top: 0;
    z-index: 10;
    width: 15px;
    height: auto;
    opacity: 0.5;
}

.grid-item-div:hover {
    border: 1px solid #55ff00;
    transform: scale(1.2);
}

.grid-item-div {
    position: relative;
    top: 0;
    width: 100%;
    height: 100%;
}

.grid-item-span-btn:hover {
    background-color: rgb(68, 191, 7);
    transform: scale(1.1);
}

.grid-item-span-btn {
    color: #FFFFFF;
    height: 16px;
    width: 16px;
    margin-right: 3px;
    background-color: #84f04e;
}

.grid-item-span {
    position: absolute;
    bottom: 0;
    left: 3px;
    max-width: 80%;
    height: 16px;
    z-index: 1;
    color: rgb(30, 29, 29);
    font-size: 12px;
    overflow: hidden;
    cursor: pointer;
    /* word-wrap: break-word;
    word-break: break-all; */
}

.grid-item-span::after {
    content: "...";
    position: absolute;
    bottom: 0;
    right: 0;
    /* padding-left: 40px;
    background: linear-gradient(to right, transparent, #fff 55%); */
}

.grid-item-span button {
    border: 0;
    border-radius: 50%;
}

.grid-item-img {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 0;
    width: 100%;
    height: 100%;
    border-radius: 8px;
}
</style>
