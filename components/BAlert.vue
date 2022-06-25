<template>
    <div :class="[_class]" class="row space-x-2 sm:w-72 sm:mx-auto md:mx-0 p-3 rounded-lg">
        <slot />
    </div>
</template>
<script>
    export default {
        props: {
            color: {
                type: String,
                default: "bg-slate-100"
            }
        },
        computed: {
            _class() {
                return [this.color];
            }
        }
    };
</script>