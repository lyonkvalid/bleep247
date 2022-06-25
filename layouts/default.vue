<template>
    <div class="col md:flex-row font-body">
        <BDrawer />
        <BLoginDialog />
        <div id="content" class="flex-1">
            <transition :duration="250" name="fade">
               <div v-if="isDrawerOpen && !this.md" @click="hideDrawer" class="overlay" />
            </transition>
            <BToolbar class="sticky top-0 z-10" />
            <Nuxt />
        </div>
    </div>
</template>
<script>
    export default {
        methods: {
            hideDrawer(){
                if(!this.md && this.isDrawerOpen)
                    this.$router.back();
            }
        }
    };
</script>