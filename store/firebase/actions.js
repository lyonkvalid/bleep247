export default {
    onAuthStateChanged({ commit } , { authUser, claims }){
        if(authUser)
            commit("ON_AUTH_STATE_CHANGED", authUser);
    }
};