<template>
  <!-- Добавляем класс single-item-mode, если элемент всего один -->
  <div class="carousel-wrapper" :class="{ 'single-item-mode': isSingleItem }">
    <div class="carousel-container">
      <div class="carousel-track" :style="trackStyle">
        <div
          v-for="(item, index) in items"
          :key="index"
          :class="['carousel-item', { 'is-center': isCenter(index) }]"
        >
          <div class="item-content">
            <img :src="item.image" :alt="item.title" />
            <p>{{ item.title }}</p>
          </div>
        </div>
      </div>
    </div>
    <!-- Прячем кнопки, если элемент один -->
    <button v-if="!isSingleItem && currentIndex > 0" @click="prev" class="carousel-control prev">←</button>
    <button v-if="!isSingleItem && currentIndex < items.length - visibleItems" @click="next" class="carousel-control next">→</button>
  </div>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      currentIndex: 0,
      isTransitioning: false,
      visibleItems: 3,
    };
  },
  computed: {
    // Новое вычисляемое свойство для проверки количества элементов
    isSingleItem() {
      return this.items.length === 1;
    },
    trackStyle() {
      // Если элемент один, не применяем смещение
      if (this.isSingleItem) {
        return {
          transition: 'none', // Также отключаем анимацию
        };
      }
      const offset = -this.currentIndex * (100 / this.visibleItems);
      return {
        transform: `translateX(${offset}%)`,
        transition: 'transform 0.5s ease',
      };
    },
  },
  methods: {
    isCenter(index) {
      const centerOffset = Math.floor(this.visibleItems / 2);
      return index === this.currentIndex + centerOffset;
    },
    next() {
      if (this.isTransitioning || this.currentIndex >= this.items.length - this.visibleItems) {
        return;
      }
      this.isTransitioning = true;
      this.currentIndex++;
      setTimeout(() => {
        this.isTransitioning = false;
      }, 500);
    },
    prev() {
      if (this.isTransitioning || this.currentIndex === 0) {
        return;
      }
      this.isTransitioning = true;
      this.currentIndex--;
      setTimeout(() => {
        this.isTransitioning = false;
      }, 500);
    },
  },
};
</script>

<style scoped>
.carousel-wrapper {
  position: relative;
  width: 100%;
  max-width: 600px; /* Ограничиваем максимальную ширину */
  padding: 0 40px; /* Оставляем место для кнопок */
  box-sizing: border-box;
}

.carousel-container {
  width: 100%;
  overflow: hidden;
}

.carousel-track {
  display: flex;
  /* Сдвигаем трек влево на половину одного элемента, чтобы центральный элемент был по центру контейнера */
}

.carousel-item {
  flex: 0 0 calc(100% / 3); /* Каждый элемент занимает треть ширины */
  padding: 50px 0 50px 0;
  box-sizing: border-box;
  transition: transform 0.5s ease, opacity 0.5s ease;
  opacity: 0.9; /* Неактивные элементы делаем полупрозрачными */
}

.item-content {
  text-align: center;
  transition: transform 0.5s ease, box-shadow 0.5s ease;
}

.item-content img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: var(--border-radius-lg);
}

.item-content p {
  margin: 15px 0;
  font-size: 1.1em;
  font-weight: normal;
  color: var(--border-color);
}

/* Стили для центрального элемента */
.carousel-item.is-center {
  opacity: 1;
  z-index: 10;
}

.carousel-item.is-center .item-content {
  transform: translateY(-20px) scale(1.08); /* Поднимаем и увеличиваем */
}

.carousel-item.is-center .item-content img {
  box-shadow: 0 20px 25px rgba(0, 0, 0, 1);
}

.carousel-control {
  position: absolute;
  top: 45%;
  transform: translateY(-50%);
  background: none;
  border: none;
  /* border-radius: 50%; */
  /* width: 40px; */
  /* height: 40px; */
  font-size: 5rem;
  cursor: pointer;
  z-index: 10;
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--border-color);
}

.prev {
  left: -50px;
}

.next {
  right: -50px
}
.carousel-wrapper.single-item-mode .carousel-container {
  /* Используем flexbox для центрирования дорожки с элементом */
  display: flex;
  justify-content: center;
  align-items: center;
}

.carousel-wrapper.single-item-mode .carousel-track {
  /* Дорожка больше не должна растягиваться */
  width: auto;
}

.carousel-wrapper.single-item-mode .carousel-item {
  /* Сбрасываем ширину элемента, чтобы он принял свой естественный размер */
  flex-basis: auto;
  opacity: 1;
  transform: scale(1);
}

.carousel-wrapper.single-item-mode .carousel-item img{
  height: 250px;
}

</style>