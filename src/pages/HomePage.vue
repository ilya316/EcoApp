<script setup>
import AirQuality from "../components/AirQuality.vue";
import NewsCard from "../components/NewsCard.vue";
</script>

<template>
    <div class="wrapper">
        <AirQuality airquality="32" city="Москва"/>
        <NewsCard v-for="i in 5" url="https://ria.ru/" imagepath="/src/assets/testimage.png" text="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Doloribus suscipit placeat nam expedita labore modi recusandae, ut magnam. Dicta, iure enim. Provident at amet maiores tempore magnam sunt eius molestias."/>
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
