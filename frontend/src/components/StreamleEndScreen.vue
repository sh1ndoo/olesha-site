<template>
  <div class="results-card">
    <div class="summary">
      <div class="summary-item">
        <span class="label">Правильный ответ</span>
        <span class="value correct-answer">{{ correctAnswer }}</span>
      </div>
      <div class="summary-item">
        <span class="label">Ваш результат</span>
        <span class="value user-result">{{ userResultPercentage }}%</span>
      </div>
    </div>

    <div class="details">
      <div v-for="(option, index) in options" :key="index" class="detail-row">
        <div class="option-text">
          {{ option.value }}({{ option.percentage }}%)
        </div>
        <div class="progress-bar-container">
          <div
            class="progress-bar"
            :class="{ 'is-incorrect': option.isIncorrect }"
            :style="{ width: option.percentage + '%' }"
          ></div>
        </div>
      </div>
    </div>
    <div class="btns">
      <a class="twitchtracker" target="_blank" :href="'https://twitchtracker.com/olesha/streams/' + streamID">TwitchTracker</a>
      <router-link to="/">На главную</router-link>
      <a class="sullygnome" target="_blank" :href="'https://sullygnome.com/channel/olesha/stream/' + streamID">SullyGnome</a>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';

// Определяем входные параметры (props), которые компонент будет принимать
defineProps({
  correctAnswer: {
    type: Number,
    required: true
  },
  streamID: {
    type: String,
    required: true
  },
  userResultPercentage: {
    type: Number,
    required: true
  },
  options: {
    type: Array,
    required: true,
    // Валидатор для проверки структуры объектов в массиве
    validator: (options) => {
      return options.every(
        (option) =>
          typeof option.value === 'number' &&
          typeof option.percentage === 'number' &&
          typeof option.isIncorrect === 'boolean'
      );
    }
  }
});
</script>

<style scoped>
/* Стили компонента, 'scoped' означает, что они применяются только к этому компоненту */
.results-card {
  background-color: var(--border-color-dark);
  border-radius: 12px;
  padding: 30px;
  max-width: 400px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica,
  Arial, sans-serif;
  color: #fff;
}

.summary {
  display: flex;
  justify-content: space-around;
  margin-bottom: 24px;
}

.summary-item {
  display: flex;
  flex-direction: column;
  text-align: center;
}

.label {
  font-size: 16px;
  color: #a0a0a5; /* Светло-серый цвет для меток */
  margin-bottom: 4px;
}

.value {
  font-size: 36px;
  font-weight: bold;
}

.user-result {
  color: #34c759; /* Ярко-зеленый цвет для результата */
}

.details {
  display: flex;
  flex-direction: column;
  gap: 16px; /* Расстояние между строками */
}

.detail-row {
  display: grid;
  grid-template-columns: 1fr 2fr; /* Разделение строки на две колонки */
  align-items: center;
  gap: 12px;
}

.option-text {
  font-size: 16px;
  font-weight: 500;
}

.progress-bar-container {
  background-color: #48484a;
  border-radius: 8px;
  height: 16px;
  overflow: hidden; /* Скрываем выходящую за пределы часть прогресс-бара */
}

.progress-bar {
  height: 100%;
  border-radius: 8px;
  background-color: #34c759; /* Зеленый цвет по умолчанию */
  transition: width 0.5s ease-in-out;
}

.progress-bar.is-incorrect {
  background-color: #ff3b30; /* Красный цвет для неправильного ответа */
}

a {
  text-decoration: none;
  color: white;
  padding: 10px;
  background-color: var(--border-color);
  border-radius: var(--border-radius-sm);
}

.btns {
  margin-top: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.twitchtracker {
  background-color: #9146FFFF;
}

.sullygnome {
  background-color: rgb(0, 168, 166);
}
</style>