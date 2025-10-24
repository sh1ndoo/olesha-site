<script setup>
import { ref } from 'vue';
import Header from './components/Header.vue';
import SocialLinks from './components/SocialLinks.vue';
import InfoGrid from './components/InfoGrid.vue';
import LargeCardGrid from './components/LargeCardGrid.vue';
import Footer from './components/Footer.vue';
import BabkafFooter from "@/components/BabkafFooter.vue";


const theme = ref('dark');

function toggleTheme() {
  theme.value = theme.value === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', theme.value);
}
</script>

<template>
  <div class="container" :class="theme">
    <Header @toggle-theme="toggleTheme" />
      <main>
        <router-view />
      </main>
    <Footer />
  </div>
  <BabkafFooter/>
</template>

<style>
:root {
  --background-color: oklch(14.5% 0 0);
  --dark-lg: rgba(16, 16, 16, 1.00);
  --dark-lg-clear-lg: rgba(16, 16, 16, 0.50);
  --dark-lg-clear-md: rgba(20, 20, 20, 0.85);
  --dark-md: rgba(20, 20, 20, 1.00);
  --dark-sm: rgba(24, 24, 24, 1.00);
  --dark-sm-clear-md: rgba(24, 24, 24, 0.85);
  --border-color: rgb(42, 42, 42);
  --border-color-dark: rgb(32, 32, 32);
  --text-color: #ffffff;
  --text-secondary-color: #a7a7a7;
  --text-thirdy-color: #7f7f7f;
  --border-radius-sm: 8px;
  --border-radius-md: 12px;
  --twitch-color: #9146FF;
  --youtube-color: #FF0000;
  --telegram-color: #2AABEE;
  --reddit-color: #f16823;
  --tiktok-color-1: #25F4EE;
  --tiktok-color-2: #FE2C55;
  --c-light: #000;
  --glass-reflex-light: 1;
  --c-dark: #fff;
  --glass-reflex-dark: 1;


  --main-width: 1120px;

}

body {
  background-color: var(--background-color);
  color: var(--text-color);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  margin: 0;
  display: block;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);

}

.container {
  max-width: 1550px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  width: var(--main-width);
  margin: 24px auto 0 auto;
  flex-grow: 1;
}

.liquidGlass-tint {
  z-index: 1;
  position: absolute;
  inset: 0;
  background: var(--dark-lg-clear-lg);
}

.liquidGlass-shine {
  position: absolute;
  inset: 0;
  z-index: 2;
  /* Важно, чтобы тень повторяла скругление углов родителя */
  border-radius: inherit;

  box-shadow:
    /* --- ЗАМЕНА light-dark() НА УНИВЕРСАЛЬНЫЙ КОД --- */
    /* 1. Тонкая, острая внутренняя тень для имитации края стекла */
      inset 0 0 2px 1px rgba(0, 0, 0, 0.07),

        /* 2. Более мягкая и размытая внутренняя тень для глубины */
      inset 0 0 10px 4px rgba(0, 0, 0, 0.05),

        /* --- ОСТАЛЬНЫЕ ТЕНИ ИЗ ОРИГИНАЛЬНОГО КОДА (УЖЕ СОВМЕСТИМЫ) --- */
        /* 3. Внешние тени для эффекта "парения" */
      0px 4px 16px rgba(17, 17, 26, 0.05),
      0px 8px 24px rgba(17, 17, 26, 0.05),
      0px 16px 56px rgba(17, 17, 26, 0.05),

        /* 4. Глубокие внутренние тени для эффекта вдавливания */
      inset 0px 4px 16px rgba(17, 17, 26, 0.05),
      inset 0px 8px 24px rgba(17, 17, 26, 0.05),
      inset 0px 16px 56px rgba(17, 17, 26, 0.05);
}


#app {
  position: relative;
}

/* Стили для планшетов (например, ширина экрана до 1024px) */
@media (max-width: 1200px) {
  .container {
    padding: 0 20px; /* Добавляем боковые отступы, чтобы контент не прилипал к краям */
  }

  main {
    width: 100%; /* Позволяем основному контенту занимать всю доступную ширину */
  }
}

/* Стили для мобильных телефонов (например, ширина экрана до 768px) */
@media (max-width: 768px) {
  body {
    -webkit-text-size-adjust: 100%; /* Предотвращаем автоматическое изменение размера текста в iOS */
  }

  .container {
    padding: 0 20px; /* Немного уменьшаем боковые отступы для маленьких экранов */
    min-height: 100vh;
  }

  main {
    width: 100%;
    padding-bottom: 20px; /* И снизу */
  }
}



</style>