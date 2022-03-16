export const state = () => ({
  tabs: [
     { name: "HOME", customize: "TOP NEWS" },
     { name: "RECENT", customize: "JUST IN" },
     { name: "POLITICS", customize: "POLITICS",  source: ["thewest", "globalnews"] },
     { name: "SPORTS", customize: "SPORTS NEWS", source: ["skysports", "si", "castanet", "thetelegraphandargus"] },
     { name: "BUSINESS", customize: "BUSINESS NEWS", source: ["yahoo_sg", "yahoo"] },
     { name: "HEALTH", customize: "HEALTH NEWS", source: ["glasgowtimes", "theguardian", "globalnews"] },
     { name: "TECHNOLOGY", customize: "TECHNOLOGY", source:["tomsguide", "thewest"] },
     { name: "ENTERTAINMENT", customize: "ENTERTAINMENT NEWS", source: ["thewest", "kotaku", "etonline"] }
  ],
  socials: [
    { name: "facebook", link:"#" },
    { name: "instagram", link:"#" },
    { name: "telegram", link:"#" },
    { name: "discord", link:"#" },
  ],
  currentArticle: null
});

export const mutations = {
  updateArticle(state, article){
    state.currentArticle = article;
  }
};