import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './pages/HomePage.vue';
import AdvicePage from './pages/AdvicePage.vue';
import ProfilePage from './pages/ProfilePage.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
    {
      path: '/',
      component: HomePage,
    },
    {
      path: '/advice',
      component: AdvicePage,
    },
    {
      path: '/profile',
      component: ProfilePage,
    },
  ],
});

const app = createApp(App)

app.use(router)

app.mount('#app')