workbox.routing.registerRoute(({
  request
}) => request.destination === 'image',
  new workbox.strategies.CacheFirst({
    cacheName: 'images',
    plugins: [
      new workbox.cacheableResponsePlugin.CacheableResponsePlugin({
        statuses: [200],
      }),
      new workbox.expirationPlugin.ExpirationPlugin({
        maxEntries: 1000000,
        maxAgeSeconds: 60 * 60 * 24 * 2,
      }),
    ],
  }),
);