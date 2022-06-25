<template>
    <div class="row space-x-6 border-b-1 text-slate-500">
        <BTabChild v-for="tab in tabs" :key="tab.id" :tab="tab" @tabSelect="value => $emit('tabSelect', value)" />
    </div>
</template>
<script>
    export default {
        emits: ["tabSelect"],
        data() {
            return {
                tabs: [{ 
                    id: 0,
                    hash: "following",
                    text: "Following",
                    mustAuthenticate: true
                },
                {
                    id: 1,
                    hash: "recommended",
                    text: "Recommended",
                    mustAuthenticate: false
                }]
            };
        }
    };
</script>