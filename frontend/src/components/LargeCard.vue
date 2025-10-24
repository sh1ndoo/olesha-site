<template>
  <router-link :to="card.href" class="card card-large" :class="card.bgClass">
    <div class="card-header">
      <img class='card-image' :src="card.image" alt="">
    </div>
    <div class="card-content">
      <h3 class="card-title">{{ card.title }}</h3>
      <p class="card-description">{{ card.description }}</p>
    </div>
  </router-link>
</template>

<script setup>
// Определяем, что компонент ожидает получить объект 'card'
defineProps({
  card: {
    type: Object,
    required: true
  }
});
</script>



<style scoped>
.card {
  border-radius: var(--border-radius-md);
  padding: 18px;
  text-decoration: none;
  color: var(--text-color);
  display: flex;
  flex-direction: column;
  transition: all 0.4s ;
  overflow: hidden;
  position: relative;
  z-index: 2;
  backdrop-filter: blur(2px);
  background: rgba(16, 16, 16, 0.55);
}

.card-title {
  margin: 0;
  color: var(--text-color);
  font-size: 1rem;
  font-weight: 600;
}

.card-description {
  margin: 8px 0 0;
  color: var(--text-color);
  font-size: 0.78rem;
  font-weight: 400;
  line-height: 1.5;
}
.card-large {
  min-height: 200px;
  position: relative;
  overflow: hidden;
  padding: 1em;
  border: 1.5px solid var(--border-color-dark);
  background-color: var(--dark-md);
}

.card-large:hover {
  background: var(--border-color-dark);
  border: 1.5px solid var(--border-color);
}

.card-header {
  position: relative;
  border-radius: var(--border-radius-md);
  overflow: hidden;
  border: none;
  height: 11em;
}


.card-large .card-content {
  position: relative;
  z-index: 1;
  padding-top: 1em;
  margin-top: 0;
}

.card-image {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); /* Магический трюк для идеального центрирования */
  border-radius: var(--border-radius-md);
  width: 100%; /* Задаем размер иконки */
  height: auto;
}
</style>