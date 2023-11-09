<script setup>
import AdviceCard from "../components/AdviceCard.vue";
import { ref } from "vue";
let input = ref("");
const cards = [
  {
    "heading": "Картон",
    "text": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Doloribus suscipit placeat nam expedita labore modi recusandae, ut magnam. Dicta, iure enim. Provident at amet maiores tempore magnam sunt eius molestias.",
    "image": "/src/assets/testimage.png"
  },
  {
    "heading": "Журналы",
    "text": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Doloribus suscipit placeat nam expedita labore modi recusandae, ut magnam. Dicta, iure enim. Provident at amet maiores tempore magnam sunt eius molestias.",
    "image": "/src/assets/testimage.png"
  },
  {
    "heading": "Стекло",
    "text": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Doloribus suscipit placeat nam expedita labore modi recusandae, ut magnam. Dicta, iure enim. Provident at amet maiores tempore magnam sunt eius molestias.",
    "image": "/src/assets/testimage.png"
  },
  {
    "heading": "Чашки",
    "text": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Doloribus suscipit placeat nam expedita labore modi recusandae, ut magnam. Dicta, iure enim. Provident at amet maiores tempore magnam sunt eius molestias.",
    "image": "/src/assets/testimage.png"
  },
  {
    "heading": "Стаканы",
    "text": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Doloribus suscipit placeat nam expedita labore modi recusandae, ut magnam. Dicta, iure enim. Provident at amet maiores tempore magnam sunt eius molestias.",
    "image": "/src/assets/testimage.png"
  },
  {
    "heading": "Металл",
    "text": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Doloribus suscipit placeat nam expedita labore modi recusandae, ut magnam. Dicta, iure enim. Provident at amet maiores tempore magnam sunt eius molestias.",
    "image": "/src/assets/testimage.png"
  }
];

function filteredList() {
  return cards.filter((card) =>
    card['heading'].toLowerCase().includes(input.value.toLowerCase())
  );
}

</script>

<template>
  <div class="search__wrap">
    <input type="text" v-model="input" placeholder="Что вы хотите выбросить?" />
  </div>
    
  <div class="wrapper">
      <div class="card" v-for="item in filteredList()">
          <AdviceCard :imagepath="item.image" :heading="item.heading" :text="item.text"/>
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
