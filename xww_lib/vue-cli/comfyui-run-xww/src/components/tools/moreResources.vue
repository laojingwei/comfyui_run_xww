<template>
    <show-page :isShowBg="false" :time="3500">
        <div class="more-res">
            <div class="more-res-div">
                {{ CHENFLAFV ? '分享一个关于AI资源比较全的网站 ' : 'Share a more comprehensive website about AI resources ' }}
                <span class="blue text-dec" @click="openUrl_('https://a2a.top/')">AI艺术天堂</span>

            </div>
            <div class="more-res-div">
                {{ CHENFLAFV ?
                    'chart-gtp（目前国内暂时免费可用，但后续会不会收费不清楚）'
                    :
                    'chart-gtp (currently available for free in China, but it is not clear whether it will be charged later) '
                }}
                <span class="blue text-dec" @click="openUrl_('https://chat123.fun/h5/?utm_source=a')">CHAT-GTP</span>
            </div>
            <div class="more-res-div">
                {{ CHENFLAFV ? '训练模型下载：' : 'Download the training model:' }}
                <div>C站---<span class="blue text-dec" @click="openUrl_('https://civitai.com/')">civitai</span></div>
                <div>国内C站---<span class="blue text-dec" @click="openUrl_('http://www.liandange.com/models')">炼丹阁</span>
                </div>
                <div>喵手AI资源站-AI相关的相关模型，prmopt，软件等资源---<span class="blue text-dec"
                        @click="openUrl_('https://resource.miaoshouai.com/')">miaoshouai</span></div>

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
            CHENFLAF: true,
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
        openUrl_(url) {
            url && this.$Xwwqt.openUrl(url)
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


.more-res {
    color: #FFFFFF;
    text-align: center;
}

.more-res-div {
    margin: 0 0 5px 0;
    padding: 10px 10px;
    border: 1px solid #FFFFFF;
    border-radius: 8px;
    background-color: rgb(0, 0, 0, 0.6);
}

.green {
    color: rgb(0, 255, 0);
}

.blue {
    color: rgb(17, 0, 255);
}

.text-dec {
    text-decoration: underline
}

.text-dec:hover {
    font-size: 18px;
    color: rgb(0, 255, 0);
    /* transform: scale(1.2); */
}

.text-dec:active {
    font-size: 16px;
}
</style>
