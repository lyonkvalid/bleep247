<template>
    <div>
        <b-img v-if="visible" :link="link" @error="onError" onerror="alert('error')" class="h-10 w-10 rounded-full" />
        <div v-else class="h-10 w-10 rounded-full bg-purple-200" />
    </div>
</template>
<script>
    export default {
        props: {
            link: {
                type: String,
                default: null
            }
        },
        data(){
            return {
                visible: Boolean(this.link)
            };
        },
        methods: {
            onError(e){
                alert("error");
            }
        }
    }
</script>