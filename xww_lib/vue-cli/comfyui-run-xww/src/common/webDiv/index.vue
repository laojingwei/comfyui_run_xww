<template>
    <div class="web-container">
        <x-frame-bypass src="https://example.org/"></x-frame-bypass>
    </div>
</template>
<script>

// import Xframe from 'x-frame-bypass'
export default {
    name: 'web-div',
    components: {
        // 'x-frame-bypass': Xframe
    },
    props: {
        url: {
            type: String,
            default: ''
        }
    },
    data() {
        return {}
    },
    computed: {
    },
    watch: {
    },
    mounted() {
    },
    methods: {
    }
}
</script>
   
<style scoped>
.web-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 991;
}
</style>