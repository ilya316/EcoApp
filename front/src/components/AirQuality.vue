<script setup>
defineProps({
  city: String,
  airquality: Number
})
</script>

<template>
  <section>
    <p class="city">{{ city }}</p>
    <div class="airquality">
      <p class="airquality_text">Качество воздуха</p>
      <p class="separator">:</p>
      <div class="airquality_box">
        <p class="airquality_value">{{ airquality }}</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
section {
  width: 100%;
  background-color: var(--main-color);
  border-radius: 6px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 12px;
  box-sizing: border-box;
}

.city {
  font-size: 3rem;
  text-align: center;
  letter-spacing: 0.75rem;
  margin-left: 0.75rem;
}

.airquality {
  display: flex;
  justify-content: space-between;
  margin: 0 auto;
  gap: 12px;
}

.airquality_text {
  text-align: center;
  display: flex;
  align-items: center;
  font-size: 1.5rem;
  max-width: 144px;
  height: 60px;
}

.airquality_box {
  text-align: center;
  max-width: 144px;
  width: 100%;
  border-radius: 6px;
  background-color: white;
  padding: 6px;
  font-size: 3rem;
  font-weight: 700;
  box-sizing: border-box;
  letter-spacing: 0.75rem;
}

.airquality_value {
  margin-left: 0.75rem;
}

.separator {
  font-size: 3rem;
}
</style>
