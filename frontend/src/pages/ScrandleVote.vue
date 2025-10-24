<template>
  <div class="food-comparison-fullscreen">
      <div class="answer-counter">
        <i class="fa-solid fa-check"></i>
        <i class="fa-solid fa-xmark"></i>
      </div>
      <div
          class="food-option left"
          @click=""
      >
        <div class="content-wrapper">
          <div class="info-box">
            <h3>Polonia Bytom, 2023 🇵🇱</h3>
            <p>Grilled sausage</p>
            <span>£2.80</span>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
</script>

<style scoped>
/* ... (все ваши стили из food-comparison-fullscreen остаются здесь без изменений) ... */
.food-comparison-fullscreen {
  position: relative; /* Необходимо для позиционирования счетчика */
  display: flex;
  height: 86vh; /* 100% высоты окна просмотра */
  font-family: Arial, sans-serif;
  flex-direction: row;
}

.food-option {
  position: relative;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  transition: transform 0.3s ease-in-out;
  overflow: hidden;
  color: white;
  border-radius: var(--border-radius-md);
}
/* Установка фоновых изображений */
.food-option.left {
  background-image: url('https://scrandle.com/static/FtvU6KsXgAIdedK.webp');
}

.food-option.right {
  background-image: url('https://scrandle.com/static/F6TppBxXYAAawNg.webp');
}

.content-wrapper {
  position: relative;
  z-index: 2;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  box-sizing: border-box;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.4);
  z-index: 1;
}

.info-box {
  background-color: rgba(0, 0, 0, 0.6);
  padding: 15px;
  border-radius: 8px;
  text-align: center;
  width: 80%;
  max-width: 300px;
  align-self: center; /* Центрируем по горизонтали */
  margin-bottom: 20px;
}

.info-box h3 {
  margin: 0 0 5px 0;
}

.info-box p {
  margin: 0 0 10px 0;
  font-size: 1.2em;
}

.info-box span {
  font-size: 1.1em;
  font-weight: bold;
}

.percentage-display {
  font-size: 4em;
  font-weight: bold;
  text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.8);
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.result-message {
  padding: 10px 20px;
  border-radius: 25px;
  font-size: 1.2em;
  font-weight: bold;
  margin-top: 20px;
  width: fit-content;
}

.correct {
  color: #28a745; /* Зеленый */
  background-color: rgba(0, 0, 0, 0.6);
  padding: 10px;
  border-radius: var(--border-radius-md);
}

.incorrect {
  color: #dc3545;
  background-color: rgba(0, 0, 0, 0.6);
  padding: 10px;
  border-radius: var(--border-radius-md);
}

/* --- Стили для нового счетчика --- */
.answer-counter {
  position: absolute;
  bottom: 25px; /* Отступ сверху */
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 30px; /* Пространство между кружками */
  z-index: 10; /* Убедимся, что счетчик поверх изображений */
  padding: 10px 20px;
  background-color: rgba(0, 0, 0, 0.6);
  border-radius: var(--border-radius-md);
}

.answer-circle {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.4); /* Полупрозрачный белый для пустого кружка */
  transition: background-color 0.3s ease;
}

.results-modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 100;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

.results-modal {
  background-color: var(--dark-sm);
  padding: 20px;
  border-radius: 14px;
  width: 90%;
  max-width: 480px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

.results-header {
  text-align: left;
  padding-bottom: 10px;
}

.results-header h2 {
  font-size: 1.2em;
  margin: 0;
  color: var(--text-color);
}

.results-answer-bar {
  display: flex;
  gap: 2px;
  margin: 20px 0;
}

.results-answer-square {
  flex-grow: 1;
  color: white;
  font-weight: bold;
  font-size: 1.1em;
  padding: 10px 0;
  text-align: center;
  border-radius: 16px;
  margin: 0 1px
}
.icon-square {
  background-color: #818181;
  flex-grow: 0;
  width: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.scores-container {
  display: flex;
  justify-content: space-around;
  padding: 10px 0;
}

.score-block {
  text-align: center;
}

.score-value {
  font-size: 2.5em;
  font-weight: bold;
  color: #d9534f;
}

.score-label {
  font-size: 0.8em;
  font-weight: bold;
  color: #d9534f;
  letter-spacing: 0.5px;
}

.buttons-container {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 20px;
}

.btn {
  padding: 10px 20px;
  border-radius: 8px;
  border: none;
  font-size: 1em;
  font-weight: bold;
  cursor: pointer;
}
.btn:hover {
  opacity: 0.9;
}

.btn-done {
  background-color: var(--border-color);
  color: white;
}
.btn-done:hover {
  background-color: var(--border-color-dark);
}

.correct-fill {
  background-color: #28a745; /* Зеленый цвет для правильного ответа */
}

.incorrect-fill {
  background-color: #dc3545; /* Красный цвет для неправильного ответа */
}

@media (max-width: 768px) {
  .food-comparison-fullscreen {
    flex-direction: column;
  }
  .food-option {
    width: auto;
  }
  .answer-circle {
    width: 15px;
    height: 15px;
  }
}
.answer-counter i {
  font-size: 5em;
  cursor: pointer;
}
.fa-check {
  color: green
}
.fa-xmark {
  color: red
}
</style>