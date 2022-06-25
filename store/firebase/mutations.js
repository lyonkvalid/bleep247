export default {
    ON_AUTH_STATE_CHANGED(state, { uid, email, emailVerified, photoURL }){
        state.user = { uid, email, emailVerified, photoURL };
    }
};