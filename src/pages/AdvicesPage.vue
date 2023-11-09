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
</script>

<template>
    <div class="wrapper">
        <div class="card" v-for="item in cards">
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
</style>
