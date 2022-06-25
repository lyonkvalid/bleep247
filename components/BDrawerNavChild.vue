<template>
    <div :class="{ 'rounded-r-full bg-purple-200 font-bold !text-purple-700': isActive }" @click="intent" class="px-4 py-3 text-slate-600">
        {{ nav.name }}
    </div>
</template>
<script>
    export default {
        props: {
            nav: {
                type: Object,
                default: {}
            }
        },
        computed: {
            isActive(){
                return this.$route.path === this.nav.path;
            }
        },
        methods: {
            intent(){
                this.$router.push({ path: this.nav.path })
            }
        }
    }
</script>