<template>
    <img :src="src" @click="$emit('click')" class="object-cover" oncontextmenu="return false;" />
</template>
<script>
    export default {
        emits: ["click"],
        props: ["asset", "link"],
        computed: {
            src(){
                return this.asset || this.link;
            }
        }
    };
</script>