class Auth {
    constructor({ store, $fire, $axios }, callback){
        this.store = store;
        this.axios = $axios;
        this.auth = $fire.auth;
        this.callback = callback;
        this.token = window.localStorage.getItem("authToken");
        // setup
        this.setup();
    }
    
    async setToken(token){
        alert(token);
        this.axios.setToken(token, "Token");
        alert("setted token now");
    }
    
    fetchToken(){
        return new Promise((resolve, reject) => {
            this.auth.onAuthStateChanged(user => {
                if(user){
                    const token = user.toJSON().stsTokenManager.accessToken;
                    this.axios.$post("/auth/token/", { token }).then(({ token }) => {
                        window.localStorage.setItem("authToken", token);
                        return token;
                    }).then(token => this.setToken(token)).then(() => this.fetchUser());
                }
                reject("Login to access");
            })
        });
    }
    
    async fetchUser(){
        alert("is this called me fetching user...");
        const user = await this.axios.$get("/api/user/").catch(e => alert(e));
        this.store.commit("SET_USER", user);
        this.callback(user);
    }
    
    setup(){
       if(this.token)
            this.setToken(this.token).then(() => this.fetchUser()).catch(e => alert(e));
        else
            this.fetchToken().catch(e => alert(e));
    }
    
    loggedIn(){
        return !!this.store.state.user;
    }
    
    user(){
        return this.store.state.user;
    }
}

export default Auth;