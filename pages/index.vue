<template>
    <div class="p-4 md:row md:flex-wrap">
        <section class="col md:row md:space-x-4 space-y-4 md:space-y-0">
            <BAlert class="md:my-auto"> 
                <b-circle class="flex-none my-auto" />
                <p class="flex-1">What are we reading today?</p>
            </BAlert>
            <BTags />
        </section>
        <section class="md:mt-2 md:w-full">
            <BStatus />
        </section>
        <section class="mt-4 md:w-full">
            <BTab @tabSelect="onTabSelect" class="sticky top-12 bg-white" />
            <BPost class="mt-8" :path="path" />
        </section>
    </div>
</template>
<script>
    export default {
        computed: {
            path: {
                get(){
                   return this.$route.query.post || "recommended";
                },
                set(value){
                    return value;
                }
            }
        },
        methods: {
            onTabSelect(tab){
                this.path = tab.hash;
            }
        },
        mounted(){
            if(this.$route.hash === "") this.$router.push({ hash: "recommended", query: { post: "recommended" } });
        }
    };
</script>