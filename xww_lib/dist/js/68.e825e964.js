"use strict";(self["webpackChunkxww"]=self["webpackChunkxww"]||[]).push([[68],{8068:function(e,t,s){s.r(t),s.d(t,{default:function(){return D}});var a=function(){var e=this,t=e._self._c;return t("show-page",[t("div",{staticClass:"tools-div"},[t("div",{staticClass:"tab-div"},e._l(e.tabList,(function(s,a){return t("div",{key:a+s.id},[t("button",{ref:s.id,refInFor:!0,class:s.isClick?"tab-div-btn selected":"tab-div-btn",attrs:{type:"button"},on:{click:function(t){return e.changeTab(s,a)}}},[e._v(" "+e._s(e.CHENFLAF?s.name:s.nameEn)+" ")])])})),0),t("div",{staticClass:"componet-div"},[t(e.showPagePath,{tag:"component",attrs:{CHENFLAFV:e.CHENFLAF}})],1)])])},i=[],r=function(){var e=this,t=e._self._c;return t("show-page",{attrs:{isShowBg:!1,time:3500}},[t("div",{staticClass:"image-data-div"},[t("div",{staticClass:"select-img-div"},[e.imageData&&e.imageData.imgBase64?e.imageData&&"NONE"===e.imageData.imgBase64?t("img",{attrs:{src:s(967)}}):t("img",{attrs:{src:"data:image/jpge;base64,"+e.imageData.imgBase64},on:{click:e.select_img}}):t("img",{attrs:{src:s(7811)},on:{click:e.select_img}})]),e.imageData?t("div",[t("div",{staticClass:"show-data-div"},[t("span",[e._v(e._s(e.CHENFLAF?"图片生成工具/方式:":"Image generating tool/type:"))]),t("span",{staticClass:"green ml text-dec",on:{mouseenter:function(t){return e.showTip("tool",t,1)},mouseleave:function(t){return e.showTip("",0)}}},[e._v(e._s(e.imageData._tool))])]),t("div",{staticClass:"show-data-div"},[t("span",[e._v("Steps:")]),t("span",{staticClass:"green ml text-dec",on:{mouseenter:function(t){return e.showTip("Steps",t,1)},mouseleave:function(t){return e.showTip("",0)}}},[e._v(e._s(e.imageData._setting["Steps"]))]),t("span",{directives:[{name:"clipboard",rawName:"v-clipboard:copy",value:e.imageData._setting["Steps"],expression:"imageData._setting['Steps']",arg:"copy"},{name:"clipboard",rawName:"v-clipboard:success",value:e.copy_success,expression:"copy_success",arg:"success"},{name:"clipboard",rawName:"v-clipboard:error",value:e.copy_error,expression:"copy_error",arg:"error"}],staticClass:"ml copy"},[e._v(e._s(e.CHENFLAF?"复制":"copy"))])]),t("div",{staticClass:"show-data-div"},[t("span",[e._v("Sampler:")]),t("span",{staticClass:"green ml text-dec",on:{mouseenter:function(t){return e.showTip("Sampler",t,1)},mouseleave:function(t){return e.showTip("",0)}}},[e._v(e._s(e.imageData._setting["Sampler"]))]),t("span",{directives:[{name:"clipboard",rawName:"v-clipboard:copy",value:e.imageData._setting["Sampler"],expression:"imageData._setting['Sampler']",arg:"copy"},{name:"clipboard",rawName:"v-clipboard:success",value:e.copy_success,expression:"copy_success",arg:"success"},{name:"clipboard",rawName:"v-clipboard:error",value:e.copy_error,expression:"copy_error",arg:"error"}],staticClass:"ml copy"},[e._v(e._s(e.CHENFLAF?"复制":"copy"))])]),t("div",{staticClass:"show-data-div"},[t("span",[e._v("CFG scale:")]),t("span",{staticClass:"green ml text-dec",on:{mouseenter:function(t){return e.showTip("CFG scale",t,1)},mouseleave:function(t){return e.showTip("",0)}}},[e._v(e._s(e.imageData._setting["CFG scale"]))]),t("span",{directives:[{name:"clipboard",rawName:"v-clipboard:copy",value:e.imageData._setting["CFG scale"],expression:"imageData._setting['CFG scale']",arg:"copy"},{name:"clipboard",rawName:"v-clipboard:success",value:e.copy_success,expression:"copy_success",arg:"success"},{name:"clipboard",rawName:"v-clipboard:error",value:e.copy_error,expression:"copy_error",arg:"error"}],staticClass:"ml copy"},[e._v(e._s(e.CHENFLAF?"复制":"copy"))])]),t("div",{staticClass:"show-data-div"},[t("span",[e._v("Seed:")]),t("span",{staticClass:"green ml text-dec",on:{mouseenter:function(t){return e.showTip("Seed",t,1)},mouseleave:function(t){return e.showTip("",0)}}},[e._v(e._s(e.imageData._setting["Seed"]))]),t("span",{directives:[{name:"clipboard",rawName:"v-clipboard:copy",value:e.imageData._setting["Seed"],expression:"imageData._setting['Seed']",arg:"copy"},{name:"clipboard",rawName:"v-clipboard:success",value:e.copy_success,expression:"copy_success",arg:"success"},{name:"clipboard",rawName:"v-clipboard:error",value:e.copy_error,expression:"copy_error",arg:"error"}],staticClass:"ml copy"},[e._v(e._s(e.CHENFLAF?"复制":"copy"))])]),t("div",{staticClass:"show-data-div"},[t("span",[e._v("Size:")]),t("span",{staticClass:"green ml text-dec",on:{mouseenter:function(t){return e.showTip("Size",t,1)},mouseleave:function(t){return e.showTip("",0)}}},[e._v(e._s(e.imageData._setting["Size"]))]),t("span",{directives:[{name:"clipboard",rawName:"v-clipboard:copy",value:e.imageData._setting["Size"],expression:"imageData._setting['Size']",arg:"copy"},{name:"clipboard",rawName:"v-clipboard:success",value:e.copy_success,expression:"copy_success",arg:"success"},{name:"clipboard",rawName:"v-clipboard:error",value:e.copy_error,expression:"copy_error",arg:"error"}],staticClass:"ml copy"},[e._v(e._s(e.CHENFLAF?"复制":"copy"))])]),t("div",{staticClass:"show-data-div"},[t("span",[e._v("Model:")]),t("span",{staticClass:"green ml text-dec",on:{mouseenter:function(t){return e.showTip("Model",t,1)},mouseleave:function(t){return e.showTip("",0)}}},[e._v(e._s(e.imageData._setting["Model"]))]),t("span",{directives:[{name:"clipboard",rawName:"v-clipboard:copy",value:e.imageData._setting["Model"],expression:"imageData._setting['Model']",arg:"copy"},{name:"clipboard",rawName:"v-clipboard:success",value:e.copy_success,expression:"copy_success",arg:"success"},{name:"clipboard",rawName:"v-clipboard:error",value:e.copy_error,expression:"copy_error",arg:"error"}],staticClass:"ml copy"},[e._v(e._s(e.CHENFLAF?"复制":"copy"))])]),t("div",{staticClass:"show-data-div"},[t("span",[e._v("Denoising strength:")]),t("span",{staticClass:"green ml text-dec",on:{mouseenter:function(t){return e.showTip("Denoising strength",t,1)},mouseleave:function(t){return e.showTip("",0)}}},[e._v(e._s(e.imageData._setting["Denoising strength"]))]),t("span",{directives:[{name:"clipboard",rawName:"v-clipboard:copy",value:e.imageData._setting["Denoising strength"],expression:"imageData._setting['Denoising strength']",arg:"copy"},{name:"clipboard",rawName:"v-clipboard:success",value:e.copy_success,expression:"copy_success",arg:"success"},{name:"clipboard",rawName:"v-clipboard:error",value:e.copy_error,expression:"copy_error",arg:"error"}],staticClass:"ml copy"},[e._v(e._s(e.CHENFLAF?"复制":"copy"))])]),t("div",{staticClass:"show-data-div"},[t("span",[e._v("Hires upscale:")]),t("span",{staticClass:"green ml text-dec",on:{mouseenter:function(t){return e.showTip("Hires upscale",t,1)},mouseleave:function(t){return e.showTip("",0)}}},[e._v(e._s(e.imageData._setting["Hires upscale"]))]),t("span",{directives:[{name:"clipboard",rawName:"v-clipboard:copy",value:e.imageData._setting["Hires upscale"],expression:"imageData._setting['Hires upscale']",arg:"copy"},{name:"clipboard",rawName:"v-clipboard:success",value:e.copy_success,expression:"copy_success",arg:"success"},{name:"clipboard",rawName:"v-clipboard:error",value:e.copy_error,expression:"copy_error",arg:"error"}],staticClass:"ml copy"},[e._v(e._s(e.CHENFLAF?"复制":"copy"))])]),t("div",{staticClass:"show-data-div"},[t("span",[e._v("Hires upscaler:")]),t("span",{staticClass:"green ml text-dec",on:{mouseenter:function(t){return e.showTip("Hires upscaler",t,1)},mouseleave:function(t){return e.showTip("",0)}}},[e._v(e._s(e.imageData._setting["Hires upscaler"]))]),t("span",{directives:[{name:"clipboard",rawName:"v-clipboard:copy",value:e.imageData._setting["Hires upscaler"],expression:"imageData._setting['Hires upscaler']",arg:"copy"},{name:"clipboard",rawName:"v-clipboard:success",value:e.copy_success,expression:"copy_success",arg:"success"},{name:"clipboard",rawName:"v-clipboard:error",value:e.copy_error,expression:"copy_error",arg:"error"}],staticClass:"ml copy"},[e._v(e._s(e.CHENFLAF?"复制":"copy"))])]),t("div",{staticClass:"show-data-div"},[t("div",[t("span",{staticClass:"text-dec",on:{mouseenter:function(t){return e.showTip("positive",t,1)},mouseleave:function(t){return e.showTip("",0)}}},[e._v("positive:")]),t("span",{directives:[{name:"clipboard",rawName:"v-clipboard:copy",value:e.imageData._positive,expression:"imageData._positive",arg:"copy"},{name:"clipboard",rawName:"v-clipboard:success",value:e.copy_success,expression:"copy_success",arg:"success"},{name:"clipboard",rawName:"v-clipboard:error",value:e.copy_error,expression:"copy_error",arg:"error"}],staticClass:"ml copy"},[e._v(e._s(e.CHENFLAF?"复制":"copy"))])]),t("textarea",{staticClass:"textarea",attrs:{type:"text"},domProps:{value:e.imageData._positive}})]),t("div",{staticClass:"show-data-div"},[t("div",[t("span",{staticClass:"text-dec",on:{mouseenter:function(t){return e.showTip("negative",t,1)},mouseleave:function(t){return e.showTip("",0)}}},[e._v("negative:")]),t("span",{directives:[{name:"clipboard",rawName:"v-clipboard:copy",value:e.imageData._negative,expression:"imageData._negative",arg:"copy"},{name:"clipboard",rawName:"v-clipboard:success",value:e.copy_success,expression:"copy_success",arg:"success"},{name:"clipboard",rawName:"v-clipboard:error",value:e.copy_error,expression:"copy_error",arg:"error"}],staticClass:"ml copy"},[e._v(e._s(e.CHENFLAF?"复制":"copy"))])]),t("textarea",{staticClass:"textarea",attrs:{type:"text"},domProps:{value:e.imageData._negative}})])]):e._e(),t("div",{staticClass:"empty-div"})])])},o=[],n={components:{},props:{CHENFLAFV:{type:Boolean,default:!0}},data(){return{CHENFLAF:!0,imageData:null,emoji:["(≧∇≦)ﾉ","(+.+)(-.-)(_ _) ..zzZZ もうだめ","ヾ(≧O≦)〃嗷~","٩(๑òωó๑)۶","( *￣▽￣)((≧︶≦*)","（*＾-＾*）","...(*￣０￣)ノ[等等我…]","n(*≧▽≦*)n","(～o￣▽￣)～o 。。。滚来滚去……o～(＿△＿o～) ~。。。","不＞(￣ε￣ = ￣3￣)<要",".....((/- -)/","-________-","(*￣▽￣)(￣▽:;.…::;.:.:::;..::;.:...","『家』 ～o(▽｀ o) =3 =3 =3","＼（＾∀＾）メ（＾∀＾）ノ","(*/ω＼*)/p.","◕ฺ‿◕ฺ✿ฺ)","Ψ(￣∀￣)Ψ","( *^-^)ρ(^0^* )","↑↑↓↓←→←→ＢＡ...┗( -o-)┛","（￣ー￣）ノ~~マ☆’.・.・:★","．《{=．．．．（嘎~嘎~嘎~）"],explain:{tool:"这是指生成该图片使用到的工具，不同的工具使用的参数可能有一些出入，即使所有参数都配置一样也不一定能生成一样。",Steps:"这是指生成图片的步数，也就是从噪声图像到目标图像的迭代次数。步数越多，生成的图片越清晰，但也越耗时。",Sampler:"这是指生成图片的采样器，也就是用于控制噪声图像的随机性的算法。不同的采样器会产生不同的风格和效果。比如DPM++ SDE Karras是一种基于DPM++ SDE2和Karras3的采样器，它可以生成更高质量和更多样化的图片。","CFG scale":"这是指生成图片的配置比例，也就是用于控制噪声图像的分辨率和细节的参数。配置比例越大，生成的图片越高清，但也越耗时。",Seed:"这是指生成图片的随机种子，也就是用于初始化噪声图像的数字。不同的随机种子会产生不同的噪声图像，从而影响最终生成的图片。",Size:"这是指生成图片的尺寸，也就是最终输出的图片的分辨率。尺寸越大，生成的图片越高清，但也越耗时。","Model hash":"这是指生成图片的模型哈希值，也就是用于标识模型文件的字符串。不同的模型文件会有不同的哈希值，用于验证模型文件是否完整和正确。",Model:"这是指生成图片的模型名称，也就是用于训练模型文件的数据集或方法的名称。不同的模型名称会有不同的风格和效果。比如3Guofeng3_v33是一种基于3Guofeng3数据集训练出来的模型，它可以生成类似于中国古典风格的图片。","Denoising strength":"这是指生成图片的去噪强度，也就是用于消除噪声图像中的杂色和锯齿的参数。去噪强度越大，生成的图片越平滑，但也越模糊。","Hires upscale":"这是指生成图片的高分辨率放大倍数，也就是用于提升输出图片分辨率和质量的参数。高分辨率放大倍数越大，输出图片分辨率越高，但也越耗时。","Hires upscaler":"这是指生成图片的高分辨率放大器，也就是用于提升输出图片分辨率和质量的算法。不同的高分辨率放大器会有不同的效果和速度。比如R- ESRGAN 4x + 是一种基于R - ESRGAN和4x + 方法结合而成的高分辨率放大器，它可以在保持细节和纹理清晰度的同时消除锯齿和模糊。",positive:"这是指生成图片的正向提示词，也就是用于描述你想要在图片中出现的内容和风格的文字。正向提示词越准确和精炼，生成的图片越符合你的期望。",negative:"这是指生成图片的负向提示词，也就是用于描述你不想在图片中出现的内容和风格的文字。负向提示词越具体和全面，生成的图片越避免不必要的错误和干扰。"},explainEn:{tool:"This refers to the tools used to generate the image. Different tools may use different parameters. Even if all parameters are configured the same, they may not generate the same image.",Steps:"This refers to the number of steps to generate the picture, that is, the number of iterations from the noisy image to the target image. The more steps you take, the clearer the picture, but the more time it takes.",Sampler:"This refers to the sampler that generates the picture, which is the algorithm used to control the randomness of the noisy image. Different samplers will produce different styles and effects. For example, DPM++ SDE Karras is a sampler based on DPM++ SDE2 and Karras3 that produces higher quality and more varied images.","CFG scale":"This refers to the configuration scale of the generated picture, which is the parameter used to control the resolution and detail of the noisy image. The larger the configuration ratio, the higher the resolution of the image, but the longer the time.",Seed:"This refers to the random seed that generates the picture, which is the number used to initialize the noisy image. Different random seeds will produce different noise images, which will affect the resulting picture.",Size:"This refers to the size of the generated image, which is the resolution of the final output image. The larger the size, the more HD the resulting image, but also the more time consuming.","Model hash":"This refers to the model hash value that generates the image, which is the string used to identify the model file. Different model files have different hash values that are used to verify that the model file is complete and correct.",Model:"This refers to the name of the model that generated the picture, that is, the name of the data set or method used to train the model file. Different model names will have different styles and effects. For example, 3Guofeng3_v33 is a model trained based on 3Guofeng3 data set, which can generate pictures similar to Chinese classical style.","Denoising strength":"This refers to the denoising intensity of the generated image, that is, the parameter used to eliminate noise and jagged in the noisy image. The more intense the denoising, the smoother the resulting image, but also the blurrier.","Hires upscale":"This refers to the high resolution magnification of the generated image, that is, the parameter used to improve the resolution and quality of the output image. The higher the high resolution magnification, the higher the resolution of the output picture, but also the more time consuming.","Hires upscaler":"This refers to the high resolution magnification of the generated image, that is, the parameter used to improve the resolution and quality of the output image. This refers to the high-resolution amplifiers that generate the images, which are algorithms used to improve the resolution and quality of the output images. Different high resolution amplifiers will have different effects and speeds. For example, R-ESRGAN 4x + is a high-resolution amplifier based on a combination of R-ESRGAN and 4x + methods that eliminates jagging and blurring while maintaining detail and texture sharpness. The higher the high resolution magnification, the higher the resolution of the output picture, but also the more time consuming.",positive:"This refers to the positive prompt words that generate the image, which is the text that describes the content and style you want to appear in the image. The more accurate and concise the positive prompts are, the more likely the resulting picture is to match your expectations.",negative:"This is the negative cue word that generates the image, which is the text that describes the content and style that you don't want to appear in the image. The more specific and comprehensive the negative prompt word, the more the generated picture is free from unnecessary errors and interference."}}},watch:{CHENFLAFV(){this.CHENFLAF=this.CHENFLAFV}},mounted(){},methods:{copy_success(){this.$Toast.show(this.CHENFLAF?"复制成功":"Copy success")},copy_error(){this.$Toast.show(this.CHENFLAF?"复制失败":"Copy failure")},showTip(e,t,s){s?this.$Toast.show(this.CHENFLAF?this.explain[e]:this.explainEn[e],6e4,t.clientX,t.clientY):this.$Toast.hide()},select_img(){this.$Xwwqt.get_image_data(),this.select_imgTime()},select_imgTime(){this.select_imgTimer&&clearTimeout(this.select_imgTimer),this.select_imgTimer=setTimeout((()=>{if(clearTimeout(this.select_imgTimer),this.$ImageData&&"start"===this.$ImageData[0])this.$Toast.show((this.CHENFLAF?"努力处理中。。。":"Try to deal with...")+this.emoji[Math.floor(20*Math.random())]),this.select_imgTime();else{if(this.$ImageData&&"noselect"===this.$ImageData[0])return;if(this.$ImageData&&"error"===this.$ImageData[0])this.$Toast.show(this.CHENFLAF?"处理失败":"Processing failure",3e3);else{let e;this.$ImageData&&(e=this.$ImageData[0]),e&&e._setting&&(e._setting=this.str2json(e._setting)),this.imageData=e,this.$Toast.show(this.CHENFLAF?"处理成功":"Processing success",3e3)}}}),1e3)},str2json(e){try{let t=e.split(/(:|,)/g);for(let e=0;e<t.length;e++)t[e]=t[e].trim(),e%2===0?t[e]='"'+t[e]+'"':":"===t[e]&&(t[e]=t[e]+" ");let s="{"+t.join("")+"}";return JSON.parse(s)}catch(t){this.$Toast.show(this.CHENFLAF?"处理失败":"Processing failure",3e3)}}}},c=n,l=s(1001),m=(0,l.Z)(c,r,o,!1,null,"8c94e730",null),p=m.exports,h=function(){var e=this,t=e._self._c;return t("show-page",{attrs:{isShowBg:!1,time:3500}},[t("div",{staticClass:"image-data-div"},[t("div",{staticClass:"select-img-div"},[e.imgBase64?"NONE"===e.imgBase64?t("img",{attrs:{src:s(967)}}):t("div",[t("img",{attrs:{src:"data:image/jpge;base64,"+e.imgBase64},on:{click:function(t){return e.select_img()}}}),t("br"),t("div",[e._v(e._s(e.CHENFLAF?"原图":"master img")+"："+e._s(e.image_data[0]["size"])+"---"+e._s(e.image_data[0]["kb"]))])]):t("img",{attrs:{src:s(1898)},on:{click:function(t){return e.select_img()}}}),e.imgBase64Compre?t("div",{staticClass:"input-div"},[t("input",{directives:[{name:"model",rawName:"v-model",value:e.w,expression:"w"}],attrs:{type:"text",placeholder:e.CHENFLAF?"宽":"width",onkeyup:"value=value.replace(/^(0+)|[^\\d]+/g,'')"},domProps:{value:e.w},on:{input:function(t){t.target.composing||(e.w=t.target.value)}}}),t("input",{directives:[{name:"model",rawName:"v-model",value:e.h,expression:"h"}],attrs:{type:"text",placeholder:e.CHENFLAF?"高":"height",onkeyup:"value=value.replace(/^(0+)|[^\\d]+/g,'')"},domProps:{value:e.h},on:{input:function(t){t.target.composing||(e.h=t.target.value)}}}),t("button",{on:{click:function(t){return e.select_img(e.image_data[0]["path"])}}},[e._v(e._s(e.CHENFLAF?"转换":"convert to"))]),t("button",{on:{click:e.save_img}},[e._v(e._s(e.CHENFLAF?"保存图片":"save img"))]),t("button",{on:{click:e.clear_img}},[e._v(e._s(e.CHENFLAF?"清空":"clear"))])]):e._e(),e.imgBase64Compre?t("div",[t("img",{attrs:{src:"data:image/jpge;base64,"+e.imgBase64Compre},on:{click:e.save_img}}),t("br"),t("div",[e._v(e._s(e.CHENFLAF?"转换后":"after conversion")+"："+e._s(e.image_data[1]["size"])+"---"+e._s(e.image_data[1]["kb"])+" ")])]):e._e()]),t("div",{staticClass:"empty-div"})])])},u=[],g={components:{},props:{CHENFLAFV:{type:Boolean,default:!0}},data(){return{w:320,h:320,CHENFLAF:!0,imgBase64:null,imgBase64Compre:null,image_data:null,emoji:["(≧∇≦)ﾉ","(+.+)(-.-)(_ _) ..zzZZ もうだめ","ヾ(≧O≦)〃嗷~","٩(๑òωó๑)۶","( *￣▽￣)((≧︶≦*)","（*＾-＾*）","...(*￣０￣)ノ[等等我…]","n(*≧▽≦*)n","(～o￣▽￣)～o 。。。滚来滚去……o～(＿△＿o～) ~。。。","不＞(￣ε￣ = ￣3￣)<要",".....((/- -)/","-________-","(*￣▽￣)(￣▽:;.…::;.:.:::;..::;.:...","『家』 ～o(▽｀ o) =3 =3 =3","＼（＾∀＾）メ（＾∀＾）ノ","(*/ω＼*)/p.","◕ฺ‿◕ฺ✿ฺ)","Ψ(￣∀￣)Ψ","( *^-^)ρ(^0^* )","↑↑↓↓←→←→ＢＡ...┗( -o-)┛","（￣ー￣）ノ~~マ☆’.・.・:★","．《{=．．．．（嘎~嘎~嘎~）"]}},watch:{CHENFLAFV(){this.CHENFLAF=this.CHENFLAFV}},mounted(){},methods:{clear_img(){this.w=320,this.h=320,this.imgBase64=null,this.imgBase64Compre=null,this.image_data=null},save_img(){this.$Xwwqt.save_base64_2_img(this.imgBase64Compre),this.save_imgTime()},save_imgTime(){this.save_imgTimer&&clearTimeout(this.save_imgTimer),this.save_imgTimer=setTimeout((()=>{if(clearTimeout(this.save_imgTimer),"start"===this.$SaveFlag)this.$Toast.show((this.CHENFLAF?"努力处理中。。。":"Try to deal with...")+this.emoji[Math.floor(20*Math.random())]),this.save_imgTime();else{if("noselect"===this.$SaveFlag)return;"error"===this.$SaveFlag?this.$Toast.show(this.CHENFLAF?"保存失败":"save failure",3e3):this.$Toast.show(this.CHENFLAF?"保存成功":"save successfully",3e3)}}),500)},select_img(e){this.$Xwwqt.resize_img_select(this.w,this.h,e),this.select_imgTime()},select_imgTime(){this.select_imgTimer&&clearTimeout(this.select_imgTimer),this.select_imgTimer=setTimeout((()=>{clearTimeout(this.select_imgTimer);let e=this.$Base64List;if(e&&"start"===e[0])this.$Toast.show((this.CHENFLAF?"努力处理中。。。":"Try to deal with...")+this.emoji[Math.floor(20*Math.random())]),this.select_imgTime();else{if(e&&"noselect"===e[0])return;e&&"error"===e[0]?this.$Toast.show(this.CHENFLAF?"处理失败":"Processing failure",3e3):(this.imgBase64=e[0],this.imgBase64Compre=e[1],this.image_data=[e[2],e[3]],this.$Toast.show(this.CHENFLAF?"处理成功":"Processing success",3e3))}}),1e3)}}},d=g,v=(0,l.Z)(d,h,u,!1,null,"510dcf3e",null),_=v.exports,f=function(){var e=this,t=e._self._c;return t("show-page",{attrs:{isShowBg:!1,time:3500}},[t("div",{staticClass:"more-res"},[t("div",{staticClass:"more-res-div"},[e._v(" "+e._s("分享一个关于AI资源比较全的网站 ")+" "),t("span",{staticClass:"blue text-dec",on:{click:function(t){return e.openUrl_("https://chat123.fun/h5/?utm_source=a2a&type=chatgpt")}}},[e._v("AI艺术天堂")])]),t("div",{staticClass:"more-res-div"},[e._v(" chart-gtp（目前国内暂时免费可用，但后续会不会收费不清楚） "),t("span",{staticClass:"blue text-dec",on:{click:function(t){return e.openUrl_("https://chat123.fun/h5/?utm_source=a")}}},[e._v("CHAT-GTP")])]),t("div",{staticClass:"more-res-div"},[e._v(" 训练模型下载： "),t("div",[e._v("C站---"),t("span",{staticClass:"blue text-dec",on:{click:function(t){return e.openUrl_("https://civitai.com/")}}},[e._v("civitai")])]),t("div",[e._v("国内C站---"),t("span",{staticClass:"blue text-dec",on:{click:function(t){return e.openUrl_("http://www.liandange.com/models")}}},[e._v("炼丹阁")])]),t("div",[e._v("喵手AI资源站-AI相关的相关模型，prmopt，软件等资源---"),t("span",{staticClass:"blue text-dec",on:{click:function(t){return e.openUrl_("https://resource.miaoshouai.com/")}}},[e._v("miaoshouai")])])]),t("div",{staticClass:"empty-div"})])])},w=[],y={components:{},props:{CHENFLAFV:{type:Boolean,default:!0}},data(){return{CHENFLAF:!0}},watch:{CHENFLAFV(){this.CHENFLAF=this.CHENFLAFV}},mounted(){},methods:{openUrl_(e){e&&this.$Xwwqt.openUrl(e)}}},C=y,b=(0,l.Z)(C,f,w,!1,null,"2d988520",null),F=b.exports,T={components:{getImageData:p,photoSize:_,moreResources:F},props:{CHENFLAF:{type:Boolean,default:!0}},data(){return{CHENFLAF:"",showPagePath:"",pageIndex:null,isRouterAlive:!0,tabList:[{id:"getImageData",name:"提取图片信息",nameEn:"Extract picture information",isClick:!1,path:"getImageData"},{id:"imageCompression",name:"图片大小",nameEn:"Photo Size",isClick:!1,path:"photoSize"},{id:"moreResources",name:"更多资源",nameEn:"More Resources",isClick:!1,path:"moreResources"}]}},mounted(){this.$nextTick((function(){this.$refs[this.tabList[0].id][0].click()}))},methods:{showTabPage(e){this.showPagePath=e.path},changeTab(e,t){this.pageIndex!==t&&((this.pageIndex||0===this.pageIndex)&&(this.tabList[this.pageIndex].isClick=!1),this.tabList[t].isClick=!0,this.pageIndex=t,this.showTabPage(e))}}},N=T,x=(0,l.Z)(N,a,i,!1,null,"28eda874",null),D=x.exports},1898:function(e,t,s){e.exports=s.p+"img/img-size.980d2fe9.png"},7811:function(e,t,s){e.exports=s.p+"img/img.8cfc106e.png"},967:function(e,t,s){e.exports=s.p+"img/no-img.d5ccbd9e.png"}}]);
//# sourceMappingURL=68.e825e964.js.map