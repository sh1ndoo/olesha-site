<template>
<div class="submit-scran-container">
<form class="scran-form-card" @submit.prevent="handleSubmit">
<h2 class="form-title">Закинуть свой скран</h2>
<!-- Блок для загрузки и предпросмотра фото -->
  <div class="form-group">
    <label for="file-upload" class="image-preview-label">
      <div class="image-preview" :class="{ 'has-image': imagePreviewUrl }">
        <img v-if="imagePreviewUrl" :src="imagePreviewUrl" alt="Предпросмотр скрана" />
        <span v-else>Нажмите, чтобы загрузить фото</span>
      </div>
    </label>
    <input
        id="file-upload"
        type="file"
        @change="handleFileUpload"
        accept="image/*"
        style="display: none;"
    />
  </div>

  <!-- Поля для ввода данных -->
  <div class="form-group">
    <label for="scran-name">Название</label>
    <input type="text" id="scran-name" v-model="scranData.name" required placeholder="Напр. Куриный бургер" />
  </div>

  <div class="form-group">
    <label for="scran-description">Краткое описание</label>
    <input type="text" id="scran-description" v-model="scranData.description" required placeholder="Напр. C картошкой фри" />
  </div>

  <!-- НОВОЕ ПОЛЕ ДЛЯ ТЕГОВ -->
  <div class="form-group">
    <label for="scran-tags">Теги (что, где, когда и др.)</label>
    <multiselect
        v-model="scranData.tags"
        :options="availableTags"
        :multiple="true"
        :close-on-select="false"
        placeholder="Выберите или найдите теги"
        label="name"
        track-by="name"
    ></multiselect>
  </div>
  <!-- КОНЕЦ НОВОГО ПОЛЯ -->

  <div class="row-inputs">
    <div class="form-group half-width">
      <label for="scran-place">Место (город, место)</label>
      <input type="text" id="scran-place" v-model="scranData.place" required placeholder="Напр. Москва, ВТБ Арена" />
    </div>

    <div class="form-group half-width">
      <label for="scran-country">Страна</label>
      <multiselect
        v-model="scranData.country"
        :options="availableCountries"
        placeholder="Выберите страну"
        :searchable="true"
        :allow-empty="false"
        label="name"
        track-by="name"
      />
    </div>
  </div>

  <div class="row-inputs">
    <div class="form-group half-width">
      <label for="scran-year">Год</label>
      <input type="number" id="scran-year" v-model="scranData.year" required placeholder="2025" />
    </div>

    <div class="form-group half-width">
      <label for="scran-price">Цена (₽)</label>
      <input type="number" id="scran-price" v-model="scranData.price" required placeholder="200.00" />
    </div>
  </div>

  <!-- Кнопки управления -->
  <div class="form-actions">
    <button type="button" class="btn btn-cancel" @click="$emit('close')">Назад</button>
    <button type="submit" class="btn btn-submit">Отправить</button>
  </div>
</form>
</div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import axios from 'axios';
import Multiselect from 'vue-multiselect'


const emit = defineEmits(['close', 'scranSubmitted']);

// Реактивный объект для хранения данных формы
const scranData = reactive({
name: '',
place: '',
country: { name: 'Россия' },
year: new Date().getFullYear(),
price: '',
imageFile: null,
description: '',
tags: [], // Добавляем поле для хранения выбранных тегов
});

// Ref для URL предпросмотра изображения
const imagePreviewUrl = ref(null);

// Ref для хранения списка всех доступных тегов
const availableTags = ref([]);
const availableCountries = ref([]);
// --- ИЗМЕНЕНИЯ В SCRIPT ---

// Функция для загрузки тегов с сервера
const fetchTags = () => {
  // Замените URL на ваш эндпоинт для получения тегов
  axios.get('http://127.0.0.1:8000/api/v1/tags/')
  .then(response => {
    // Предполагается, что сервер возвращает массив объектов вида { id: 1, name: 'Бургеры' }
    availableTags.value = response.data;
  })
  .catch(error => {
    console.error("Ошибка при загрузке тегов:", error);
  });
};

const fetchCountries = () => {
  // Замените URL на ваш эндпоинт для получения тегов
  axios.get('http://127.0.0.1:8000/api/v1/countries/')
  .then(response => {
    // Предполагается, что сервер возвращает массив объектов вида { id: 1, name: 'Бургеры' }
    availableCountries.value = response.data;
  })
  .catch(error => {
    console.error("Ошибка при загрузке стран:", error);
  });
};



// Вызываем загрузку тегов при монтировании компонента
onMounted(() => {
  fetchTags();
  fetchCountries();
});

// --- КОНЕЦ ИЗМЕНЕНИЙ В SCRIPT ---

const handleFileUpload = (event) => {
  const file = event.target.files?.[0]; // берем первый файл
  if (!file) return;

  scranData.imageFile = file;
  imagePreviewUrl.value = URL.createObjectURL(file);
};

const handleSubmit = () => {
  if (!scranData.imageFile) {
    alert('Пожалуйста, загрузите фото вашего скрана.');
    return;
  }

  const formData = new FormData();
  formData.append('name', scranData.name);
  formData.append('description', scranData.description);
  formData.append('place', scranData.place);
  formData.append('country', scranData.country.name);
  formData.append('year', scranData.year);
  formData.append('price', scranData.price);
  formData.append('image', scranData.imageFile);

  // Добавляем теги в FormData.
  // Отправляем массив ID или названий, в зависимости от того, что ожидает ваш бэкенд.
  // Здесь мы отправляем массив названий.
  if (scranData.tags && scranData.tags.length > 0) {
    const tagNames = scranData.tags.map(tag => tag.name);
    // Добавляем каждый тег отдельно, если бэкенд ожидает массив
    tagNames.forEach(tagName => {
      formData.append('tags', tagName);
    });
  }

  axios.post('http://127.0.0.1:8000/api/v1/scran/', formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
  .then(response => {
    console.log('Ответ сервера:', response.data);
    emit('scranSubmitted', scranData);
    alert('Спасибо! Ваш скран отправлен на модерацию.');
    emit('close');
  })
  .catch(error => {
    console.error('Ошибка при отправке данных:', error);
    alert('Произошла ошибка при отправке данных.');
  });
};
</script>
<!-- Стили для vue-multiselect нужно импортировать отдельно -->
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style scoped>
/* Ваши существующие стили остаются без изменений */
.submit-scran-container {
display: flex;
justify-content: center;
align-items: center;
height: 88vh;
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

.scran-form-card {
background-color: var(--dark-sm);
padding: 30px;
border-radius: 16px;
box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
width: 90%;
max-width: 500px;
color: var(--text-color);
}

.form-title {
text-align: center;
font-size: 1.8em;
margin-bottom: 25px;
margin-top: 0;
}

.form-group {
margin-bottom: 15px;
}

label {
display: block;
margin-bottom: 5px;
font-weight: bold;
font-size: 0.9em;
color: #ccc;
}

input[type="text"],
input[type="number"] {
width: 100%;
padding: 12px;
border-radius: var(--border-radius-md);
border: 1px solid var(--border-color);
background-color: var(--dark-md);
color: #ccc;
font-size: 1em;
box-sizing: border-box;
}

input::placeholder {
  color: var(--text-thirdy-color);
}

input:focus {
outline: none;
border-color: rgb(240, 182, 114);
}

.image-preview-label {
cursor: pointer;
}

.image-preview {
width: 100%;
height: 200px;
border: 2px dashed var(--border-color);
border-radius: 16px;
display: flex;
justify-content: center;
align-items: center;
color: #888;
transition: border-color 0.3s ease;
overflow: hidden;
}

.image-preview:hover {
border-color: rgb(240, 182, 114);
}

.image-preview.has-image {
border-style: solid;
padding: 0;
}

.image-preview img {
width: 100%;
height: 100%;
object-fit: cover;
}

.row-inputs {
display: flex;
gap: 15px;
}

.half-width {
flex: 1;
}

.form-actions {
display: flex;
justify-content: space-between;
margin-top: 30px;
}

.btn {
padding: 12px 25px;
border-radius: 8px;
border: none;
font-size: 1em;
font-weight: bold;
cursor: pointer;
transition: all 0.2s ease;
}

.btn:hover {
opacity: 0.8;
}

.btn-cancel {
background-color: var(--border-color);
color: white;
}

.btn-submit {
background-color: rgba(240, 182, 114, 0.7);
color: white;
}

/* Стилизация для vue-multiselect, чтобы он соответствовал вашему дизайну */
.form-group :deep(.multiselect__tags) {
background-color: var(--dark-md);
border: 1px solid var(--border-color);
border-radius: var(--border-radius-md);
padding: 10px 40px 0px 12px;
}

.form-group :deep(.multiselect__input) {
background-color: var(--dark-md);
color: var(--text-color);
  padding: 0;
  margin-bottom: 12px;
  padding-top: 2px;
  height: 20px;
}

.form-group :deep(.multiselect__input)::placeholder {
background-color: var(--dark-md);
color: var(--text-thirdy-color);
}

.form-group :deep(.multiselect) {
color: var(--text-color);
}

.form-group :deep(.multiselect__select) {
  top: 3px
}

.form-group :deep(.multiselect__single),
.form-group :deep(.multiselect__placeholder) {
  color: var(--text-thirdy-color);
  background-color: var(--dark-md);
  margin-bottom: 12px;
  font-size: 1rem;
}

.form-group :deep(.multiselect__single) {
  color: #ccc;
  padding: 0
}

.form-group :deep(.multiselect__content-wrapper) {
    background-color: var(--dark-md);
    border: 1px solid var(--border-color);
    border-radius: var(--border-radius-md);
    margin: 8px 0;
}

.half-width :deep(.multiselect__option--selected)::after,
.half-width :deep(.multiselect__option--highlight)::after {
  display: none;
}
.form-group :deep(.multiselect__option--selected),
.form-group :deep(.multiselect__option--highlight) {
  background-color: rgba(240, 182, 114, 0.7);
  border-radius: 12px;
  font-weight: normal;
  color: var(--text-color);
  margin: 5px;
}


.form-group :deep(.multiselect__option--selected)::after,
.form-group :deep(.multiselect__option--highlight)::after {
background-color: rgba(240, 182, 114, 0.7);
  border-radius: 12px;
  font-weight: normal;
  color: var(--text-color)
}

.form-group :deep(.multiselect__tag) {
background-color: rgba(240, 182, 114, 0.7);
  margin-bottom: 7px;
}

.form-group :deep(.multiselect__tag-icon):hover {
background-color: rgba(215, 155, 87, 0.7);
}

.form-group :deep(.multiselect__tag-icon):after {
  color: white
}




input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Для Firefox */
input[type=number] {
  -moz-appearance: textfield;
}
</style>




