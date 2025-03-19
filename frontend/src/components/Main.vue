<template>
    <div class="page">
        <header>
            <div class="logo">
                <img src="../assets/logo.png" width="70px">
            </div>
            <div class="title">
                <h1>Ярославский промышленно- экономический колледж <br/></h1>
                <h2>имени Н. П. Пастухова</h2>
            </div>

            <div class="refs-header">
                <div class="refs-header2">
                    <label>Кабинеты</label>
                    <label>Преподавателю</label>
                    <label>Расписание</label>
                    <label>Замены</label>

                    <div class="menu-bttn" @click="toggleMenu">
                        <div class="burger">
                            <span class="line" v-bind:class="{ open: isOpen }"></span>
                            <span class="line" v-bind:class="{ open: isOpen }"></span>
                            <span class="line" v-bind:class="{ open: isOpen }"></span>
                        </div>
                        
                    </div>
                </div>
            </div>
            
        </header>

        <main>
            <div class="menu"></div>
            <div class="swap"></div>
            <div class="aside"></div>
            <div class="ad"></div>
            <div class="body"></div>
        </main>

        <footer></footer>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                isOpen: false,
            }
        },

        methods: {
            toggleMenu() {
                this.isOpen = !this.isOpen;
            }
        }
    }

</script>

<style scoped>

    .page {
        position: absolute;
        left: 0;
        top: 0;

        box-sizing: border-box;
        display: flex;
        flex-direction: column;

        width: 100%;
        height: 2104px;
        min-width: 1000px;
    }
    header {
        position: relative;
        left: 0;
        top: 0;
        width: 100%;
        height: 80px;
        margin-bottom: 30px;
        display: flex;
        flex-direction: row;

        box-sizing: border-box;
        border: 0.5px solid rgb(0, 139, 135);
        background: linear-gradient(90.00deg, rgb(0, 211, 213) 0.001%,
            rgb(31, 139, 132) 24.1%,rgb(43, 152, 138) 46.6%,
            rgb(54, 152, 131) 72.1%,rgb(25, 124, 102) 99.999%);
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

    h2 {
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
        align-items: center;
        margin-left: 40px;
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
        font-family: Montserrat;
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

    .menu-bttn:hover {
        background: rgb(40, 142, 118);
    }

    .menu-bttn:hover .line {
        background: rgb(210, 210, 210);
    }

    .burger {
        position: relative;
        left: 4px;
        height: 30px;
        align-content: center;
    }

    .line {
      display: block;
      width: 21px;
      height: 1.5px;
      margin: 6px;
      background-color: white;
      transition: all 0.3s ease;
   }

    .line.open:nth-child(1) {
        transform: rotate(45deg) translate(5px, 5.5px);
    }

    .line.open:nth-child(2) {
        opacity: 0;
    }

    .line.open:nth-child(3) {
        transform: rotate(-45deg) translate(5px, -5px);
    }

    main {
        box-sizing: border-box;
        display: flex;
        flex-wrap: wrap;
        align-tracks: left;
        margin-bottom: 30px;

        display: grid;
        grid-template-columns: 23% 50% 21%;
        grid-template-rows: 10% 21.9% 64.05%;
        grid-template-areas: 
            "menu swap aside"
            "menu ad ad"
            "body body body";
        column-gap: 30px;
        row-gap: 30px;

        position: relative;
        left: 16%;
        top: 0;
        width: 68%;
        min-width: 800px;
        height: 70%;
    }

    .menu {
        position: relative;
        grid-area: menu;
        width: 100%;
        height: 530px;
        margin-right: 3%;

        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }

    .swap {
        position: relative;
        grid-area: swap;
        width: 100%;
        height: 180px;
        margin-right: 3%;

        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }

    .aside {
        position: relative;
        grid-area: aside;
        width: 100%;
        height: 180px;

        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }

    .ad {
        position: relative;
        grid-area: ad;
        width: 100%;
        height: 100%;
        margin-top: 30px;

        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }

    .body {
        position: relative;
        grid-area: body;
        width: 100%;
        margin-top: 30px;

        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }

    footer {
        position: relative;
        display: flex;
        width: 68%;
        height: 149px;

        left: 16%;

        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }
</style>