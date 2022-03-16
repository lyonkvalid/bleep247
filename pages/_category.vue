<template>
  <div>
    <div v-if="$fetchState.pending" class="flex justify-center items-center" style="height: 65vh;">
      <img src="/icons/loading.svg" class="w-16 h-16" />
    </div>
    <div v-else id="content" class="flex flex-col md:flex-row-reverse">
      <div>
        <default-list v-for="(article, i) in banner" :key="i" :article="article" />
      </div>
      <div>
        <default-banner v-for="(article, i) in articles" :key="i" :article="article" />
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    layout: "main",
    data() {
      return {
        articles: [],
        banner: []
      };
    },
    asyncData({
      params
    }) {
      const category = (params.category === "home") ? null: params.category;
      return {
        category
      };
    },
    async fetch() {
      const articles = await ((this.category) ? ((this.category === "world" || this.category === "recent") ? this.$special("general") : this.$category(this.category, this.$getTab().source.join(","))) : this.$headline());
      this.banner = articles.splice(0, 1);
      this.articles = articles;
    }
  };  
</script>