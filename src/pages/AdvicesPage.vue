<script setup>
import AdviceCard from "../components/AdviceCard.vue";
import { onMounted, ref } from "vue";
import axios from "axios"
let input = ref("");
let data = ref(null);
onMounted(() => {
    try {
      axios.get('http://127.0.0.1:8000/wastes/examples/').then(response => {data.value = response.data})
  } catch (error) {
      console.error('Ошибка: ', error);
  }
})

function filteredList() {
  return data.value.filter((card) =>
    card['name'].toLowerCase().includes(input.value.toLowerCase())
  );
}

</script>

<template>
  <div class="search__wrap">
    <input type="text" v-model="input" placeholder="Что вы хотите выбросить?" />
  </div>
    
  <div class="wrapper">
      <div class="card" v-if="data" v-for="item in filteredList()">
          <AdviceCard imagepath="/src/assets/testimage.png" :heading="item.name" :text="item.description"/>
      </div>
  </div>
</template>

<style scoped>
.wrapper {
    display: flex;
    flex-direction: column;
    gap: 6px;
    align-items: center;
    max-width: calc(100% - 24px);
    margin: 6px auto 0;
}

.search__wrap {
  height: 48px;
  width: calc(100% - 24px);
  margin: 6px 12px;
  border-radius: 6px;
  box-sizing: border-box;
  border: 5px solid var(--main-color);
  background-color: var(--main-color);
}
input {
  width: 100%;
  height: 100%;
  border: 1px solid var(--main-color);
  border-radius: 6px;
  box-sizing: border-box;
  padding: 0;
  text-align: center;
  font-size: 1rem;
}

</style>
