<template>
    <show-page>
        <div class="tools-div">
            <div class="tab-div">
                <div v-for="(item, index) in tabList" :key="index + item.id">
                    <button type="button" :ref="item.id" :class="item.isClick ? 'tab-div-btn selected' : 'tab-div-btn'"
                        @click="changeTab(item, index)">
                        {{ CHENFLAF ? item.name : item.nameEn }}
                    </button>
                </div>
            </div>
            <div class="componet-div">
                <component :is="showPagePath" :CHENFLAFV="CHENFLAF"></component>
            </div>
        </div>
    </show-page>
</template>

<script>

import getImageData from '../tools/getImageData.vue';
import photoSize from '../tools/photoSize.vue';
import moreResources from '../tools/moreResources.vue';
export default {
    components: {
        getImageData,
        photoSize,
        moreResources,
    },
    props: {
        CHENFLAF: {
            type: Boolean,
            default: true,
        },
    },
    data() {
        return {
            CHENFLAF: '',
            showPagePath: '',
            pageIndex: null,
            isRouterAlive: true,
            tabList: [
                { id: 'getImageData', name: "提取图片信息", nameEn: "Extract picture information", isClick: false, path: 'getImageData' },
                { id: 'imageCompression', name: "图片大小", nameEn: "Photo Size", isClick: false, path: 'photoSize' },
                { id: 'moreResources', name: "更多资源", nameEn: "More Resources", isClick: false, path: 'moreResources' },
            ],
        };
    },

    mounted() {
        this.$nextTick(function () {
            this.$refs[this.tabList[0].id][0].click();
        })
    },

    methods: {
        showTabPage(item) {
            this.showPagePath = item.path;
        },
        changeTab(item, i) {
            if (this.pageIndex === i) {
                return;
            }

            (this.pageIndex || this.pageIndex === 0) && (this.tabList[this.pageIndex].isClick = false);
            this.tabList[i].isClick = true;
            this.pageIndex = i;

            this.showTabPage(item);
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

.tools-div {
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
    height: 96vh;
    /* background-color: rgb(0, 0, 0, 0.5); */
    overflow: hidden;
}

.tab-div {
    position: relative;
    top: 30px;
    left: 0;
    z-index: 880;
    width: 100%;
    height: auto;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
    overflow-x: scroll;
}

.tab-div::-webkit-scrollbar {
    display: none;
}

.componet-div {
    position: absolute;
    top: 100px;
    left: 0;
    width: 100%;
    height: 85vh;
    overflow-y: scroll;
}

.componet-div::-webkit-scrollbar {
    display: none;
}

.selected {
    background-image: linear-gradient(to right, rgb(51 213 31), rgb(33 112 0)) !important;
}

.tab-div-btn {
    min-width: 100px;
    margin: 0 20px;
    padding: 10px;
    font-size: 14px;
    color: #ffffff;
    border-radius: 8px;
    opacity: 1;
    background-image: linear-gradient(to right, rgb(0, 0, 0), rgb(183, 183, 183));
}

.tab-div-btn:hover {
    color: #55ff00;
    /* transform: scale(1.1); */
    background-image: linear-gradient(to right, rgb(0, 0, 0), rgb(129, 128, 128));
}
</style>
