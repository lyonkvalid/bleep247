<template>
    <div class="row space-x-2 md:max-w-1/2 md:px-2 md:pb-4">
        <BAvatar class="flex-none" />
        <div class="flex-1 col space-y-2">
            <header class="row">
                <div class="flex-none">
                    <span>Oguntunde Caleb</span> <span class="text-sm text-slate-500">@lyonkvalid</span>
                </div>
                <div class="flex-1">
                    <BPostSetting />
                </div>
            </header>
            <b class="text-lg font-merriweather">
                Scalability and Simplicity is a solution to complexity.
            </b>
            <div class="row">
                <div class="flex-none row space-x-3">
                    <div class="px-4 py-0.5 bg-slate-100 rounded-full text-sm">
                        Android
                    </div>
                    <p class="text-slate-500 my-auto text-sm">
                        3 mins read
                    </p>
                </div>
                <div class="flex-1">
                    <b-img :asset="require('~/assets/img/icons/ic_bookmark.png')" class="w-6 h-6 float-right" />
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {};
    </script>