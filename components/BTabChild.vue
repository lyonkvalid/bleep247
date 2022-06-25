<template>
    <span :class="{ [activeClass]: isActive }" @click="intent" class="py-2">{{ tab.text }}</span>
</template>
<script>
    export default {
        middleware: "auth",
        emits: ["tabSelect"],
        props: {
            tab: {
                type: Object,
                default: {}
            }
        },
        data(){
            return {
                activeClass: ["px-1 text-black border-b-1 border-black"]
            };
        },
        computed: {
            hash(){
                return this.toHash(this.tab.hash);
            },
            isActive(){
                return this.$route.hash == this.hash;
            }
        },
        methods: {
            intent(){
                const hash =  this.tab.mustAuthenticate && !this.loggedIn  ? 
                   "auth" : this.tab.hash;
                const query = this.tab.mustAuthenticate && !this.loggedIn ? null : { post: this.tab.hash };
                this.$router.push({ hash, query });
            }
        }
    }
</script>