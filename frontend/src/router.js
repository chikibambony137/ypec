import { createRouter, createWebHistory } from "vue-router";
import LoginForm from "./components/LoginForm.vue";
import MainPage from "./components/MainPage.vue";
import Welcome from "./components/Welcome.vue";
import RegForm from "./components/RegForm.vue";

export default createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: Welcome },
        { path: '/login', component: LoginForm },
        { path: '/home', component: MainPage },
        { path: '/registration', component: RegForm },
    ]
})