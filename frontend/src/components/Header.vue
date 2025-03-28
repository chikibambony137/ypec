<template>
    <a href="/" class="refToHome">
        <div class="logo">
            <img src="../assets/logo.png" width="70px">
        </div>
        <div class="title">
            <h1>Ярославский промышленно- экономический колледж <br/></h1>
            <h2>имени Н. П. Пастухова</h2>
        </div>
    </a>

    <div class="refs-header">
        <div class="refs-header2">
            <a href="/cabinets"><label>Кабинеты</label></a>
            <a href="/forteacher"><label>Преподавателю</label></a>
            <a href="/raspisanie"><label>Расписание</label></a>
            <a href="/changes"><label>Замены</label></a>
        </div>
    </div>
</template>

<script>
import MenuBttn from './MenuBttn.vue';

export default {
    components: { MenuBttn },
}
</script>

<style scoped>
    .refToHome {
        position: relative;
        margin-left: 12.2%;
        top: 2px;
        cursor: pointer;
        display: flex;
        
    }

    .logo {
        position: relative;
        margin-left: 16%;
        top: 5px;
        cursor: pointer;
    }

    .title {
        margin-left: 10px;
        height: 90%;
        cursor: pointer;
    }

    h1 {
        width: 280px;
        height: 70%;
        margin-top: 3px;
        font-size: 17px;
        margin-bottom: 1px;

        /* Ярославский промышленно-экономический колледж имени Н. П. Пастухова */
        display: flex;
        flex-direction: row;
        align-items: center;
        position: relative;
        font-family: 'Montserrat', sans-serif;  
        font-weight: 700;
        color: rgb(255, 255, 255);  
        
    }

    .title h2 {
        margin-top: 0px;
        font-size: 12px;
        font-family: 'Montserrat', sans-serif;  
        font-style: normal;
        font-weight: 300;
        color: rgb(255, 255, 255);  
    }

    .refs-header {
        position: relative;
        width: 41.5%;
        min-width: 450px;
        align-items: center;
        margin-left: 6.4%;
        display: flex;
        flex-direction: row;
    }

    .refs-header2 {
        box-sizing: border-box;
        display: flex;
        flex-wrap: wrap;

        position: absolute;
        right: 0px;
        align-items: center;
    }

    .refs-header2 label, .menu-bttn {
        margin-left: 28px;
        display: flex;
        flex-direction: row;
        align-items: center;

        color: rgb(255, 255, 255);
        font-family: 'Montserrat', sans-serif;  
        font-size: 13px;
        font-weight: 500;
        line-height: 20px;
        letter-spacing: 0%;
        text-align: center;
        cursor: pointer;
        height: 20px;
    }

    .refs-header2 label:hover {
        color: rgb(210, 210, 210);
    }

    .menu-bttn {
        height: 40px;
        width: 40px;

        border-radius: 5px;
        box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.25);
        background: rgb(46, 161, 135);
    }
</style>