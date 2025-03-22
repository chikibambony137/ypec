<template>
    <div class="menu-bttn" @click="toggleMenu">
        <div class="burger">
            <span class="line" v-bind:class="{ open: isOpen }"></span>
            <span class="line" v-bind:class="{ open: isOpen }"></span>
            <span class="line" v-bind:class="{ open: isOpen }"></span>
        </div>
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

<style>
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
</style>