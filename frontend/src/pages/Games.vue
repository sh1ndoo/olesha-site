<script setup>

import LargeCardGrid from "@/components/LargeCardGrid.vue";
import {ref} from "vue";
import LargeCardGridOut from "@/components/LargeCardGridOut.vue";

const largeCards = ref([
  {
    href: 'https://flappyuter.com/',
    image: 'https://i.postimg.cc/3w70CRy0/Screenshot-2025-10-12-at-05-57-57.png',
    title: 'FlappyUter',
    description: ''
  },
  {
    href: 'https://uterup.ru/',
    image: 'https://i.postimg.cc/Bb74f0dC/temp-Image8-Ae1n-N.avif',
    title: 'UterUp',
    description: ''
  },
]);
</script>

<template>
  <h1 style="text-align: center; font-size: 2.5rem; margin-bottom: 1rem">Игры комьюнити</h1>
  <div class="description">
    <p>Если вы хотите добавить свою игру, свяжитесь в телеграм @ifknow_me</p>
  </div>
  <LargeCardGridOut :large-cards="largeCards"/>
</template>

<style scoped>
.description {
  text-align: center;
  font-size: 0.9rem;
  margin-bottom: 3rem
}
</style>