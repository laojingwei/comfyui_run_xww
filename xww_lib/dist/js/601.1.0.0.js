"use strict";(self["webpackChunkxww"]=self["webpackChunkxww"]||[]).push([[601],{5601:function(t,i,e){e.r(i),e.d(i,{default:function(){return c}});var s=function(){var t=this,i=t._self._c;return i("show-page",[i("div",{staticClass:"custom-node-box"},[i("div",{staticClass:"custom-node-tab"},[i("button",{staticClass:"button",attrs:{id:"tabBtn0"},on:{click:function(i){return t.changeShow(0)}}},[t.CHENFLAF?i("span",[t._v(" 自定义节点列表 ")]):i("span",[t._v(" Customize the node list ")])]),i("button",{staticClass:"button",attrs:{id:"tabBtn1"},on:{click:function(i){return t.changeShow(1)}}},[t.CHENFLAF?i("span",[t._v(" 自定义节点下载地址 ")]):i("span",[t._v(" Customize the node download address ")])])]),1==t.pageIndex?i("div",{staticClass:"custom-node-search"},[i("input",{directives:[{name:"model",rawName:"v-model",value:t.searchValue,expression:"searchValue"}],staticClass:"custom-node-search-ipt",attrs:{type:"text",placeholder:t.CHENFLAF?"地址太多不好找？试试输入内容精确查找吧":"Too many addresses to find? Try entering content for precise search."},domProps:{value:t.searchValue},on:{input:function(i){i.target.composing||(t.searchValue=i.target.value)}}}),i("button",{staticClass:"custom-node-search-btn",on:{click:t.clear}},[t._v(t._s(t.CHENFLAF?"清空":"clear"))])]):t._e(),i("div",{ref:"customNodeListDiv",staticClass:"custom-node-list"},[t._l(t.customNodeList,(function(e,s){return i("div",{key:s+e.name},[i("div",{staticClass:"cntl-div"},[i("div",{staticClass:"cntl-div-sub"},[i("span",[t._v(t._s(e.name))]),t.CHENFLAF?i("div",[i("button",{staticClass:"sub-button",on:{click:function(i){return t.refresh(e,s)}}},[t._v("刷新")]),i("button",{staticClass:"sub-button",on:{click:function(i){return t.file_status(e,s)},mouseenter:function(i){return t.file_stat_tips(i)},mouseleave:function(i){return t.file_stat_tips()}}},["1"===e.git_detail.fileStat?i("span",{staticClass:"green1"},[t._v(" 已启用 ")]):i("span",{staticClass:"red"},[t._v(" 已禁用 ")])])]):i("div",[i("button",{staticClass:"sub-button",on:{click:function(i){return t.refresh(e,s)}}},[t._v("refresh")]),i("button",{staticClass:"sub-button",on:{click:function(i){return t.file_status(e,s)},mouseenter:function(i){return t.file_stat_tips(i)},mouseleave:function(i){return t.file_stat_tips()}}},["1"===e.git_detail.fileStat?i("span",{staticClass:"green1"},[t._v(" Enabled ")]):i("span",{staticClass:"red"},[t._v(" disabled ")])])]),e.git_detail.sourcePath?i("div",[i("button",{staticClass:"sub-button",on:{click:function(i){return t.openUrl_(e.git_detail.sourcePath+"#readme")}}},[t._v(t._s(t.CHENFLAF?"使用说明":"instructions"))])]):t._e()]),e.git_detail&&e.git_detail.localHexsha?i("div",{staticClass:"cntl-div-sub"},[i("div",[t.CHENFLAF?i("span",[t._v(" 当前版本： ")]):i("span",[t._v(" Current Version: ")]),i("span",[t._v(t._s(e.git_detail.localTime))]),i("div",{staticClass:"green text-dec",on:{click:function(i){return t.openUrl(e,e.git_detail.localHexsha)}}},[t._v(t._s(t.subStringF(e.git_detail.localHexsha,20)))])]),t.CHENFLAF?i("div",["1"===e.git_detail.isNew?i("span",[t._v("远程最新版本：")]):i("span",[t._v("本地最新版本：")]),i("span",[t._v(t._s(e.git_detail.newTime))]),i("div",{staticClass:"blue text-dec",on:{click:function(i){return t.openUrl(e,e.git_detail.newHexsha)}}},[t._v(t._s(t.subStringF(e.git_detail.newHexsha,20)))])]):i("div",["1"===e.git_detail.isNew?i("span",[t._v("Remote latest version:")]):i("span",[t._v("Latest Local version:")]),i("span",[t._v(t._s(e.git_detail.newTime))]),i("div",{staticClass:"blue"},[t._v(t._s(t.subStringF(e.git_detail.newHexsha,20)))])])]):i("div",{staticClass:"cntl-div-sub"},[i("div",[i("span",[t._v(" "+t._s(t.CHENFLAF?t.nogitTip:t.nogitTipEn)+" ")])])]),i("div",{staticClass:"cntl-div-sub"},[e.git_detail.newHexsha?i("button",{staticClass:"sub-button",on:{click:function(i){return t.checkout(e,s)}}},[t.CHENFLAF?i("span",[t._v(" 切换到最新版 ")]):i("span",[t._v(" Switch to the latest version ")])]):t._e(),e.git_detail.prevHexsha?i("button",{staticClass:"sub-button",on:{click:function(i){return t.checkout(e,s,e.git_detail.prevHexsha)}}},[t.CHENFLAF?i("span",[t._v(" 当前版本的上一个版本 ")]):i("span",[t._v(" The previous version of the current version ")])]):t._e(),i("button",{staticClass:"sub-button",on:{click:function(i){return t.opendir(e)}}},[t.CHENFLAF?i("span",[t._v(" 打开文件夹 ")]):i("span",[t._v(" Open a folder ")])])])])])})),i("div",{staticClass:"empty-div"})],2),i("div",{ref:"customNodeLoadDiv",staticClass:"custom-node-load"},[i("div",{staticClass:"custom-node-load-div"},[i("div",{staticClass:"custom-node-load-label"},[t.CHENFLAF?i("label",[t._v("使用git地址进行克隆安装")]):i("label",[t._v("Use git address for clone installation")])]),i("textarea",{directives:[{name:"model",rawName:"v-model",value:t.inputValue,expression:"inputValue"}],attrs:{type:"text",placeholder:t.CHENFLAF?"请输入 git clone 地址，如：https://github.com/laojingwei/comfy_translation_node.git":"Enter git clone address such as：https://github.com/laojingwei/comfy_translation_node.git"},domProps:{value:t.inputValue},on:{input:function(i){i.target.composing||(t.inputValue=i.target.value)}}}),t._v(" "),i("button",{on:{click:function(i){return t.gitClone(t.inputValue,0)}}},[t.CHENFLAF?i("span",[t._v(" 安装（普通） ")]):i("span",[t._v(" Installation (normal) ")])]),i("button",{on:{click:function(i){return t.gitClone(t.inputValue,1)}}},[t.CHENFLAF?i("span",[t._v(" 安装（加速1） ")]):i("span",[t._v(" Installation (Acceleration 1) ")])]),i("button",{on:{click:function(i){return t.gitClone(t.inputValue,2)}}},[t.CHENFLAF?i("span",[t._v(" 安装（加速2） ")]):i("span",[t._v(" Installation (Acceleration 2) ")])]),i("div",[i("div",{staticClass:"link-div"},[i("div",{staticClass:"sub-link-div"},[t._v(t._s(t.CHENFLAF?"名称/作者":"name/author"))]),i("div",{staticClass:"sub-link-div"},[t._v(t._s(t.CHENFLAF?"地址":"url"))]),i("div",{staticClass:"sub-link-div"},[t._v(t._s(t.CHENFLAF?"操作":"operation"))])]),t._l(t.customNodeLink,(function(e,s){return i("div",{key:s+e.name,ref:s+t.refEnd,refInFor:!0,staticClass:"link-div"},[i("div",{staticClass:"sub-link-div"},[i("div",{domProps:{innerHTML:t._s(e.name)}}),i("div",{staticClass:"gray",domProps:{innerHTML:t._s(e.author)}})]),i("div",{staticClass:"sub-link-div"},[e.gitUrl?i("div",{staticClass:"green text-dec1",on:{click:function(i){return t.openUrl_(e.gitUrl)}}},[t._v("gitUrl:▶ "),i("span",{staticClass:"blue fontsize12 text-dec",domProps:{innerHTML:t._s(e.gitUrl)}})]):t._e(),e.civitaiUrl?i("div",{staticClass:"red text-dec1",on:{click:function(i){return t.openUrl_(e.civitaiUrl)}}},[t._v(" civitaiUrl:▶ "),i("span",{staticClass:"red1 fontsize12 text-dec",domProps:{innerHTML:t._s(e.civitaiUrl)}})]):t._e()]),e.installed&&1==e.installed?i("div",{staticClass:"sub-link-div"},[i("button",{attrs:{disabled:!0}},[t._v(t._s(t.CHENFLAF?"已安装":"Installed"))])]):e.installed&&2==e.installed?i("div",{staticClass:"sub-link-div"},[i("button",{attrs:{disabled:!0}},[t._v(t._s(t.CHENFLAF?"安装中":"Installation in progress"))])]):e.gitUrl?i("div",{staticClass:"sub-link-div"},[i("button",{on:{click:function(i){return t.check_git_url(e.gitUrl,0,s)}}},[t._v(t._s(t.CHENFLAF?"安装(普通)":"Installation(normal)"))]),i("button",{on:{click:function(i){return t.check_git_url(e.gitUrl,1,s)}}},[t._v(t._s(t.CHENFLAF?"安装(加速1)":"Installation(Acceleration1)"))]),i("button",{on:{click:function(i){return t.check_git_url(e.gitUrl,2,s)}}},[t._v(t._s(t.CHENFLAF?"安装(加速2)":"Installation(Acceleration2)"))])]):i("div",{staticClass:"sub-link-div"},[i("button",{on:{click:function(i){return t.openUrl_(e.civitaiUrl)}}},[t._v(t._s(t.CHENFLAF?"打开网址":"Open URL"))])])])}))],2),i("div",{staticClass:"empty-div"})])])])])},a=[],o=(e(7658),{props:{CHENFLAF:{type:Boolean,default:!0}},data(){return{isUpdate:!1,pageIndex:0,searchValue:"",refEnd:"customNodeLink",customNodeList:[],customNodeLink:[],customNodeLinkBk:[],inputValue:"",nogitTip:"非git版，无法对版本进行操作，请自行前往原作者发布地方查看是否有更新",nogitTipEn:"Non git version, you cannot operate on the version, please go to the original author To see if there is an update",emoji:["(≧∇≦)ﾉ","(+.+)(-.-)(_ _) ..zzZZ もうだめ","ヾ(≧O≦)〃嗷~","٩(๑òωó๑)۶","( *￣▽￣)((≧︶≦*)","（*＾-＾*）","...(*￣０￣)ノ[等等我…]","n(*≧▽≦*)n","(～o￣▽￣)～o 。。。滚来滚去……o～(＿△＿o～) ~。。。","不＞(￣ε￣ = ￣3￣)<要",".....((/- -)/","-________-","(*￣▽￣)(￣▽:;.…::;.:.:::;..::;.:...","『家』 ～o(▽｀ o) =3 =3 =3","＼（＾∀＾）メ（＾∀＾）ノ","(*/ω＼*)/p.","◕ฺ‿◕ฺ✿ฺ)","Ψ(￣∀￣)Ψ","( *^-^)ρ(^0^* )","↑↑↓↓←→←→ＢＡ...┗( -o-)┛","（￣ー￣）ノ~~マ☆’.・.・:★","．《{=．．．．（嘎~嘎~嘎~）"]}},watch:{searchValue(){this.searchValue&&this.searchValue.length>0?this.search():this.customNodeLink=JSON.parse(JSON.stringify(this.customNodeLinkBk))}},mounted(){document.getElementById("tabBtn0").style.backgroundImage="linear-gradient(to right, rgb(51 213 31), rgb(33 112 0))",document.getElementById("tabBtn1").style.backgroundImage="linear-gradient(to right, rgb(0, 0, 0), rgb(183, 183, 183))",this.$GitCloneFlag&&-1!==this.$GitCloneFlag.indexOf("start#-#")||this.$Xwwqt.get_node_data(),this.getData(1e3)},methods:{clear(){this.searchValue=""},search(){if(this.searchValue&&this.customNodeLink){let t=new RegExp(this.searchValue,"gi");this.customNodeLink=JSON.parse(JSON.stringify(this.customNodeLinkBk));let i=this.customNodeLink,e=[];for(let s=0;s<i.length;s++){let a=i[s].name,o=i[s].author,n=i[s].gitUrl,l=i[s].civitaiUrl,r=0;a.match(t)&&(i[s].name=a.replace(t,(function(t){return`<span style="background-color: #55ff00;">${t}</span>`})),r=1),o.match(t)&&(i[s].author=o.replace(t,(function(t){return`<span style="background-color: #55ff00;">${t}</span>`})),r=1),n.match(t)&&(i[s].gitUrl=n.replace(t,(function(t){return`<span style="background-color: #55ff00;">${t}</span>`})),r=1),l.match(t)&&(i[s].civitaiUrl=l.replace(t,(function(t){return`<span style="background-color: #55ff00;">${t}</span>`})),r=1),1==r&&e.push(i[s])}this.customNodeLink=e}},check_git_url(t,i,e){t&&(!t.endsWith(".git")&&(t=`${t}.git`),this.gitClone(t,i,e))},openUrl_(t){t&&this.$Xwwqt.openUrl(t)},openUrl(t,i){t.git_detail.gitUrl&&this.$Xwwqt.openUrl(t.git_detail.gitUrl+i)},file_stat_tips(t){t?this.$Toast.show(this.CHENFLAF?"禁用期间，启动ComfyUI控制台出现下面提示是正常的： Skip F:\\xxx\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\xxx module for custom nodes due to the lack of NODE_CLASS_MAPPINGS.":"When disabled, the following message is normal when starting the ComfyUI console: Skip F:\\xxx\\ComfyUI_windows_portable\\ComfyUI\\custom_nodes\\xxx module for custom nodes due to the lack of NODE_CLASS_MAPPINGS.",3e4,t.clientX,t.clientY):this.$Toast.hide()},file_statusTime(t){this.file_statusTimer&&clearTimeout(this.file_statusTimer),this.file_statusTimer=setTimeout((()=>{clearTimeout(this.file_statusTimer),this.$GitFlag&&"start"!==this.$GitFlag?"error"===this.$GitFlag||"warn"===this.$GitFlag?this.$Toast.show(this.CHENFLAF?"设置失败":"Setting failure",3e3):(this.customNodeList[t].git_detail["fileStat"]=this.$GitFlag,this.$Toast.show(this.CHENFLAF?"设置成功":"Setting  Successful",3e3)):(this.$Toast.show(this.CHENFLAF?"正在努力处理中。。。":"Is trying to deal with..."),this.file_statusTime(t))}),1e3)},file_status(t,i){let e="1"===t.git_detail["fileStat"]?"ban":"use";this.$Toast.show(this.CHENFLAF?"正在刷新中。。。":"Being refreshed..."),this.$Xwwqt.file_stat(t.path,e),this.file_statusTime(i)},refreshTime(t){this.refreshTimer&&clearTimeout(this.refreshTimer),this.refreshTimer=setTimeout((()=>{clearTimeout(this.refreshTimer),this.$RefreshData&&"NONE"!==this.$RefreshData[0]?"error"===this.$RefreshData[0]?this.$Toast.show(this.CHENFLAF?"刷新失败":"Refresh failure",3e3):(this.customNodeList[t].git_detail=this.$RefreshData[0],this.$Toast.show(this.CHENFLAF?"刷新成功":"Refresh successfully",3e3)):(this.tip=this.CHENFLAF?["正在获取自定义节点最新信息。。。","这么慢？嗯，是有点慢。。。","努力加载中，请稍等。。。","国内gitHub环境就这样。。。","有时稍微等会也是一种放松。。。"]:["Getting updates on custom nodes... "," so slow? Well, a little slow... ","trying to load, please wait... "," the domestic gitHub environment is like this... ","sometimes waiting a little is a kind of relaxation... "],this.$Toast.show(this.tip[Math.floor(5*Math.random())]+this.emoji[Math.floor(20*Math.random())]),this.refreshTime(t))}),1e3)},refresh(t,i){t.git_detail&&"Y"===t.git_detail.noGit?this.$Toast.show(this.CHENFLAF?"该节点不是git版本，无法进行刷新":"This node is not a git version and cannot be refreshed",4e3):(this.$Toast.show(this.CHENFLAF?"正在刷新中。。。":"Being refreshed..."),this.$Xwwqt.refresh_data(t.path,t.name),this.refreshTime(i))},gitCloneTime(t,i){let e="gitCloneTimer";(i||0==i)&&(e=this.customNodeLink[i]["name"]),this[e]&&clearTimeout(this[e]),this[e]=setTimeout((()=>{clearTimeout(this[e]),this.$GitCloneFlag==="start#-#"+e?(this.$Toast.show((this.CHENFLAF?"正在努力安装中。。。":"Working on installation...")+this.emoji[Math.floor(20*Math.random())]),this.gitCloneTime(t,i)):this.$GitCloneFlag==="error#-#"+e?((i||0==i)&&(this.customNodeLink[i]["installed"]="",this.customNodeLinkBk[i]["installed"]=""),this.$Toast.show(this.CHENFLAF?"安装失败":"Installation failure",3e3)):this.$GitCloneFlag==="warn#-#"+e?((i||0==i)&&(this.customNodeLink[i]["installed"]="",this.customNodeLinkBk[i]["installed"]=""),this.$Toast.show(this.CHENFLAF?"安装失败，请查看控制台详细信息":"Installation failed. Please see console details",3e3)):((i||0==i)&&(this.customNodeLink[i]["installed"]="1",this.customNodeLinkBk[i]["installed"]="1"),this.$Toast.show(this.CHENFLAF?"安装成功":"Successful installation",3e3),this.isUpdate=!0)}),1e3)},gitClone(t,i,e){if(!t)return void this.$Toast.show(this.CHENFLAF?"链接地址不能为空":"The link address cannot be empty");if(this.$GitCloneFlag&&-1!==this.$GitCloneFlag.indexOf("start#-#"))return void this.$Toast.show(this.CHENFLAF?"已有在执行中的安装任务，请等待该任务安装完成后再重试":"An installation task is in progress. Wait until the installation is complete and try again");let s="gitCloneTimer";(e||0==e)&&(this.customNodeLink[e]["installed"]="2",this.customNodeLinkBk[e]["installed"]="2",s=this.customNodeLink[e]["name"]),this.$Toast.show(this.CHENFLAF?"正在安装中。。。":"Being installed..."),this.$Xwwqt.clone_from(t,i,s),this.gitCloneTime(i,e)},changeShow(t){this.pageIndex!==t&&(this.$velocity(this.$refs.customNodeLoadDiv,"finish"),this.$velocity(this.$refs.customNodeListDiv,"finish"),this.pageIndex=t,0===t?(this.$GitCloneFlag&&-1!==this.$GitCloneFlag.indexOf("start#-#")||this.isUpdate&&(this.isUpdate=!1,this.$Xwwqt.get_node_data()),this.getData(1e3),document.getElementById("tabBtn0").style.backgroundImage="linear-gradient(to right, rgb(51 213 31), rgb(33 112 0))",document.getElementById("tabBtn1").style.backgroundImage="linear-gradient(to right, rgb(0, 0, 0), rgb(183, 183, 183))",this.$velocity(this.$refs.customNodeLoadDiv,{left:"200%"},{duration:500}),this.$velocity(this.$refs.customNodeListDiv,{left:0},{duration:500})):(document.getElementById("tabBtn1").style.backgroundImage="linear-gradient(to right, rgb(51 213 31), rgb(33 112 0))",document.getElementById("tabBtn0").style.backgroundImage="linear-gradient(to right, rgb(0, 0, 0), rgb(183, 183, 183))",this.$velocity(this.$refs.customNodeLoadDiv,{left:0},{duration:500}),this.$velocity(this.$refs.customNodeListDiv,{left:"200%"},{duration:500}),this.$GitCloneFlag&&-1!==this.$GitCloneFlag.indexOf("start#-#")||this.$Xwwqt.getCustomNodeLink(),this.customNodeLinkTime()),this.pageIndex=t)},customNodeLinkTime(){this.customNodeLinkTimer=setTimeout((()=>{clearTimeout(this.customNodeLinkTimer),this.$CustomNodeLink?(this.customNodeLink=this.$CustomNodeLink,this.customNodeLinkBk=JSON.parse(JSON.stringify(this.customNodeLink))):this.customNodeLinkTime()}),500)},subStringF(t,i){return t?t.substring(0,i)+"...":""},getData(t){this.mountedCustomNodeTimer=setTimeout((()=>{clearTimeout(this.mountedCustomNodeTimer),this.$GitData&&"error"===this.$GitData[0]?this.$Toast.show(this.CHENFLAF?"获取数据失败。。。":"Failed to obtain data...",3e3):this.$GitData&&"NONE"!==this.$GitData[0]?this.customNodeList=this.$GitData:(this.$Toast.show((this.CHENFLAF?"获取数据中。。。":"Obtain data in...")+this.emoji[Math.floor(20*Math.random())]),this.getData(2e3))}),t)},checkout(t,i,e){if("1"!==t.git_detail.fileStat)return void this.$Toast.show(this.CHENFLAF?"请先启用再切换。。。":"Please enable before switching...");if(!e&&t.git_detail.localHexsha===t.git_detail.newHexsha)return void this.$Toast.show(this.CHENFLAF?"你当前代码已是最新":"Your current code is up to date",3e3);this.$Toast.show(this.CHENFLAF?"切换中。。。":"Switching...");let s=t.path,a=e||t.git_detail.newHexsha;this.$Xwwqt.git_checkout(s,a,t.name),this.checkout_resTime(i)},checkout_resTime(t){this.checkoutResTimer&&clearTimeout(this.checkoutResTimer),this.checkoutResTimer=setTimeout((()=>{clearTimeout(this.checkoutResTimer),this.$CheckoutGitData&&"NONE"!==this.$CheckoutGitData[0]?"error"===this.$CheckoutGitData[0]?this.$Toast.show(this.CHENFLAF?"切换失败":"Switchover failure",3e3):(this.customNodeList[t].git_detail=this.$CheckoutGitData[0],this.$Toast.show(this.CHENFLAF?"切换成功":"Successful switchover",3e3)):(this.$Toast.show((this.CHENFLAF?"努力切换中。。。":"Trying to switch...")+this.emoji[Math.floor(20*Math.random())]),this.checkout_resTime(t))}),1e3)},opendir(t){this.$Xwwqt.open_local_file(t.path,"dir")}}}),n=o,l=e(1001),r=(0,l.Z)(n,s,a,!1,null,"77112599",null),c=r.exports}}]);
//# sourceMappingURL=601.1.0.0.js.map