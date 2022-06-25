<template>
    <div class="col p-4">
        <section class="">
            <BTags />
            <div class="">
                <div class="row space-x-2">
                    <div class="flex-none">
                        <BCircle><b-img src="#" class="w-6 h-6" /> </BCircle>
                        <b class="text-xl">{{ tag }}</b>
                    </div>
                </div>
                <div class="row">
                    <BOverlapImg :images="[]" />
                    <div class="">
                        <p class="inline-block"> <span>47K</span> <span class="text-slate-500">Writers</span> </p>
                        <p class="inline-block"> <span>35K</span> <span class="text-slate-500">Stories</span> </p>
                    </div>
                </div>
                <div class="row">
                    <button class="px-2 py-1 bg-purple-700">Follow</button>
                    <button class="px-2 py-1 border-1 border-purple-700 text-purple-700 ring-1 ring-purple-400">Start writing</button>
                </div>
                <div class="mt-4 py-2 px-4 border-b-1">
                    <BFilter :filters="[]" />
                </div>
            </div>
        </section>
        <section class="mt-4">
            <BPost />
        </section>
    </div>
</template>
<script>
    export default {
        
    };
</script>