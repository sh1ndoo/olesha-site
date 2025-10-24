<script setup>
import { ref } from 'vue';
import LargeCard from './LargeCard.vue';
import LargeCardOut from "@/components/LargeCardOut.vue";
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
    <LargeCardOut
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
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}
</style>