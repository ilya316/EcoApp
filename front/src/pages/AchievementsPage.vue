<script setup>
import StatsAir from '../components/icons/StatsAir.vue';
import StatsGarbage from '../components/icons/StatsGarbage.vue';
import StatsWater from '../components/icons/StatsWater.vue';
const stats = {'air':'10','garbage':'10','water':'30'};
const achievements = [
    {
    'name': 'Хранитель воды',
    'desc': 'Сохранить 10 литров воды',
    'image': '/src/assets/Medal.svg'
    },
    {
    'name': 'Хранитель земли',
    'desc': 'Переработать 10 килограммов мусора',
    'image': '/src/assets/Medal.svg'
    },
    {
    'name': 'Хранитель воздуха',
    'desc': 'Сохранить 10 килограммов воздуха',
    'image': '/src/assets/Medal.svg'
    }
]
</script>

<template>
    <section class="achievements">
        <p class="achievements__heading">Полученные достижения</p>
        <ul class="achievements__list">
            <li class="achievement" v-for="achievement in achievements">
                <img :src="achievement.image" alt="Награда">
                <div>
                    <p class="achievement__heading">{{achievement.name}}</p>
                    <p class="achievement__text">{{achievement.desc}}</p>
                </div>
            </li>
        </ul>
        <p class="achievements__heading">Неполученные достижения</p>
        <ul class="achievements__list">
            <li class="achievement" v-for="achievement in achievements">
                <img :src="achievement.image" alt="Награда">
                <div>
                    <p class="achievement__heading">{{achievement.name}}</p>
                    <p class="achievement__text">{{achievement.desc}}</p>
                </div>
            </li>
        </ul>
    </section>
</template>

<style scoped>
.achievements__heading {
    text-align: center;
    font-weight: 700;
    font-size: 1.25rem;
    margin: 12px 0;
}

.achievement__heading {
    font-size: 1rem;
    font-weight: 700;
}

.achievement__text {
    font-size: 0.75rem;
}

.achievement {
    display: flex;
    gap: 12px;
    margin-top: 6px;
}
</style>
