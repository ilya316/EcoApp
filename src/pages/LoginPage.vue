<script setup>

</script>

<template>
    <form action="/">
        <p class="heading">Авторизация</p>
        <label for="login" class="visually-hidden">Логин</label>
        <div class="field_wrap">
            <input class="field" type="text" id="login" name="login" placeholder="Логин">
        </div>
        <label for="password" class="visually-hidden">Пароль</label>
        <div class="field_wrap">
            <input class="field" type="text" id="password" name="password" placeholder="Пароль">
        </div>
        <input class="button" type="submit" value="Войти">
        <div class="reg_link">
            <p class="link_text">Нет аккаунта?</p>
            <a href="register">Зарегистрируйся</a>
        </div>
    </form>
</template>

<style scoped>
.heading {
    font-size: 1.5rem;
}

.reg_link {
    display: flex;
    gap: 6px;
}

a {
    color: var(--help-color);
    text-decoration: underline;
}

form {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    margin-top: calc(50vh - 168px);
}
.field {
    width: 100%;
    height: 100%;
    border: 1px solid var(--main-color);
    border-radius: 6px;
    box-sizing: border-box;
    padding: 0;
    text-align: center;
}

.field_wrap {
    height: 48px;
    width: calc(100% - 24px);
    margin: 0 12px;
    border-radius: 6px;
    box-sizing: border-box;
    border: 5px solid var(--main-color);
    background-color: var(--main-color);
}

input {
    font-size: 1.25rem;
}
.button {
    background-color: var(--main-color);
    height: 48px;
    width: calc(100% - 24px);
    margin: 0 12px;
    border-radius: 6px;
    color: white;
}
</style>
