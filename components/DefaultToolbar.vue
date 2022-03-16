<template>
  <header class="flex flex-col bg-yellow-200 md:bg-gray-100 md:text-white sticky top-0">
    
       <DefaultNav class="md:hidden" :isNavOpen="is_nav_open" @close="navToggle" />
    <div class="flex flex-row basis-full">
      <div class="container md:w-1/5 flex flex-row md:bg-yellow-500 p-2">
        <default-img src="/icons/menu.jpg" alt="menu" class="w-6 h-6 md:hidden" @toggle="navToggle" />
        <default-img src="/icon.png" class="object-cover mx-auto md:mx-0" width="100em" height="100em" />
        <select id="language-picker" class="hidden md:inline ml-6 bg-transparent">
          <option>En</option>
        </select>
      </div>
      <div class="hidden md:inline w-screen flex items-center px-3">
        <default-img src='/icons/menu.jpg' align="right" class="mt-3" />
      </div>
    </div>
    <div class="flex flex-nowrap overflow-x-auto text-sm md:text-lg md:pt-2">
      <default-tab v-for="tab in tabs" :key="tab.src || tab.name.toLowerCase()" :tab="tab" />
    </div>
  </header>
</template>
<script>
  export default {
    data() {
       return {
         is_nav_open: false
       };
    },
    computed: {
      tabs() {
        return this.$store.state.tabs;
      },
    },
    methods: {
      navToggle(event){
        this.is_nav_open  = !this.is_nav_open;
      }
    }
  };
</script>