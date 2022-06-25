<template>
    <div :class="_class" class="rounded-full"><slot /></div>
</template>
<script>
    export default {
        props: {
            size: {
                type: String,
                default: "xs"
            },
            color: {
                type: String,
                default: "bg-green-500"
            }
        },
        data(){
            return {
                sizeVariant: {
                    xs: "w-3 h-3",
                    sm: "",
                    md: "w-8 h-8"
                }
            };
        },
        computed: {
            _class(){
                return [this.sizeVariant[this.size], this.color];
            }
        }
    };
</script>