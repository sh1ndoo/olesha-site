<template>
  <div class="profile-card">
    <!-- Заголовок профиля с фоном и аватаром -->
    <header class="profile-header">
      <img :src="user.background" alt="User Background" class="profile-background" />
      <div class="avatar-container">
        <img :src="user.avatar" alt="User Avatar" class="profile-avatar" />
      </div>
    </header>

    <!-- Основная информация -->
    <section class="profile-info">
      <div class="info-left">
        <h1 class="nickname">{{ user.nickname }}</h1>
        <p class="message-count">Количество сообщений в чате: {{ user.messageCount }}</p>
      </div>
      <div class="info-right">
        <h2 class="aggression-title" @click="showToxicityTooltip = !showToxicityTooltip">
          Оценка агрессии (by AI) ⓘ
        </h2>
        <div class="aggression-score">
          <span class="score-value">{{ user.aggressionScore }}/10</span>
          <div class="score-bar-container">
            <div class="score-bar" :style="{ width: `${user.aggressionScore * 10}%` }"></div>
          </div>
        </div>
        <!-- Всплывающее окно -->
        <div v-if="showToxicityTooltip" class="toxicity-tooltip">
          <p><pre>Общая оценка токсичности: 7

Краткое обоснование: Пользователь демонстрирует высокий уровень токсичности, регулярно используя прямые оскорбления, нецензурную лексику и агрессивные выпады в адрес других участников чата. Его коммуникация в моменты недовольства носит преимущественно деструктивный и уничижительный характер. Хотя в его сообщениях отсутствует язык вражды, частота и интенсивность оскорблений являются основной причиной для высокой оценки.

Ключевые примеры:

"@thelastsekret мне кажется ты идиот, просто этого не осознаешь"
"ну так может вы рандомных долбоебов не имеющих ко мне отношения не будете обсуждать в моём чате?"
"старина, съеби нахуй"
"иди траву потрогай долбоёб"
"съебите нахуй отсюда с этим говном, на кой хуй вы какие вбросы сюда тащите и обсасываете?"
          </pre></p>
        </div>
      </div>
    </section>

    <!-- Навигация по вкладкам -->
    <nav class="profile-nav">
<!--      <button @click="activeTab = 'messages'" :class="{ active: activeTab === 'messages' }">-->
<!--        История сообщений-->
<!--      </button>-->
<!--      <button @click="activeTab = 'achievements'" :class="{ active: activeTab === 'achievements' }">-->
<!--        Достижения-->
<!--      </button>-->
      <button @click="activeTab = 'skrandls'" :class="{ active: activeTab === 'skrandls' }">
        История скранов
      </button>
    </nav>

    <!-- Содержимое вкладок -->
    <div class="profile-content">
      <!-- История сообщений -->
<!--      <div v-if="activeTab === 'messages'" class="content-section">-->
<!--        <div class="messages-header">-->
<!--          <div class="date-selector-container">-->
<!--            <select class="date-selector">-->
<!--              <option>2025-10</option>-->
<!--            </select>-->
<!--          </div>-->
<!--          <input type="text" class="search-input" placeholder="Search">-->
<!--        </div>-->
<!--        <div class="messages-list">-->
<!--          <div v-for="message in user.messages" :key="message.id" class="message-item">-->
<!--            <span class="timestamp">{{ message.timestamp }}</span>-->
<!--            <div class="message-content">-->
<!--                <span class="username-wrapper">-->
<!--                    <img src="/images/glitch_flat_purple.png" class="icon" />-->
<!--                    <img :src="user.avatar" alt="User Avatar" class="message-avatar" />-->
<!--                    <span class="username">{{ user.nickname }}:</span>-->
<!--                </span>-->
<!--              <span class="message-text" v-html="message.text"></span>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->

      <!-- Достижения -->
<!--      <div v-if="activeTab === 'achievements'" class="content-section">-->
<!--        <h2 class="content-title">Достижения</h2>-->
<!--        <div class="achievements-grid">-->
<!--          <div v-for="achievement in user.achievements" :key="achievement.id" class="achievement-card">-->
<!--            <div class="achievement-icon">{{ achievement.icon }}</div>-->
<!--            <h3 class="achievement-name">{{ achievement.name }}</h3>-->
<!--            <p class="achievement-description">{{ achievement.description }}</p>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->

      <!-- История скрендлов -->
      <div v-if="activeTab === 'skrandls'" class="content-section">
        <div class="skrandl-summary">
          <h3 class="summary-title">Среднее угаданное количество</h3>
          <p class="summary-value">{{ averageGuessedAmount }}/10</p>
        </div>
        <div class="skrandl-list">
          <div v-for="skrandl in user.skrandlHistory" :key="skrandl.id" class="skrandl-item">
            <div>
              <p class="skrandl-name">Скран #{{ skrandl.id }}</p>
              <p class="skrandl-details">{{ skrandl.guessedAmount }}/10</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const activeTab = ref('skrandls');
const showToxicityTooltip = ref(false); // Добавляем состояние для всплывающего окна

const user = ref({
  nickname: 'Olesha (ЭТО ПРИМЕР(кроме оценки токсичности и кол-ва сообщений), НАСТОЯЩИЙ ФУНКЦИОНАЛ В РАЗРАБОТКЕ)',
  avatar: '/images/olesha_tv.png',
  background: '/images/olesha_back.png',
  messageCount: 4494,
  aggressionScore: 7,
  messages: [
    { id: 1, text: '!nuke 100 писик и попик 1000000', timestamp: '2025-10-18 05:35:16' },
    { id: 2, text: 'https://7tv.app/emotes/01K7EFRMCBARSTTTZZAYNK3RHN', timestamp: '2025-10-17 23:23:25' },
    { id: 3, text: 'https://uterup.ru/', timestamp: '2025-10-16 23:45:16' },
    { id: 4, text: '!nuke 300 1000000 музыки', timestamp: '2025-10-11 22:13:05' },
    { id: 5, text: '!nuke 300 1000000 музыку', timestamp: '2025-10-11 22:12:46' },
    { id: 6, text: '!nuke 300 1000000 музыку музыки музыка', timestamp: '2025-10-11 22:12:25' },
    { id: 7, text: '!nuke музыка музыки музыку 10000000 10000000', timestamp: '2025-10-11 22:11:53' },
    { id: 8, text: '<img src="/images/emote.png" class="emote"/>', timestamp: '2025-10-10 23:03:18' },
    { id: 9, text: '<img src="/images/emote.png" class="emote"/>', timestamp: '2025-10-10 23:03:17' },
    { id: 10, text: '<img src="/images/emote.png" class="emote"/>', timestamp: '2025-10-10 23:03:17' },
    { id: 11, text: '<img src="/images/emote.png" class="emote"/>', timestamp: '2025-10-10 23:03:17' },
    { id: 12, text: '<img src="/images/emote.png" class="emote"/>', timestamp: '2025-10-10 23:03:16' },
    { id: 13, text: '<img src="/images/emote.png" class="emote"/>', timestamp: '2025-10-10 23:03:16' },
    { id: 14, text: '<img src="/images/emote.png" class="emote"/>', timestamp: '2025-10-10 23:03:15' },
    { id: 15, text: '<img src="/images/emote.png" class="emote"/>', timestamp: '2025-10-10 23:03:15' },
    { id: 16, text: '<img src="/images/emote.png" class="emote"/>', timestamp: '2025-10-10 23:03:14' },
    { id: 17, text: '<img src="/images/emote.png" class="emote"/>', timestamp: '2025-10-10 23:03:14' },
    { id: 18, text: '<img src="/images/emote2.png" class="emote-long"/> <img src="/images/emote2.png" class="emote-long"/> <img src="/images/emote2.png" class="emote-long"/>', timestamp: '2025-10-10 22:23:55' },
    { id: 19, text: '<img src="/images/emote2.png" class="emote-long"/>', timestamp: '2025-10-10 22:23:55' },
    { id: 20, text: '<img src="/images/emote2.png" class="emote-long"/> <span class="f-word">F5F5</span> <img src="/images/emote2.png" class="emote-long"/> <span class="f-word">F5F5</span> <img src="/images/emote2.png" class="emote-long"/> <span class="f-word">F5F5</span> <img src="/images/emote2.png" class="emote-long"/>', timestamp: '2025-10-10 22:23:54' },
    { id: 21, text: '<img src="/images/emote2.png" class="emote-long"/> <span class="f-word">F5F5</span>', timestamp: '2025-10-10 22:23:54' },
    { id: 22, text: '<img src="/images/emote2.png" class="emote-long"/> <span class="f-word">F5F5</span>', timestamp: '2025-10-10 22:23:53' },
    { id: 23, text: '<img src="/images/emote2.png" class="emote-long"/>', timestamp: '2025-10-10 22:23:53' },
    { id: 24, text: '<img src="/images/emote2.png" class="emote-long"/>', timestamp: '2025-10-10 22:23:52' },
    { id: 25, text: '<img src="/images/emote2.png" class="emote-long"/>', timestamp: '2025-10-10 22:23:52' },
    { id: 26, text: '<img src="/images/emote2.png" class="emote-long"/>', timestamp: '2025-10-10 22:23:51' },
    { id: 27, text: '<img src="/images/emote2.png" class="emote-long"/>', timestamp: '2025-10-10 22:23:51' },
    { id: 28, text: 'https://www.ea.com/twitchlinking', timestamp: '2025-10-10 22:09:37' },
  ],
  achievements: [
    { id: 1, name: 'Мастер чата', icon: '💬', description: 'Отправить 1000 сообщений' },
    { id: 2, name: 'Ветеран', icon: '🛡️', description: 'Быть с нами больше года' },
    { id: 3, name: 'Донатер', icon: '💰', description: 'Поддержать стримера' },
    { id: 4, name: 'Полуночник', icon: '🦉', description: 'Смотреть стрим после полуночи' },
  ],
  skrandlHistory: [
    { id: 1, score: 8, guessedAmount: 7 },
    { id: 2, score: 9, guessedAmount: 9 },
    { id: 3, score: 6, guessedAmount: 5 },
    { id: 4, score: 10, guessedAmount: 10 },
    { id: 5, score: 7, guessedAmount: 6 },
  ],
});

const averageGuessedAmount = computed(() => {
  if (user.value.skrandlHistory.length === 0) return 0;
  const total = user.value.skrandlHistory.reduce((acc, skrandl) => acc + skrandl.guessedAmount, 0);
  return (total / user.value.skrandlHistory.length).toFixed(1);
});
</script>

<style scoped>
/* Общие стили */

.profile-card {
  width: 100%;
  border-radius: var(--border-radius-md);
  overflow: hidden;
  --text-color-dimmed: #8e8e8e;
  --background-color-secondary: #181818;
}

/* Заголовок */
.profile-header {
  position: relative;
  height: 190px;
}

.profile-background {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: var(--border-radius-md);
}

.avatar-container {
  position: absolute;
  bottom: -48px; /* Смещаем аватар вниз */
  left: 24px;
}

.profile-avatar {
  width: 96px;
  height: 96px;
  border-radius: 50%;
  border: 4px solid var(--background-color); /* Фон под аватаром */
}

/* Основная информация */
.profile-info {
  background-color: var(--background-color);
  padding: 16px 24px 24px;
  padding-top: 56px; /* Оставляем место для аватара */
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.nickname {
  font-size: 28px;
  font-weight: bold;
  margin: 0;
}

.message-count {
  color: #adadb8;
  margin-top: 4px;
}

.info-right {
  text-align: right;
}

.aggression-title {
  font-size: 16px;
  font-weight: 600;
  margin: 0;
}

.aggression-score {
  display: flex;
  align-items: center;
  margin-top: 8px;
}

.score-value {
  font-size: 22px;
  font-weight: bold;
  margin-right: 12px;
}

.score-bar-container {
  width: 120px;
  height: 16px;
  background-color: #3a3a3d;
  border-radius: 8px;
  overflow: hidden;
}

.score-bar {
  height: 100%;
  background-color: #e91916;
  border-radius: 8px;
  transition: width 0.3s ease;
}

/* Навигация */
.profile-nav {
  background-color: var(--background-color);
  padding: 8px 24px;
  display: flex;
  gap: 16px;
}

.profile-nav button {
  background: none;
  border: none;
  color: #efeff1;
  padding: 10px 16px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  border-bottom: 3px solid transparent;
  transition: color 0.2s, border-color 0.2s;
}

.profile-nav button:hover {
  color: rgb(240, 182, 114); /* Фиолетовый акцент */
}

.profile-nav button.active {
  color: rgb(240, 182, 114);
  border-bottom-color: rgb(240, 182, 114);
}

/* Контент */
.profile-content {
  padding: 24px;
}

.content-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 16px;
}

/* Список сообщений */
.messages-header {
  display: flex;
  margin-bottom: 16px;
}

.date-selector-container {
  position: relative;
  margin-right: 8px;
}

.date-selector {
  background-color: #3a3a3d;
  color: white;
  padding: 8px 12px;
  border: 1px solid #3a3a3d;
  border-radius: 4px;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}

.date-selector-container::after {
  content: '▼';
  font-size: 12px;
  color: #adadb8;
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
}

.search-input {
  flex-grow: 1;
  background-color: #3a3a3d;
  color: white;
  padding: 8px 12px;
  border: 1px solid #3a3a3d;
  border-radius: 4px;
}

.messages-list {
  display: flex;
  flex-direction: column;
}

.message-item {
  display: flex;
  align-items: center;
  padding: 2px 0;
  font-size: 14px;
  height: 18px;
}

.timestamp {
  color: var(--text-color-dimmed);
  min-width: 140px;
  margin-right: 16px;
  font-variant-numeric: tabular-nums;
}

.message-content {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.username-wrapper {
  display: flex;
  align-items: center;
  margin-right: 8px;
  height: 16px;
}
.username-wrapper img {
  height: 16px;
  margin-right: 8px;
}

.username {
  font-weight: bold;
  color: #f0b672;
}

.message-text {
  word-break: break-all;
  display: flex;
  align-items: center;
}
.message-text img {
  height: 18px;
}

:deep(.f-word) {
  font-weight: bold;
  margin: 0 4px;
}

/* Сетка достижений */
.achievements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 16px;
}

.achievement-card {
  background-color: #2c2c31;
  padding: 16px;
  border-radius: 6px;
  text-align: center;
}

.achievement-icon {
  font-size: 40px;
  margin-bottom: 8px;
}

.achievement-name {
  font-weight: 600;
  margin: 0;
}

.achievement-description {
  font-size: 13px;
  color: #adadb8;
  margin-top: 4px;
}

/* История скрендлов */
.skrandl-summary {
  text-align: center;
  margin-bottom: 24px;
}

.summary-title {
  color: #adadb8;
  margin: 0;
}

.summary-value {
  font-size: 24px;
  font-weight: bold;
}

.skrandl-list {
  display: grid;
  flex-direction: column;
  gap: 12px;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
}

.skrandl-item {
  background-color: #2c2c31;
  padding: 16px;
  border-radius: 6px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.skrandl-name {
  font-weight: 600;
  font-size: 1.5rem;
  margin: 0;
}

.skrandl-details {
  font-size: 1.5rem;
  color: #adadb8;
  text-align: center;
  margin: 10px;
}

.skrandl-score {
  font-size: 18px;
  font-weight: bold;
}

.info-right {
  text-align: right;
  position: relative; /* Для позиционирования всплывающего окна */
}

.aggression-title {
  font-size: 16px;
  font-weight: 600;
  margin: 0;
  cursor: pointer; /* Указываем, что элемент кликабельный */
}

.toxicity-tooltip {
  position: absolute;
  top: 100%; /* Позиционируем под заголовком */
  right: 0;
  width: 280px;
  height: auto;
  background-color: #2c2c31;
  border: 1px solid #444;
  border-radius: var(--border-radius-md);
  padding: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  z-index: 10;
  text-align: left;
  font-size: 14px;
  color: #efeff1;
}

.toxicity-tooltip p {
  margin: 0 0 8px 0;
}
.toxicity-tooltip p:last-child {
  margin-bottom: 0;
}
pre {
  overflow-x: auto;
  overflow-y: auto;
  height: 100%;
  white-space: pre-wrap;
}
</style>