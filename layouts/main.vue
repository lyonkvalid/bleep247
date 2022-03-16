<template>
  <div id="wrapper">
    <div class="flex flex-col">
      <div id="header">
        <DefaultToolbar />
      </div>
      <div id="section" class="h-screen overflow-y-auto">
        <div class="flex items-center p-2 pt-3">
          <div class="inline-block w-1 h-6 bg-yellow-300" style=""></div>
          <h1 id="customize" class="inline-block ml-1 bold">{{ customize }}</h1>
        </div>
        <Nuxt />
        <div id="footer" class="bg-gray-900 rounded-t-2xl p-2 pt-4 text-gray-100">
          <default-img src="icon.jpg" class="w-24 filter-yellow-600" />
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
    watch: {
      $route(to, from) {
        customize.innerHTML = this.$getTab().customize;
      }
    },
    computed: {
      customize() {
        return this.$getTab().customize;
      },
      socials() {
        return this.$store.state.socials;
      }
    },
    mounted() {
      section.style.height = (section.clientHeight - 135.2) + "px";
    },
  };
</script>