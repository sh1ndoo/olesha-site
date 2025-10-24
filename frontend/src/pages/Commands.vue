<script setup>
import MarkDownRenderer from "@/components/MarkDownRenderer.vue";
import { ref } from 'vue';
const markdownInput = ref(
    `
> [!COMMAND] !music
> Отображает играющую музыку в данный момент
> \`\`\`
> user: !music
> holy_bot: @user, Never Gonna Give You Up
> \`\`\`

> [!COMMAND] !title
> Отображает название стрима на данный момент
> \`\`\`
> user: !title
> holy_bot: @user, тсс, стрим спит, не шумите
> \`\`\`

> [!COMMAND] !играли
> Показывает какое колличество времени была выставлена та или иная категория
> \`\`\`
> user: !играли
> holy_bot: @user, Just Chatting [01:00:00] | Megabonk [03:00:00] | BATTLEFIELD 6 [00:30:00].
> \`\`\`

> [!COMMAND] !game !gametime
> Показывает текущую категорию и её продолжительность
> \`\`\`
> user: !game
> holy_bot: @user, BATTLEFIELD 6 [00:30:00]
> \`\`\`
> \`\`\`
> user: !gametime
> holy_bot: @user, BATTLEFIELD 6 [00:30:00]
> \`\`\`

> [!COMMAND] !duel @user [кол-во мини-приколов]
> Вызов на _дуэль_
> \`\`\`
> user1: !duel @user2 1000
> StreamElements: @user2, @user1 хочет сразиться с вами на дуэли за 1000 Мини-приколы. Вы можете !accept или !deny в течение 2 минут
> user2: !accept
> StreamElements: user1 победил в Дуэли против user2 EZ и выиграл 30 Мини-приколы Clap
> \`\`\`

> [!COMMAND] !balance [nickname]
> Просмотр своего баланса мини-приколов или другого чаттера
> \`\`\`
> user: !balance
> StreamElements: У user 100000 мини-приколов xdd
> \`\`\`
> \`\`\`
> user: !balance user2
> StreamElements: У user2 200000 мини-приколов xdd
> \`\`\`

> [!COMMAND] !8ball
> Ответ от _шара_
> \`\`\`
> user: !8ball стрим сегодня?
> StreamElements: @user, шар «восьмерка» говорит: да я сам не знаю EZ
> \`\`\`





# Ссылки
> [!COMMAND] !tg
> Отправляет ссылку на лучший телеграм канал
> \`\`\`
> user: !tg
> StreamElements: Телега: https://t.me/etoolesha
> \`\`\`

> [!COMMAND] !tg+
> Отправляет ссылку на лучший платный телеграм канал
> \`\`\`
> user: !tg+
> StreamElements: Платная Сабка + членство в элитном клубе/экслюзивный постинг/розыгрыши игр с (ан)Саб-Дней и многое другое™ https://t.me/tribute/app?startapp=s9Bd
> \`\`\`

> [!COMMAND] !reddit
> Отправляет ссылку на лучший саб-реддит
> \`\`\`
> user: !reddit
> StreamElements: https://www.reddit.com/r/olesha/ Официальный Саб-Реддит ОТКРЫТ! Кладезь контента, посвященного каналу, для самых искушенных: мемы, арты, мнения, тэйки и многое другое™, на который стример будет регулярно реагировать на трансляциях!
> \`\`\`

> [!COMMAND] !tiktok
> Отправляет ссылку на лучший тикток
> \`\`\`
> user: !tiktok
> StreamElements: ТикТок Официальный СКИБИДИ СИГМА РИЗЗЛЕР TikTok канал ЗАПУЩЕН! Необходимо подписаться (если вы не леймик, офк): https://www.tiktok.com/@tiktokolesha
> \`\`\`



`
);
</script>

<template>
  <h1 style="text-align: center; font-size: 2.5rem; margin-bottom: 3rem">Комманды Twitch чата</h1>
  <MarkDownRenderer :source="markdownInput" />
</template>

<style scoped>
.description {
  text-align: center;
  font-size: 0.9rem;
  margin-bottom: 3rem
}
</style>