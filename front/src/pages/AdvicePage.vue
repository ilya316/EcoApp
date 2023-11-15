<script setup>
const props = defineProps({
  id: String,
})
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
function findcard() {
  return cards.find((card) =>
    card['heading'].toLowerCase().includes(props.id.toLowerCase())
  );
}
console.log(findcard());
</script>

<template>
    <div class="wrapper">
        <div class="img__wrap">
            <img :src="findcard().image" alt="Пример мусора">
        </div>
        <p class="heading">{{findcard().heading}}</p>
        <p class="text">{{findcard().text}}</p>
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
