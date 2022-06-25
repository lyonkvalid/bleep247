import { GoogleAuthProvider, FacebookAuthProvider, TwitterAuthProvider, GithubAuthProvider } from "firebase/auth";

export default [
    {
        name: "Google",
        provider: GoogleAuthProvider
    },
    {
        name: "Facebook",
        provider: FacebookAuthProvider
    },
    {
        name: "Twitter",
        provider: TwitterAuthProvider
    },
    {
        name: "GitHub",
        provider: GithubAuthProvider
    }
];