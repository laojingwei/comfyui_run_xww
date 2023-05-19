import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

const router = new VueRouter({
    routes: [
        // 添加具体的路由配置：配置的本质就是将路由映射到组件
        // 选项：name path component redirect children
        // name:路由名称
        // path:路由路径，如果想要进入默认页面，那么path需要配置成'/'
        // component:路由所映射的组件对象
        // redirect:重定向，可以把path的路径重定向到其它路径
        {
            name: 'bg',
            path: '/',
            // 异步引入组件,确保匹配了路由才加载组件
            component: () => import('@/components/mainPageBg.vue')
        },
        {
            name: 'start_config',
            path: '/start_config',
            // 异步引入组件,确保匹配了路由才加载组件
            component: () => import('@/components/startConfig/startConfig.vue')
        },
        {
            name: 'molelsShow',
            path: '/molelsShow',
            // 异步引入组件,确保匹配了路由才加载组件
            component: () => import('@/components/molelsShow/molelsShow.vue')
        },
        {
            name: 'upDownload',
            path: '/upDownload',
            // 异步引入组件,确保匹配了路由才加载组件
            component: () => import('@/components/upDownload/upDownload.vue')
        },
        {
            name: 'customNode',
            path: '/customNode',
            // 异步引入组件,确保匹配了路由才加载组件
            component: () => import('@/components/customNode/customNode.vue')
        },
        {
            name: 'tools',
            path: '/tools',
            // 异步引入组件,确保匹配了路由才加载组件
            component: () => import('@/components/tools/tools.vue')
        }

    ]
})
export default router