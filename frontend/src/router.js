import { createRouter, createWebHistory } from "vue-router";
import Main from "./components/Main.vue";
import Abiturientam from "./components/Menu-components/Abiturientam.vue";
import Teachers from "./components/Menu-components/Teachers.vue";
import Students from "./components/Menu-components/Students.vue";
import News from "./components/Menu-components/News.vue";
import College from "./components/Menu-components/College.vue";
import Tech from "./components/Menu-components/Tech.vue";
import HimTech from "./components/Menu-components/HimTech.vue";
import FinPrav from "./components/Menu-components/FinPrav.vue";
import Zaoch from "./components/Menu-components/Zaoch.vue";
import DopObr from "./components/Menu-components/DopObr.vue";
import Proft from "./components/Menu-components/Proft.vue";
import WorkShops from "./components/Menu-components/Workshops.vue";

export default createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: Main },
        { path: '/abiturientam', component: Abiturientam },
        { path: '/teachers', component: Teachers },
        { path: '/students', component: Students },
        { path: '/news', component: News },
        { path: '/college', component: College },
        { path: '/tech', component: Tech },
        { path: '/himtech', component: HimTech },
        { path: '/finprav', component: FinPrav },
        { path: '/zaoch', component: Zaoch },
        { path: '/dopobr', component: DopObr },
        { path: '/professionalitet', component: Proft },
        { path: '/workshops', component: WorkShops },
    ]
})