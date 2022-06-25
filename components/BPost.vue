<template>
    <div class="col sm:row space-y-8 md:space-y-0 md:flex-wrap">
        <div v-if="posts" :data-insight-index="story">
            <div v-if="posts.length > 0" >
                <BPostChild
                    v-for="post in posts"
                    :key="post.id" 
                    :post="post" 
                    :data-insights-object-id="post.id" 
                    :data-insights-position="index" />
            </div>
            <div v-else>
                No Item found
            </div>
        </div>
        <div v-else>
            loading...
        </div>
    </div>
</template>
<script>
    export default {
        props: {
            query: {
                type: String,
                default: ""
            },
            path: {
                type: String,
                default: ""
            }
        },
        data(){
            return {
                posts: null
            };
        },
        watch: {
            path(value){
                this.$fetch();
            }
        },
        async fetch(){
             this.posts = await this.$axios.get(`/api/story/${this.path}?${this.query}`).then(({ data })=> data);
        }
    };
</script>