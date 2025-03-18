<template>
    <div class="regForm">
        <div>
            <a class="toLogin" @click="goToLogin"><u>Login ></u></a>
        </div>
        <div>
            <h1>Register</h1>
            <form @submit.prevent="Register">
                <p><input type="login" class="reg-input" v-model="login" placeholder="Login / Email" maxlength=50/></p>
                <p><input type="password" class="reg-input" v-model="password" placeholder="Password" maxlength=50/></p>
                <p><input type="password" class="reg-input" v-model="password2" placeholder="Password again" maxlength=50/></p>
                <p><button type="submit" class="reg-button">Register</button></p>
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
                password: '',
                password2: ''
            };
        },
        methods: {
            async Register() {
                try {
                    if (this.password == this.password2){
                        const response = await fetch(`${this.API_URL}/register`, {
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

                        alert(`Пользователь "${this.login}" зарегистрирован`)

                        this.$router.push('/login')
                    }
                    else {
                        alert('Пароли не совпадают!')
                    }
                } catch (error) {
                    alert('Ошибка: ' + error.message);
                }
            },

            goToLogin() {
                this.$router.push('/login')
            },
        },
    }
</script>

<style scoped>

</style>