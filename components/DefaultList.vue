<template>
  <div class="border-b-2 pb-2" @click="intent">
    <div class="flex md:flex-row flex-col flex-nowrap md:items-center items-start px-2 py-2">
      <div class="md:basis-3/4 basis-full">
        <default-img :src="article.urlToImage || article.image_url" class="md:w-64 rounded-lg w-screen" />
      </div>
      <div class="flex flex-row md:container ml-2 mt-2">
        <div class="container">
          <p class="text-uppercase text-sm font-medium"> {{ source }} </p>
          <h1 class="font-bold">{{ article.title }}</h1>
          <p class="text-gray-500 text-xs"> {{ $formatDate(article.publishedAt || article.pubDate ) }} </p>
        </div>
        <div class="ml-1 mt-2 md:mt-4">
          <default-img src="/icons/more.jpg" class="w-4 md:w-8 rotate-90" />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    props: {
      article: {
        type: Object,
        default: Object
      },
    },
    computed: {
      source(){
        const _source = this.article.source_id || this.article.source.name;
        return _source.replace(_source[0], _source[0].toUpperCase());
      }
    },
    methods: {
      intent(event){
        this.$store.commit("updateArticle", this.article);
        this.$router.push({ path: `/articles/${this.article.title}` });
      }
    }
  };
</script>