<template>
  <div v-if="isNavOpen">
    <aside class="sidenav pt-3 pb-5" style="z-index: 20;">
      <div class="flex items-center px-3">
        <input type="text" placeholder="Search For Articles" class="p-2 container bg-white rounded-l-sm bold" />
        <div class="inline-block p-3 bg-yellow-400 rounded-r-sm"><default-img src="/icons/search.jpg" class="w-4" /></div>
      </div>
      <div class="mt-4">
        <h1 class="bold text-lg p-2">Top Search</h1>
        <div class="mt-2 flex flex-row overflow-x-auto">
          <button v-for="i in 10" :key="1" class="rounded-full bg-yellow-400 px-4 py-1 mx-1">#Buhari</button>
        </div>
      </div>
    </aside>
  </div>
</template>
<script>
  export default {
    props: {
      isNavOpen: {
        type: Boolean,
        default: Boolean
      }
    },
    computed: {
      tabs() {
        return this.$store.state.tabs;
      }
    }
  };
</script>