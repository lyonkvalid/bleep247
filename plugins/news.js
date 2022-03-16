import humanDate from "human-date";

const api_key = "pub_5183c733d535a537fea99fea41acdfc8d82f";

export default ({ app, store, $axios, $route }, inject) => {
  inject("category", (category, source, page=1, q="", lang = "en") => {
    return $axios.get(`https://newsdata.io/api/1/news?apikey=${api_key}&language=en&page=${page}&category=${category}&domain=${source}`).then(({ data }) => data.results).catch(e => console.log(e));
  });
  
  inject("headline", (page=1) => {
    return $axios.get(`https://newsdata.io/api/1/news?apikey=${api_key}&language=en&domain=nypost,metro,skynews&page=${page}`).then(({ data }) => data.results);
  });
  
  inject("special", (category, page=1) => {
    return $axios.get(`https://newsdata.io/api/1/news?apikey=${api_key}&language=en&domain=cnn,nbcnews&category=top`).then(({ data }) => data.results).catch(e => console.log(e));
  });
  
  inject("formatDate", (string) => {
    return humanDate.relativeTime(new Date(string));
  });
  
  inject("getTab", () => {
     const tabs = store.state.tabs;
     return tabs.filter(tab => app.router.currentRoute.path.includes(tab.name.toLowerCase()))[0];
  });
};