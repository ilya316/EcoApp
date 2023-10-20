<script setup>
import SidebarMenu from './SidebarMenu.vue';
import ProfileIcon from './icons/IconProfile.vue';
import { RouterLink } from 'vue-router';
import { ref } from 'vue'
const isActive = ref(false)
</script>

<template>
  <header>
    <nav :class="{'active' : isActive}">
      <SidebarMenu @toggle="() => isActive = !isActive"/>
    </nav>
      <RouterLink to="/" class="logo" @click="() => isActive = false">
        EcoApp
      </RouterLink>
      <RouterLink to="/profile" class="profile">
        <ProfileIcon/>
      </RouterLink>
  </header>
</template>

<style scoped>
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px;
  background-color: var(--main-color);
}
.menu, .profile, .logo {
  height: 24px;
}

.logo {
  text-align: center;
  font-family: 'Jura', sans-serif;
  font-size: 20px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  letter-spacing: 3.6px;
  text-decoration: none;
  color: var(--text-color);
}

.sidebar {
  position: fixed;
  top: 48px;
  width: 312px;
  transform: translate(-312px);
}

.sidebar.open {
  transform: translate(0px);
}
</style>
