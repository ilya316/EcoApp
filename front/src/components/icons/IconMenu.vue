<template>
    <svg class="icon" width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path class="first" d="M3 6H21" stroke="#022601" stroke-width="2" stroke-linecap="round"/>
        <path class="second" d="M3 12H21" stroke="#022601" stroke-width="2" stroke-linecap="round"/>
        <path class="third" d="M3 12H21" stroke="#022601" stroke-width="2" stroke-linecap="round"/>
        <path class="fourth" d="M3 18H21" stroke="#022601" stroke-width="2" stroke-linecap="round"/>
    </svg>
</template>

<style scoped>
.first,.second,.third,.fourth {
    transform-origin: 50% 50%;
    transition: all 300ms ease-out;
}
    .active > .menu > .icon > .second {
        transform: rotate(45deg);
    }
    .active > .menu > .icon > .third {
        transform: rotate(-45deg);
    }
    .active > .menu > .icon > .first, .active > .menu > .icon > .fourth {
        display: none;
    }
</style>