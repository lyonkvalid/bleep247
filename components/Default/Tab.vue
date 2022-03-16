<template>
  <span id="tab" class="pt-2 px-2 inline-block">
    <nuxt-link :to="`/${link}`" class="tab pb-2 inline-block text-gray-500 mx-1"> {{ tab.name }} </nuxt-link>
  </span>
</template>
<script>
  export default {
    props: {
      tab: {
        type: Object,
        default: Object
      }
    },
    computed: {
      link() {
         return this.tab.name.toLowerCase();
      }
    }
  };
</script>