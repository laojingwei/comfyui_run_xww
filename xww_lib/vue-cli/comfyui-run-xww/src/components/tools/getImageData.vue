<template>
    <show-page :isShowBg="false" :time="3500">
        <div class="image-data-div">
            <div class="select-img-div">
                <img v-if="!imageData || !imageData.imgBase64" src="@/assets/img.png" @click="select_img" />
                <img v-else-if="imageData && imageData.imgBase64 === 'NONE'" src="@/assets/no-img.png" />
                <img v-else :src="'data:image/jpge;base64,' + imageData.imgBase64" @click="select_img" />
            </div>
            <div v-if="imageData">
                <div class="show-data-div">
                    <span>{{ CHENFLAF ? '图片生成工具/方式:' : 'Image generating tool/type:' }}</span>
                    <span class="green ml text-dec" @mouseenter="showTip('tool', $event, 1)" @mouseleave="showTip('', 0)">{{
                        imageData._tool }}</span>
                </div>
                <div class="show-data-div">
                    <span>Steps:</span>
                    <span class="green ml text-dec" @mouseenter="showTip('Steps', $event, 1)"
                        @mouseleave="showTip('', 0)">{{
                            imageData._setting['Steps'] }}</span>
                    <span class="ml copy" v-clipboard:copy="imageData._setting['Steps']" v-clipboard:success="copy_success"
                        v-clipboard:error="copy_error">{{
                            CHENFLAF ? '复制' : 'copy' }}</span>
                </div>
                <div class="show-data-div">
                    <span>Sampler:</span>
                    <span class="green ml text-dec" @mouseenter="showTip('Sampler', $event, 1)"
                        @mouseleave="showTip('', 0)">{{
                            imageData._setting['Sampler'] }}</span>
                    <span class="ml copy" v-clipboard:copy="imageData._setting['Sampler']"
                        v-clipboard:success="copy_success" v-clipboard:error="copy_error">{{
                            CHENFLAF ? '复制' : 'copy' }}</span>
                </div>
                <div class="show-data-div">
                    <span>CFG scale:</span>
                    <span class="green ml text-dec" @mouseenter="showTip('CFG scale', $event, 1)"
                        @mouseleave="showTip('', 0)">{{
                            imageData._setting['CFG scale'] }}</span>
                    <span class="ml copy" v-clipboard:copy="imageData._setting['CFG scale']"
                        v-clipboard:success="copy_success" v-clipboard:error="copy_error">{{
                            CHENFLAF ? '复制' : 'copy' }}</span>
                </div>
                <div class="show-data-div">
                    <span>Seed:</span>
                    <span class="green ml text-dec" @mouseenter="showTip('Seed', $event, 1)" @mouseleave="showTip('', 0)">{{
                        imageData._setting['Seed'] }}</span>
                    <span class="ml copy" v-clipboard:copy="imageData._setting['Seed']" v-clipboard:success="copy_success"
                        v-clipboard:error="copy_error">{{
                            CHENFLAF ? '复制' : 'copy' }}</span>
                </div>
                <div class="show-data-div">
                    <span>Size:</span>
                    <span class="green ml text-dec" @mouseenter="showTip('Size', $event, 1)" @mouseleave="showTip('', 0)">{{
                        imageData._setting['Size'] }}</span>
                    <span class="ml copy" v-clipboard:copy="imageData._setting['Size']" v-clipboard:success="copy_success"
                        v-clipboard:error="copy_error">{{
                            CHENFLAF ? '复制' : 'copy' }}</span>
                </div>
                <div class="show-data-div">
                    <span>Model:</span>
                    <span class="green ml text-dec" @mouseenter="showTip('Model', $event, 1)"
                        @mouseleave="showTip('', 0)">{{
                            imageData._setting['Model'] }}</span>
                    <span class="ml copy" v-clipboard:copy="imageData._setting['Model']" v-clipboard:success="copy_success"
                        v-clipboard:error="copy_error">{{
                            CHENFLAF ? '复制' : 'copy' }}</span>
                </div>
                <div class="show-data-div">
                    <span>Denoising strength:</span>
                    <span class="green ml text-dec" @mouseenter="showTip('Denoising strength', $event, 1)"
                        @mouseleave="showTip('', 0)">{{
                            imageData._setting['Denoising strength'] }}</span>
                    <span class="ml copy" v-clipboard:copy="imageData._setting['Denoising strength']"
                        v-clipboard:success="copy_success" v-clipboard:error="copy_error">{{
                            CHENFLAF ? '复制' : 'copy' }}</span>
                </div>
                <div class="show-data-div">
                    <span>Hires upscale:</span>
                    <span class="green ml text-dec" @mouseenter="showTip('Hires upscale', $event, 1)"
                        @mouseleave="showTip('', 0)">{{
                            imageData._setting['Hires upscale'] }}</span>
                    <span class="ml copy" v-clipboard:copy="imageData._setting['Hires upscale']"
                        v-clipboard:success="copy_success" v-clipboard:error="copy_error">{{
                            CHENFLAF ? '复制' : 'copy' }}</span>
                </div>
                <div class="show-data-div">
                    <span>Hires upscaler:</span>
                    <span class="green ml text-dec" @mouseenter="showTip('Hires upscaler', $event, 1)"
                        @mouseleave="showTip('', 0)">{{
                            imageData._setting['Hires upscaler'] }}</span>
                    <span class="ml copy" v-clipboard:copy="imageData._setting['Hires upscaler']"
                        v-clipboard:success="copy_success" v-clipboard:error="copy_error">{{
                            CHENFLAF ? '复制' : 'copy' }}</span>
                </div>
                <div class="show-data-div">
                    <div>
                        <span class="text-dec" @mouseenter="showTip('positive', $event, 1)"
                            @mouseleave="showTip('', 0)">positive:</span>
                        <span class="ml copy" v-clipboard:copy="imageData._positive" v-clipboard:success="copy_success"
                            v-clipboard:error="copy_error">{{
                                CHENFLAF ? '复制' : 'copy' }}</span>
                    </div>
                    <textarea type="text" class="textarea" :value="imageData._positive" />
                </div>
                <div class="show-data-div">
                    <div>
                        <span class="text-dec" @mouseenter="showTip('negative', $event, 1)"
                            @mouseleave="showTip('', 0)">negative:</span>
                        <span class="ml copy" v-clipboard:copy="imageData._negative" v-clipboard:success="copy_success"
                            v-clipboard:error="copy_error">{{
                                CHENFLAF ? '复制' : 'copy' }}</span>
                    </div>
                    <textarea type="text" class="textarea" :value="imageData._negative" />
                </div>
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
            imageData: null,
            emoji: ['(≧∇≦)ﾉ', '(+.+)(-.-)(_ _) ..zzZZ もうだめ', 'ヾ(≧O≦)〃嗷~', '٩(๑òωó๑)۶', '( *￣▽￣)((≧︶≦*)', '（*＾-＾*）', '...(*￣０￣)ノ[等等我…]', 'n(*≧▽≦*)n', '(～o￣▽￣)～o 。。。滚来滚去……o～(＿△＿o～) ~。。。', '不＞(￣ε￣ = ￣3￣)<要', '.....((/- -)/', '-________-', '(*￣▽￣)(￣▽:;.…::;.:.:::;..::;.:...', '『家』 ～o(▽｀ o) =3 =3 =3', '＼（＾∀＾）メ（＾∀＾）ノ', '(*/ω＼*)/p.', '◕ฺ‿◕ฺ✿ฺ)', 'Ψ(￣∀￣)Ψ', '( *^-^)ρ(^0^* )', '↑↑↓↓←→←→ＢＡ...┗( -o-)┛', '（￣ー￣）ノ~~マ☆’.・.・:★', '．《{=．．．．（嘎~嘎~嘎~）'],
            explain: {
                "tool": "这是指生成该图片使用到的工具，不同的工具使用的参数可能有一些出入，即使所有参数都配置一样也不一定能生成一样。",
                "Steps": "这是指生成图片的步数，也就是从噪声图像到目标图像的迭代次数。步数越多，生成的图片越清晰，但也越耗时。",
                "Sampler": "这是指生成图片的采样器，也就是用于控制噪声图像的随机性的算法。不同的采样器会产生不同的风格和效果。比如DPM++ SDE Karras是一种基于DPM++ SDE2和Karras3的采样器，它可以生成更高质量和更多样化的图片。",
                "CFG scale": "这是指生成图片的配置比例，也就是用于控制噪声图像的分辨率和细节的参数。配置比例越大，生成的图片越高清，但也越耗时。",
                "Seed": "这是指生成图片的随机种子，也就是用于初始化噪声图像的数字。不同的随机种子会产生不同的噪声图像，从而影响最终生成的图片。",
                "Size": "这是指生成图片的尺寸，也就是最终输出的图片的分辨率。尺寸越大，生成的图片越高清，但也越耗时。",
                "Model hash": "这是指生成图片的模型哈希值，也就是用于标识模型文件的字符串。不同的模型文件会有不同的哈希值，用于验证模型文件是否完整和正确。",
                "Model": "这是指生成图片的模型名称，也就是用于训练模型文件的数据集或方法的名称。不同的模型名称会有不同的风格和效果。比如3Guofeng3_v33是一种基于3Guofeng3数据集训练出来的模型，它可以生成类似于中国古典风格的图片。",
                "Denoising strength": "这是指生成图片的去噪强度，也就是用于消除噪声图像中的杂色和锯齿的参数。去噪强度越大，生成的图片越平滑，但也越模糊。",
                "Hires upscale": "这是指生成图片的高分辨率放大倍数，也就是用于提升输出图片分辨率和质量的参数。高分辨率放大倍数越大，输出图片分辨率越高，但也越耗时。",
                "Hires upscaler": "这是指生成图片的高分辨率放大器，也就是用于提升输出图片分辨率和质量的算法。不同的高分辨率放大器会有不同的效果和速度。比如R- ESRGAN 4x + 是一种基于R - ESRGAN和4x + 方法结合而成的高分辨率放大器，它可以在保持细节和纹理清晰度的同时消除锯齿和模糊。",
                "positive": "这是指生成图片的正向提示词，也就是用于描述你想要在图片中出现的内容和风格的文字。正向提示词越准确和精炼，生成的图片越符合你的期望。",
                "negative": "这是指生成图片的负向提示词，也就是用于描述你不想在图片中出现的内容和风格的文字。负向提示词越具体和全面，生成的图片越避免不必要的错误和干扰。",
            },
            explainEn: {
                "tool": "This refers to the tools used to generate the image. Different tools may use different parameters. Even if all parameters are configured the same, they may not generate the same image.",
                "Steps": "This refers to the number of steps to generate the picture, that is, the number of iterations from the noisy image to the target image. The more steps you take, the clearer the picture, but the more time it takes.",
                "Sampler": "This refers to the sampler that generates the picture, which is the algorithm used to control the randomness of the noisy image. Different samplers will produce different styles and effects. For example, DPM++ SDE Karras is a sampler based on DPM++ SDE2 and Karras3 that produces higher quality and more varied images.",
                "CFG scale": "This refers to the configuration scale of the generated picture, which is the parameter used to control the resolution and detail of the noisy image. The larger the configuration ratio, the higher the resolution of the image, but the longer the time.",
                "Seed": "This refers to the random seed that generates the picture, which is the number used to initialize the noisy image. Different random seeds will produce different noise images, which will affect the resulting picture.",
                "Size": "This refers to the size of the generated image, which is the resolution of the final output image. The larger the size, the more HD the resulting image, but also the more time consuming.",
                "Model hash": "This refers to the model hash value that generates the image, which is the string used to identify the model file. Different model files have different hash values that are used to verify that the model file is complete and correct.",
                "Model": "This refers to the name of the model that generated the picture, that is, the name of the data set or method used to train the model file. Different model names will have different styles and effects. For example, 3Guofeng3_v33 is a model trained based on 3Guofeng3 data set, which can generate pictures similar to Chinese classical style.",
                "Denoising strength": "This refers to the denoising intensity of the generated image, that is, the parameter used to eliminate noise and jagged in the noisy image. The more intense the denoising, the smoother the resulting image, but also the blurrier.",
                "Hires upscale": "This refers to the high resolution magnification of the generated image, that is, the parameter used to improve the resolution and quality of the output image. The higher the high resolution magnification, the higher the resolution of the output picture, but also the more time consuming.",
                "Hires upscaler": "This refers to the high resolution magnification of the generated image, that is, the parameter used to improve the resolution and quality of the output image. This refers to the high-resolution amplifiers that generate the images, which are algorithms used to improve the resolution and quality of the output images. Different high resolution amplifiers will have different effects and speeds. For example, R-ESRGAN 4x + is a high-resolution amplifier based on a combination of R-ESRGAN and 4x + methods that eliminates jagging and blurring while maintaining detail and texture sharpness. The higher the high resolution magnification, the higher the resolution of the output picture, but also the more time consuming.",
                "positive": "This refers to the positive prompt words that generate the image, which is the text that describes the content and style you want to appear in the image. The more accurate and concise the positive prompts are, the more likely the resulting picture is to match your expectations.",
                "negative": "This is the negative cue word that generates the image, which is the text that describes the content and style that you don't want to appear in the image. The more specific and comprehensive the negative prompt word, the more the generated picture is free from unnecessary errors and interference.",
            }
        };
    },

    watch: {
        CHENFLAFV() {
            this.CHENFLAF = this.CHENFLAFV;
        }
    },

    mounted() {
        // TODO: test
        // let data = { "_negative": "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry,multiple breasts, (mutated hands and fingers:1.5 ), (long body :1.3), (mutation, poorly drawn :1.2) , black-white, bad anatomy, liquid body, liquid tongue, disfigured, malformed, mutated, anatomical nonsense, text font ui, error, malformed hands, long neck, blurred, lowers, lowres, bad anatomy, bad proportions, bad shadow, uncoordinated body, unnatural body, fused breasts, bad breasts, huge breasts, poorly drawn breasts, extra breasts, liquid breasts, heavy breasts, missing breasts, huge haunch, huge thighs, huge calf, bad hands, fused hand, missing hand, (badhandv4:1.2)", "_positive": "nuclear explosion behide,flames of war,(rain:1.2),detailed lighting,(detailed water:1.2),long bangs,hair between eyes,white bowties,flower,blank stare,beautiful detailed glow,beautiful detailed eyes,beautiful detailed girl,(multicolored hair:1.2),(gradient hair:1.2),(very long hair:1.2),(floating hair:1.2),panorama,masterpiece,best quality,ultra-detailed,illustration,disheveled hair,frills,1girl,solo,dynamic angle,big top sleeves,floating,beautiful detailed sky,beautiful detailed water,beautiful detailed eyes,overexposure,side blunt bangs,hair between eyes,ribbons,bowties,buttons,bare shoulders,detailed wet clothes,blank stare,pleated skirt,flowers,smile,large breasts,moonflower,black wings ", "_setting": "Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 7, Seed: 1020570958, Size: 512x512, Model hash: 4078eb4174, Model: 3Guofeng3_v33, Denoising strength: 0.7, Hires upscale: 2, Hires upscaler: R-ESRGAN 4x+", "_tool": "A1111-sd-webUI create PNG", "imgBase64": "NONE" };
        // if (data && data._setting) {
        //     data._setting = this.str2json(data._setting);
        // }
        // this.imageData = data;
    },

    methods: {
        copy_success() {
            this.$Toast.show(this.CHENFLAF ? "复制成功" : "Copy success");
        },
        copy_error() {
            this.$Toast.show(this.CHENFLAF ? "复制失败" : "Copy failure");
        },
        showTip(i, e, t) {
            if (!t) {
                this.$Toast.hide();
            } else {
                this.$Toast.show(this.CHENFLAF ? this.explain[i] : this.explainEn[i], 60000, e.clientX, e.clientY);
            }
        },
        select_img() {
            this.$Xwwqt.get_image_data();
            this.select_imgTime();
        },
        select_imgTime() {
            this.select_imgTimer && clearTimeout(this.select_imgTimer);
            this.select_imgTimer = setTimeout(() => {
                clearTimeout(this.select_imgTimer);
                // this.$Xwwqt.py_print(JSON.stringify(this.$ImageData && this.$ImageData[0] === "start"))
                if (this.$ImageData && this.$ImageData[0] === "start") {
                    this.$Toast.show((this.CHENFLAF ? '努力处理中。。。' : 'Try to deal with...') + this.emoji[Math.floor(Math.random() * 20)]);
                    this.select_imgTime();

                } else if (this.$ImageData && this.$ImageData[0] === "noselect") {
                    return;
                } else if (this.$ImageData && this.$ImageData[0] === "error") {
                    this.$Toast.show(this.CHENFLAF ? '处理失败' : 'Processing failure', 3000);
                } else {
                    let data;
                    this.$ImageData && (data = this.$ImageData[0]);
                    if (data && data._setting) {
                        data._setting = this.str2json(data._setting);
                    }
                    this.imageData = data;
                    this.$Toast.show(this.CHENFLAF ? '处理成功' : 'Processing success', 3000);
                }
            }, 1000);
        },
        str2json(str) {
            try {

                let arr = str.split(/(:|,)/g); // 将字符串按照冒号和逗号分割成数组

                for (let i = 0; i < arr.length; i++) {
                    arr[i] = arr[i].trim();
                    if (i % 2 === 0) { // 如果是偶数索引，表示是键或值 
                        arr[i] = '"' + arr[i] + '"'; // 在两边加上引号 
                    } else if (arr[i] === ':') { // 如果是冒号 
                        arr[i] = arr[i] + ' '; // 在后面加上一个空格 
                    }
                }

                let newStr = '{' + arr.join('') + '}'; // 将数组重新拼接成字符串

                return JSON.parse(newStr);
            } catch (error) {
                this.$Toast.show(this.CHENFLAF ? '处理失败' : 'Processing failure', 3000);
            }
        }
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

.select-img-div {
    display: flex;
    justify-content: center;
}

.select-img-div img {
    width: 300px;
    opacity: 0.9;
    border-radius: 10px;
    transform-origin: top center;
}

.select-img-div img:hover {
    opacity: 1;
    transform: scale(1.1);
}

.tools-div {
    width: 100%;
    height: 95vh;
    /* background-color: rgb(0, 0, 0, 0.5); */
}

.tab-div {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 880;
    width: 100%;
    height: auto;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.image-data-div {
    padding-left: 30px;
    text-align: left;
    color: #ffffff;
}

.show-data-div {
    margin: 10px;
}

.selected {
    background-image: linear-gradient(to right, rgb(51 213 31), rgb(33 112 0)) !important;
}

.tab-div-btn {
    margin: 30px 20px;
    padding: 10px;
    font-size: 14px;
    color: #ffffff;
    border-radius: 8px;
    opacity: 1;
    background-image: linear-gradient(to right, rgb(0, 0, 0), rgb(183, 183, 183));
}

.tab-div-btn:hover {
    color: #55ff00;
    transform: scale(1.1);
    background-image: linear-gradient(to right, rgb(0, 0, 0), rgb(129, 128, 128));
}

.green {
    color: #55ff00;
}

.copy:hover {
    color: #2d8202;
}

.copy:active {
    color: #143305;
}

.ml {
    margin-left: 18px;
}

.text-dec {
    text-decoration: underline
}

.text-dec:hover {
    color: #2d8202;
    /* transform: scale(1.2); */
}

.textarea {
    width: 80%;
    min-width: 50%;
    max-width: 99.8%;
}
</style>
