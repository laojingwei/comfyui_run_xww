import Vue from 'vue'
import App from './App.vue'
import router from '@/router/index.js'
import Com from '@/common/com.js'
import Toast from '@/common/Toast/index.vue'
import versionControl from '@/common/versionControl/index.vue'
import VueGridLayout from 'vue-grid-layout'
import Velocity from 'velocity-animate'
import ShowPage from '@/common/showPage'
import VueParticles from 'vue-particles'
import VueClipboards from 'vue-clipboard2'
// 挂载到$velocity
Vue.prototype.$velocity = Velocity
Vue.prototype.$Com = Com
Vue.prototype.$ISCHANGE = false
// 注册为全局组件
Vue.component('GridLayout', VueGridLayout.GridLayout)
Vue.component('GridItem', VueGridLayout.GridItem)
Vue.component('ShowPage', ShowPage)
Vue.use(VueParticles)
Vue.use(VueClipboards)

// 注册toast组件
const ToastPlugin = {
    install(Vue) {
        // 挂载到$Toast
        Vue.prototype.$Toast = new Vue(Toast).$mount();
        // 在body中插入Toast节点
        document.body.appendChild(Vue.prototype.$Toast.$el);
    },
};
Vue.use(ToastPlugin)

// 注册versionControl组件
const versionControlPlugin = {
    install(Vue) {
        // 挂载到$Vc
        Vue.prototype.$Vc = new Vue(versionControl).$mount();
        // 在body中插入versionControlPlugin节点
        document.body.appendChild(Vue.prototype.$Vc.$el);
    },
};
Vue.use(versionControlPlugin)


// 搭建qt通信，此过程为同步，不过连接过程很快的，注意，调用$xwwqt最好不要在created里调用，要不然会得到一个undefined
function initQWebChannel() {
    if (typeof qt !== "undefined") {
        // eslint-disable-next-line no-undef
        new QWebChannel(qt.webChannelTransport, (channel) => {
            Vue.prototype.$Xwwqt = channel.objects.xwwqt;
            Vue.prototype.$Xwwqt.isHaveComfyUI.connect((data) => {
                Vue.prototype.$IsHaveComfyUI = data;
            });
            Vue.prototype.$Xwwqt.mySignal.connect((data) => {
                Vue.prototype.$Xwwsignal = data;
            });
            Vue.prototype.$Xwwqt.base64List.connect((data) => {
                Vue.prototype.$Base64List = data;
            });
            Vue.prototype.$Xwwqt.modelsData.connect((data) => {
                Vue.prototype.$ModelsData = data;
            });
            Vue.prototype.$Xwwqt.moreselect.connect((data) => {
                Vue.prototype.$Moreselect = data;
            });
            Vue.prototype.$Xwwqt.layoutData.connect((data) => {
                Vue.prototype.$LayoutData = data;
            });
            Vue.prototype.$Xwwqt.runStatData.connect((data) => {
                Vue.prototype.$RunStatData = data;
            });
            Vue.prototype.$Xwwqt.changeModesPath.connect((data) => {
                Vue.prototype.$ChangeModesPath = data;
            });
            Vue.prototype.$Xwwqt.useYmalFlag.connect((data) => {
                Vue.prototype.$UseYmalFlag = data;
            });
            Vue.prototype.$Xwwqt.changeImgBase64.connect((data) => {
                Vue.prototype.$ChangeImgBase64 = data;
            });
            Vue.prototype.$Xwwqt.notTipsFlag.connect((data) => {
                Vue.prototype.$NotTipsFlag = data;
            });
            Vue.prototype.$Xwwqt.updateCuiBat.connect((data) => {
                Vue.prototype.$UpdateCuiBat = data;
            });
            Vue.prototype.$Xwwqt.gitFlag.connect((data) => {
                Vue.prototype.$GitFlag = data;
            });
            Vue.prototype.$Xwwqt.progress.connect((data) => {
                Vue.prototype.$Progress = data;
            });
            Vue.prototype.$Xwwqt.gitCloneFlag.connect((data) => {
                Vue.prototype.$GitCloneFlag = data;
            });
            Vue.prototype.$Xwwqt.gitComfyuiData.connect((data) => {
                Vue.prototype.$GitComfyuiData = data;
            });
            Vue.prototype.$Xwwqt.gitData.connect((data) => {
                Vue.prototype.$GitData = data;
            });
            Vue.prototype.$Xwwqt.checkoutGitData.connect((data) => {
                Vue.prototype.$CheckoutGitData = data;
            });
            Vue.prototype.$Xwwqt.chenFlag.connect((data) => {
                Vue.prototype.$ChenFlag = data;
            });
            Vue.prototype.$Xwwqt.refreshData.connect((data) => {
                Vue.prototype.$RefreshData = data;
            });
            Vue.prototype.$Xwwqt.imageData.connect((data) => {
                Vue.prototype.$ImageData = data;
            });
            Vue.prototype.$Xwwqt.saveFlag.connect((data) => {
                Vue.prototype.$SaveFlag = data;
            });
            Vue.prototype.$Xwwqt.customNodeLink.connect((data) => {
                Vue.prototype.$CustomNodeLink = data;
            });
            Vue.prototype.$Xwwqt.addModelList.connect((data) => {
                Vue.prototype.$AddModelList = data;
            });
            Vue.prototype.$Xwwqt.downloadModelFlag.connect((data) => {
                Vue.prototype.$DownloadModelFlag = data;
            });
            Vue.prototype.$Xwwqt.updateXwwV.connect((data) => {
                Vue.prototype.$UpdateXwwV = data;
            });
            Vue.prototype.$Xwwqt.updateXww.connect((data) => {
                Vue.prototype.$UpdateXww = data;
            });
            Vue.prototype.$Xwwqt.donloadFlag.connect((data) => {
                Vue.prototype.$DonloadFlag = data;
            });
        });
    } else {
        console.log('未连接到qt...');
    }
}
initQWebChannel()

Vue.config.productionTip = false
new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
