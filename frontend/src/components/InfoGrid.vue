<script setup>
import { ref } from 'vue';
import SmallCard from './SmallCard.vue';

const cards = ref([
  {
    icon: '/images/rules.webp',
    title: 'Правила',
    href: '/rules',
    description: 'Правила Twitch, Reddit и Telegram',
    color: 'rgba(62,253,0,0.2)',
  },
  // {
  //   icon: 'https://cdn.7tv.app/emote/01G167ZYB800091NG8SM9AJ4XY/4x.png',
  //   title: 'Смайлы',
  //   description: 'Список смайлов в чате и их значение',
  //   status: 'Обновляется',
  //   color: 'rgba(255,214,0,0.2)',
  // },
  {
    icon: '/images/gaming.webp',
    title: 'Игры',
    href: '/games',
    description: 'Все игры комьюнити собранные в одном месте',
    status: 'Обновляется',
    color: 'rgba(255,230,202,0.2)',
  },
  {
    icon: '/images/commands.webp',
    title: 'Команды',
    href: '/commands',
    description: 'Список команд в Twitch чате',
    status: 'Обновляется',
    color: 'rgba(62,253,0,0.2)',
  },
  // {
  //   icon: 'https://cdn.7tv.app/emote/01GB8R1ZF0000BX30STW7STTS2/4x.png',
  //   title: 'Пасты',
  //   description: 'База паст нашего коммьюнити на одной странице',
  //   color: 'rgba(255,255,255,0.2)',
  // },
  // {
  //   icon: 'https://cdn.7tv.app/emote/01F6Q37ZYG000A6S4F82DF5PRF/4x.png',
  //   title: 'Статистика',
  //   description: 'Как часто происходит что-либо на стримах',
  //   color: 'rgba(0,109,255,0.2)',
  // },
  // {
  //   icon: 'https://cdn.7tv.app/emote/01HC3698700002NZKPADJSHWY4/4x.webp',
  //   title: 'Сотрудничество',
  //   href: '/commercial',
  //   description: 'Если хотите разместить рекламу на Twitch канале',
  //   color: 'rgba(255,126,0,0.2)',
  // },
  {
    icon: '/images/cinema.webp',
    title: 'Аукционы',
    href: '/list',
    description: 'Список всего, что выпадало на Ауках',
    color: 'rgba(113,113,113,0.2)',
  },
  {
    icon: '/images/art.webp',
    title: 'Искусство',
    href: '/art',
    description: 'Всевозможные работы по нашему любимому стримеру',
    color: 'rgba(62,253,0,0.2)',
  },
  {
    icon: '/images/scrandle.avif',
    title: 'Olesha Scrandle',
    href: '/scrandle',
    description: 'Открыт прием заявок',
    color: 'rgba(255,206,118,0.2)',
  }
]);
</script>

<template>
  <section class="info-grid grid-small">
    <SmallCard v-for="card in cards" :key="card.title" :card="card" />
  </section>
</template>


<style scoped>
.info-grid {
  display: grid;
  gap: 13px;
  margin-bottom: 24px;
}

.grid-small {
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

@media (max-width: 768px) {
  .info-grid {
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  }
}
</style>