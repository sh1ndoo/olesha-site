<template>
  <div class="media-container" @click='showMenu' >
    <i class="fa-regular fa-user"></i>
    <transition name="fade-slide">
<!--      <div v-if="isMenuVisible" class="dropdown-menu">-->
<!--        <a href="https://www.twitch.tv/olesha" class="dropdown-item">-->
<!--          <img src='/images/glitch_flat_purple.png' alt="">-->
<!--          <div class="about">-->
<!--            <div class="title">Войти через Twitch</div>-->
<!--          </div>-->
<!--        </a>-->
<!--      </div>-->
      <div v-if="isMenuVisible" class="dropdown-menu">
        <router-link to="/profile" class="dropdown-item">
          <i class="fa-regular fa-user"></i>
          <div class="about">
            <div class="title">Профиль</div>
          </div>
        </router-link>
        <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" class="dropdown-item">
          <i class="fa-solid fa-gear"></i>
            <div class="about">
            <div class="title">Настройки</div>
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
  position: relative;
  background: none;
  border: none;
  color: var(--text-secondary-color);
  cursor: pointer;
  font-size: 1.2rem;
  transition: color 0.3s ease;
}

/* Стили для выпадающего меню */
.dropdown-menu {
  position: absolute;
  top: 230%;
  right: -1.2em;
  background-color: var(--dark-sm-clear-md);
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius-md);
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  display: flex;
  flex-direction: column;
  min-width: 250px; /* Минимальная ширина меню */
  z-index: 50; /* Чтобы меню было поверх других элементов */
  backdrop-filter: blur(3px);
  padding: 7px;
  transition: all 0.3s ease; /* 5. Анимируем только прозрачность */
  font-size: 1rem;
}

.title {
  align-content: center;
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


.dropdown-menu router-link {
  padding: 10px 15px;
  text-decoration: none;
  color: #ffffff;
  border-radius: var(--border-radius-md);
}

.dropdown-menu router-link:hover {
  background-color: #3c3c3c;
}

.media-container:hover {
  color: var(--text-color);
}
.media-container i {
  z-index: 1;
}
.dropdown-item {
  display: flex;
}
.dropdown-item img {
  height: 30px;
  margin-right: 10px;
}
.dropdown-item i {
  height: 30px;
  margin-right: 10px;
  font-size: 20px;
  align-items: center;
  display: flex;
}
.about {
  width: auto;
  justify-content: center;
  display: flex;
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

</style>