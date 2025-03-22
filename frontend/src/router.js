import { createRouter, createWebHistory } from "vue-router";
import Main from "./components/Main.vue";

export default createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: Main },
        { path: '/abiturientam', component: Abiturientam },

    ]
})