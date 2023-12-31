import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './pages/HomePage.vue';
import MapPage from './pages/MapPage.vue';
import AdvicesPage from './pages/AdvicesPage.vue';
import AdvicePage from './pages/AdvicePage.vue';
import ProfilePage from './pages/ProfilePage.vue';
import LoginPage from './pages/LoginPage.vue';
import RegisterPage from './pages/RegisterPage.vue';
import ExportPage from './pages/ExportPage.vue';
import AchievementsPage from './pages/AchievementsPage.vue';

import VueGoogleMaps from '@fawmi/vue-google-maps';

const router = createRouter({
    history: createWebHistory(),
    routes: [
    {
      path: '/',
      component: HomePage,
    },
    {
      path: '/map',
      component: MapPage,
    },
    {
      path: '/export',
      component: ExportPage,
    },
    {
      path: '/advices',
      component: AdvicesPage,
    },
    {
      path: '/advices/:id',
      name:'advice',
      props: true,
      component: AdvicePage,
    },
    {
      path: '/profile',
      component: ProfilePage,
    },
    {
      path: '/login',
      component: LoginPage,
    },
    {
      path: '/register',
      component: RegisterPage,
    },
    {
      path: '/achievements',
      component: AchievementsPage,
    },
  ],
});

const app = createApp(App)

app.use(router)

app.use(VueGoogleMaps, {
  load: {
      key: '',
  },
})

app.mount('#app')