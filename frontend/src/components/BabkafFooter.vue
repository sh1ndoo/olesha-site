<template>
  <div
      class="collision-scene"
      :class="{ 'start-animation': isAnimating }"
  >
    <div class="car" @animationend="handleAnimationEnd" @click="triggerAnimation">
      <img class="car-svg" src="https://i.postimg.cc/g23Ty8dk/i-5-no-bg-preview-carve-photos.png" alt="">
    </div>

    <!-- Изображение столба -->
    <div class="pillar">
      <img class="pillar-svg" src="https://i.postimg.cc/MKfQFYnf/image-no-bg-preview-carve-photos.png" alt="">
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Реактивная переменная для контроля состояния анимации
const isAnimating = ref(false);

// Функция для запуска анимации по клику
function triggerAnimation() {
  // Если анимация уже идет, ничего не делаем
  if (isAnimating.value) {
    return;
  }
  // Запускаем анимацию
  isAnimating.value = true;
}

// Функция для сброса состояния после завершения анимации
function handleAnimationEnd() {
  // Завершаем анимацию
  isAnimating.value = false;
}
</script>

<style scoped>
/* --- Сцена --- */
.collision-scene {
  position: absolute; /* Обязательно для позиционирования дочерних элементов */
  width: 100%;      /* Ширина нашей сцены */
  height: 80px;       /* Высота нашей сцены */
  overflow: hidden;   /* Скрывает элементы, которые выходят за пределы сцены */
  margin: 0 0 0 auto;  /* Центрирование для примера */
  right: 0;
  bottom: 0;
}

/* --- Элементы сцены (общие стили) --- */
.car, .pillar {
  position: absolute;
  bottom: 0; /* Все элементы стоят на "земле" */
  transition: transform 0.3s ease;
}

/* --- Машина --- */
.car {
  right: 300px; /* Начальная позиция машины */
  width: 100px;
  z-index: 9; /* Машина за столбом */
}
.car-svg {
  height: 5em;
  cursor: pointer;
}

/* --- Столб --- */
.pillar {
  right: -50px; /* Изначально столб находится за пределами сцены справа */
  width: 20px;
  height: 80px;
  z-index: 2; /* Столб перед машиной */
}
.pillar-svg {
  fill: var(--text-secondary-color); /* Цвет столба */
  height: 5em;
}

/* --- Логика анимации --- */
/* Когда на сцену добавляется класс .start-animation, запускаем анимации для дочерних элементов */

.collision-scene.start-animation .pillar {
  animation: pillar-strike 4.2s cubic-bezier(0.5, 0, 0.1, 1);
}

.collision-scene.start-animation .car {
  animation: car-crash 4.2s ease-out forwards;
}


/* --- Описание ключевых кадров анимации --- */

/* Анимация для столба */
@keyframes pillar-strike {
  0% {
    transform: translateX(0); /* Начальная позиция (справа за сценой) */
  }
  30% {
    transform: translateX(-50px); /* Небольшой "замах" назад */
  }
  100% {
    /* Резкое движение влево для "удара" по машине */
    transform: translateX(-220vw);
  }
}

/* Анимация для машины */
@keyframes car-crash {
  /* Первые 60% времени машина стоит на месте, ожидая удара */
  0%, 45% {
    transform: translateX(0) rotate(0);
  }

  /* Момент удара */
  55%, 90% {
    transform: translateX(-20px) translateY(20px) rotate(-90deg);
  }

  /* Возвращение в исходное состояние */
  100% {
    transform: translateX(0) rotate(0);
  }
}

@media (max-width: 1024px) {
  .collision-scene {
    display: none;
  }
}
</style>