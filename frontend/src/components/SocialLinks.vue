<script setup>
import { ref } from 'vue';
import YouTube from "@/components/YouTube.vue";
import Telegram from "@/components/Telegram.vue";
import Twitch from "@/components/Twitch.vue";
import TikTok from "@/components/TikTok.vue";
import Reddit from "@/components/Reddit.vue";
</script>

<template>
  <section class="social-links">
    <Twitch />
    <Reddit />
    <Telegram />
    <TikTok />
    <YouTube />
  </section>
</template>


<style scoped>
.social-links {
  display: grid;
  grid-template-columns: repeat(5, minmax(100px, 1fr));
  gap: 16px;
  margin: 0 0 24px 0;
}

.social-link {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 36px;
  border-radius: var(--border-radius-md);
  text-decoration: none;
  color: white;
  transition: transform 0.2s ease;
}

.social-link::before {
  content: ''; /* 2. Обязательно для псевдоэлемента */
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;

  background-color: rgba(0, 0, 0, 0.15); /* 3. Черный слой с 40% прозрачности */

  opacity: 0; /* 4. Изначально слой полностью прозрачен (невидим) */
  transition: opacity 0.3s ease; /* 5. Анимируем только прозрачность */
}
.social-link:hover::before {
  opacity: 1; /* 6. При наведении делаем слой видимым */
}

.social-link svg {
  width: 32px;
  height: 32px;
}

.social-link i {
  z-index: 1;
}

@media (max-width: 1024px) {
  .social-links {
    /* Можно немного уменьшить отступ между элементами */
    gap: 14px;
  }
}

/* --- СТИЛИ ДЛЯ МОБИЛЬНЫХ ТЕЛЕФОНОВ (до 768px) --- */
@media (max-width: 768px) {
  .social-links {
    gap: 12px; /* Делаем отступ еще меньше */
    margin: 20px 0; /* Уменьшаем вертикальный отступ секции */
    grid-template-columns: repeat(3, minmax(0, 1fr));

  }

  .social-link {
    /*
      Уменьшаем внутренний отступ (padding). 36px - это слишком много
      для маленькой кнопки на мобильном устройстве.
    */
    padding: 28px;
  }

  .social-link svg {
    /* Иконки можно оставить прежними (32px), так как это хороший
       размер для сенсорного ввода, или немного уменьшить. */
    width: 30px;
    height: 30px;
  }
}

</style>