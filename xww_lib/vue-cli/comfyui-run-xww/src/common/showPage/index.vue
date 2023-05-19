<template>
    <div class="show-page">
        <!-- color: String类型。默认’#dedede’。粒子颜色。
            particleOpacity: Number类型。默认0.7。粒子透明度。
            particlesNumber: Number类型。默认80。粒子数量。
            shapeType: String类型。默认’circle’。可用的粒子外观类型有："circle","edge","triangle", "polygon","star"。
            particleSize: Number类型。默认80。单个粒子大小。
            linesColor: String类型。默认’#dedede’。线条颜色。
            linesWidth: Number类型。默认1。线条宽度。
            lineLinked: 布尔类型。默认true。连接线是否可用。
            lineOpacity: Number类型。默认0.4。线条透明度。
            linesDistance: Number类型。默认150。线条距离。
            moveSpeed: Number类型。默认3。粒子运动速度。
            hoverEffect: 布尔类型。默认true。是否有hover特效。
            hoverMode: String类型。默认true。可用的hover模式有: "grab", "repulse", + "bubble"。
            clickEffect: 布尔类型。默认true。是否有click特效。
            clickMode: String类型。默认true。可用的click模式有: "push", "remove", "repulse", "bubble"。-->
        <div v-if="isShowPar" class="particels-div" @click="clickBg">
            <vue-particles color="#a7f238" :particleOpacity="0.8" :particlesNumber="100" shapeType="circle"
                :particleSize="5" linesColor="#ff8585" :linesWidth="1" :lineLinked="true" :lineOpacity="0.4"
                :linesDistance="150" :moveSpeed="3" :hoverEffect="true" hoverMode="grab" :clickEffect="true"
                clickMode="repulse"></vue-particles>
        </div>
        <div class="show-page-main">
            <div ref="showPageMainDiv" class="show-page-main-div">
                <slot></slot>
            </div>
        </div>
        <img v-if="isShowBg" ref="showPageImg" class="show-page-solo" src="../../assets/solo.png" @click="clickBg">
        <img v-if="isShowBg" ref="showPageImgLogo" class="show-page-logo" src="../../assets/logo.png">
    </div>
</template>

<script>

export default {
    name: 'show-page',
    props: {
        isShowPar: {
            type: Boolean,
            default: false,
        },
        opacity: {
            type: Number,
            default: 0.4,
        },
        isShowBg: {
            type: Boolean,
            default: true,
        },
        isClickBg: {
            type: Boolean,
            default: false,
        },
        time: {
            trype: Number,
            default: 5000
        }
    },
    data() {
        return {
            inputValue: '',
            inputValue1: '',
            inputValue2: '',
            scale: 1,
        };
    },

    mounted() {
        /* eslint-disable */
        this.isShowBg && this.$velocity(this.$refs.showPageImg, { opacity: this.opacity, translateX: [200, [50, 8]] }, { duration: this.time });
        this.$velocity(this.$refs.showPageMainDiv, { opacity: 1, translateX: [-1000, [50, 8]] }, { duration: this.time - 2000 });
        this.isShowBg && this.$velocity(this.$refs.showPageImgLogo, { opacity: this.opacity }, { duration: this.time - 1000, delay: this.time - 2000 });
    },

    methods: {
        clickBg() {
            if (!this.isClickBg) {
                return;
            }
            this.$velocity(this.$refs.showPageImg, "finish");
            if (this.scale === 1) {
                this.scale = 1.2;
            } else {
                this.scale = 1;
            }
            this.$velocity(this.$refs.showPageImg, { scale: this.scale }, { duration: 1000 });
        }
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.show-page {
    width: 100%;
    background: #443f40;
}

.show-page-main {
    position: absolute;
    top: 0;
    right: 0;
    z-index: 2;
    display: flex;
    flex-direction: column;
    width: 100%;
    /* height: 100vh; */
    /* margin: 60px; */
}

.particels-div {
    position: absolute;
    z-index: 99;
    top: 0;
    width: 100%;
    height: 100%;
}

.show-page-main-div {
    position: relative;
    display: flex;
    flex-direction: column;
    width: 100%;
    /* margin-right: 200px; */
    opacity: 0;
    margin-left: 1000px;
}

.show-page-solo {
    position: fixed;
    z-index: 1;
    top: -60px;
    left: -200px;
    width: 100%;
    height: auto;
    opacity: 0;
    /* display: none; */
}

.show-page-logo {
    position: fixed;
    z-index: 0;
    top: -60px;
    left: 0;
    width: 100%;
    height: auto;
    opacity: 0;
    /* display: none; */
}
</style>
