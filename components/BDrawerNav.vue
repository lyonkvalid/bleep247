<template>
    <nav class="col space-y-4 h-[100vh]">
        <BDrawerNavChild v-for="(nav, index) in navs" :key="index" :nav="nav" />
    </nav>
</template>
<script>
    import { navs } from "../src/ui/drawer.js";
  
    export default {
        data(){
            return {
                navs
            };
        }
    };
</script>