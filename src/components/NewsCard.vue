<script setup>
defineProps({
  imagepath: String,
  text: String,
  url: String,
})
</script>

<template>
  <div>
    <img :src="imagepath" alt="test">
    <p>{{ text }}</p>
    <a :href="url">Посмотреть новость</a>
  </div>
</template>

<style scoped>
  a {
    position: absolute;
    inset: 0;
    opacity: 0;
  }

  img { 
    object-fit: cover;
    height:100%;
    width: 100%;
    border-radius: 6px;
    position: absolute;
    z-index: -1;
  }
  div {
    position: relative;
    border-radius: 6px;
    height: 288px;
    width: 100%;
  }
  p {
    position: absolute;
    background-color: rgba(255, 255, 255, 0.75);
    text-shadow: 0px 0px 0px var(--text-color);
    font-size: 1.25rem;
    padding: 6px;
    border-radius: 6px;
    bottom: 0;
  }
</style>
