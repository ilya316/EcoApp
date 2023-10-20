<script setup>

</script>

<template>
    <section class="profile">
        <img class="profile__image" src="../assets/testimage.png" alt="profile image">
        <p class="profile__name">Иван Иванов</p>
    </section>
    <section class="stats">
        <p>Общая статистика</p>
        <ul>
            <li>
                <img src="" alt="">
                <p>Test</p>
            </li>
            <li>
                <img src="" alt="">
                <p>Test</p>
            </li>
            <li>
                <img src="" alt="">
                <p>Test</p>
            </li>
        </ul>
    </section>
    <section class="achievements">
        <p>Достижения</p>
        <ul>
            <li>
                <img src="" alt="">
                <p>Test</p>
            </li>
            <li>
                <img src="" alt="">
                <p>Test</p>
            </li>
            <li>
                <img src="" alt="">
                <p>Test</p>
            </li>
        </ul>
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
</style>
