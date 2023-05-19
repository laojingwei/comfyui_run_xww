<template>
    <show-page>
        <div class="custom-node-box">
            <div class="custom-node-tab">
                <button id="tabBtn0" class="button" @click="changeShow(0)">
                    <span v-if="CHENFLAF">
                        自定义节点列表
                    </span>
                    <span v-else>
                        Customize the node list
                    </span>
                </button>
                <button id="tabBtn1" class="button" @click="changeShow(1)">
                    <span v-if="CHENFLAF">
                        自定义节点下载地址
                    </span>
                    <span v-else>
                        Customize the node download address
                    </span>
                </button>
            </div>
            <div class="custom-node-search" v-if="pageIndex == 1">
                <input class="custom-node-search-ipt" type="text" v-model="searchValue"
                    :placeholder="CHENFLAF ? '地址太多不好找？试试输入内容精确查找吧' : 'Too many addresses to find? Try entering content for precise search.'">
                <button class="custom-node-search-btn" @click="clear">{{ CHENFLAF ? '清空' : 'clear' }}</button>
            </div>
            <div ref="customNodeListDiv" class="custom-node-list">
                <div v-for="(item, index) in customNodeList" :key="index + item.name">
                    <div class="cntl-div">
                        <div class="cntl-div-sub">
                            <span>{{ item.name }}</span>
                            <div v-if="CHENFLAF">
                                <button class="sub-button" @click="refresh(item, index)">刷新</button>
                                <button class="sub-button" @click="file_status(item, index)"
                                    @mouseenter="file_stat_tips($event)" @mouseleave="file_stat_tips()">
                                    <span v-if="item.git_detail.fileStat === '1'" class="green1">
                                        已启用
                                    </span>
                                    <span v-else class="red">
                                        已禁用
                                    </span>
                                </button>
                            </div>
                            <div v-else>
                                <button class="sub-button" @click="refresh(item, index)">refresh</button>
                                <button class="sub-button" @click="file_status(item, index)"
                                    @mouseenter="file_stat_tips($event)" @mouseleave="file_stat_tips()">
                                    <span v-if="item.git_detail.fileStat === '1'" class="green1">
                                        Enabled
                                    </span>
                                    <span v-else class="red">
                                        disabled
                                    </span>
                                </button>
                            </div>
                            <div v-if="item.git_detail.sourcePath">
                                <button class="sub-button" @click="openUrl_(item.git_detail.sourcePath + '#readme')">{{
                                    CHENFLAF
                                    ? '使用说明' : 'instructions'
                                }}</button>
                            </div>
                        </div>
                        <div class="cntl-div-sub" v-if="item.git_detail && item.git_detail.localHexsha">
                            <div>
                                <span v-if="CHENFLAF">
                                    当前版本：
                                </span>
                                <span v-else>
                                    Current Version:
                                </span>
                                <span>{{ item.git_detail.localTime }}</span>
                                <div class="green text-dec" @click="openUrl(item, item.git_detail.localHexsha)">{{
                                    subStringF(item.git_detail.localHexsha, 20) }}</div>
                            </div>
                            <div v-if="CHENFLAF">
                                <span v-if="item.git_detail.isNew === '1'">远程最新版本：</span>
                                <span v-else>本地最新版本：</span>
                                <span>{{ item.git_detail.newTime }}</span>
                                <div class="blue text-dec" @click="openUrl(item, item.git_detail.newHexsha)">{{
                                    subStringF(item.git_detail.newHexsha,
                                        20) }}</div>
                            </div>
                            <div v-else>
                                <span v-if="item.git_detail.isNew === '1'">Remote latest version:</span>
                                <span v-else>Latest Local version:</span>
                                <span>{{ item.git_detail.newTime }}</span>
                                <div class="blue">{{ subStringF(item.git_detail.newHexsha, 20) }}</div>
                            </div>
                        </div>
                        <div class="cntl-div-sub" v-else>
                            <div>
                                <span>
                                    {{
                                        CHENFLAF ?
                                        nogitTip : nogitTipEn
                                    }}
                                </span>
                            </div>
                        </div>
                        <div class="cntl-div-sub">
                            <button @click="checkout(item, index)" class="sub-button" v-if="item.git_detail.newHexsha">
                                <span v-if="CHENFLAF">
                                    切换到最新版
                                </span>
                                <span v-else>
                                    Switch to the latest version
                                </span>
                            </button>
                            <button v-if="item.git_detail.prevHexsha"
                                @click="checkout(item, index, item.git_detail.prevHexsha)" class="sub-button">
                                <span v-if="CHENFLAF">
                                    当前版本的上一个版本
                                </span>
                                <span v-else>
                                    The previous version of the current version
                                </span>
                            </button>
                            <button @click="opendir(item)" class="sub-button">
                                <span v-if="CHENFLAF">
                                    打开文件夹
                                </span>
                                <span v-else>
                                    Open a folder
                                </span>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="empty-div"></div>
            </div>
            <div ref="customNodeLoadDiv" class="custom-node-load">
                <div class="custom-node-load-div">
                    <div class="custom-node-load-label">
                        <label v-if="CHENFLAF">使用git地址进行克隆安装</label>
                        <label v-else>Use git address for clone installation</label>
                    </div>
                    <textarea type="text" v-model="inputValue"
                        :placeholder="CHENFLAF ? '请输入 git clone 地址，如：https://github.com/laojingwei/comfy_translation_node.git' : 'Enter git clone address such as：https://github.com/laojingwei/comfy_translation_node.git'" />
                    <button @click="gitClone(inputValue, 0)">
                        <span v-if="CHENFLAF">
                            安装（普通）
                        </span>
                        <span v-else>
                            Installation (normal)
                        </span>
                    </button>
                    <button @click="gitClone(inputValue, 1)">
                        <span v-if="CHENFLAF">
                            安装（加速1）
                        </span>
                        <span v-else>
                            Installation (Acceleration 1)
                        </span>
                    </button>
                    <button @click="gitClone(inputValue, 2)">
                        <span v-if="CHENFLAF">
                            安装（加速2）
                        </span>
                        <span v-else>
                            Installation (Acceleration 2)
                        </span>
                    </button>
                    <div>
                        <div class="link-div">
                            <div class="sub-link-div">{{ CHENFLAF ? "名称/作者" : "name/author" }}</div>
                            <div class="sub-link-div">{{ CHENFLAF ? "地址" : "url" }}</div>
                            <div class="sub-link-div">{{ CHENFLAF ? "操作" : "operation" }}</div>
                        </div>
                        <div class="link-div" v-for="(item, index) in customNodeLink" :key="index + item.name"
                            :ref="index + refEnd">
                            <div class="sub-link-div">
                                <div v-html="item.name"></div>
                                <div class="gray" v-html="item.author"></div>
                            </div>
                            <div class="sub-link-div">
                                <div v-if="item.gitUrl" class="green text-dec1" @click="openUrl_(item.gitUrl)">gitUrl:▶
                                    <span class="blue fontsize12 text-dec" v-html="item.gitUrl"></span>
                                </div>
                                <div v-if="item.civitaiUrl" class="red text-dec1" @click="openUrl_(item.civitaiUrl)">
                                    civitaiUrl:▶
                                    <span class="red1 fontsize12 text-dec" v-html="item.civitaiUrl"></span>
                                </div>
                            </div>
                            <div class="sub-link-div" v-if="item.installed && item.installed == 1">
                                <button :disabled="true">{{ CHENFLAF ? "已安装" :
                                    "Installed" }}</button>
                            </div>
                            <div class="sub-link-div" v-else-if="item.installed && item.installed == 2">
                                <button :disabled="true">{{ CHENFLAF ? "安装中" :
                                    "Installation in progress" }}</button>
                            </div>
                            <div class="sub-link-div" v-else-if="item.gitUrl">
                                <button @click="check_git_url(item.gitUrl, 0, index)">{{ CHENFLAF ? "安装(普通)" :
                                    "Installation(normal)" }}</button>
                                <button @click="check_git_url(item.gitUrl, 1, index)">{{ CHENFLAF ? "安装(加速1)" :
                                    "Installation(Acceleration1)" }}</button>
                                <button @click="check_git_url(item.gitUrl, 2, index)">{{ CHENFLAF ? "安装(加速2)" :
                                    "Installation(Acceleration2)" }}</button>
                            </div>
                            <div class="sub-link-div" v-else>
                                <button @click="openUrl_(item.civitaiUrl)">{{ CHENFLAF ? "打开网址" : "Open URL" }}</button>
                            </div>
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
    props: {
        CHENFLAF: {
            type: Boolean,
            default: true,
        },
    },
    data() {
        return {
            isUpdate: false,
            pageIndex: 0,
            searchValue: '',
            refEnd: 'customNodeLink',
            customNodeList: [],
            customNodeLink: [],
            customNodeLinkBk: [],
            // customNodeList: [],
            inputValue: '',
            nogitTip: "非git版，无法对版本进行操作，请自行前往原作者发布地方查看是否有更新",
            nogitTipEn: "Non git version, you cannot operate on the version, please go to the original author To see if there is an update",
            emoji: ['(≧∇≦)ﾉ', '(+.+)(-.-)(_ _) ..zzZZ もうだめ', 'ヾ(≧O≦)〃嗷~', '٩(๑òωó๑)۶', '( *￣▽￣)((≧︶≦*)', '（*＾-＾*）', '...(*￣０￣)ノ[等等我…]', 'n(*≧▽≦*)n', '(～o￣▽￣)～o 。。。滚来滚去……o～(＿△＿o～) ~。。。', '不＞(￣ε￣ = ￣3￣)<要', '.....((/- -)/', '-________-', '(*￣▽￣)(￣▽:;.…::;.:.:::;..::;.:...', '『家』 ～o(▽｀ o) =3 =3 =3', '＼（＾∀＾）メ（＾∀＾）ノ', '(*/ω＼*)/p.', '◕ฺ‿◕ฺ✿ฺ)', 'Ψ(￣∀￣)Ψ', '( *^-^)ρ(^0^* )', '↑↑↓↓←→←→ＢＡ...┗( -o-)┛', '（￣ー￣）ノ~~マ☆’.・.・:★', '．《{=．．．．（嘎~嘎~嘎~）'],
        };
    },

    watch: {
        searchValue() {
            if (this.searchValue && this.searchValue.length > 0) {
                this.search();
            } else {
                this.customNodeLink = JSON.parse(JSON.stringify(this.customNodeLinkBk))
            }
        }
    },

    mounted() {
        // // TODO: test
        // this.customNodeList = [{ 'name': 'comfy_translation_node', 'path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node', 'git_detail': { 'name': 'HEAD', 'localHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'localTime': '2023-04-24T20:59:04', 'newHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'newTime': '2023-04-24T20:59:04' }, 'rep_path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node' }, { 'name': 'comfy_translation_node', 'path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node', 'git_detail': { 'name': 'HEAD', 'localHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'localTime': '2023-04-24T20:59:04', 'newHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'newTime': '2023-04-24T20:59:04' }, 'rep_path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node' }, { 'name': 'comfy_translation_node', 'path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node', 'git_detail': { 'name': 'HEAD', 'localHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'localTime': '2023-04-24T20:59:04', 'newHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'newTime': '2023-04-24T20:59:04' }, 'rep_path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node' }, { 'name': 'comfy_translation_node', 'path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node', 'git_detail': { 'name': 'HEAD', 'localHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'localTime': '2023-04-24T20:59:04', 'newHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'newTime': '2023-04-24T20:59:04' }, 'rep_path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node' }, { 'name': 'comfy_translation_node', 'path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node', 'git_detail': { 'name': 'HEAD', 'localHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'localTime': '2023-04-24T20:59:04', 'newHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'newTime': '2023-04-24T20:59:04' }, 'rep_path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node' }, { 'name': 'comfy_translation_node', 'path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node', 'git_detail': { 'name': 'HEAD', 'localHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'localTime': '2023-04-24T20:59:04', 'newHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'newTime': '2023-04-24T20:59:04' }, 'rep_path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node' }, { 'name': 'comfy_translation_node', 'path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node', 'git_detail': { 'name': 'HEAD', 'localHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'localTime': '2023-04-24T20:59:04', 'newHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'newTime': '2023-04-24T20:59:04' }, 'rep_path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node' }, { 'name': 'comfy_translation_node', 'path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node', 'git_detail': { 'name': 'HEAD', 'localHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'localTime': '2023-04-24T20:59:04', 'newHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'newTime': '2023-04-24T20:59:04' }, 'rep_path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node' }, { 'name': 'comfy_translation_node', 'path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node', 'git_detail': { 'name': 'HEAD', 'localHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'localTime': '2023-04-24T20:59:04', 'newHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'newTime': '2023-04-24T20:59:04' }, 'rep_path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node' }, { 'name': 'comfy_translation_node', 'path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node', 'git_detail': { 'name': 'HEAD', 'localHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'localTime': '2023-04-24T20:59:04', 'newHexsha': 'f8facad6c3b5baed838714b6673a9910f2b312dd', 'newTime': '2023-04-24T20:59:04' }, 'rep_path': 'f:\\测试文件夹\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\comfy_translation_node' }]
        // this.customNodeLink = [{ "author": "xww", "civitaiUrl": "https://civitai.com/models/42647/comfyui-comfytranslationnode", "gitUrl": "https://github.com/laojingwei/comfy_translation_node", "name": "comfy_translation_node" }, { "author": "xww", "civitaiUrl": "https://civitai.com/models/49851/comfyui-comfyassembletagsnode", "gitUrl": "https://github.com/laojingwei/comfy_assemble_tags_node", "name": "comfy_assemble_tags_node" }, { "author": "paulo-coronado", "civitaiUrl": "https://civitai.com/models/42974/comfyui-clip-blip-node", "gitUrl": "https://github.com/paulo-coronado/comfy_clip_blip_node", "name": "comfy_clip_blip_node" }, { "author": "space-nuko", "civitaiUrl": "", "gitUrl": "https://github.com/space-nuko/ComfyBox", "name": "ComfyBox" }, { "author": "camenduru", "civitaiUrl": "https://civitai.com/models/25284/comfyui-colab", "gitUrl": "https://github.com/camenduru/comfyui-colab", "name": "comfyui-colab" }, { "author": "ltdrdata", "civitaiUrl": "", "gitUrl": "https://github.com/ltdrdata/ComfyUI-Manager", "name": "ComfyUI-Manager" }, { "author": "rvion", "civitaiUrl": "", "gitUrl": "https://github.com/rvion/CushyNodes", "name": "CushyNodes" }, { "author": "rvion", "civitaiUrl": "", "gitUrl": "https://github.com/rvion/CushyStudio", "name": "CushyStudio" }, { "author": "WASasquatch", "civitaiUrl": "", "gitUrl": "https://github.com/WASasquatch/comfyui-plugins", "name": "comfyui-plugins" }, { "author": "diontimmer", "civitaiUrl": "https://civitai.com/models/24869/comfyui-custom-nodes-by-xss", "gitUrl": "https://github.com/diontimmer/ComfyUI-Vextra-Nodes", "name": "ComfyUI-Vextra-Nodes" }, { "author": "BlenderNeko", "civitaiUrl": "https://civitai.com/models/28295/cutoff-for-comfyui", "gitUrl": "https://github.com/BlenderNeko/ComfyUI_Cutoff", "name": "ComfyUI_Cutoff" }, { "author": "Derfuu", "civitaiUrl": "https://civitai.com/models/21558/", "gitUrl": "https://github.com/Derfuu/Derfuu_ComfyUI_ModdedNodes", "name": "Derfuu_ComfyUI_ModdedNodes" }, { "author": "LucianoCirino", "civitaiUrl": "https://civitai.com/models/32342/efficiency-nodes-for-comfyui", "gitUrl": "https://github.com/LucianoCirino/efficiency-nodes-comfyui", "name": "efficiency-nodes-comfyui" }, { "author": "m99", "civitaiUrl": "https://civitai.com/models/24690/", "gitUrl": "", "name": "facerestore" }, { "author": "Isle_of_Chaos", "civitaiUrl": "", "gitUrl": "https://civitai.com/models/31696/gpt-node-comfyui", "name": "gpt-node-comfyui" }, { "author": "LEv145", "civitaiUrl": "https://civitai.com/models/31126/imagesgrid-comfy-plugin-xy-plot", "gitUrl": "https://github.com/LEv145/images-grid-comfy-plugin", "name": "images-grid-comfy-plugin" }, { "author": "ltdrdata", "civitaiUrl": "https://civitai.com/models/33192/comfyui-impact-pack", "gitUrl": "https://github.com/ltdrdata/ComfyUI-Impact-Pack", "name": "ComfyUI-Impact-Pack" }, { "author": "m99", "civitaiUrl": "https://civitai.com/models/26836/comfyui-loopback-nodes", "gitUrl": "", "name": "comfyui-loopback-nodes" }, { "author": "BadCafeCode", "civitaiUrl": "https://civitai.com/models/52723/masquerade-nodes-comfyui", "gitUrl": "https://github.com/BadCafeCode/masquerade-nodes-comfyui", "name": "masquerade-nodes-comfyui" }, { "author": "Bocian", "civitaiUrl": "https://civitai.com/models/21100/", "gitUrl": "", "name": "Multiple Subject Workflows" }, { "author": "CyberSnacc", "civitaiUrl": "https://civitai.com/models/50440/comfyui-node-setup-lora-stack", "gitUrl": "", "name": "comfyui-node-setup-lora-stack" }, { "author": "xXAdonesXx", "civitaiUrl": "https://civitai.com/models/33905/nodegpt", "gitUrl": "https://github.com/xXAdonesXx/NodeGPT", "name": "NodeGPT" }, { "author": "BlenderNeko", "civitaiUrl": "https://civitai.com/models/46229", "gitUrl": "https://github.com/BlenderNeko/ComfyUI_ADV_CLIP_emb", "name": "ComfyUI_ADV_CLIP_emb" }, { "author": "omar92", "civitaiUrl": "https://civitai.com/models/21996", "gitUrl": "https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92", "name": "QualityOfLifeSuit_Omar92" }, { "author": "Kaharos94", "civitaiUrl": "", "gitUrl": "https://github.com/Kaharos94/ComfyUI-Saveaswebp", "name": "ComfyUI-Saveaswebp" }, { "author": "fretts4505", "civitaiUrl": "https://civitai.com/models/28238/simple-text-style-template-node-for-comfyui", "gitUrl": "", "name": "simple-text-style-template-node-for-comfyui" }, { "author": "diSty", "civitaiUrl": "https://civitai.com/models/27574/", "gitUrl": "https://github.com/diStyApps/seait", "name": "seait" }, { "author": "sylym", "civitaiUrl": "https://civitai.com/models/26799/vid2vid-node-suite-for-comfyui", "gitUrl": "https://github.com/sylym/comfy_vid2vid", "name": "comfy_vid2vid" }, { "author": "ComfyUI_Dave_CustomNode", "civitaiUrl": "https://civitai.com/models/24537/", "gitUrl": "https://github.com/Davemane42/ComfyUI_Dave_CustomNode", "name": "Davemane42" }, { "author": "WASasquatch", "civitaiUrl": "https://civitai.com/models/20215/wass-comfyui-workspaces-hr-fix-and-more", "gitUrl": "", "name": "wass-comfyui-workspaces-hr-fix-and-more" }, { "author": "WASasquatch", "civitaiUrl": "https://civitai.com/models/20793/", "gitUrl": "https://github.com/WASasquatch/was-node-suite-comfyui", "name": "was-node-suite-comfyui" }, { "author": "ctdde", "civitaiUrl": "https://civitai.com/models/22651/", "gitUrl": "", "name": "ComfyUI Workflows" }, { "author": "CyberSnacc", "civitaiUrl": "https://civitai.com/models/54555/embeddingscompare-comfyui", "gitUrl": "", "name": "embeddings_compare" }, { "author": "pythongosssss", "civitaiUrl": "", "gitUrl": "https://github.com/pythongosssss/ComfyUI-Custom-Scripts", "name": "ComfyUI-Custom-Scripts" }, { "author": "lilly1987", "civitaiUrl": "https://civitai.com/models/21611/", "gitUrl": "https://github.com/lilly1987/ComfyUI_node_Lilly", "name": "ComfyUI_node_Lilly" }, { "author": "theally", "civitaiUrl": "https://civitai.com/models/20443/", "gitUrl": "", "name": "Custom Workflows" }, { "author": "theally", "civitaiUrl": "https://civitai.com/models/19625/", "gitUrl": "", "name": "ComfyUI Custom Nodes" }, { "author": "trojblue", "civitaiUrl": "", "gitUrl": "https://github.com/trojblue/trNodes", "name": "trNodes" }];
        // this.customNodeLinkBk = JSON.parse(JSON.stringify(this.customNodeLink))

        // main
        document.getElementById("tabBtn0").style.backgroundImage = "linear-gradient(to right, rgb(51 213 31), rgb(33 112 0))";
        document.getElementById("tabBtn1").style.backgroundImage = "linear-gradient(to right, rgb(0, 0, 0), rgb(183, 183, 183))";
        if (!this.$GitCloneFlag || this.$GitCloneFlag.indexOf("start#-#") === -1) {
            this.$Xwwqt.get_node_data();
        }
        this.getData(1000);
    },

    methods: {
        clear() {
            this.searchValue = "";
        },
        search() {
            if (this.searchValue && this.customNodeLink) {
                let reg = new RegExp(this.searchValue, "gi")
                this.customNodeLink = JSON.parse(JSON.stringify(this.customNodeLinkBk))
                // let scrollI = null;
                // let refVal = null;
                let list = this.customNodeLink;
                let list1 = [];
                for (let i = 0; i < list.length; i++) {
                    let name = list[i].name;
                    let author = list[i].author;
                    let gitUrl = list[i].gitUrl;
                    let civitaiUrl = list[i].civitaiUrl;
                    let m = 0;
                    if (name.match(reg)) {
                        // !refVal && (refVal = `${i}${this.refEnd}`);
                        list[i].name = name.replace(reg, function (match) {
                            return `<span style="background-color: #55ff00;">${match}</span>`;
                        });
                        m = 1;
                    }
                    if (author.match(reg)) {
                        // !refVal && (refVal = `${i}${this.refEnd}`);
                        list[i].author = author.replace(reg, function (match) {
                            return `<span style="background-color: #55ff00;">${match}</span>`;
                        });
                        m = 1;
                    }
                    if (gitUrl.match(reg)) {
                        // !refVal && (refVal = `${i}${this.refEnd}`);
                        list[i].gitUrl = gitUrl.replace(reg, function (match) {
                            return `<span style="background-color: #55ff00;">${match}</span>`;
                        });
                        m = 1;
                    }
                    if (civitaiUrl.match(reg)) {
                        // !refVal && (refVal = `${i}${this.refEnd}`);
                        list[i].civitaiUrl = civitaiUrl.replace(reg, function (match) {
                            return `<span style="background-color: #55ff00;">${match}</span>`;
                        });
                        m = 1;
                    }
                    if (m == 1) {
                        list1.push(list[i]);
                    }
                }
                this.customNodeLink = list1;
                // if (refVal) {
                //     let targetbox = this.$refs[refVal][0];
                //     this.$refs['customNodeLoadDiv'].scrollTop = targetbox.offsetTop;
                // }
            }
        },
        check_git_url(url, i, j) {
            if (url) {
                !url.endsWith(".git") && (url = `${url}.git`)
                this.gitClone(url, i, j)
            }
        },
        openUrl_(url) {
            url && this.$Xwwqt.openUrl(url)
        },
        openUrl(item, hexsha) {
            item.git_detail.gitUrl && this.$Xwwqt.openUrl(item.git_detail.gitUrl + hexsha)
        },
        file_stat_tips(e) {
            if (e) {
                this.$Toast.show(this.CHENFLAF ? '禁用期间，启动ComfyUI控制台出现下面提示是正常的： Skip F:\\xxx\\ComfyUI_windows_portable\ComfyUI\\custom_nodes\\xxx module for custom nodes due to the lack of NODE_CLASS_MAPPINGS.' : 'When disabled, the following message is normal when starting the ComfyUI console: Skip F:\\xxx\\ComfyUI_windows_portable\ComfyUI\\custom_nodes\\xxx module for custom nodes due to the lack of NODE_CLASS_MAPPINGS.', 30000, e.clientX, e.clientY);
            } else {
                this.$Toast.hide();
            }
        },
        file_statusTime(index) {
            this.file_statusTimer && clearTimeout(this.file_statusTimer);
            this.file_statusTimer = setTimeout(() => {
                clearTimeout(this.file_statusTimer);
                if (this.$GitFlag && this.$GitFlag !== "start") {
                    if (this.$GitFlag === "error") {
                        this.$Toast.show(this.CHENFLAF ? '设置失败' : 'Setting failure', 3000);
                    } else if (this.$GitFlag === "warn") {
                        this.$Toast.show(this.CHENFLAF ? '设置失败' : 'Setting failure', 3000);
                    } else {
                        this.customNodeList[index].git_detail["fileStat"] = this.$GitFlag;
                        this.$Toast.show(this.CHENFLAF ? '设置成功' : 'Setting  Successful', 3000);
                    }
                } else {
                    this.$Toast.show(this.CHENFLAF ? '正在努力处理中。。。' : 'Is trying to deal with...');
                    this.file_statusTime(index);
                }
            }, 1000);
        },
        file_status(item, index) {
            let type = item.git_detail["fileStat"] === "1" ? "ban" : "use";
            this.$Toast.show(this.CHENFLAF ? '正在刷新中。。。' : 'Being refreshed...');
            this.$Xwwqt.file_stat(item.path, type);
            this.file_statusTime(index);
        },
        refreshTime(index) {
            this.refreshTimer && clearTimeout(this.refreshTimer);
            this.refreshTimer = setTimeout(() => {
                clearTimeout(this.refreshTimer);
                if (this.$RefreshData && this.$RefreshData[0] !== "NONE") {
                    if (this.$RefreshData[0] === "error") {
                        this.$Toast.show(this.CHENFLAF ? '刷新失败' : 'Refresh failure', 3000);
                    } else {
                        this.customNodeList[index].git_detail = this.$RefreshData[0];
                        this.$Toast.show(this.CHENFLAF ? '刷新成功' : 'Refresh successfully', 3000);
                    }
                } else {
                    this.tip = this.CHENFLAF ? ['正在获取自定义节点最新信息。。。', '这么慢？嗯，是有点慢。。。', '努力加载中，请稍等。。。', '国内gitHub环境就这样。。。', '有时稍微等会也是一种放松。。。'] : ['Getting updates on custom nodes... ', ' so slow? Well, a little slow... ', 'trying to load, please wait... ', ' the domestic gitHub environment is like this... ', 'sometimes waiting a little is a kind of relaxation... ']
                    this.$Toast.show(this.tip[Math.floor(Math.random() * 5)] + this.emoji[Math.floor(Math.random() * 20)]);
                    this.refreshTime(index);
                }
            }, 1000);
        },
        refresh(item, index) {
            if (item.git_detail && item.git_detail.noGit === "Y") {
                this.$Toast.show(this.CHENFLAF ? '该节点不是git版本，无法进行刷新' : 'This node is not a git version and cannot be refreshed', 4000);
                return;
            }
            this.$Toast.show(this.CHENFLAF ? '正在刷新中。。。' : 'Being refreshed...');
            this.$Xwwqt.refresh_data(item.path, item.name);
            this.refreshTime(index);
        },
        gitCloneTime(index, j) {
            let name = "gitCloneTimer";
            if (j || j == 0) {
                name = this.customNodeLink[j]["name"];
            }
            this[name] && clearTimeout(this[name]);
            this[name] = setTimeout(() => {
                clearTimeout(this[name]);
                if (this.$GitCloneFlag === "start#-#" + name) {
                    this.$Toast.show((this.CHENFLAF ? '正在努力安装中。。。' : 'Working on installation...') + this.emoji[Math.floor(Math.random() * 20)]);
                    this.gitCloneTime(index, j);
                } else {
                    if (this.$GitCloneFlag === "error#-#" + name) {
                        if (j || j == 0) {
                            this.customNodeLink[j]["installed"] = "";
                            this.customNodeLinkBk[j]["installed"] = "";
                        }
                        this.$Toast.show(this.CHENFLAF ? '安装失败' : 'Installation failure', 3000);
                    } else if (this.$GitCloneFlag === "warn#-#" + name) {
                        if (j || j == 0) {
                            this.customNodeLink[j]["installed"] = "";
                            this.customNodeLinkBk[j]["installed"] = "";
                        }
                        this.$Toast.show(this.CHENFLAF ? '安装失败，请查看控制台详细信息' : 'Installation failed. Please see console details', 3000);
                    } else {
                        if (j || j == 0) {
                            this.customNodeLink[j]["installed"] = "1";
                            this.customNodeLinkBk[j]["installed"] = "1";
                        }
                        this.$Toast.show(this.CHENFLAF ? '安装成功' : 'Successful installation', 3000);
                        this.isUpdate = true;
                    }
                }
            }, 1000);
        },
        gitClone(path, i, j) {
            if (!path) {
                this.$Toast.show(this.CHENFLAF ? '链接地址不能为空' : 'The link address cannot be empty');
                return;
            }
            if (this.$GitCloneFlag && this.$GitCloneFlag.indexOf("start#-#") !== -1) {
                this.$Toast.show(this.CHENFLAF ? '已有在执行中的安装任务，请等待该任务安装完成后再重试' : 'An installation task is in progress. Wait until the installation is complete and try again');
                return;
            }
            let name = 'gitCloneTimer';
            if (j || j == 0) {
                this.customNodeLink[j]["installed"] = "2";
                this.customNodeLinkBk[j]["installed"] = "2";
                name = this.customNodeLink[j]["name"];
            }
            this.$Toast.show(this.CHENFLAF ? '正在安装中。。。' : 'Being installed...');
            this.$Xwwqt.clone_from(path, i, name);
            this.gitCloneTime(i, j);
        },
        changeShow(i) {
            if (this.pageIndex === i) {
                return;
            }
            this.$velocity(this.$refs.customNodeLoadDiv, "finish");
            this.$velocity(this.$refs.customNodeListDiv, "finish");
            this.pageIndex = i;
            if (i === 0) {
                if (!this.$GitCloneFlag || this.$GitCloneFlag.indexOf("start#-#") === -1) {
                    if (this.isUpdate) {
                        this.isUpdate = false;
                        this.$Xwwqt.get_node_data();
                    }
                }
                this.getData(1000);
                document.getElementById("tabBtn0").style.backgroundImage = "linear-gradient(to right, rgb(51 213 31), rgb(33 112 0))";
                document.getElementById("tabBtn1").style.backgroundImage = "linear-gradient(to right, rgb(0, 0, 0), rgb(183, 183, 183))";
                this.$velocity(this.$refs.customNodeLoadDiv, { left: "200%" }, { duration: 500 });
                this.$velocity(this.$refs.customNodeListDiv, { left: 0 }, { duration: 500 });
            } else {
                document.getElementById("tabBtn1").style.backgroundImage = "linear-gradient(to right, rgb(51 213 31), rgb(33 112 0))";
                document.getElementById("tabBtn0").style.backgroundImage = "linear-gradient(to right, rgb(0, 0, 0), rgb(183, 183, 183))";
                this.$velocity(this.$refs.customNodeLoadDiv, { left: 0 }, { duration: 500 });
                this.$velocity(this.$refs.customNodeListDiv, { left: "200%" }, { duration: 500 });
                if (!this.$GitCloneFlag || this.$GitCloneFlag.indexOf("start#-#") === -1) {
                    this.$Xwwqt.getCustomNodeLink();
                }
                this.customNodeLinkTime();
            }
            this.pageIndex = i;
        },
        customNodeLinkTime() {
            this.customNodeLinkTimer = setTimeout(() => {
                clearTimeout(this.customNodeLinkTimer);
                if (this.$CustomNodeLink) {
                    this.customNodeLink = this.$CustomNodeLink;
                    this.customNodeLinkBk = JSON.parse(JSON.stringify(this.customNodeLink))
                    // this.$Xwwqt.py_print(JSON.stringify(this.customNodeLink))
                } else {
                    this.customNodeLinkTime();
                }
            }, 500);
        },
        subStringF(str, i) {
            if (!str) {
                return '';
            }
            return str.substring(0, i) + '...';
        },
        getData(t) {
            this.mountedCustomNodeTimer = setTimeout(() => {
                clearTimeout(this.mountedCustomNodeTimer);
                if (this.$GitData && this.$GitData[0] === "error") {
                    this.$Toast.show(this.CHENFLAF ? "获取数据失败。。。" : 'Failed to obtain data...', 3000);
                } else if (this.$GitData && this.$GitData[0] !== "NONE") {
                    this.customNodeList = this.$GitData;
                } else {
                    this.$Toast.show((this.CHENFLAF ? "获取数据中。。。" : 'Obtain data in...') + this.emoji[Math.floor(Math.random() * 20)]);
                    this.getData(2000);
                }
            }, t);
        },
        checkout(item, index, prev) {
            if (item.git_detail.fileStat !== '1') {
                this.$Toast.show(this.CHENFLAF ? '请先启用再切换。。。' : 'Please enable before switching...');
                return;
            }
            if (!prev && item.git_detail.localHexsha === item.git_detail.newHexsha) {
                this.$Toast.show(this.CHENFLAF ? '你当前代码已是最新' : 'Your current code is up to date', 3000);
                return;
            }
            this.$Toast.show(this.CHENFLAF ? '切换中。。。' : 'Switching...');
            let path = item.path;
            let hexsha = prev ? prev : item.git_detail.newHexsha;
            this.$Xwwqt.git_checkout(path, hexsha, item.name);
            this.checkout_resTime(index);
        },
        checkout_resTime(index) {
            this.checkoutResTimer && clearTimeout(this.checkoutResTimer);
            this.checkoutResTimer = setTimeout(() => {
                clearTimeout(this.checkoutResTimer);
                if (this.$CheckoutGitData && this.$CheckoutGitData[0] !== "NONE") {
                    if (this.$CheckoutGitData[0] === "error") {
                        this.$Toast.show(this.CHENFLAF ? '切换失败' : 'Switchover failure', 3000);
                    } else {
                        this.customNodeList[index].git_detail = this.$CheckoutGitData[0];
                        this.$Toast.show(this.CHENFLAF ? '切换成功' : 'Successful switchover', 3000);
                    }
                } else {
                    this.$Toast.show((this.CHENFLAF ? '努力切换中。。。' : 'Trying to switch...') + this.emoji[Math.floor(Math.random() * 20)]);
                    this.checkout_resTime(index);
                }
            }, 1000);
        },
        opendir(item) {
            this.$Xwwqt.open_local_file(item.path, 'dir');
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

.text-dec {
    text-decoration: underline
}

.text-dec:hover {
    transform: scale(1.2);
}

.text-dec:active {
    transform: scale(0.9);
}

.text-dec1:hover {
    transform: scale(1.2);
}

.text-dec1:active {
    transform: scale(0.9);
}

.custom-node-box {
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
    height: 95vh;
    overflow: hidden;
}

.custom-node-search {
    display: flex;
    justify-content: flex-start;
    position: absolute;
    top: 75px;
    left: 30px;
    width: 100%;
    height: auto;
}

.custom-node-search-ipt {
    width: 50%;
    height: auto;
    margin-left: 25%;
    border-radius: 4px;
}

.custom-node-search-btn {
    margin-left: 10px;
    border-radius: 4px;
}

.custom-node-search-btn:hover {
    color: #38a302;
    transform: scale(1.1);
}

.custom-node-search-btn:active {
    transform: scale(0.9);
}

.custom-node-tab {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: auto;
}

.custom-node-tab .button:hover {
    color: #55ff00;
    transform: scale(1.1);
    background-image: linear-gradient(to right, rgb(0, 0, 0), rgb(129, 128, 128));
}

.custom-node-tab .button {
    margin: 30px 20px;
    padding: 10px;
    font-size: 14px;
    color: #ffffff;
    border-radius: 8px;
    opacity: 1;
    background-image: linear-gradient(to right, rgb(0, 0, 0), rgb(183, 183, 183));
}

.custom-node-tab .button:active {
    /* opacity: 0.8; */
    transform: scale(0.95);
    background-image: linear-gradient(to right, rgb(63, 75, 62), rgb(0, 255, 34));
}

.custom-node-list {
    position: absolute;
    top: 100px;
    left: 0;
    right: 0;
    width: 100%;
    height: 100%;
    padding: 10px 10px;
    overflow: scroll;
    color: #FFFFFF;
    /* transform: 1; */
    /* background-color: #55ff00; */
}

.custom-node-load {
    position: absolute;
    top: 100px;
    left: 200%;
    right: 0;
    width: 100%;
    height: 100%;
    padding: 10px 10px;
    overflow: scroll;
    color: #FFFFFF;
    /* transform: 1; */
}

.custom-node-load-div {
    display: flex;
    flex-direction: column;
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
}

.custom-node-load-label {
    padding: 10px;
    color: #45bb00;
    text-align: center;
    align-items: center;
    background: rgba(0, 0, 0, 0.8);
    ;
    border-radius: 5px;
}

.custom-node-load textarea {
    min-width: 50%;
    max-width: 99.8%;
    background: #000000;
    color: #ffffff;
    border-radius: 5px;
}

.custom-node-load input {
    font-size: 20px;
    height: 50px;
    border: 1px solid #000000;
    border-radius: 2px;
    text-align: center;
    align-items: center;
}

.custom-node-load button:hover {
    transform: scale(1.05);
}

.custom-node-load button {
    font-size: 24px;
    margin: 10px 30%;
    width: 40%;
    /* background: #8d77d1; */
    background-image: linear-gradient(rgb(51, 51, 51), #fffdfd);
    border: 1px solid #000000;
    border-radius: 8px;
}

.custom-node-load button:active {
    /* opacity: 0.8; */
    transform: scale(0.95);
    background-image: linear-gradient(rgb(80, 79, 79), rgb(255, 255, 255));
}

.cntl-div {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    width: 100%;
    height: 100px;
    /* padding: 10px; */
    border: 1px solid #FFFFFF;
    background: rgb(0, 0, 0, 0.8);
}


.cntl-div:hover {
    color: #444cea;
    background-color: rgb(31, 42, 26);
}

.cntl-div-sub {
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    width: 33.333%;
    height: 100px;
    border-right-style: solid;
    font-size: 14px;
}

.cntl-div-sub:last-child {
    width: 33.333%;
    border-right-style: none;
}

.sub-cntl-div-detail {
    border: 1px solid #FFFFFF;
}

.fontsize12 {
    font-size: 12px;
}

.gray {
    color: gray;
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

.green-bg {
    background-color: #55ff00;
}

.red {
    color: red;
}

.red1 {
    color: #ef6868;
}

.sub-button {
    margin: 5px 5px;
    border: 1px solid #000000;
    border-radius: 5px;
    font-size: 12px;
}

.sub-button:hover {
    transform: scale(1.2);
    background-color: rgb(193, 213, 191);
    color: #38a302 !important;
}

.sub-button:active {
    transform: scale(0.9);
}


.link-div {
    display: flex;
    justify-content: flex-start;
    width: 100%;
    height: auto;
    background: rgb(0, 0, 0, 0.8);
    border: 1px solid #ffffff;
    text-align: center;
    align-items: center;
}

.link-div:hover {
    color: #444cea;
    background-color: rgb(31, 42, 26);
}

.link-div button {
    min-width: 100px;
    width: auto;
    font-size: 14px;
    margin: 0 0 5px;
}

.sub-link-div {
    display: flex;
    border-right-style: solid;
    flex-direction: column;
    padding: 5px;
    width: 33%;
    min-height: 90px;
    text-align: center;
    /* line-height: 2; */
    align-items: center;
    word-wrap: break-word;
    word-break: break-all;
    justify-content: center;
}

.sub-link-div:last-child {
    border-right-style: none;
}
</style>
