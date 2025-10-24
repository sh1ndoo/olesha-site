<template>
  <div class="small-images">
    <img v-for="i in 7" :key="i" style="z-index: 1; position: absolute" :src="card.icon">
    <router-link :to="card.href" class="card card-small">
      <div style="z-index: 2; position: relative">
        <div class="card-header">
          <div class="icon" :style="{backgroundColor: card.color}">
            <img :src="card.icon">
          </div>
        </div>
        <h3 class="card-title">{{ card.title }}</h3>
        <p class="card-description">{{ card.description }}</p>
      </div>
    </router-link>
  </div>
</template>

<script setup>
defineProps({
  card: Object
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
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.0);
  overflow: hidden;
  position: relative;
  z-index: 2;
  backdrop-filter: blur(10px);
  background: var(--dark-md);
  border: 1.5px solid var(--border-color-dark);
}





.card:hover {
  backdrop-filter: blur(2px);
  background: var(--dark-lg-clear-lg);
  border: 1.5px solid #171616;
}
.card-small .card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.card-small .icon {
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6px;
  background-color: rgba(0, 255, 140, 0.17);
  border-radius: 7px;
  position: relative;
}

.card-small .icon img {
  width: 100%;
  height: 100%;
}
.status-tag {
  background-color: #3a3a3a;
  color: var(--text-secondary-color);
  font-size: 0.75rem;
  padding: 4px 10px;
  border-radius: 12px;
}
.card-title {
  font-weight: bold;
  margin: 0 0 4px 0;
  font-size: 0.95rem;
}

.card-description {
  color: #e2e2e2;
  font-size: 0.78rem;
  line-height: 1.4;
  margin: 0.5em 0px 0px 0px;
}
.small-images {
  position: relative;
  overflow: hidden;
  display: grid;
}
.small-images>img {
  position: absolute;
  width: 30px; /* Размер маленьких изображений */
  height: 30px;

  /* Используем переменные для позиционирования и трансформации */
  left: var(--x, 50%); /* Значение по умолчанию 50% */
  top: var(--y, 50%);
  transform: translate(-50%, -50%) rotate(var(--r, 0deg)) scale(var(--s, 1));
}
.small-images img:nth-child(1) {
  --x: 50%;
  --y: 0%;
  --r: 22deg;
  --s: 1.3;
}
.small-images img:nth-child(2) {
  --x: 85%;
  --y: 25%;
  --r: -15deg;
  --s: 1.3; /* Чуть крупнее */
}
.small-images img:nth-child(3) {
  --x: 32%;
  --y: 31%;
  --r: -15deg;
  --s: 1.3;
}
.small-images img:nth-child(4) {
  --x: 100%;
  --y: 64%;
  --r: -15deg;
  --s: 1.3;
}
.small-images img:nth-child(5) {
  --x: 76%;
  --y: 65%;
  --r: -15deg;
  --s: 1.3;
}
.small-images img:nth-child(6) {
  --x: 14%;
  --y: 13%;
  --r: -15deg;
  --s: 1.3;
}
.small-images img:nth-child(7) {
  --x: 62%;
  --y: 40%;
  --r: 122deg;
  --s: 1.3;
}
.small-images img:nth-child(8) {
  --x: 20%;
  --y: 25%;
  --r: -15deg;
  --s: 1.3; /* Чуть крупнее */
}
</style>