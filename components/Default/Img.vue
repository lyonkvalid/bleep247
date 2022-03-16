<template>
  <img :src="src" :alt="alt" class="cover" oncontextmenu="return false;" @click="$emit('toggle')" />
</template>
<script>
  export default {
    props: {
      src: {
        type: String,
        default: String
      },
      alt: {
        type: String,
        default: String
      }
    }
  };
</script>