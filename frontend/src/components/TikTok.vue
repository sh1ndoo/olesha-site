<template>
  <a style="border: 1px solid var(--border-color-dark)" class="media-container" href="https://www.tiktok.com/@tiktokolesha" target="_blank">
    <svg style="position: absolute; bottom: 25%" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 30 30" alt="TikTok" height="35" width="35">
      <path fill="#25F4EE" d="M9.875 11.842v-1.119A9 9 0 0 0 8.7 10.64c-4.797-.006-8.7 3.9-8.7 8.708a8.7 8.7 0 0 0 3.718 7.134A8.68 8.68 0 0 1 1.38 20.55c0-4.737 3.794-8.598 8.495-8.707"></path>
      <path fill="#25F4EE" d="M10.087 24.526c2.14 0 3.89-1.707 3.966-3.83l.007-18.968h3.462a7 7 0 0 1-.109-1.202h-4.727l-.006 18.968a3.98 3.98 0 0 1-3.967 3.83 3.9 3.9 0 0 1-1.846-.46 3.95 3.95 0 0 0 3.22 1.662m13.905-16.36V7.111a6.5 6.5 0 0 1-3.584-1.067 6.57 6.57 0 0 0 3.584 2.122"></path>
      <path fill="#FE2C55" d="M20.41 6.044a6.54 6.54 0 0 1-1.617-4.316h-1.265a6.56 6.56 0 0 0 2.881 4.316M8.707 15.365a3.98 3.98 0 0 0-3.974 3.976c0 1.528.87 2.858 2.134 3.523a3.94 3.94 0 0 1-.754-2.321 3.98 3.98 0 0 1 3.973-3.976c.41 0 .805.07 1.176.185v-4.833a9 9 0 0 0-1.176-.083c-.07 0-.134.006-.204.006v3.708a4 4 0 0 0-1.175-.185"></path>
      <path fill="#FE2C55" d="M23.992 8.166v3.676a11.25 11.25 0 0 1-6.579-2.116v9.622c0 4.8-3.903 8.713-8.706 8.713a8.67 8.67 0 0 1-4.99-1.579 8.7 8.7 0 0 0 6.37 2.781c4.797 0 8.706-3.906 8.706-8.714v-9.621a11.25 11.25 0 0 0 6.579 2.116v-4.73q-.718-.002-1.38-.148"></path>
      <path data-v-2c3c4429="" fill="#fff" d="M17.413 19.348V9.726a11.25 11.25 0 0 0 6.58 2.116V8.166a6.57 6.57 0 0 1-3.584-2.122 6.6 6.6 0 0 1-2.887-4.316h-3.463l-.006 18.968a3.98 3.98 0 0 1-3.967 3.83 3.99 3.99 0 0 1-3.225-1.656 3.99 3.99 0 0 1-2.134-3.523A3.98 3.98 0 0 1 8.7 15.372c.409 0 .805.07 1.176.185v-3.708c-4.702.103-8.496 3.964-8.496 8.701 0 2.29.888 4.373 2.338 5.933a8.67 8.67 0 0 0 4.989 1.58c4.797 0 8.706-3.913 8.706-8.715M30.048"></path>    </svg>
  </a>
</template>

<script>
</script>

<style scoped>
/* Стили для контейнера */
.media-container {
  position: relative; /* Важно для позиционирования меню */
  display: flex;
  background: linear-gradient(black);
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
.media-container svg {
  z-index: 1;
  color: var(--text-color)
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