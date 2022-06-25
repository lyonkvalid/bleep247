export default {
    target: 'static',
    ssr: false,

    head: {
        title: 'bleep247',
        meta: [{
            charset: 'utf-8'
        },
            {
                name: 'viewport',
                content: 'width=device-width, initial-scale=1'
            },
            {
                hid: 'description',
                name: 'description',
                content: ''
            },
            {
                name: 'format-detection',
                content: 'telephone=no'
            },
        ],
        link: [{
            rel: 'icon',
            type: 'image/x-icon',
            href: '/favicon.ico'
        }],
    },

    css: ['~assets/css/fonts',
        '~assets/css/index'],

    plugins: [
        '~plugins/screen',
        '~plugins/swiper',
        '~plugins/animate',
        '~plugins/tooltip',
        '~plugins/auth',
        '~plugins/mixin',
        '~plugins/instantSearch'
    ],

    components: true,

    buildModules: [
        '@nuxtjs/google-fonts',
        'nuxt-windicss',
    ],

    modules: [
        '@nuxtjs/axios',
        '@nuxtjs/pwa',
        '@nuxt/content',
        '@nuxtjs/gtm',
        [
            '@nuxtjs/firebase',
            {
                config: {
                    apiKey: 'AIzaSyDkyhL77UWQiDiJvG7JA5omFMWzqzPry7c',
                    authDomain: 'bleep247.firebaseapp.com',
                    projectId: 'bleep247',
                    storageBucket: 'bleep247.appspot.com',
                    messagingSenderId: '787770111156',
                    appId: '1:787770111156:web:e1fe0c5b10af8136e993e1',
                    measurementId: 'G-8454E6SM2T'
                },
                services: {
                    auth: {
                        persistence: 'local',
                        initialize: {
                            subscribeManually: false,
                            onAuthStateChangedAction: 'firebase/onAuthStateChanged',
                            onAuthStateChangedMutation: 'firebase/ON_AUTH_STATE_CHANGED'
                        }
                    }
                }
            }]
    ],

    axios: {
        baseURL: 'http://localhost:8000/',
    },

    pwa: {
        manifest: {
            lang: 'en',
        },
    },

    content: {},

    googleFonts: {
        download: true,
        base64: true,
        families: {
            Nunito: true,
            Merriweather: true
        },
    },

    algolia: {
        apiKey: '<YOUR_SEARCH_API_KEY>',
        applicationId: '<YOUR_APPLICATION_ID>',
    },

    gtm: {
        id: 'GTM-PB8K9SB',
    },

    build: {},
};