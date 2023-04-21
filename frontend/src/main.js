import BootstrapVue3 from 'bootstrap-vue-3';
import { createApp } from 'vue';

import { plugin, defaultConfig } from '@formkit/vue';
import { createMultiStepPlugin } from '@formkit/addons';

import App from './App.vue';
import router from './router';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css';

import '@formkit/themes/genesis';
import '@formkit/addons/css/multistep';

const config = defaultConfig({
  plugins: [createMultiStepPlugin()],
  theme: 'genesis',
});

createApp(App)
  .use(router)
  .use(BootstrapVue3)
  .use(plugin, config)
  .mount('#app');
