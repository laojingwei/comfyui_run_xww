"use strict";(self["webpackChunkxww"]=self["webpackChunkxww"]||[]).push([[306],{8306:function(t,e,o){o.r(e),o.d(e,{default:function(){return r}});var a=function(){var t=this,e=t._self._c;return e("show-page",[e("img",{ref:"errImg",staticClass:"err-img",attrs:{src:o(5551)}}),e("label",[t.CHENFLAF?e("span",[t._v(" ComfyUI整合包更新：一般只需要更新ComfyUI代码就可以了，如果更新ComfyUI后没法使用，那说明作者新增了python依赖，这时可以使用“更新ComfyUI代码和python依赖”按钮进行全部更新。 ")]):e("span",[t._v(' ComfyUI integration package update: Generally, you only need to update the ComfyUI code. If the ComfyUI update cannot be used, it means that the author has added python dependencies. In this case, you can use the "Update ComfyUI code and python dependencies" button for all updates. ')])]),e("button",{on:{click:function(e){return t.updateCui("update_comfyui.bat")}}},[t.CHENFLAF?e("span",[t._v(" 只更新ComfyUI代码 ")]):e("span",[t._v(" Update ComfyUI code only ")])]),e("button",{on:{click:function(e){return t.updateCui("update_comfyui_and_python_dependencies.bat")}}},[t.CHENFLAF?e("span",[t._v(" 更新ComfyUI代码和python依赖 ")]):e("span",[t._v(" Update ComfyUI code and python dependencies ")])]),e("br"),e("br"),e("label",[t.CHENFLAF?e("span",[t._v(" 项目下载：没下载过项目的可选择下面按钮进行下载，项目大小在1.4G左右，如果你下载下来的压缩包小于1.4G，请重新下载或更换其它方式下载；如果你的网络访问gitHub比较快，推荐使用普通下载，如果比较慢，可选择国内加速进行下载，这两个加速方式本人试了好几次速度感觉还可以；如果实在运气不佳所有方式都很慢或没法下载，那你可以在bilibili里找找看哪位up主有提供百度网盘的ComfyUI整合包去下载，本人穷开不起网盘(⊙o⊙)… ")]):e("span",[t._v(" Project download: If you have not downloaded the project, you can choose the button below to download it. The size of the project is about 1.4G. If the compressed package you downloaded is less than 1.4G, please re-download or download it in other ways; If your network access to gitHub is relatively fast, it is recommended to use ordinary download, if relatively slow, you can choose to download the domestic acceleration, the speed of these two ways I have tried several times feel ok; If you are really unlucky all the way is slow or can not download, then you can look in bilibili to see which master has Baidu web disk ComfyUI integration package to download, I can not afford to open the web disk (⊙o⊙)... ")])]),e("button",{on:{click:function(e){return t.downLoad(3)}}},[t.CHENFLAF?e("span",[t._v(" 项目下载（推荐下载） ")]):e("span",[t._v(" Project download (recommended download) ")])]),e("br"),e("button",{on:{click:function(e){return t.downLoad(0)}}},[t.CHENFLAF?e("span",[t._v(" 项目下载（普通下载） ")]):e("span",[t._v(" Project download (normal download) ")])]),e("br"),e("button",{on:{click:function(e){return t.downLoad(1)}}},[t.CHENFLAF?e("span",[t._v(" 项目下载（国内加速1下载） ")]):e("span",[t._v(" Project download (Domestic accelerated 1 download) ")])]),e("br"),e("button",{on:{click:function(e){return t.downLoad(2)}}},[t.CHENFLAF?e("span",[t._v(" 项目下载（国内加速2下载） ")]):e("span",[t._v(" Project download (Domestic accelerated 2 download) ")])]),e("br"),e("br"),e("label",[t.CHENFLAF?e("span",[t._v(" 启动器版本更新：点击可更新最新版 ")]):e("span",[t._v(" Initiator version update: Click to update the latest version ")])]),t.isLatestVersion?e("button",[t.CHENFLAF?e("span",[t._v(" 已是最新 ")]):e("span",[t._v(" It's the latest version ")])]):e("button",{on:{click:t.updateXww}},[t.CHENFLAF?e("span",[t._v(" 更新 ")]):e("span",[t._v(" update ")])])])},s=[],i={props:{CHENFLAF:{type:Boolean,default:!0}},data(){return{isLatestVersion:!0,isShowErrImg:!1,emoji:["(≧∇≦)ﾉ","(+.+)(-.-)(_ _) ..zzZZ もうだめ","ヾ(≧O≦)〃嗷~","٩(๑òωó๑)۶","( *￣▽￣)((≧︶≦*)","（*＾-＾*）","...(*￣０￣)ノ[等等我…]","n(*≧▽≦*)n","(～o￣▽￣)～o 。。。滚来滚去……o～(＿△＿o～) ~。。。","不＞(￣ε￣ = ￣3￣)<要",".....((/- -)/","-________-","(*￣▽￣)(￣▽:;.…::;.:.:::;..::;.:...","『家』 ～o(▽｀ o) =3 =3 =3","＼（＾∀＾）メ（＾∀＾）ノ","(*/ω＼*)/p.","◕ฺ‿◕ฺ✿ฺ)","Ψ(￣∀￣)Ψ","( *^-^)ρ(^0^* )","↑↑↓↓←→←→ＢＡ...┗( -o-)┛","（￣ー￣）ノ~~マ☆’.・.・:★","．《{=．．．．（嘎~嘎~嘎~）"],inputValue:"",inputValue1:"",inputValue2:"",updateStart:"",updateStart1:""}},mounted(){this.$Xwwqt.check_xww_v(),this.check_xww_vTime()},methods:{check_xww_vTime(){this.check_xww_vTimer&&clearTimeout(this.check_xww_vTimer),this.check_xww_vTimer=setTimeout((()=>{if(clearTimeout(this.check_xww_vTimer),this.$UpdateXwwV&&"start"===this.$UpdateXwwV[0]){this.CHENFLAF;this.check_xww_vTime()}else if(this.$UpdateXwwV&&"error"===this.$UpdateXwwV[0]){this.CHENFLAF}else if(this.$UpdateXwwV&&this.$UpdateXwwV[0]){let t=this.$UpdateXwwV[0];if(t["localHexsha"]!==t["newHexsha"]){this.isLatestVersion=!1;let t=this.CHENFLAF?"启动器有更新，你可点击最下面启动器更新按钮进行更新":"The launcher has updated, you can click the launcher update button at the bottom to update";this.$Toast.show(t)}else this.isLatestVersion=!0}}),500)},randomString(t,e){let o="";for(let a=0;a<t;a++){let t=Math.floor(Math.random()*e.length),a=e.charAt(t);o+=a}return o},updateTimer(t,e){this.updateAllTimer&&clearTimeout(this.updateAllTimer),this.updateAllTimer=setTimeout((()=>{if(this.$Toast.hide(),clearTimeout(this.updateAllTimer),"finish"!==this.$UpdateCuiBat){this.tip=this.CHENFLAF?"正在努力处理中，请勿退出或进行其它操作。。。(进度请看控制台)":"Please do not exit or perform other operations while trying to process... (Please refer to the console for progress)";let e=[this.tip,this.randomString(this.tip.length,this.tip)];this.$Toast.show(e[Math.floor(2*Math.random())]+this.emoji[Math.floor(20*Math.random())],5e3),this.updateTimer(t,5e3)}}),e)},updateCui(t){"start"!==this.$DonloadFlag&&"start"!==this.$UpdateCuiBat&&"start"!==this.$UpdateXww?(this.$velocity(this.$refs.errImg,"finish"),this.$velocity(this.$refs.errImg,{height:400,opacity:1},{duration:3e3}),this.$velocity(this.$refs.errImg,{height:0,opacity:0},{duration:3e3,delay:2e4}),this.$Xwwqt.updateCui(t),this.updateTimer(t,100)):this.$Toast.show(this.CHENFLAF?"已有其它任务正在下载中，请稍等。。。":"Other tasks are downloading, please wait...",3e3)},updateXwwTime(){this.updateXwwTimer&&clearTimeout(this.updateXwwTimer),this.updateXwwTimer=setTimeout((()=>{clearTimeout(this.updateXwwTimer),"start"===this.$UpdateXww?(this.$Toast.show(this.CHENFLAF?`正在更新，请稍等。。。${this.emoji[Math.floor(20*Math.random())]}`:`Updating, please wait...${this.emoji[Math.floor(20*Math.random())]}`),this.updateXwwTime()):"error"===this.$UpdateXww?(this.isLatestVersion=!1,this.$Toast.show(this.CHENFLAF?"更新失败":"Update failed",3e3)):"success"===this.$UpdateXww&&(this.$Toast.show(this.CHENFLAF?"更新成功，如果有些功能无法使用时，请退出启动器重新启动":"The update was successful. If some functions are not available, please exit the launcher and start again",3e3),this.isLatestVersion=!0)}),1e3)},updateXww(){if("start"===this.$DonloadFlag||"start"===this.$UpdateCuiBat||"start"===this.$UpdateXww)return void this.$Toast.show(this.CHENFLAF?"已有其它任务正在下载中，请稍等。。。":"Other tasks are downloading, please wait...",3e3);this.$Toast.show(this.CHENFLAF?"正在更新，请稍等。。。":"Updating, please wait...");let t=this.$UpdateXwwV[0];this.$Xwwqt.update_xww(t.newHexsha),this.updateXwwTime()},downLoad(t){"start"!==this.$DonloadFlag&&"start"!==this.$UpdateCuiBat&&"start"!==this.$UpdateXww?(this.$Toast.show(this.CHENFLAF?"正在下载项目，请耐心等待，可前往控制台查看下载进度":"Downloading the project, please wait patiently, you can go to the console to check the download progress",3e3),this.$Xwwqt.downloadProject(t),this.downLoadTime()):this.$Toast.show(this.CHENFLAF?"已有其它任务正在下载中，请稍等。。。":"Other tasks are downloading, please wait...",3e3)},downLoadTime(){this.downLoadTimer&&clearTimeout(this.downLoadTimer),this.downLoadTimer=setTimeout((()=>{clearTimeout(this.downLoadTimer),"start"===this.$DonloadFlag?(this.$Toast.show(this.CHENFLAF?`正在努力下载中。。。${this.emoji[Math.floor(20*Math.random())]}`:`Working on downloading...${this.emoji[Math.floor(20*Math.random())]}`),this.downLoadTime()):"error"===this.$DonloadFlag?this.$Toast.show(this.CHENFLAF?"下载失败":"Download failed",3e3):"success"===this.$DonloadFlag&&this.$Toast.show(this.CHENFLAF?"下载成功":"Download successfully",3e3)}),2e3)}}},n=i,h=o(1001),d=(0,h.Z)(n,a,s,!1,null,"236c6d6a",null),r=d.exports},5551:function(t,e,o){t.exports=o.p+"img/error.71a4ce4c.png"}}]);
//# sourceMappingURL=306.921bae39.js.map