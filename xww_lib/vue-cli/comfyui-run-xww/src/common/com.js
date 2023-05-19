/* eslint-disable */
let com = {
    check_time: function (t1, t2) {
        const currentTime = new Date().getTime();
        if (currentTime - t2 < t1) {
            return [false, t2];
        }
        t2 = currentTime;
        return [true, t2];
    },

    // 这个方法会受浏览器的同源策略限制
    check_web: async function () {
        let http = require('http');
        try {
            await new Promise((resolve, reject) => {
                http.get('http://127.0.0.1:8188/', (res) => {
                    // 如果状态码是2xx，表示成功 
                    if (res.statusCode.toString()[0] === '2') {
                        resolve();
                    } else {
                        // 否则表示失败
                        reject(new Error(`Status code: ${res.statusCode}`));
                    }
                }).on('error', (e) => {
                    // 如果发生错误，也表示失败 
                    reject(e);
                });
            });
            return true;
        } catch (e) {
            return false;
        }
    },

    // 这个不受浏览器的同源策略限制，但只能判断这连接是否正常
    async checkUrl() {
        try {
            await new Promise((resolve, reject) => {
                fetch('http://127.0.0.1:8188/', { mode: "no-cors" })
                    .then(response => {
                        resolve();
                    })
                    .catch(error => {
                        reject(new Error(error));
                    });
            });
            return true;
        } catch (e) {
            return false;
        }
    },

    format_time: function (time) {
        // 把字符串转换为毫秒数
        let ms = Date.parse(time);
        // 创建一个Date对象
        let date = new Date(ms);
        // 获取年份
        let year = date.getFullYear();
        // 获取月份（0-11）
        let month = date.getMonth();
        // 获取日期（1-31）
        let day = date.getDate();
        // 获取星期（0-6）
        let week = date.getDay();
        // 定义一个星期数组
        let weeks = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"];
        // 把数字转换为中文
        let weekName = weeks[week];
        // 拼接成你想要的格式
        let formattedDate = year + "年" + month + "月" + day + "日" + weekName + date.toLocaleTimeString();
        // 输出结果
        return formattedDate;
    }
}
module.exports = com;