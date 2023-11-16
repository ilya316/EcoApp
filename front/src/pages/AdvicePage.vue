<script setup>
import { onMounted, ref } from "vue";
import axios from "axios"
const props = defineProps({
  id: String,
})
let data = ref(null);
onMounted(() => {
    try {
      axios.get('http://127.0.0.1:8000/wast_examples/').then(response => {data.value = findcard(response.data);})
      
    } catch (error) {
      console.error('Ошибка: ', error);
  }
})

function findcard(data) {
  console.log()
  return data.find((card) =>
    card['name'].toLowerCase().includes(props.id.toLowerCase())
  );
}


</script>

<template>
    <div class="wrapper" v-if="data">
        <div class="img__wrap">
            <img src="/src/assets/testimage.png" alt="Пример мусора">
        </div>
        <p class="heading">{{data.name}}</p>
        <p class="text">{{data.description}}</p>
    </div>
</template>

<style scoped>
.wrapper {
    max-width: calc(100% - 24px);
    margin: 6px auto 0;
}

img {
    width: 100%;
    object-fit: cover;
    border-radius: 6px;
    display: block;
}
.img__wrap {
    border-radius: 6px;
    box-sizing: border-box;
    border: 6px solid var(--main-color);
    height: fit-content;
    background-color: var(--main-color);
    margin-bottom: 12px;
}

.heading {
    font-weight: 700;
    font-size: 1.25rem;
    margin-bottom: 6px;
}
.text {
    font-size: 1rem;
}
</style>
