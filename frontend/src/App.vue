<template>
    <div class="page">
        <header>
            <Header></Header>
        </header>

        <main>
            <div class="menu">
                <Menu></Menu>
            </div>

            <div class="info">
                <router-view></router-view>
            </div>
        </main>

        <footer>
            <Footer></Footer>
        </footer>
    </div>
</template>

<script>
    import Menu from './components/Menu.vue'
    import Header from './components/Header.vue'
    import Footer from './components/Footer.vue';

    export default {
        components: { Menu, Header, Footer },
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
        height: 1620px;
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

    main {
        box-sizing: border-box;
        display: flex;
        flex-wrap: wrap;
        align-tracks: left;
        margin-bottom: 30px;

        display: grid;
        grid-template-columns: 22% 78%;
        grid-template-rows: 40% 57.69%;
        grid-template-areas: 
            "menu info"
            "body body";
        column-gap: 30px;

        position: relative;
        left: 16%;
        top: 0;
        width: 67.7%;
        min-width: 800px;
        height: 1315px;
    }

    .menu {
        position: relative;
        grid-area: menu;
        width: 100%;
        height: 530px;
        padding: 5px;

        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }

    .info {
        position: relative;
        grid-area: info;
        width: 96.4%;
        height: 530px;
    }

    footer {
        position: relative;
        display: flex;
        width: 67.7%;
        height: 149px;

        left: 16%;

        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }

</style>
