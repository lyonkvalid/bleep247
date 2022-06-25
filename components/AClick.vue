<template>
    <div @click="send">
        <slot />
    </div>
</template>
<script>
    export default {
        props: {
            indexName: String,
            id: Number,
        },
        computed: {
            userId(){
                return this.$auth.user.uid;
            }
        },
        methods: {
            send(){
                this.$axios.$post(`/api/click/${this.indexName}`, {
                    type: "click",
                    id: this.id,
                    user: this.userId,
                    indexName: this.indexName
                });
            }
        }
    };
</script>