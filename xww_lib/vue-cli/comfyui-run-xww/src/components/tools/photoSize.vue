<template>
    <show-page :isShowBg="false" :time="3500">
        <div class="image-data-div">
            <div class="select-img-div">
                <img v-if="!imgBase64" src="@/assets/img-size.png" @click="select_img()" />
                <img v-else-if="imgBase64 === 'NONE'" src="@/assets/no-img.png" />
                <div v-else>
                    <img :src="'data:image/jpge;base64,' + imgBase64" @click="select_img()" />
                    <br>
                    <div>{{ CHENFLAF ? '原图' : 'master img' }}：{{ image_data[0]["size"] }}---{{ image_data[0]["kb"] }}</div>
                </div>
                <div class="input-div" v-if="imgBase64Compre">
                    <input type="text" :placeholder="CHENFLAF ? '宽' : 'width'" v-model="w"
                        onkeyup="value=value.replace(/^(0+)|[^\d]+/g,'')" />
                    <input type="text" :placeholder="CHENFLAF ? '高' : 'height'" v-model="h"
                        onkeyup="value=value.replace(/^(0+)|[^\d]+/g,'')" />
                    <button @click="select_img(image_data[0]['path'])">{{ CHENFLAF ? '转换' : 'convert to' }}</button>
                    <button @click="save_img">{{ CHENFLAF ? '保存图片' : 'save img' }}</button>
                    <button @click="clear_img">{{ CHENFLAF ? '清空' : 'clear' }}</button>
                </div>
                <div v-if="imgBase64Compre">
                    <img :src="'data:image/jpge;base64,' + imgBase64Compre" @click="save_img" />
                    <br>
                    <div>{{ CHENFLAF ? '转换后' : 'after conversion' }}：{{ image_data[1]["size"] }}---{{ image_data[1]["kb"] }}
                    </div>
                </div>
            </div>
            <div class="empty-div"></div>
        </div>
    </show-page>
</template>

<script>
export default {
    components: {
    },
    props: {
        CHENFLAFV: {
            type: Boolean,
            default: true,
        },
    },
    data() {
        return {
            w: 320,
            h: 320,
            CHENFLAF: true,
            imgBase64: null,
            imgBase64Compre: null,
            image_data: null,
            emoji: ['(≧∇≦)ﾉ', '(+.+)(-.-)(_ _) ..zzZZ もうだめ', 'ヾ(≧O≦)〃嗷~', '٩(๑òωó๑)۶', '( *￣▽￣)((≧︶≦*)', '（*＾-＾*）', '...(*￣０￣)ノ[等等我…]', 'n(*≧▽≦*)n', '(～o￣▽￣)～o 。。。滚来滚去……o～(＿△＿o～) ~。。。', '不＞(￣ε￣ = ￣3￣)<要', '.....((/- -)/', '-________-', '(*￣▽￣)(￣▽:;.…::;.:.:::;..::;.:...', '『家』 ～o(▽｀ o) =3 =3 =3', '＼（＾∀＾）メ（＾∀＾）ノ', '(*/ω＼*)/p.', '◕ฺ‿◕ฺ✿ฺ)', 'Ψ(￣∀￣)Ψ', '( *^-^)ρ(^0^* )', '↑↑↓↓←→←→ＢＡ...┗( -o-)┛', '（￣ー￣）ノ~~マ☆’.・.・:★', '．《{=．．．．（嘎~嘎~嘎~）'],
        };
    },

    watch: {
        CHENFLAFV() {
            this.CHENFLAF = this.CHENFLAFV;
        }
    },

    mounted() {
    },

    methods: {
        clear_img() {
            this.w = 320;
            this.h = 320;
            this.imgBase64 = null;
            this.imgBase64Compre = null;
            this.image_data = null;
        },
        save_img() {
            this.$Xwwqt.save_base64_2_img(this.imgBase64Compre)
            this.save_imgTime();
        },
        save_imgTime() {
            this.save_imgTimer && clearTimeout(this.save_imgTimer);
            this.save_imgTimer = setTimeout(() => {
                clearTimeout(this.save_imgTimer);
                if (this.$SaveFlag === "start") {
                    this.$Toast.show((this.CHENFLAF ? '努力处理中。。。' : 'Try to deal with...') + this.emoji[Math.floor(Math.random() * 20)]);
                    this.save_imgTime();
                } else if (this.$SaveFlag === "noselect") {
                    return;
                } else if (this.$SaveFlag === "error") {
                    this.$Toast.show(this.CHENFLAF ? '保存失败' : 'save failure', 3000);
                } else {
                    this.$Toast.show(this.CHENFLAF ? '保存成功' : 'save successfully', 3000);
                }
            }, 500);
        },
        select_img(path) {
            this.$Xwwqt.resize_img_select(this.w, this.h, path);
            this.select_imgTime();
        },
        select_imgTime() {
            this.select_imgTimer && clearTimeout(this.select_imgTimer);
            this.select_imgTimer = setTimeout(() => {
                clearTimeout(this.select_imgTimer);
                let base64List = this.$Base64List;
                if (base64List && base64List[0] === "start") {
                    this.$Toast.show((this.CHENFLAF ? '努力处理中。。。' : 'Try to deal with...') + this.emoji[Math.floor(Math.random() * 20)]);
                    this.select_imgTime();
                } else if (base64List && base64List[0] === "noselect") {
                    return;
                } else if (base64List && base64List[0] === "error") {
                    this.$Toast.show(this.CHENFLAF ? '处理失败' : 'Processing failure', 3000);
                } else {
                    this.imgBase64 = base64List[0];
                    this.imgBase64Compre = base64List[1];
                    this.image_data = [base64List[2], base64List[3]];
                    this.$Toast.show(this.CHENFLAF ? '处理成功' : 'Processing success', 3000);
                }
            }, 1000);
        },
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.empty-div {
    width: 100%;
    height: 30vh;
    /* background-color: red; */
}

.input-div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 100px;
}

.mt10 {
    margin-top: 10px;
}

.input-div input {
    margin: 0 10px 10px 10px;
    border-radius: 4px;
    text-align: center;
}

.input-div input:hover {
    transform: scale(1.1);
}

.input-div button {
    margin: 0 10px 10px 10px;
    border-radius: 4px;
    text-align: center;
}

.input-div button:hover {
    transform: scale(1.1);
}

.input-div button:active {
    transform: scale(0.9);
}

.select-img-div {
    display: flex;
    justify-content: center;
}

.select-img-div img {
    width: 300px;
    opacity: 0.9;
    border-radius: 10px;
    transform-origin: top center;
}

.select-img-div img:hover {
    opacity: 1;
    transform: scale(1.1);
}

.image-data-div {
    padding-left: 30px;
    text-align: left;
    color: #ffffff;
}
</style>
