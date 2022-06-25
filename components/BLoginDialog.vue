<template>
    <BDialog id="auth" :show="show">
        <div class="col px-4">
        <div class="flex-none pt-2 pb-4">
            <div class="row">
                <span @click="$router.back()" class="text-2xl">&times;</span>
            </div>
            <div class="mt-4 text-center">
                <b class="text-2xl font-bold">Grant access to Bleep247</b>
                <p class="text-slate-500 mt-2 text-sm">Manage your account, check notifications, comment on stories, and more.</p>
            </div>
        </div>
        <div class="flex-1 mt-8 col space-y-4">
            <div v-for="(provider, index) in providers" :key="index" @click="authenticate(provider.provider)" class="row border-1 rounded-sm">
                <div class="p-2 border-r-1">
                    <b-img :asset="require(`~/assets/img/icons/social/ic_${provider.name.toLowerCase()}.png`)" class="w-6 h-6" />
                </div>
                <div class="text-slate-700 m-auto"> Continue with {{ provider.name }} </div>
            </div>
        </div>
        </div>
    </BDialog>
</template>
<script>
    import { getAuth, signInWithPopup, fetchSignInMethodsForEmail } from "firebase/auth";
    import providers from "../src/loginProviders";
    
    export default {
        data(){
            return {
                providers
            };
        },
        computed: {
            show(){
                return !this.loggedIn;
            }
        },
        methods: {
            authenticate(provider, callback=null){
                const auth = getAuth();
                const _provider = new provider();
                return signInWithPopup(auth, _provider).then(({ user }) => {
                    alert("loggedIn");
                    callback === null ? this.$router.back() : callback(user);
                }).catch(error => {
                    if(error.code === "auth/account-exists-with-different-credential"){
                        const pendingCred = error.credential;
                        const email = error.email || error.customData.email;
                        
                        return fetchSignInMethodsForEmail(auth, email).then(methods => {
                           const provider = this.providers.find(obj => methods[0].includes(obj.name.toLowerCase()));
                           this.authenticate(provider.provider, user => {
                                user.linkAndRetrieveDataWithCredential(pendingCred).then(userCred => {
                                    this.$router.back();
                                    alert("loggedIn");
                                });
                            });
                        }).catch(e => alert(e));
                    }
                });
            }
        }
    };
</script>