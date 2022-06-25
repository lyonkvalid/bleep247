<template>
    <v-popover class="float-right">
        <b-img :asset="require('~/assets/img/icons/ic_more.png')" class="tooltip-target w-5 h-5 float-right" />
       
            <div class="font-body text-slate-600" slot="popover">
                <div v-for="action in actions" :key="action.link" class="first:border-b-1 first:py-4 px-4 py-2 last:pb-4 last:pt-2">
                    {{ action.text }}
                </div>
            </div>
    </v-popover>
</template>
<script>
    export default {
        data(){
            return {
                actions: [
                    {
                        link: "/%o/flag/",
                        text: "Show less like this"
                    },
                    {
                        link: "/%o/mute_author/",
                        text: "Mute this Author"
                    },
                    {
                        link: "/%o/mute_publication/",
                        text: "Mute this publication"
                    },
                    {
                        link: "/%o/report/",
                        text: "Report"
                    }
                ]
            }
        }
    };
</script>