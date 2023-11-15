<script setup>
import MenuIcon from './icons/IconMenu.vue'
import AdviceIcon from './icons/IconAdvice.vue'
import MapIcon from './icons/IconMap.vue'
import ExportIcon from './icons/IconExport.vue'

import { RouterLink } from 'vue-router';

</script>

<template>
  <button class="menu" @click="$emit('toggle')">
    <MenuIcon />
  </button>
  <ul class="sidebar">
    <li>
      <RouterLink to="/map" @click="$emit('toggle')">
        <MapIcon />
        <p>Карта мест приёма отходов</p>
      </RouterLink>
    </li>
    <li>
      <RouterLink to="/advices" @click="$emit('toggle')">
        <AdviceIcon />
        <p>Советы по утилизации</p>
      </RouterLink>
    </li>
    <li>
      <RouterLink to="/export" @click="$emit('toggle')">
        <ExportIcon />
        <p>Компании по вывозу мусора</p>
      </RouterLink>
    </li>
    <li>
      <RouterLink to="/tasks" @click="$emit('toggle')">
        <AdviceIcon />
        <p>Полезные привычки</p>
      </RouterLink>
    </li>
  </ul>
</template>

<style scoped>
.menu{
  height: 24px;
}
.sidebar {
  position: fixed;
  top: 48px;
  left: 0;
  width: 312px;
  transform: translate(-100%);
  transition: transform 300ms ease-out;
  height: 100%;
  width: calc(100% - 48px);
  background-color: var(--main-color);
  display: flex;
  flex-direction: column;
  gap: 12px;
  z-index: 1000;
}

.active > .sidebar {
  transform: translate(0);
}

li:first-child {
  margin-top: 12px;
}

a {
  margin-left:6px ;
  display: flex;
  align-items: center;
  text-decoration: none;
  height: 48px;
  width: calc(100% - 12px);
  box-sizing: border-box;
  background-color: var(--help-color);
  border-radius: 6px;
  border: 1px solid var(--text-color);
  padding: 12px;
  gap: 12px;
  font-weight: 700;
}
</style>
