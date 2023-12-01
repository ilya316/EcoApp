<script setup>
import { onMounted, ref } from "vue";
import axios from "axios"
let data = ref(null);

onMounted(() => {
    try {
      axios.get('http://127.0.0.1:8000/wastes/sites/').then(response => {data.value = getcoords(response.data);})
  } catch (error) {
      console.error('Ошибка: ', error);
  }
})

function getcoords(data) {
    let a = []
    for (let i = 0; i < data.length; i++) {
        a.push({lat: data[i].longitude, lng: data[i].lattitude})
    }
    return a
}

</script>

<template>

   <GMapMap
      :center="{lat: 55.751244, lng: 37.618423}"
      :zoom="15"
      :icon="'https://cdn0.iconfinder.com/data/icons/ecology-68/64/recycle-bin-garbage-trash-1024.png'"
      map-type-id="terrain"
      class="map"
  >
    <GMapCluster :zoomOnClick="true">
        <GMapMarker
            v-if="data"
            v-for="item in data"
            :position="item"
        >
        </GMapMarker>
    </GMapCluster>

  </GMapMap>
  
</template>

<style scoped>
.map {
    width: 100vw;
    height: calc(100vh - 48px);
}
</style>
