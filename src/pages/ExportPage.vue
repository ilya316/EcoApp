<script setup>
import AdviceCard from "../components/AdviceCard.vue";
let data =[
  {"url": "https://musor-msk.ru/img/logo.png",
  "name":"Вывоз мусора в Москве"},
  {"url": "https://glavmusor.ru/wp-content/uploads/2017/09/logo.png",
  "name":"Главмусор"},
  {"url": "https://musorzao.ru/images/logo/logo-13.svg",
  "name":"С-транс"},
  {"url": "https://vivozmusora.ru/images/logo-header.png",
  "name":"ДДБ Сервис"},
  // {"url": "",
  // "name":""}
]
</script>

<template>
  <div class="wrapper">
      <div class="card" v-if="data" v-for="item in data">
        <img :src="item.url" :alt="item.name">
        <p class="text">{{ item.name }}</p>
      </div>
  </div>
</template>

<style scoped>
  .wrapper {
    display: flex;
    flex-wrap: wrap;
    margin: 6px auto;
    max-width: calc(100% - 18px);
    gap: 6px;
  }
  .text {
    font-size: 1rem;
    font-weight: 700;
  }
  .card { 
    background-color: var(--main-color);
    padding: 6px;
    border-radius: 6px;
    max-width: calc(50% - 15px);
  }
  img {
    background-color: white;
    padding: 6px;
    border-radius: 6px;
    width: calc(100% - 12px);
    object-fit: cover;
  }
</style>
