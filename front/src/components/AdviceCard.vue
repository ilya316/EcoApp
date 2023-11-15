<script setup>
defineProps({
  imagepath: String,
  text: String,
  heading: String,
})
</script>

<template>
  <div class="card">
    <img :src="imagepath" alt="test">
    <div>
      <p class="heading">{{ heading }}</p>
      <p class="text">{{ text }}</p>
    </div>
    <RouterLink :to="{ name: 'advice', params: { id: heading }}" class="view">
      <p>Посмотреть советы</p>
    </RouterLink>
  </div>
</template>

<style scoped>
  .view {
      position: absolute;
      inset: 0;
      opacity: 0;
    }
  .card { 
    position: relative;
    height: 96px;
    width: 100%;
    border-radius: 6px;
    display: flex;
    gap: 12px;
    padding: 6px;
    background-color: var(--main-color);
    box-sizing: border-box;
  }

  img {
    width: 126px;
    height: 84px;
    object-fit: cover;
    border-radius: 6px;
  }

  .heading {
    font-size: 1rem;
    font-weight: 700;
  }
  .text {
    height: 59px;
    overflow: hidden;
    font-size: 0.75rem;
    margin-top: 6px;
    box-sizing: border-box;
  }
</style>
