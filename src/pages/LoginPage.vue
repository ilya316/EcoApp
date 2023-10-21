<script setup>

</script>

<template>
    <form action="/">
        <p>Авторизация</p>
        <label for="login" class="visually-hidden">Логин</label>
        <input class="field" type="text" id="login" name="login" placeholder="Логин">
        <label for="lname" class="visually-hidden">Пароль</label>
        <input class="field" type="text" id="lname" name="lname" placeholder="Пароль">
        <input class="button" type="submit" value="Войти">
    </form>
</template>

<style scoped>
form {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
}

input {
    height: 48px;
    width: calc(100% - 24px);
    margin: 0 12px;
    border-radius: 6px;
    box-sizing: border-box;
}
.field {
    border: 6px solid var(--main-color);
    padding: 0;
}

.button {
    background-color: var(--main-color);
}
</style>
