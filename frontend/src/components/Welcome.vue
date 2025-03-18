<template>
    <div class="welcome-div">
        <h1>Добро пожаловать!</h1>
        <button class="login-button" @click="goToLogin">Войти</button>        
    </div>
</template>

<script>
    export default {
        methods: {
          goToLogin() {
            this.$router.push('/login')
          }
        }
    }
</script>

<style scoped>

</style>