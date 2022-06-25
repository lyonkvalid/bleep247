<template>
    <div>
        <div v-if="false">
            <p class="uppercase md:hidden">Your Topics</p>
            <b-scroll-x class="mt-2 ml-2">
                <b-pill>Software Engineering</b-pill>
            </b-scroll-x>
        </div>
        <div v-else class="flex">
            <div class="mr-2 px-3 py-1 text-2xl bg-slate-100 rounded-full">&plus;</div>
            <p class="my-auto">Keep up with latest in any topic</p>
        </div>
    </div>
</template>
<script>
    export default {};
</script>