<template>
    <div v-if="isShow">
        <div class="toast-position" :style="style" v-if="positionShow">
            <button class="keep-out toast-btn" v-if="closeBtn" @click="hide">close</button>
            <div v-html="message"></div>
        </div>
        <div :class="keepOut ? 'toast-div keep-out' : 'toast-div keep-out-no'" v-else>
            <div class="toast" :style="style">
                <button class="keep-out toast-btn" v-if="closeBtn" @click="hide">close</button>
                <div v-html="message"></div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'toast-div',
    data() {
        return {
            positionShow: false,
            isShow: false,
            message: '',
            timer: null,
            style: '',
            keepOut: false,
            closeBtn: false
        };
    },
    mounted() {
        this.w = document.body.clientWidth;
        this.h = document.body.clientHeight;
    },
    methods: {
        show(message, params, x, y) {
            this.hide();
            let time = 2000;
            if (params && typeof (params) === 'object') {
                time = params.time;
                this.keepOut = params.keepOut
                this.closeBtn = params.closeBtn
            } else {
                time = params || 2000;
            }
            // console.log('---------------', x, y)
            if (x && y) {
                if (this.w - x < 200) {
                    x = x - 100;
                } else {
                    x = x + 30;
                }
                if (this.y - y < 50) {
                    y = y - 100;
                } else {
                    y = y - 50;
                }
                this.style = `left:${x}px;top:${y}px;`;
                this.positionShow = true;
            } else {
                this.style = '';
            }
            this.message = message;
            this.isShow = true;
            if (this.timer) {
                clearTimeout(this.timer);
            }
            this.timer = setTimeout(() => {
                this.positionShow = false;
                this.isShow = false;
            }, time);
        },
        hide() {
            if (this.timer) {
                clearTimeout(this.timer);
            }
            this.keepOut = false;
            this.closeBtn = false;
            this.positionShow = false;
            this.isShow = false;
        }
    },
};
</script>

<style scoped>
.toast-div {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    z-index: 999;
}

.keep-out {
    pointer-events: auto;
}

.keep-out-no {
    pointer-events: none;
}

.toast-position {
    position: fixed;
    left: 0;
    top: 0;
    max-width: 200px;
    background-color: #333;
    color: #fff;
    padding: 10px;
    border-radius: 5px;
    word-wrap: break-word;
    word-break: break-all;
    z-index: 999;
}

.toast {
    position: relative;
    max-width: 200px;
    background-color: #333;
    color: #fff;
    padding: 10px;
    border-radius: 5px;
    word-wrap: break-word;
    word-break: break-all;
}

.toast-btn {
    position: relative;
    left: 75%;
}
</style>
