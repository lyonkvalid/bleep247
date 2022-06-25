<template>
    <span :class="[this.color]" @click="$emit('click')" class="py-2 px-4 text-sm rounded-full"><slot /></span>
</template>
<script>
    export default {
        emits: ["click"],
        props: {
            color: {
                type: String,
                default: "bg-slate-100"
            }
        }
    };
</script>