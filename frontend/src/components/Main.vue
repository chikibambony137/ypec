<template>
    <div class="page">
        <header></header>

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
        width: 70%;
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
        width: 70%;
        height: 149px;

        left: 16%;

        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }
</style>