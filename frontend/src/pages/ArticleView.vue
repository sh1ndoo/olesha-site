<template>
  <div class="article-page">
    <!-- Показываем индикатор загрузки -->
    <div v-if="loading" class="loading-state">Загрузка статьи...</div>

    <!-- Показываем ошибку, если она произошла -->
    <div v-else-if="error" class="error-state">
      <h1>Ошибка</h1>
      <p>{{ error }}</p>
    </div>

    <!-- Отображаем статью, когда она загружена -->
    <article v-else-if="article">
      <MarkDownRenderer :source="article.content" />
    </article>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
// 1. Импортируем `useRoute` для доступа к параметрам URL
import { useRoute } from 'vue-router';
import MarkDownRenderer from "@/components/MarkDownRenderer.vue";

// --- Имитация API для получения данных статьи ---
const fakeApiDatabase = {
  '1': {
    content:
        `
# А нету
`
  },
  '2': {
    content:
        `
# Расширения

## <img style="margin: 0; border-radius: 0" src="https://d4.alternativeto.net/JWCnYstwM-apRwcBiVUp-TB7ZHMo2PhmonCoP_MC-JI/rs:fit:140:140:0/g:ce:0:0/exar:1/YWJzOi8vZGlzdC9pY29ucy83dHZfMjQxNTUyLnN2Zw.svg" width="20" height="20" alt="7tv Icon">  **7TV — Расширение для браузера**

**7TV** — это популярное расширение, которое позволяет вам видеть и использовать тысячи дополнительных пользовательских эмоутов на Twitch и YouTube. В абсолютном большинстве случаев его достаточно для комфортного чатинга.

#### 🌐 **Официальный сайт:** [7tv.app](https://7tv.app/)

#### **📥 Скачать 7TV:**
*   [<img style="margin: 0" src="https://upload.wikimedia.org/wikipedia/commons/e/e1/Google_Chrome_icon_%28February_2022%29.svg" width="20" height="20" alt="Chrome"> **Google Chrome, <img style="margin: 0" src="https://upload.wikimedia.org/wikipedia/commons/4/49/Opera_2015_icon.svg" width="20" height="20" alt="Chrome"> Opera, <img style="margin: 0" src="https://upload.wikimedia.org/wikipedia/commons/8/84/Yandex.Browser_icon.svg" width="20" height="20" alt="Chrome"> Яндекс Браузер, <img style="margin: 0" src="https://upload.wikimedia.org/wikipedia/commons/9/98/Microsoft_Edge_logo_%282019%29.svg" width="20" height="20" alt="Chrome"> Edge**](https://chrome.google.com/webstore/detail/7tv/ammjkodgmmoknidbanneddgankgfejfh)
*   [<img style="margin: 0" src="https://upload.wikimedia.org/wikipedia/commons/a/a0/Firefox_logo%2C_2019.svg" width="20" height="20" alt="Firefox"> **Mozilla Firefox**](https://7tv.app/)


## <img style="margin: 0; border-radius: 0" src="https://www.frostyapp.io/logo.svg" width="20" height="20" alt="Frosty Icon"> **Frosty — Мобильное приложение для Twitch**

**Frosty** — это альтернативное мобильное приложение для просмотра Twitch, которое создано для лучшего опыта в чате. Оно интегрирует поддержку эмоутов из **7TV**, BetterTTV (BTTV) и FrankerFaceZ (FFZ), которые не отображаются в официальном приложении Twitch.

#### 🌐 **Официальный сайт:** [frostyapp.io](https://www.frostyapp.io/)

#### **📥 Скачать Frosty:**
*   [<img style="margin: 0; border-radius: 0" src="https://upload.wikimedia.org/wikipedia/commons/6/67/App_Store_%28iOS%29.svg" width="20" height="20" alt="App Store"> **App Store (iOS)**](https://apps.apple.com/us/app/frosty-for-twitch/id1635541252)
*   [<img style="margin: 0; border-radius: 0" src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_Play_2022_icon.svg" width="20" height="20" alt="Google Play"> **Google Play (Android)**](https://play.google.com/store/apps/details?id=io.frostyapp.frosty)`
  },
  '3': {
    content:
        `
# Wplace
## [Wplace](https://wplace.live/) — цифровой холст, где можно разрисовать любую точку на карте мира.
Этот сайт, создали пользователи соцсети Reddit в конце июля 2025 года. Авторы Wplace вдохновлялись сообществом r/place, которое в 2017 году запустило сайт с квадратной площадью в миллион пикселей.

У Wplace схожая с r/place концепция, но вместо пустого холста используется карта Земли. После регистрации желающий может вставить 64 пикселя куда пожелает, лимиты одинаковы для всех. После этого раз в 30 секунд начисляют еще по одному пикселю.

## Как пользоваться сайтом Wplace
1. Зайдите на сайт и нажмите на кнопку Log In в правом верхнем углу.
2. Зарегистрируйтесь с помощью аккаунта Google или Twitch.
3. Выберите любое понравившееся место на карте, нажмите на кнопку Paint, чтобы закрасить пиксель выбранным цветом. Помните, что пиксель можно ставить раз в минуту.

## Где находятся основные арты сообщества
1. [Uter Island](https://wplace.live/?lat=76.3151201039058&lng=95.37389615302733&zoom=11.198292140518463)
  | Общий план острова |
  | :---: |
  | ![Описание 1](/images/island.png) |

2. [Питерский филиал 1](https://wplace.live/?lat=59.93876857998747&lng=30.389853184277328&zoom=13.124357892544428)
  | Штаб Olesha Entertainment |
  | :---: |
  | ![Описание 1](/images/piter_1.png) |

3. [Питерский филиал 2](https://wplace.live/?lat=60.004567041173324&lng=30.79063443427734&zoom=12.544862902091255)
  | Огромный Утер |
  | :---: |
  | ![Описание 1](/images/piter_2.png) |

# Галерея Артов
###### Хотите добавить свой арт? Свяжитесь со мной в телеграм @ifknow_me
###### (Я пока добавил просто первые попавшиеся)
  | [Огромный Пиксельный Утер](https://wplace.live/?lat=76.23111273399499&lng=95.78715787177734&zoom=12.267100310098034) | [Втулковая пирамида](https://wplace.live/?lat=76.17107414922626&lng=95.67729459052734&zoom=13.492527839193672) | [Айсберг по Olesha](https://wplace.live/?lat=76.30467795247029&lng=95.50379849677734&zoom=12.793831398675922) |
  | :---: | :---: | :---: |
  | ![Описание 1](/images/big_uter.png) | ![Описание 1](/images/tower.png) | ![Описание 1](/images/ice.png) |

  | [КОТЫ НА АРБУЗЕ!!!](https://wplace.live/?lat=76.30846465519949&lng=95.26913052802733&zoom=13.640088162995111) |
  | :---: |
  | ![Описание 1](/images/cats.png) |

`
  }
};
const getArticleBySlug = (slug) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => { // Имитируем задержку сети
      if (fakeApiDatabase[slug]) {
        resolve(fakeApiDatabase[slug]);
      } else {
        reject('Статья не найдена (404)');
      }
    }, 300);
  });
};
// ---------------------------------------------

// 2. Получаем доступ к текущему маршруту. Этот объект реактивен!
const route = useRoute();

// Состояние компонента
const article = ref(null);
const loading = ref(false);
const error = ref(null);

// 3. Функция для загрузки данных
const fetchArticleData = async (slug) => {
  loading.value = true;
  error.value = null;
  article.value = null; // Сбрасываем старые данные
  try {
    article.value = await getArticleBySlug(slug);
  } catch (err) {
    error.value = err;
  } finally {
    loading.value = false;
  }
};

// 4. Загружаем данные, когда компонент впервые создан
onMounted(() => {
  fetchArticleData(route.params.id); // `id` - это имя параметра из path: '/articles/:id'
});

// 5. САМОЕ ВАЖНОЕ: Следим за изменениями в URL
// Этот блок кода необходим, чтобы компонент обновился при переходе
// с одной статьи на другую (например, с /articles/slug-1 на /articles/slug-2)
watch(
    () => route.params.id,
    (newId) => {
      // Если компонент уже на экране, onMounted не вызовется,
      // поэтому мы "ловим" изменение параметра :id и перезапускаем загрузку
      if (newId) {
        fetchArticleData(newId);
      }
    }
);

function editArticle() {
  alert(`Начинаем редактирование статьи "${article.value.title}"`);
}
</script>

<style scoped>
.article-page { max-width: 750px; margin: 0 auto 0 auto; }
.loading-state, .error-state { text-align: center; padding: 3rem; color: #888; }
.error-state { color: red; }
</style>