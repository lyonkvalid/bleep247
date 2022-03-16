<template>
    <div id="wrapper">
    <div class="flex flex-col">
      <div id="header">
        <DefaultToolbar />
      </div>
      <div id="section" class="h-screen overflow-y-auto">
        <Nuxt />
        <div id="footer" class="bg-gray-900 rounded-t-2xl p-2 pt-4 text-gray-100">
          <default-img src="/icon.jpg" class="w-24 filter-yellow-600" />
          <div class="flex items-center my-3">
            <NuxtLink v-for="social in socials" :key="social.name" :to="social.link" class="mr-2"><default-img :src="`/social/${social.name}.jpg`" class="w-6 filter-yellow-50" /></NuxtLink>
          </div>
          <p class="text-center bold">© Oasis™</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    computed: {
      socials() {
        return this.$store.state.socials;
      }
    },
    mounted() {
      section.style.height = (section.clientHeight - 135.2) + "px";
    },
  };
</script>