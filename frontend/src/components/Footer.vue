<template>
  <footer class="site-footer">
    made by <a href="https://t.me/ifknow_me" target="_blank" rel="noopener noreferrer">ifknow</a> with ❤️
  </footer>
</template>

<script>
import BabkafFooter from "@/components/BabkafFooter.vue";

export default {
  name: 'SiteFooter',
  components: {BabkafFooter}
}
</script>

<style scoped>
.site-footer {
  text-align: center; /* Центрируем текст */
  padding: 40px 15px; /* Добавляем отступы сверху/снизу и по бокам */
  margin-top: 20px; /* Небольшой отступ от основного контента */
  font-size: 0.9em; /* Слегка уменьшаем шрифт */
  color: #888; /* Делаем текст менее навязчивым */
  z-index: 8;
}

.site-footer a {
  color: #777; /* Цвет ссылки */
  font-weight: 600; /* Делаем имя чуть жирнее */
  text-decoration: none; /* Убираем подчеркивание */
  transition: color 0.3s ease; /* Плавный переход цвета при наведении */
}

.site-footer a:hover {
  color: #333; /* Цвет ссылки при наведении */
}
</style>