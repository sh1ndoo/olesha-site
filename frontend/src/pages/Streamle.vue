<template>
  <!-- Отображаем основной блок только после того, как данные загружены -->
  <div class="stream-stats-card" v-if="streamData">
    <h1 class="stream-title">{{ streamData.title }}</h1>
    <p class="stream-date">{{ formatDate(streamData.date) }}</p>

    <div class="carousel">
      <!-- Передаем отформатированный список игр в карусель -->
      <AdvancedCarousel :items="carouselItems" />
    </div>

    <div class="stats-grid">
      <!-- Длительность -->
      <div class="stat-box">
        <span v-if="revealedStats.duration" class="value">{{ formatLength(streamData.length) }}</span>
        <span v-else class="value">?</span>
        <span class="label duration">Длительность</span>
      </div>

      <!-- Подписалось -->
      <div class="stat-box">
        <span v-if="revealedStats.subscriptions" class="value">{{ streamData.follower_gain }}</span>
        <span v-else class="value">?</span>
        <span class="label subscribed">Подписалось</span>
      </div>

      <!-- Минут просмотра -->
      <div class="stat-box">
        <!-- Заменено на view_minutes, как в модели -->
        <span v-if="revealedStats.watchHours" class="value">{{ formatLength(streamData.view_minutes) }}</span>
        <span v-else class="value">?</span>
        <span class="label watch-hours">Время просмотра</span>
      </div>

      <!-- Максимум зрителей -->
      <div class="stat-box">
        <span v-if="revealedStats.peakViewers" class="value">{{ streamData.max_viewers }}</span>
        <span v-else class="value">?</span>
        <span class="label peak-viewers">Пиковый онлайн</span>
      </div>
    </div>

    <div class="average-viewers">
      <input v-model="userGuess" class="avg-value" placeholder="1234" @keyup.enter="handleGuess" :disabled="isGameOver">
      <div class="avg-label">Средний онлайн</div>
    </div>

    <button class="checkmark" @click="handleGuess" :disabled="isGameOver">✓</button>

    <div class="extra-stats">
      <div v-for="(guess, index) in guessHistory" :key="index" class="extra-stat">
        <span>{{ guess.value }}</span>
        <span :class="{ positive: guess.trend === 'positive', negative: guess.trend === 'negative' }">
          {{ guess.closeness.toFixed(2) }}%
          <template v-if="guess.trend === 'positive'">↑</template>
          <template v-if="guess.trend === 'negative'">↓</template>
        </span>
      </div>
    </div>

    <!-- Модальное окно теперь использует данные из API -->
    <div v-if="isGameOver" class="modal-overlay">
      <div class="modal-content">
        <StreamleEndScreen
          :correct-answer="streamData.avg_viewers"
          :user-result-percentage="bestGuessPercentage"
          :options="endScreenOptions"
          :streamID="streamData.id_stream"
        />
      </div>
    </div>
  </div>
  <!-- Показываем сообщение о загрузке, пока ждем ответ от API -->
  <div v-else>
    <p>Загрузка данных...</p>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue';
import AdvancedCarousel from '@/components/Carousel.vue';
import StreamleEndScreen from '@/components/StreamleEndScreen.vue';
import axios from 'axios'; // Не забудьте установить axios: npm install axios

// Реактивное состояние для хранения данных стрима
const streamData = ref(null);
const userGuess = ref('');
const guessHistory = ref([]);
const isGameOver = ref(false);

const revealedStats = reactive({
  duration: false,
  subscriptions: false,
  watchHours: false,
  peakViewers: false
});

const statsToReveal = ['duration', 'subscriptions', 'watchHours', 'peakViewers'];
let revealedCount = 0;

// Выполняем запрос к API при монтировании компонента
onMounted(async () => {
  try {
    // Делаем GET-запрос к вашему эндпоинту
    const response = await axios.get('/api/v1/random_stream');
    // Сохраняем полученные данные в реактивное состояние
    streamData.value = response.data;
    console.log(streamData.value);
  } catch (error) {
    console.error("Ошибка при загрузке данных о стриме:", error);
    // Здесь можно добавить обработку ошибок, например, показать сообщение пользователю
  }
});

const bestGuessPercentage = computed(() => {
  if (guessHistory.value.length === 0) return 0;
  const maxCloseness = Math.max(...guessHistory.value.map(g => g.closeness));
  return parseFloat(maxCloseness.toFixed(2));
});

const endScreenOptions = computed(() => {
  return guessHistory.value
    .slice()
    .reverse()
    .map(guess => ({
      value: guess.value,
      percentage: parseFloat(guess.closeness.toFixed(2)),
      isIncorrect: guess.trend === "negative"
    }));
});

const handleGuess = () => {
  // Проверяем, что игра не окончена и данные загружены
  if (isGameOver.value || !streamData.value) return;

  const guessValue = parseInt(userGuess.value);
  if (isNaN(guessValue) || guessValue <= 0) return;

  // Используем avg_viewers из API как правильный ответ
  const actualAverageViewers = streamData.value.avg_viewers;
  const min = Math.min(actualAverageViewers, guessValue);
  const max = Math.max(actualAverageViewers, guessValue);
  const closeness = (min / max) * 100;

  let trend = 'neutral';
  if (guessHistory.value.length > 0) {
    const previousCloseness = guessHistory.value[0].closeness;
    trend = closeness > previousCloseness ? 'positive' : (closeness < previousCloseness ? 'negative' : 'neutral');
  }

  guessHistory.value.unshift({
    value: guessValue,
    closeness: closeness,
    trend: trend
  });

  if (guessHistory.value.length >= 5) {
    isGameOver.value = true;
  } else {
    if (revealedCount < statsToReveal.length) {
      revealedStats[statsToReveal[revealedCount]] = true;
      revealedCount++;
    }
  }

  userGuess.value = '';
};

// Вычисляемое свойство для преобразования данных игр для карусели
const carouselItems = computed(() => {
  if (streamData.value && streamData.value.games_played) {
    return streamData.value.games_played.map(game => ({
      title: game.title,
      // Убедитесь, что ваш API возвращает полный URL к изображению
      image: game.image
    }));
  }
  return [];
});


// Вспомогательная функция для форматирования даты
const formatDate = (dateString) => {
  if (!dateString) return '';
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString('ru-RU', options);
};

// Вспомогательная функция для форматирования длительности из секунд
const formatLength = (minutes) => {
  if (isNaN(minutes) || minutes < 0) return '0ч 0м';
  const h = Math.floor(minutes / 60);
  const m = Math.floor(minutes % 60);
  return `${h}ч ${m}м`;
};

</script>

















<style scoped>
.modal-overlay {
  position: fixed; /* Позиционирование относительно окна браузера */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7); /* Черный цвет с 70% прозрачности для затемнения */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; /* Высокий z-index, чтобы быть поверх всего */
}

.modal-content {
  /* Сам компонент StreamleEndScreen уже имеет свои стили (карточку),
     поэтому здесь дополнительных стилей не требуется.
     Родитель .modal-overlay уже отцентрировал его. */
  z-index: 1001; /* На всякий случай, чтобы был выше оверлея */
}
.stream-stats-card {
  color: #fff;
  font-family: 'Inter', sans-serif;
  padding: 24px;
  border-radius: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 800px;
  margin: 0 auto;
}

.stream-title {
  font-size: 24px;
  font-weight: 600;
  margin: 0;
  text-align: center;
}

.stream-date {
  font-size: 14px;
  color: #8A8A8A;
  margin-top: 4px;
}

.carousel {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  margin: 20px 0 0 0;
}

.arrow {
  font-size: 32px;
  color: #555;
  cursor: pointer;
  padding: 0 10px;
}

.carousel-items {
  display: flex;
  gap: 10px;
}

.item {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 12px;
  color: #ccc;
}

.item img {
  //width: 100px;
  //height: 140px;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 8px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(150px, 1fr));
  gap: 12px;
  width: 100%;
}

.stat-box {
  background-color: var(--dark-sm);
  border-radius: 10px;
  padding: 12px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.stat-box.hint {
  border: 1px solid #FFD700;
  box-shadow: 0 0 10px #FFD700, 0 0 5px #FFD700 inset;
  cursor: pointer;
  color: #FFD700;
}

.stat-box .value {
  font-size: 20px;
  font-weight: 600;
}

.stat-box .label {
  font-size: 12px;
  margin-top: 4px;
}

.label.duration { color: #FF3E3E; }
.label.subscribed { color: #3498DB; }
.label.watch-hours { color: #A991D4; }
.label.peak-viewers { color: #18BC9C; }

.average-viewers {
  background-color: var(--dark-sm);
  border-radius: 10px;
  padding: 12px 0;
  width: 100%;
  margin-top: 12px;
  text-align: center;
  position: relative;
}

.avg-value {
 font-size: 20px;
  font-weight: 600;
  background-color: rgba(175, 87, 87, 0);
  color: white;
  border: none;
  text-align: center;
  margin-bottom: 4px;
}

.avg-value:focus {
  outline: none;
}

.avg-label {
  font-size: 12px;
  color: #18BC9C;
}

.checkmark {
  width: 24px;
  height: 24px;
  background-color: var(--border-color-dark);
  border-radius: 8px;
  color: #4CAF50;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  border: none;
  margin-top: 10px;
  padding: 20px;
  font-size: 1.5rem;
  cursor: pointer;
}

.extra-stats {
  margin-top: 25px;
  width: 20%;
  display: flex;
  flex-direction: column;
  gap: 8px;
  border-radius: 10px;
}

.extra-stat {
  display: flex;
  justify-content: space-between;
  font-size: 16px;
  font-weight: 500;
  padding: 12px;
  background-color: var(--dark-sm);
  border-radius: var(--border-radius-md);
}

.positive { color: #4CAF50; }
.negative { color: #F44336; }
</style>





















