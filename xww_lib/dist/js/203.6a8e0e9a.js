"use strict";(self["webpackChunkxww"]=self["webpackChunkxww"]||[]).push([[203],{6203:function(e,t,s){s.r(t),s.d(t,{default:function(){return h}});var o=function(){var e=this,t=e._self._c;return t("show-page",{attrs:{isShowPar:!0,opacity:1,isClickBg:!0}},[t("div",{ref:"statement",staticClass:"statement-div"},[t("div",{domProps:{innerHTML:e._s(e.statementDec)}})])])},i=[],n={name:"main-page-bg",props:{CHENFLAF:{type:Boolean,default:!0}},data(){return{statementDec:"",statementDecList:["声明：","1、使用本启动器/源码即代表您同意并遵守这些条款和条件，如果您不同意，请不要使用本启动器/源码。","2、源码开放，你可以拿源码去进行任意修改，但请不要用于商用，商用必究！","3、本启动器/源码仅供学习和娱乐使用，不保证生成的图片的准确性、完整性、合法性或适用性。","4、本启动器/源码不对生成的图片的版权、知识产权或其他权利负责，也不对生成的图片造成的任何损失或纠纷负责。","5、你使用本启动器/源码生成的图片，必须遵守相关的法律法规，不得用于任何违法或不道德的目的；如果你违反了这一条款，你将自行承担所有责任和后果，与本启动器/源码无关。"],statementDecListEn:["Statement","1、By using this launcher/source code, you agree to and comply with these terms and conditions. If you do not agree, please do not use this launcher/source code.","2、The source code is open, you can take the source code and make any modifications, but please do not use it for commercial purposes, commercial use will be investigated!","3、This launcher/source code is for learning and entertainment purposes only, and does not guarantee the accuracy, completeness, legality or applicability of the generated images.","4、This launcher/source code is not responsible for the copyright, intellectual property or other rights of the generated images, nor is it responsible for any loss or dispute caused by the generated images.","5、You must comply with relevant laws and regulations when using the images generated by this launcher/source code, and do not use them for any illegal or immoral purposes; if you violate this clause, you will bear all responsibility and consequences by yourself, and this launcher/source code has nothing to do with it."]}},watch:{CHENFLAF(){this.showDec(100)}},mounted(){this.showDec(2e3)},methods:{showDec(e){this.showDecTimer&&clearTimeout(this.showDecTimer),this.statementDec="";let t=this.CHENFLAF?this.statementDecList.join("<br>"):this.statementDecListEn.join("<br>"),s=t.split("");this.showDecTime(s,e,0)},showDecTime(e,t,s){this.showDecTimer=setTimeout((()=>{clearTimeout(this.showDecTimer);let o=e.length;s<o&&(this.statementDec=`${this.statementDec}${e[s]}`,t=this.CHENFLAF?60:20,this.showDecTime(e,t,s+1))}),t)}}},a=n,r=s(1001),c=(0,r.Z)(a,o,i,!1,null,"7702149d",null),h=c.exports}}]);
//# sourceMappingURL=203.6a8e0e9a.js.map