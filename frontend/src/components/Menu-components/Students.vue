<template>
    <div class="info">
        <h2>Студентам</h2>
    </div>

    <div class="body">
        stud
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
        left: -257px;
        width: 133.1%;
        height: 755px;
        margin-top: 30px;

        box-sizing: border-box;
        border: 2px solid rgba(136, 136, 136, 0.17);
        border-radius: 20px;
        box-shadow: 1px 1px 2px 0px rgba(0, 0, 0, 0.25);
        background: rgb(255, 255, 255);
    }
</style>