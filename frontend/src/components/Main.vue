<template>
    <div class="page">
        <div class="swap">
            <img src="../assets/prof-label.png" width="90%">
        </div>

        <div class="aside">
            <img src="../assets/r-farm.png" width="90%">
        </div>

        <div class="info">
            <div class="ad-text">
                12 апреля 2025 года состоится Единый день открытых дверей Федерального проекта
                <a href="https://ypec.ru/professionalitet/" target="_blank">«Профессионалитет»</a><br/>
                Приглашаем вас посетить мероприятие по адресу:
                г. Ярославль, улица Гагарина, дом 8 <br/>
                Начало мероприятия — 9.00 ч. <br/>
                <a href="https://ypec.ru/2025/03/%D0%B5%D0%B4%D0%B8%D0%BD%D1%8B%D0%B9-%D0%B4%D0%B5%D0%BD%D1%8C-%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D1%82%D1%8B%D1%85-%D0%B4%D0%B2%D0%B5%D1%80%D0%B5%D0%B9-2/#more-11492" target="_blank">
                    Программа проведения</a>
            </div>

            <img src="../assets/ad1.png" width="50%" style="margin: 20px;">
        </div>
    </div>
</template>

<script>

</script>

<style scoped>
    .page {
        height: 100%;
        width: 100%;

        display: grid;
        grid-template-columns: 52.5% 22%;
        grid-template-rows: 28% 66.3%;
        grid-template-areas: 
            "swap aside"
            "info info";
        column-gap: 30px;
        box-sizing: border-box;
    }
    
    .swap {
        position: relative;
        grid-area: swap;
        width: 100%;
        height: 100%;
        align-content: center;
        text-align: center;

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
        height: 100%;
        align-content: center;
        text-align: center;

        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }

    .info {
        position: relative;
        grid-area: info;
        width: 100%;
        height: 100%;
        margin-top: 30px;

        display: flex;
        flex-direction: row;
        align-items: center;

        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }

    .ad-text {
        color: rgb(0, 0, 0);
        font-family: 'Montserrat', sans-serif;  
        font-size: 15px;
        font-weight: 400;
        line-height: 23px;
        letter-spacing: 0%;
        text-align: left;

        margin: 20px;
    }

    .ad-text a {
        text-decoration: underline;
        color: rgb(44, 154, 128);
    }

    .ad-text a:hover {
        background: rgb(226, 252, 246);
    }

</style>