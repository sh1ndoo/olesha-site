<template>
  <a class="media-container" href="https://www.reddit.com/r/olesha/" target="_blank">
    <i class="fa-brands fa-reddit-alien fa-2xl"></i>
  </a>
</template>

<script>
</script>

<style scoped>
/* Стили для контейнера */
.media-container {
  position: relative; /* Важно для позиционирования меню */
  display: flex;
  background-color: var(--reddit-color);
  border-radius: var(--border-radius-md);
  padding: 36px;
  justify-content: center;
  cursor: pointer;
  text-decoration: none;
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
  color:var(--text-color)
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
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

</style>