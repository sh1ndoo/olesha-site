<template>
  <div class="main-menu-container">
    <div class="menu-card">
      <h1 class="title">Olesha Scrandle</h1>
      <div class="button-group-1">
        <button class="btn btn-vote-scran" @click="$emit('voteScran')">
          Голосовать
        </button>
        <button class="btn btn-submit-scran" @click="$emit('submitScran')">
          Закинуть свой скран
        </button>
      </div>
      <div class="button-group-3">
        <button class="btn btn-play-daily" @click="$emit('startGame', 'daily')">
          Play Daily
        </button>
        <button class="btn btn-play-test" @click="$emit('startGame', 'test')">
          Play Test
        </button>
        <button class="btn btn-play-practice" @click="$emit('startGame', 'practice')">
          Play Practice
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainMenu',
  emits: ['startGame', 'submitScran'] // Явное объявление событий
};
</script>

<style scoped>
.main-menu-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 88vh; /* Занимает всю высоту как и игровой компонент */
}

.menu-card {
  background-color: var(--dark-sm); /* Предполагая, что у вас есть такая переменная */
  padding: 40px;
  border-radius: 16px;
  text-align: center;
  width: 90%;
  max-width: 480px;
}

.title {
  font-size: 2.5em;
  font-weight: bold;
  color: var(--text-color); /* Предполагая, что у вас есть такая переменная */
  margin-bottom: 30px;
  margin-top: 0;
}

.button-group-3 {
  display: grid;
  grid-template-columns: repeat(3, minmax(150px, 1fr));
  gap: 15px;
  margin-top: 15px;
}

.button-group-1 {
  display: grid;
  grid-template-columns: repeat(1, minmax(150px, 1fr));
  gap: 15px;
}

.btn {
  padding: 15px 20px;
  border-radius: 16px;
  border: none;
  font-size: 1.1em;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  color: white;
}

.btn:hover {
  opacity: 0.9;
}

.btn-play-daily {
  background-color: rgba(108, 117, 125, 0.05); /* Зеленый */
}

.btn-submit-scran {
  background-color: #007bff; /* Синий */
}

.btn-vote-scran {
  background-color: rgba(108, 117, 125, 0.05); /* Серый */
}

.btn-play-test {
  background-color: #ffc107; /* Желтый */
  color: #212529; /* Темный текст для лучшей читаемости */
}

.btn-play-practice {
  background-color: rgba(108, 117, 125, 0.05); /* Серый */
}

@media (max-width: 600px) {
  .button-group-3 {
      grid-template-columns: repeat(1, minmax(150px, 1fr));
  }
}
</style>