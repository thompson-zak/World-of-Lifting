import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.use(BootstrapVue);

createApp(App).use(router).mount('#app');
