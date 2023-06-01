import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import PowerliftingHomePage from '../components/powerlifting/PowerliftingHomePage.vue';
import StrongmanHomePage from '../components/odd_lifts/StrongmanHomePage.vue';
import RunningHomePage from '../components/running/RunningHomePage.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage,
  },
  {
    path: '/powerlifting',
    name: 'powerlifting',
    component: PowerliftingHomePage,
  },
  {
    path: '/oddLifts',
    name: 'oddLifts',
    component: StrongmanHomePage,
  },
  {
    path: '/running',
    name: 'running',
    component: RunningHomePage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
