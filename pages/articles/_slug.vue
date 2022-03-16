<template>
  <article class="p-2">
    <NuxtLink to="#" class="text-yellow-500 text-sm">{{ article.country.join("").toUpperCase() }}</NuxtLink>
    <div class="mt-4">
      <h1 class="text-lg font-bold">{{ article.title }}</h1>
      <h6 class="text-gray-500 mt-2 text-sm">By <b class="bold">{{ article.source_id }} </b> • {{ $formatDate(article.pubDate) }}</h6>
      
      <cption class="my-3 mt-5">
        <figure class="px-3 mt-4">
          <default-img :src="article.image_url" class="w-screen h-1/2" />
        </figure>
        <figcaption class="text-center mt-2 text-sm text-gray-500"><i>{{ article.description }}</i></figcaption>
      </cption>
      <div class="mt-4 p-1" v-html="article.content"></div>
    </div>
  </article>
</template>
<script>
  export default {
    computed: {
      article() {
        return this.$store.state.currentArticle;
      }
    }
  };
</script>