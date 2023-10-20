<script setup>
import MenuIcon from './icons/IconMenu.vue'
import AdviceIcon from './icons/IconAdvice.vue'
import MapIcon from './icons/IconMap.vue'
import ExportIcon from './icons/IconExport.vue'
import { ref } from 'vue'
import { RouterLink } from 'vue-router';
const isActive = ref(false)
</script>

<template>
  <button class="menu" :class="{'active' : isActive}" @click="() => isActive = !isActive">
    <MenuIcon :class="{'active' : isActive}" />
  </button>
  <ul class="sidebar" :class="{'active' : isActive}">
    <li>
      <RouterLink to="/map" @click="() => isActive = !isActive">
        <MapIcon />
        <p>Карта мест приёма отходов</p>
      </RouterLink>
    </li>
    <li>
      <RouterLink to="/advice" @click="() => isActive = !isActive">
        <AdviceIcon />
        <p>Советы по утилизации</p>
      </RouterLink>
    </li>
    <li>
      <RouterLink to="/export" @click="() => isActive = !isActive">
        <ExportIcon />
        <p>Компании по вывозу мусора</p>
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
}

.sidebar.active {
  transform: translate(0);
}

.menu.active {

}

a {
  display: flex;
}
</style>
