<template>
    <div class="info">
        <div style="margin: 20px;">
        <h2>Абитуриентам</h2>
        Подача документов может осуществляться любым из следующих способов:
        <ol>
            <li> Личное предоставление документов; </li>
            <li> Через операторов почтовой связи: 150046, г. Ярославль ул. Гагарина д. 8 </li>    
            <li> В электронной форме на адрес электронной почты priem.ypec.yaroslavl@yarregion.ru, priem@ypec.ru; </li>    
            <li> Через портал «Госуслуги»; </li>
            <li> Через многофункциональный центр «Мои документы» </li>
        </ol>

        <h3 style="margin-bottom: 10px;"> Памятка абитуриенту для подачи документов через портал «Госуслуги» </h3>

            Информацию о поступлении в образовательное учреждение Вы можете получить на сайте государственных услуг
            (для получения информации необходимо пройти регистрацию и подать заявление со всеми необходимыми данными).<br/>

            Прием документов начинается с <b>16 июня 2025 года.</b><br/>                                 

        <h3 style="margin-bottom: 10px;">График работы приемной комиссии</h3>

            <li> Понедельник — четверг: 09.00 — 17.00 </li>
            <li> Пятница: 09.00 — 13.00 </li>    
            <li> Суббота, Воскресенье: выходной </li>

        <h3 style="margin-bottom: 10px;"> Контакты приемной комиссии: </h3> 

            Телефон: <a href="tel: 8(4852)44-44-63">8(4852)44-44-63</a>, e-mail: <a href="e-mail: priem@ypec.ru">priem@ypec.ru</a> <br/>

            Группа в VK: <a href="https://vk.com/ypec_ru" target="_blank">https://vk.com/ypec_ru</a> 

        </div>
    </div>

    <div class="body">
        <div style="margin: 20px; text-align: center;">
            <h2>Программы подготовки специалистов среднего звена в рамках федерального проекта «Профессионалитет»<br/>
                ОЧНАЯ ФОРМА ОБУЧЕНИЯ</h2>
            
                <table>
                    <thead>
                        <tr>
                            <th>Код специальности</th>
                            <th>Наименование специальности</th>
                            <th>Нормативный срок обучения</th>
                            <th>Условия обучения</th>
                        </tr>
                    </thead>


                    <tbody>

                        <tr>
                        <td colspan="4">НА БАЗЕ ОСНОВНОГО ОБЩЕГО ОБРАЗОВАНИЯ (9 КЛАССОВ)</td>
                        </tr>

                        <tr>
                            <td>18.02.12</td>
                            <td>Технология аналитического контроля химических соединений</td>
                            <td>3 года 8 мес.</td>
                            <td>бюджет</td>
                        </tr>

                        <tr>
                            <td>18.02.15</td>
                            <td>Биохимическое производство</td>
                            <td>3 года 6 мес.</td>
                            <td>бюджет</td>
                        </tr>
                    </tbody>
                </table>

        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
    .info {
        grid-area: "info";
        height: 100%;
        width: 100%;
        max-width: 100%;
        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }

    .body {
        position: absolute;
        grid-area: body;
        left: -33%;
        width: 132.8%;
        height: 755px;
        margin-top: 30px;

        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }

    td, th {
        padding: 10px;
    }

    table, td, th {
        border-collapse: collapse;
        border: 1px solid #000000;
    }
</style>