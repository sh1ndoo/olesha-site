<script setup>
import { ref } from 'vue';
import LargeCard from './LargeCard.vue';
defineProps({
  largeCards: {
    type: Object,
    required: true
  }
});
</script>

<template>
  <section class="info-grid grid-large">
    <!-- Используем v-for для рендеринга каждой карточки -->
    <LargeCard
        v-for="card in largeCards"
        :key="card.title"
        :card="card"
    />
  </section>
</template>


<style scoped>
.info-grid {
  display: grid;
  gap: 13px;
  margin-bottom: 24px;
}

.grid-large {
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}
</style>