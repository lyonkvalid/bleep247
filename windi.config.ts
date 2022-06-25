import { defineConfig } from '@windicss/plugin-utils';

export default defineConfig({
    attributify: false,
    theme: {
      fontFamily: {
         body: 'Nunito',
         merriweather: 'Merriweather'
      },
    },
    shortcuts: {
        "col": "flex flex-col",
        "row": "flex flex-row"
    }
});