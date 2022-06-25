<template>
    <transition name="custom-bounce" :duration="500">
        <div v-if="isVisible" class="fixed top-0 w-full h-full md:right-0 md:w-[76.5%] md:col bg-[rgba(0,0,0,0.4)] z-20">
               <div class="target bg-white md:rounded-lg h-full w-full md:w-1/2 md:h-auto md:p-4 md:m-auto">
                    <slot />
               </div>
           </div>
       </transition>
</template>
<script>
    export default {
        props: {
            id: {
                type: String,
                default: "dialog"
            },
            show: {
                type: Boolean,
                default: true 
            }
        },
        data(){
            return {
                isVisible: this.getVisibility()
            };
        },
        watch: {
            $route(to){
                this.isVisible = this.getVisibility(to);
            },
            isVisible(visible){
                content.style.position = visible ? "fixed" : null;
            }
        },
        methods:{
            getVisibility(route=null){
                return (route || this.$route).hash.includes(this.id) && this.show;
            }
        }
    };
</script>