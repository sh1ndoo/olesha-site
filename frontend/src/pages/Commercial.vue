<script setup>
import { ref, readonly } from 'vue';

function useClipboard() {
  const isCopied = ref(false);
  const isSupported = navigator && 'clipboard' in navigator;
  const copy = async (text) => {
    if (!isSupported) {
      console.error('Clipboard API не поддерживается вашим браузером.');
      return;
    }

    try {
      await navigator.clipboard.writeText(text);
      isCopied.value = true;
      setTimeout(() => {
        isCopied.value = false;
      }, 2000);
    } catch (err) {
      console.error('Ошибка при копировании:', err);
    }
  };

  // readonly() защищает состояние от изменения извне компонента
  return {
    isCopied: readonly(isCopied),
    copy,
    isSupported,
  };
}
const { isCopied, copy, isSupported } = useClipboard()
const email = ref('oleshareklama@gmail.com');
</script>

<template>
  <h1 style="text-align: center; font-size: 2.5rem; margin-bottom: 1rem">Сотрудничество</h1>
  <div class="description">
    <div class="quote">
      <div class="quote-left">
        <i class="fa-solid fa-exclamation"></i>
      </div>
      <p>Оффтоп игнорится. По букам/казино просьба не беспокоить.</p>
    </div>
  </div>
  <div class="main">
    <div style="flex-direction: column" class="quote">
      <div style="display: flex; flex-direction: row;">
        <div style="background-color: rgba(255,174,0,0.2); padding: 0.5em 0.5em" class="quote-left">
          <i style="color: rgba(255,174,0,1); font-size: 1.5rem" class="fa-solid fa-envelope"></i>
        </div>
        <p style="font-size: 1.15rem; font-weight: 600">{{email}}</p>
      </div>
      <div style="display: flex; flex-direction: row; margin-bottom: 0.9em">
        <a class="btn" href="mailto:oleshareklama@gmail.com">Написать</a>
          <a class="btn">
            <span style="visibility: hidden">Скопировать адрес</span>
            <Transition name="fade" mode="out-in">
              <span :key="isCopied" @click="copy(email)">
                {{ isCopied ? 'Скопировано!' : 'Скопировать адрес' }}
              </span>
            </Transition>
          </a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.description {
  text-align: center;
  font-size: 0.9rem;
  margin-bottom: 3rem
}
.quote {
  display: flex;
  flex-direction: row;
  font-size: 0.9rem;
  width: fit-content;
  margin: 0 auto;
  background-color: var(--dark-sm);
  padding: 0 0.9em;
  border-radius: var(--border-radius-md);
  border: 1px solid var(--border-color);
}

.quote p{
  align-content: center;
  margin-left: 0.7em;
  margin-right: 0.5em;
}

.quote-left {
  padding: 0.5em 1.03em;
  margin: 0.9em 0;
  background-color: rgba(255, 0, 0, 0.25);
  border-radius: var(--border-radius-sm);
}

.quote-left i {
  font-weight: 800;
  font-size: 1rem;
  color: rgb(255, 0, 0);
}
.btn {
  padding: 0.5em 1.03em;
  background-color: var(--border-color);
  text-decoration: none;
  color:var(--text-color);
  border-radius: var(--border-radius-sm);
  margin-right: 0.5em;
  transition: all ease 0.3s;
  display: grid; /* 1. Включаем Grid Layout */
  place-items: center; /* 2. Центрируем содержимое по горизонтали и вертикали */
  cursor: pointer;

}
.btn:hover {
  background-color: var(--border-color-dark);
}
/* Базовые стили для плавного перехода */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

/* Начальное состояние для входящего элемента (полностью прозрачный) */
.fade-enter-from,
  /* Конечное состояние для уходящего элемента (полностью прозрачный) */
.fade-leave-to {
  opacity: 0;
}
.btn > * {
  grid-area: 1 / 1;
}

@media (max-width: 768px) {

  /* Адаптируем верхний блок с цитатой */
  .description .quote {
    align-items: center;
    text-align: center;
  }

  .description .quote p {
    margin: 0;
    margin-left: 0.7em;
  }
}
</style>