<template>
    <div class="loginForm">
        <div>
            <a class="toRegister" @click="goToReg"><u>Register ></u></a>
        </div>
        <div>
            <h1>Login</h1>
            <form @submit.prevent="Login">
                <p><input type="login" class="login-input" v-model="login" placeholder="Login / Email" maxlength=50/></p>
                <p><input type="password" class="login-input" v-model="password" placeholder="Password" maxlength=50/></p>
                <p><button type="submit" class="login-button">Login</button></p>
                <a class="forgotPassword" href="/home"><u>Forgot password?</u></a>
            </form>
        </div>        
    </div>
</template>

<script>
    import Config from "./config.js"

    export default {
        data() {
            return {
                API_URL: Config.api,
                login: '',
                password: ''
            };
        },

        methods: {
            async Login() {
                try {
                    const response = await fetch(`${this.API_URL}/login`, {
                        method: 'POST',
                        body: new URLSearchParams({
                            username: this.login,
                            password: this.password,
                        }).toString(),
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',
                        },
                    });

                    if (!response.ok) {
                        const errorData = await response.json();
                        throw new Error(errorData.detail || 'Ошибка при авторизации');
                    }

                    const result = await response.json();

                    // Сохранение токена в localStorage
                    localStorage.setItem('access_token', result.access_token);
                    localStorage.setItem('user_name', this.login); // надо добавить автора при добавлении рецепта

                    // Перенаправление на домашнюю страницу
                    this.goToHome();
                } catch (error) {
                    alert('Ошибка: ' + error.message);
                }
            },

            goToReg() {
                this.$router.push('/registration')
            },

            goToHome() {
                this.$router.push('/home')
            }
        },
    }
</script>

<style scoped>

</style>