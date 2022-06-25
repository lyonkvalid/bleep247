import Vue from "vue";

if(!Vue.__mixin__){
    Vue.__mixin__ = true;
    Vue.mixin({
        data(){
            return {
                screenWidth: window.innerWidth
            };
        },
        computed: {
            sm(){
                return this.screenWidth > 640;
            },
            md(){
                return this.screenWidth > 758;
            },
            isDrawerOpen: {
                set(value){
                    return this.value || this.md;
                },
                get(){
                    return this.$route.hash.includes("drawer") || this.md;
                }
            },
            loggedIn(){
                return this.$store.state.user;
            }
        },
        methods: {
            onResize(){
                this.screenWidth = window.innerWidth;
            },
            toHash(value){
                return value.trim().length === 0 ? "" : `#${value}`;
            }
        },
        mounted(){
            this.$nextTick(() => {
                window.addEventListener("resize", this.onResize);
            });
        },
        beforeDestroy(){
            window.removeEventListener("resize", this.onResize);
        }
    });
}