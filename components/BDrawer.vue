<template>
  <transition 
    :duration="250"
    name="slide"
    enter-active-class="slideInLeft"
    leave-active-class="slideOutLeft"> 
    <aside id="drawer" v-if="isDrawerOpen" :class="customClass" class="col fixed md:block md:static h-full md:h-[100vh] w-58 bg-slate-100 z-20 shadow-sm">
        <BAvatar :link="photoURL" class="flex-none m-2" />
        <BDrawerNav class="flex-1 mt-4 pr-4" />
        <div class="flex-none py-2 px-4 border-t-1">
            <span> Settings</span>
        </div>
    </aside>
    </transition>
</template>
<script>
    export default {
        computed: {
            photoURL(){
                return this.$store.getters["firebase/photoURL"];
            }
        },
        watch: {
            $route(to){
                this.isDrawerOpen = to.hash.includes("drawer");
            },
            screenWidth(){
                this.isDrawerOpen = this.$route.hash.includes("drawer");
            },
            isDrawerOpen(state){
                content.style.position = state ? "fixed" : null;
            }
        }
    };
</script>