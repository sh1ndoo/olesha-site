<template>
  <div class="media-container" @click="showMenu" >
    <i class="fa-brands fa-telegram fa-2xl"></i>
    <transition name="fade-slide">
    <div v-if="isMenuVisible" class="dropdown-menu">
      <a href="https://t.me/tribute/app?startapp=s9Bd" target="_blank" class="dropdown-item">
        <img src='/images/olesha_tg+.avif' alt="">
        <div class="about">
          <div class="title">Бабаба с бебебе</div>
          <div class="description">Приватка</div>
        </div>
      </a>
      <a href="https://t.me/etoolesha" target="_blank" class="dropdown-item">
        <img src="/images/olesha_tg.avif" alt="">
        <div class="about">
          <div class="title">Олёша</div>
          <div class="description">Оффициальный тг канал</div>
        </div>
      </a>
    </div>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isMenuVisible: false, // По умолчанию меню скрыто
    };
  },
  methods: {
    showMenu() {
      this.isMenuVisible = this.isMenuVisible === false ? true : false;
    },
  }
};
</script>

<style scoped>
/* Стили для контейнера */
.media-container {
  position: relative; /* Важно для позиционирования меню */
  display: flex;
  background-color: var(--telegram-color);
  border-radius: var(--border-radius-md);
  padding: 36px;
  justify-content: center;
  cursor: pointer;
}

/* Стили для выпадающего меню */
.dropdown-menu {
  position: absolute;
  top: 110%; /* Располагаем меню под иконкой */
  right: auto;
  background-color: var(--dark-sm-clear-md);
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius-md);
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  display: flex;
  flex-direction: column;
  min-width: 250px; /* Минимальная ширина меню */
  z-index: 5; /* Чтобы меню было поверх других элементов */
  backdrop-filter: blur(3px);
  padding: 7px;
  transition: all 0.3s ease; /* 5. Анимируем только прозрачность */
}

/* Стили для ссылок в меню */
.dropdown-menu a {
  padding: 10px 15px;
  text-decoration: none;
  color: #ffffff;
  border-radius: var(--border-radius-md);
}

.dropdown-menu a:hover {
  background-color: #3c3c3c;
}
.media-container::before {
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
.media-container:hover::before {
  opacity: 1; /* 6. При наведении делаем слой видимым */
}
.media-container i {
  z-index: 1;
}
.dropdown-item {
  display: flex;
}
.dropdown-item img {
  height: 40px;
  margin-right: 10px;
  border-radius: 50%;
}
.about {
  width: auto;
  justify-content: center;
}
.title {
  padding-bottom: 5px;
}
.description {
  font-size: 0.7rem;
}
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 2.2);
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-5px);
}
@media (max-width: 768px) {

  /* Адаптируем верхний блок с цитатой */
  .dropdown-menu {
    right: 0;
  }
}

</style>