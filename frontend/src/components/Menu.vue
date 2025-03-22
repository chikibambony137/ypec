<template>
    <div class="menu-ref">
        <div class="icon">
            <img src="../assets/abiturientam.png" width="20px"/>
        </div>
        <h2>Абитуриентам</h2>
    </div>

    <div class="menu-ref">
        <div class="icon">
            <img src="../assets/teachers.png" width="20px"/>
        </div>
        <h2>Преподавателям</h2>
    </div>

    <div class="menu-ref">
        <div class="icon">
            <img src="../assets/students.png" width="20px"/>
        </div>
        <h2>Студентам</h2>
    </div>

    <div class="menu-ref">
        <div class="icon">
            <img src="../assets/news.png" width="20px"/>
        </div>
        <h2>Новости</h2>
    </div>

    <div class="menu-ref">
        <div class="icon">
            <img src="../assets/college.png" width="20px"/>
        </div>
        <h2>О колледже</h2>
    </div>

    <div class="menu-ref" style="padding-bottom: 4px;">
        <div class="icon">
            <img src="../assets/tech.png" width="20px"/>
        </div>
        <h2>Техническое отделение</h2>
    </div>

    <div class="menu-ref" style="padding-bottom: 10px;">
        <div class="icon">
            <img src="../assets/himtech.png" width="20px"/>
        </div>
        <h2>Химико-технологическое отделение</h2>
    </div>

    <div class="menu-ref" style="padding-bottom: 4px;">
        <div class="icon">
            <img src="../assets/finprav.png" width="20px"/>
        </div>
        <h2>Финансово-правовое отделение</h2>
    </div>

    <div class="menu-ref" style="padding-bottom: 4px;">
        <div class="icon">
            <img src="../assets/zaoch.png" width="20px"/>
        </div>
        <h2>Заочное отделение</h2>
    </div>

    <div class="menu-ref" style="padding-bottom: 4px;">
        <div class="icon">
            <img src="../assets/dopobr.png" width="20px"/>
        </div>
        <h2>Дополнительное образование</h2>
    </div>

    <div class="menu-ref">
        <div class="icon">
            <img src="../assets/professionalitet.png" width="20px"/>
        </div>
        <h2>Профессионалитет</h2>
    </div>
    
    <div class="menu-ref">
        <div class="icon">
            <img src="../assets/workshops.png" width="20px"/>
        </div>
        <h2>Мастерские</h2>
    </div>
</template>

<script>
export default {

}
</script>

<style>
    .menu-ref {
        display: flex;
        flex-direction: row;
        align-items: center;
        height: 34px;
        cursor: pointer;
    }

    .menu-ref:hover h2 {
        color: rgb(44, 154, 128);
    }

    .icon {
        margin-top: 4px;
        margin-left: 5px;
    }

    .menu h2 {
        display: flex;
        flex-direction: row;
        align-items: center;
        color: rgb(0, 0, 0);
        font-family: 'Montserrat', sans-serif;  
        font-size: 13px;
        font-weight: 400;
        line-height: 20px;
        letter-spacing: 0%;
        text-align: left;
        margin-left: 4px;
        line-height: 18px;
    }
</style>