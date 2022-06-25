import Auth from "../src/auth.js";

export default (ctx, inject) => {
    const auth = new Auth(ctx, () => null);
    inject("auth", auth);
};