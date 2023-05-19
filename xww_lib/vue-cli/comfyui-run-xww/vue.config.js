/* eslint-disable  */
const path = require("path");
const systemConfig = { version: "1.0.0" };
const MiniCssExtractPlugin = require("mini-css-extract-plugin"); //表示自定义的系统配置
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    // 基本路径/-----这里为了打包出来能使用index.html，我改成了./
    publicPath: "./",
    // 输出文件目录-----为了方便python项目的代码读取打包内容，修改了打包位置
    outputDir: path.resolve(__dirname, "../../dist"),
    // eslint-loader 是否在保存的时候检查
    lintOnSave: true,
    configureWebpack: {
        output: {
            // 输出重构  打包编译后的 文件名称  【模块名称.版本号】
            filename: `js/[name].${systemConfig.version}.js`,
            chunkFilename: `js/[name].${systemConfig.version}.js`
        },
        plugins: [
            new MiniCssExtractPlugin({
                // 修改打包后css文件名
                filename: `css/[name].${systemConfig.version}.css`,
                chunkFilename: `css/[name].${systemConfig.version}.css`
            })
        ]
    },
    // 增加支持http
    configureWebpack: {
        performance: {
            hints: 'error', // 枚举
            maxAssetSize: 30000000, // 整数类型（以字节为单位） // 单个文件大小超出就提示
            maxEntrypointSize: 500000000, // 整数类型（以字节为单位） // 入口文件大小超出设定的值 就提示
            assetFilter: function (assetFilename) {
                // 提供资源文件名的断言函数
                return assetFilename.endsWith('.css') || assetFilename.endsWith('.js')
            }
        },
        resolve: { fallback: { http: require.resolve('stream-http') } }
    },
    // configureWebpack: {
    //     // webpack < 5 npm install stream-http
    //     // resolve: {
    //     //     fallback: {
    //     //         http: require.resolve('stream-http')
    //     //     }
    //     // }
    //     // webpack >= 5 npm install url
    //     resolve: { fallback: { url: require.resolve('url/') } }
    // }
    // 修改打包后img文件名
    // chainWebpack: config => {
    //     config.module
    //         .rule("images")
    //         .use("url-loader")
    //         .tap(options => {
    //             options.name = `img/[name].${systemConfig.version}.[ext]`;
    //             options.fallback = {
    //                 loader: "file-loader",
    //                 options: {
    //                     name: `img/[name].${systemConfig.version}.[ext]`
    //                 }
    //             };
    //             return options;
    //         });
    // },
    // webpack-dev-server 相关配置
    // devServer: {
    //     open: true,
    //     host: "localhost",
    //     port: 8080,
    //     https: false,
    //     hotOnly: false,
    //     proxy: {
    //         "/api/app": {
    //             target: "http://localhost:8080",
    //             changeOrigin: true, //是否跨域
    //             pathRewrite: {
    //                 "^/api/app": "/api/app" //重写接口
    //             }
    //         }
    //     }
    // }
});