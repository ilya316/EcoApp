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
    <section class="profile">
        <img class="profile__image" src="../assets/testimage.png" alt="profile image">
        <p class="profile__name">Иван Иванов</p>
    </section>
    <section class="stats">
        <p class="stats__heading">Общая статистика</p>
        <ul class="stats__list">
            <li>
                <div class="stat">
                    <StatsAir />
                    <p class="value">{{stats.air}}</p>
                </div>
                <p class="stats__text"><span>Килограммов</span> Воздуха сохранено</p>
            </li>
            <li>
                <div class="stat">
                    <StatsGarbage />
                    <p class="value">{{stats.garbage}}</p>
                </div>
                <p class="stats__text"><span>Килограммов</span> Мусора переработано</p>
            </li>
            <li>
                <div class="stat">
                    <StatsWater />
                    <p class="value">{{stats.water}}</p>
                </div>
                <p class="stats__text"><span>Литров</span> Воды сохранено</p>
            </li>
        </ul>
    </section>
    <section class="achievements">
        <p class="achievements__heading">Последние достижения</p>
        <ul class="achievements__list">
            <li class="achievement" v-for="achievement in achievements">
                <img :src="achievement.image" alt="Награда">
                <div>
                    <p class="achievement__heading">{{achievement.name}}</p>
                    <p class="achievement__text">{{achievement.desc}}</p>
                </div>
            </li>
        </ul>
        <a href="achievements" class="view__all">Посмотреть все...</a>
    </section>
</template>

<style scoped>
.profile {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.profile__image {
    height: 120px;
    width: 120px;
    padding: 20px;
    object-fit: cover;
    border-radius: 50%;
}

.profile__name {
    font-weight: 700;
    font-size: 1.25rem;
}

.stats__list {
    display: flex;
    justify-content: space-around;
}

.stat {
    position: relative;
}

.value { 
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;

    font-weight: 700;
    font-size: 1.5rem;
}

span {
    font-weight: 700;
    font-size: 0.875rem;
}

.stats__text {
    text-align: center;
    display: flex;
    flex-direction: column;
    font-size: 0.6875rem;
    max-width: 100px;
}

.stats__heading, .achievements__heading {
    text-align: center;
    font-weight: 700;
    font-size: 1.25rem;
    margin: 12px 0 6px;
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
    margin: 6px 12px;
}

.view__all {
    display: block;
    width: fit-content;
    font-size: 1rem;
    font-weight: 700;
    text-align: center;
    margin: 0 auto;
    color: var(--help-color);
}

</style>
