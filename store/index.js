export default {
    state(){
        return {
            user: null
        };
    },
    mutations: {
        SET_USER(state, user){
            state.user = user;
        }
    }
};