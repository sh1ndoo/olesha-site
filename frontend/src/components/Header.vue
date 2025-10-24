<template>
  <header class="liquidGlass-wrapper header">
    <LiquidGlassFilter />
    <div class="liquidGlass-tint"></div>
    <div class="liquidGlass-shine"></div>
    <div class="liquidGlass-text">
      <div class="header-wrapper">
        <router-link to="/" class="logo">
          <img src="https://i.postimg.cc/vTQd3Jrc/az7-Sf-edited-free-carve-photos-2.png" alt="Логотип Olesha Entertainment">
        </router-link>
        <nav class="nav">
          <div class="nav-links">
            <router-link to="/">Главная</router-link>
            <router-link to="/rules">Правила</router-link>
            <router-link to="/games">Игры</router-link>
            <router-link to="/scrandle">Scran</router-link>
            <router-link to="/list">Аукционы</router-link>
            <router-link to="/art">Искусство</router-link>
            <!--            <a href="#">Смайлы</a>-->
            <router-link to="/commands">Команды</router-link>
<!--            <router-link to="/commercial">Сотрудничество</router-link>-->
          </div>
          <ProfileIcon />
        </nav>
      </div>
    </div>
  </header>
</template>

<script setup>
import LiquidGlassFilter from "@/components/LiquidGlassFilter.vue";
import ProfileIcon from "@/components/ProfileIcon.vue";
defineEmits(['toggle-theme']);

if (
    /^((?!chrome|android).)*safari/i.test(navigator.userAgent)
) {
  document.documentElement.classList.add('is-safari');
}
</script>

<style scoped>
/* Базовые стили (сохраняем ваши) */

.header {
  display: flex;
  position: sticky;
  top: 20px;
  /* Убираем фиксированную ширину, чтобы сделать компонент гибким */
  width: auto;
  margin: 0 0 24px 0; /* Используем отступы по бокам вместо центрирования через auto */
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  border-radius: 1em;
  border: 1px solid var(--border-color);
  backdrop-filter: blur(3px) url(#filter) ;
  z-index: 10;
  box-shadow: 0 0 2px 1px color-mix(in oklch, canvasText, #0000 65%) inset,
  0 0 10px 4px color-mix(in oklch, canvasText, #0000 85%) inset,
  0px 4px 16px rgba(17, 17, 26, 0.05),
  0px 8px 24px rgba(17, 17, 26, 0.05),
  0px 16px 56px rgba(17, 17, 26, 0.05),
  0px 4px 16px rgba(17, 17, 26, 0.05) inset,
  0px 8px 24px rgba(17, 17, 26, 0.05) inset,
  0px 16px 56px rgba(17, 17, 26, 0.05) inset;

}

.is-safari .header {
  backdrop-filter: blur(10px);
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo img {
  border-radius: 5%;
  height: 40px;
  cursor: pointer;
}

.header,
.header > div {
  border-radius: 16px;
}

.header-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center; /* Добавлено для лучшего выравнивания */
  width: 100%; /* Растягиваем обертку на всю доступную ширину */
}
.liquidGlass-wrapper {
  display: flex;
  font-weight: 600;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 2.2);
}

.liquidGlass-text {
  z-index: 3;
  width: -webkit-fill-available;
}
.nav {
  display: flex;
  align-items: center;
  gap: 20px;
}

.nav-links {
  display: flex;
  align-items: center;
  height: 100%;
}

.nav-links a {
  color: var(--text-secondary-color);
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.3s ease;
  align-content: center;
  height: 100%;
  padding: 0.7em 1em;
  font-weight: 500;
  border-radius: var(--border-radius-md);
  white-space: nowrap; /* Предотвращаем перенос текста в ссылках */
}
.nav-links a:hover {
  background-color: var(--border-color);
}

nav a.router-link-active {
  color: var(--text-color);
}

.profile-btn:hover {
  color: var(--text-color);
}

/* --- АДАПТИВНЫЕ СТИЛИ --- */
@media (max-width: 1550px) {
  .header {
    backdrop-filter: blur(10px);
    margin: 0 15px 24px 15px; /* Используем отступы по бокам вместо центрирования через auto */
  }
}

/* Планшеты (1024px и меньше) */
@media (max-width: 1024px) {
  .header {
    margin: 0 20px 24px 20px; /* Уменьшаем боковые отступы */
  }

  .nav-links a {
    font-size: 0.85rem; /* Немного уменьшаем шрифт */
  }
}

/* Мобильные устройства (968px и меньше) */
@media (max-width: 868px) {
  .header {
    margin: 0 0px 24px 0px; /* Уменьшаем отступы для мобильных */
    padding: 8px 15px; /* Уменьшаем внутренние отступы */

  }

  .nav-links {
    /*
      Скрываем навигационные ссылки.
      Здесь предполагается, что появится иконка-бургер для открытия меню.
    */
    display: none;
  }

  .nav {
    gap: 15px; /* Уменьшаем расстояние между элементами в навигации */
  }

  /* Если у вас нет бургер-меню, то иконка профиля будет единственным элементом в .nav */
  .header-wrapper {
    /* Логотип слева, иконка профиля справа */
    justify-content: space-between;
  }
}
</style>
