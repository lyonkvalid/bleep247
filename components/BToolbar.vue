<template>
    <header class="row p-2 bg-white">
        <div @click="openDrawer" class="flex-none md:hidden">
            <b-img :asset="require('~/assets/img/icons/ic_menu.png')" class="h-6 w-6" />
        </div>
        <div class="flex-1 md:hiden">
            <BLogo class="mx-auto" />
        </div>
    </header>
</template>
<script>
    export default {
        methods: {
            openDrawer(){
                event.stopPropagation();
                this.$router.push({ hash: "drawer" });
            }
        }
    };
</script>