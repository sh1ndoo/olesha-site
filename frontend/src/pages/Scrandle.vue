<template>
  <div>
    <MainMenu
        v-if="!gameStarted && !showingSubmitForm"
        @startGame="handleStartGame"
        @submitScran="handleOpenSubmitForm"
    />

    <SubmitScran
        v-else-if="showingSubmitForm"
        @close="handleCloseSubmitForm"
        @scranSubmitted="handleScranSubmission"
    />


    <div v-else-if="gameStarted" class="food-comparison-fullscreen">
      <template v-if="!showResults">
        <!-- Счетчик ответов -->
        <div class="answer-counter">
          <span
              v-for="(answer, index) in answerHistory"
              :key="index"
              class="answer-circle"
              :class="{
            'correct-fill': answer === 'correct',
            'incorrect-fill': answer === 'incorrect'
          }"
          ></span>
        </div>

        <!-- Левый вариант -->
        <div
            class="food-option left"
            @click="!selectedOption && selectOption('sausage')"
            :class="{ 'selected': selectedOption }"
        >
          <div class="content-wrapper">
            <div v-if="selectedOption" class="percentage-display correct">72%</div>
            <div class="info-box">
              <h3>Polonia Bytom, 2023 🇵🇱</h3>
              <p>Grilled sausage</p>
              <span>£2.80</span>
            </div>
          </div>
          <div v-if="selectedOption" class="overlay"></div>
        </div>

        <!-- Правый вариант -->
        <div
            class="food-option right"
            @click="!selectedOption && selectOption('burger')"
            :class="{ 'selected': selectedOption }"
        >
          <div class="content-wrapper">
            <div v-if="selectedOption" class="percentage-display incorrect">28%</div>
            <div class="info-box">
              <h3>Folkestone Invicta, 2025 🏴󠁧󠁢󠁥󠁮󠁧󠁿</h3>
              <p>Chicken Burger</p>
              <span>£6.00</span>
            </div>
          </div>
          <div v-if="selectedOption" class="overlay"></div>
        </div>
      </template>

      <!-- Окно результатов -->
      <div v-if="showResults" class="results-modal-overlay">
        <div class="results-modal">
          <div class="results-header">
            <h2>Scrandle, {{ currentDate }}</h2>
          </div>
          <div class="results-answer-bar">
            <div
                v-for="(result, index) in answerHistory"
                :key="index"
                class="results-answer-square"
                :class="{
              'correct-fill': result === 'correct',
              'incorrect-fill': result === 'incorrect'
            }"
            >
              {{ index + 1 }}
            </div>
          </div>
          <div class="scores-container">
            <div class="score-block">
              <div class="score-value">{{ userScore }}/{{ totalQuestions }}</div>
              <div class="score-label">{{ userScoreText }}</div>
            </div>
            <div class="score-block">
              <div class="score-value">{{ communityAverage }}/{{ totalQuestions }}</div>
              <div class="score-label">СРЕДНИЙ</div>
            </div>
          </div>
          <div class="buttons-container">
            <button class="btn btn-done" @click="goToMenu">Готово</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import MainMenu from './ScrandleMenu.vue'; // Убедитесь, что путь к файлу верный
import SubmitScran from "@/pages/SubmitScran.vue"; // 1. Импортируем новый компонент

export default {
  components: {
    SubmitScran,
    MainMenu // Регистрируем компонент меню
  },
  setup() {
    const gameStarted = ref(false); // Новое состояние для отслеживания начала игры
    const gameMode = ref(''); // Состояние для хранения режима игры
    const showingSubmitForm = ref(false); // 3. Новое состояние для формы


    const selectedOption = ref(null);
    const correctAnswer = 'sausage';
    const root = document.documentElement;

    const totalQuestions = 10;
    const answerHistory = ref(Array(totalQuestions).fill(null));
    const currentRound = ref(0);
    const userScore = ref(0);
    const showResults = ref(false);

    const communityAverage = ref(5.7);
    const currentDate = ref(new Date().toISOString().slice(0, 10));

    onMounted(() => {
      root.style.setProperty('--main-width', '100%');
    });

    onUnmounted(() => {
      root.style.removeProperty('--main-width');
    });

    const handleStartGame = (mode) => {
      gameMode.value = mode;
      gameStarted.value = true;
      if (mode === 'daily' || mode === 'practice') {
        alert('В разработке');
        gameStarted.value = false;
      }
      console.log(`Starting game in ${mode} mode`);
      restartGame(false); // Сбрасываем игру, но не показываем меню
    };

    const handleOpenSubmitForm = () => {
      showingSubmitForm.value = true;
    };
    const handleCloseSubmitForm = () => {
      showingSubmitForm.value = false;
    };
    const handleScranSubmission = (data) => {
      console.log('Получены данные из формы в родительском компоненте:', data);
      // Здесь можно, например, отправить их на сервер
    };

    const handleSubmitScran = () => {
      // Здесь будет логика для кнопки "Закинуть Свой скран"
      // Например, открытие модального окна или переход на другую страницу
      alert('Функционал добавления своего скрэна в разработке!');
    };

    const selectOption = (option) => {
      if (selectedOption.value || currentRound.value >= totalQuestions) return;

      selectedOption.value = option;
      const isCorrect = option === correctAnswer;

      answerHistory.value[currentRound.value] = isCorrect ? 'correct' : 'incorrect';
      if (isCorrect) {
        userScore.value++;
      }

      setTimeout(() => {
        currentRound.value++;
        if (currentRound.value >= totalQuestions) {
          showResults.value = true;
        } else {
          selectedOption.value = null;
          // Here you would load new data for comparison
        }
      }, 1200);
    };

    const userScoreText = computed(() => {
      const score = userScore.value;
      if (score <= 4) {
        return "BRO...";
      } else if (score <= 7) {
        return "НУ НОРМ";
      } else if (score < 10) {
        return "РЕСПЕКТ";
      } else {
        return "АНБЕЛИВЕРЫЫЫЫ";
      }
    });

    // Изменено: теперь можно выбрать, возвращаться ли в меню
    const restartGame = (backToMenu = true) => {
      currentRound.value = 0;
      userScore.value = 0;
      answerHistory.value.fill(null);
      selectedOption.value = null;
      showResults.value = false;
      if (backToMenu) {
        gameStarted.value = false;
      }
    };

    // Новая функция для кнопки "Готово"
    const goToMenu = () => {
      restartGame(true); // Сброс игры и возврат в меню
    };

    return {
      gameStarted,
      showingSubmitForm, // Не забудьте вернуть новое состояние
      handleStartGame,
      handleOpenSubmitForm,
      handleCloseSubmitForm,
      handleScranSubmission,
      handleSubmitScran,
      selectedOption,
      selectOption,
      answerHistory,
      showResults,
      userScore,
      totalQuestions,
      userScoreText,
      communityAverage,
      currentDate,
      goToMenu, // Используем новую функцию
    };
  },
};
</script>

<style scoped>
/* ... (все ваши стили из food-comparison-fullscreen остаются здесь без изменений) ... */
.food-comparison-fullscreen {
  position: relative; /* Необходимо для позиционирования счетчика */
  display: flex;
  height: 86vh; /* 100% высоты окна просмотра */
  font-family: Arial, sans-serif;
  flex-direction: row;
  gap: 20px
}

.food-option {
  position: relative;
  width: 50%;
  height: 100%;
  background-size: cover;
  background-position: center;
  cursor: pointer;
  transition: transform 0.3s ease-in-out;
  overflow: hidden;
  color: white;
  border-radius: var(--border-radius-md);

}

.food-option:hover:not(.selected) {
  transform: scale(1.01); /* Небольшое увеличение при наведении, если выбор еще не сделан */
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
  gap: 10px; /* Пространство между кружками */
  z-index: 10; /* Убедимся, что счетчик поверх изображений */
  padding: 10px;
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
</style>