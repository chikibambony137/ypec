<template>
    <div class="menu-ref" @click="moveToAbiturientam">
        <div class="icon">
            <img src="../assets/abiturientam.png" width="20px"/>
        </div>
        <h2>Абитуриентам</h2>
    </div>

    <div class="menu-ref" @click="moveToTeachers">
        <div class="icon">
            <img src="../assets/teachers.png" width="20px"/>
        </div>
        <h2>Преподавателям</h2>
    </div>

    <div class="menu-ref" @click="moveToStudents">
        <div class="icon">
            <img src="../assets/students.png" width="20px"/>
        </div>
        <h2>Студентам</h2>
    </div>

    <div class="menu-ref" @click="moveToNews">
        <div class="icon">
            <img src="../assets/news.png" width="20px"/>
        </div>
        <h2>Новости</h2>
    </div>

    <div class="menu-ref" @click="moveToCollege">
        <div class="icon">
            <img src="../assets/college.png" width="20px"/>
        </div>
        <h2>О колледже</h2>
    </div>

    <div class="menu-ref" style="padding-bottom: 4px;" @click="moveToTech">
        <div class="icon">
            <img src="../assets/tech.png" width="20px"/>
        </div>
        <h2>Техническое отделение</h2>
    </div>

    <div class="menu-ref" style="padding-bottom: 10px;" @click="moveToHimTech">
        <div class="icon">
            <img src="../assets/himtech.png" width="20px"/>
        </div>
        <h2>Химико-технологическое отделение</h2>
    </div>

    <div class="menu-ref" style="padding-bottom: 4px;" @click="moveToFinPrav">
        <div class="icon">
            <img src="../assets/finprav.png" width="20px"/>
        </div>
        <h2>Финансово-правовое отделение</h2>
    </div>

    <div class="menu-ref" @click="moveToZaoch">
        <div class="icon">
            <img src="../assets/zaoch.png" width="20px"/>
        </div>
        <h2>Заочное отделение</h2>
    </div>

    <div class="menu-ref" @click="moveToDopObr">
        <div class="icon">
            <img src="../assets/dopobr.png" width="20px"/>
        </div>
        <h2>Дополнительное образование</h2>
    </div>

    <div class="menu-ref" @click="moveToProft">
        <div class="icon">
            <img src="../assets/professionalitet.png" width="20px"/>
        </div>
        <h2>Профессионалитет</h2>
    </div>

    <div class="menu-ref" @click="moveToWorkshops">
        <div class="icon">
            <img src="../assets/workshops.png" width="20px"/>
        </div>
        <h2>Мастерские</h2>
    </div>
</template>

<script>
export default {
    methods: {
        moveToAbiturientam() {
            this.$router.push('/abiturientam')
        },

        moveToTeachers() {
            this.$router.push('/teachers')
        },

        moveToStudents() {
            this.$router.push('/students')
        },

        moveToNews() {
            this.$router.push('/news')
        },

        moveToCollege() {
            this.$router.push('/college')
        },

        moveToTech() {
            this.$router.push('/tech')
        },

        moveToHimTech() {
            this.$router.push('/himtech')
        },

        moveToFinPrav() {
            this.$router.push('/finprav')
        },

        moveToZaoch() {
            this.$router.push('/zaoch')
        },

        moveToDopObr() {
            this.$router.push('/dopobr')
        },

        moveToProft() {
            this.$router.push('/professionalitet')
        },

        moveToWorkshops() {
            this.$router.push('/workshops')
        },

    }
}
</script>

<style scoped>
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