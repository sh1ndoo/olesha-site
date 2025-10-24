<template>
  <div class="markdown-content" v-html="parsedMarkdown"></div>
</template>

<script setup>
import { computed } from 'vue';
// 1. Убедитесь, что вы импортируете КЛАСС `Marked`, а не функцию `marked`
import { Marked } from 'marked';
// 2. Убедитесь, что вы импортируете само расширение
const alertIcons = {
  note: '<svg class="octicon" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path></svg>',
  tip: '<svg class="octicon" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M8 16A8 8 0 1 1 8 0a8 8 0 0 1 0 16ZM5.75 8.5h.5V12h3V8.5h.5a.75.75 0 0 0 .75-.75V7a.75.75 0 0 0-.75-.75h-4.5a.75.75 0 0 0-.75.75v.75a.75.75 0 0 0 .75.75Zm.75-2.25h3a.25.25 0 0 1 .25.25v.25a.25.25 0 0 1-.25.25h-3a.25.25 0 0 1-.25-.25V6.5a.25.25 0 0 1 .25-.25ZM8 2.5a.75.75 0 0 0 0 1.5.75.75 0 0 0 0-1.5Z"></path></svg>',
  warning: '<svg class="octicon" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path></svg>',
  caution: '<svg class="octicon" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v9.5A1.75 1.75 0 0 1 14.25 13H8.061l-2.574 2.573A1.458 1.458 0 0 1 3 14.543V13H1.75A1.75 1.75 0 0 1 0 11.25Zm1.75-1a.25.25 0 0 0-.25.25v9.5c0 .138.112.25.25.25h2v1.543a.25.25 0 0 0 .427.177L7.12 12H14.25a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25ZM8 8.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM8 3.5a.75.75 0 0 1 .75.75v2.5a.75.75 0 0 1-1.5 0v-2.5A.75.75 0 0 1 8 3.5Z"></path></svg>',

};
const customAlertExtension = {
  name: 'alert',
  level: 'block',

  // Ищем наш синтаксис в начале строки
  start(src) {
    return src.match(/^ {0,3}> ?\[!(\w+)\]/)?.index;
  },

  tokenizer(src) {
    const rule = /^ {0,3}> ?\[!(\w+)\](?:[ \t]([^\r\n]+))?\r?\n((?:(?: {0,3}>[^\r\n]*\r?\n?)+)?)/;
    const match = rule.exec(src);

    if (match) {
      const raw = match[0];
      const type = match[1].toLowerCase();
      const title = match[2] || type.charAt(0).toUpperCase() + type.slice(1);
      let body = match[3] || '';
      body = body.replace(/(^|\n) {0,3}> ?/g, '$1');

      const token = {
        type: 'alert',
        raw,
        alertType: type,
        title,
        body,
        tokens: [] // Важно! this.lexer.blockTokens будет вызван позже для этого массива
      };

      this.lexer.blockTokens(token.body, token.tokens);

      return token;
    }
  },

  renderer(token) {
    // 1. Получаем SVG-код иконки из нашей коллекции.
    // Если иконки для такого типа нет, вернется пустая строка.
    const iconSvg = alertIcons[token.alertType] || '';

    // 2. Рендерим тело алерта в HTML
    const bodyHtml = this.parser.parse(token.tokens);

    // 3. Возвращаем финальную HTML-разметку, ВСТАВЛЯЯ иконку перед заголовком
    return `
    <div class="markdown-alert markdown-alert-${token.alertType}">
      <span class="markdown-alert-title">
        ${iconSvg}
        <span>${token.title}</span>
      </span>
      ${bodyHtml}
    </div>`;
  }
};
// 3. Создайте НОВЫЙ экземпляр парсера
const marked = new Marked();

// 4. САМЫЙ ВАЖНЫЙ ШАГ: Примените расширение к этому экземпляру
marked.use({ extensions: [customAlertExtension] });
// --- Остальная логика компонента ---
const props = defineProps({
  source: {
    type: String,
    required: true
  }
});

const parsedMarkdown = computed(() => {
  if (props.source) {
    // 5. Убедитесь, что вы используете метод .parse() от ВАШЕГО настроенного экземпляра
    return marked.parse(props.source);
  }
  return '';
});
</script>

<style scoped>
/* Добавим немного стилей, чтобы результат выглядел красиво */
.markdown-content {
  line-height: 1.6;
}

/* Стили будут применяться к тегам, которые сгенерирует marked */
.markdown-content :deep(h1),
.markdown-content :deep(h2) {
  padding-bottom: 0.3em;
  margin-top: 0;
  margin-bottom: 16px;
}

.markdown-content :deep(h1) {
  font-size: 2rem;
}

.markdown-content :deep(h1),
.markdown-content :deep(h6) {
  text-align: center;
}
.markdown-content :deep(h6) {
  margin-top: 0;
  font-weight: 500;
  font-size: 0.7rem;
}
.markdown-content :deep(code) {
  font-family: monospace;
  background-color: var(--dark-lg);
  margin: 0;
  border-radius: 6px;
  padding: 5px;
}

.markdown-content :deep(pre code) {
  padding: 0;
}

.markdown-content :deep(pre) {
  background-color: var(--dark-lg);
  padding: 16px;
  overflow: auto;
  border-radius: 6px;
  margin-bottom: 0;
}

.markdown-content :deep(blockquote) {
  padding: 0 1em;
  color: #6a737d;
  border-left: 0.25em solid #dfe2e5;
  background-color: var(--background-color);
  margin-left: 0;
}


.markdown-content :deep(.markdown-alert) {
  padding: 1rem 1.25rem;
  margin-bottom: 1rem;
  border-left: 0.25rem solid #e2e8f0;
  border-radius: 0.25rem;
}

.markdown-content :deep(.markdown-alert-title) {
  display: flex; /* 1. Включаем Flexbox */
  align-items: center; /* 2. Выравниваем иконку и текст по вертикали */
  gap: 0.5rem; /* 3. Добавляем небольшой отступ между иконкой и текстом */
  font-weight: bold;
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

/* Стилизация для каждого типа алерта */

/* [NOTE] */
.markdown-content :deep(.markdown-alert-note) {
  border-left-color: #3b82f6; /* Blue */
  background-color: rgba(59, 130, 246, 0.1);
}

/* [COMMAND] */
.markdown-content :deep(.markdown-alert-command) {
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius-md);
  background-color: var(--dark-sm);
}
.markdown-content :deep(.markdown-alert-command .octicon) {
  color:#3b82f6;
}

/* [TIP] */
.markdown-content :deep(.markdown-alert-tip) {
  border-left-color: #22c55e; /* Green */
  background-color: rgba(34, 197, 94, 0.1);
}

/* [IMPORTANT] */
.markdown-content :deep(.markdown-alert-important) {
  border-left-color: #8b5cf6; /* Purple */
  background-color: rgba(139, 92, 246, 0.1);
}

/* [WARNING] */
.markdown-content :deep(.markdown-alert-warning) {
  border-left-color: #f97316; /* Orange */
  background-color: rgba(249, 115, 22, 0.1);
}

/* [CAUTION] */
.markdown-content :deep(.markdown-alert-caution) {
  border-left-color: #ef4444; /* Red */
  background-color: rgba(239, 68, 68, 0.1);
}

.markdown-content :deep(.markdown-alert-title .octicon) {
  fill: currentColor;
}

.markdown-content :deep(p) {
  margin: 0;
}

.markdown-content :deep(li td img) {
  width: 100%;
}
.markdown-content :deep(.markdown-alert-command td img) {
  width: 100%;
}
.markdown-content :deep(td img) {
  width: 246px;
}
.markdown-content :deep(img) {
  border-radius: var(--border-radius-md);
  margin: 1em 0
}

.markdown-content :deep(a) {
  text-decoration-color: rgba(255, 144, 0, 0.6);
  text-decoration-style: wavy;
  color: var(--text-color);
}
.markdown-content :deep(ol) {
  padding-left: 1.2em;
}
.markdown-content :deep(li::marker) {
  margin-right: 1.2em;
}


@media (max-width: 1024px) {
  /*
    Для таблиц мы добавляем возможность горизонтальной прокрутки,
    чтобы они не сжимали остальной контент и не вылезали за пределы экрана.
  */
  .markdown-content :deep(table) {
    display: block;
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch; /* Плавная прокрутка на iOS */
  }

  /*
    Это самое важное правило. Мы убираем фиксированную ширину у изображений
    и заставляем их масштабироваться под размер контейнера.
  */
  .markdown-content :deep(td img) { /* Переопределяем ваш стиль width: 246px */
    max-width: 100%;
    height: auto; /* Сохраняем пропорции изображения */
    width: auto;  /* Сбрасываем фиксированную ширину, если она была */
  }
}


/* --- ДОПОЛНИТЕЛЬНЫЕ УЛУЧШЕНИЯ ДЛЯ МОБИЛЬНЫХ ТЕЛЕФОНОВ --- */
@media (max-width: 768px) {
  /* Уменьшаем отступы у заголовков, чтобы сэкономить вертикальное пространство */
  .markdown-content :deep(h1),
  .markdown-content :deep(h2) {
    margin-top: 20px;
    margin-bottom: 12px;
  }

  /* Делаем шрифт заголовков чуть меньше */
  .markdown-content :deep(h1) {
    font-size: 1.8rem;
  }
  .markdown-content :deep(h2) {
    font-size: 1.5rem;
  }

  /* Уменьшаем боковые отступы у блоков с цитатами и уведомлениями */
  .markdown-content :deep(blockquote) {
    padding: 0 0.8em;
    border-left-width: 0.2em;
  }

  .markdown-content :deep(.markdown-alert) {
    padding: 0.8rem 1rem;
  }

  /* Уменьшаем отступы у блоков с кодом */
  .markdown-content :deep(pre) {
    padding: 12px;
  }
}
</style>