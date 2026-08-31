# Design partner guide

## Для кого это

Design partner — независимый product-консультант, небольшая product/design/marketing-студия или founder-led B2B-команда, которая готова применить workflow к одному реальному объекту и честно сказать, где он не сработал. Это **не** beta-тест SaaS, не бесплатный аудит с обещанным результатом и не предложение передать доступ ко всем системам.

> Цель совместного run: выяснить, помогает ли pack отделить market evidence от object proof и назвать следующий недостающий факт. Цель не в том, чтобы получить «да, продукт готов», список лидов или гарантию PMF.

## Формат участия

| Этап | Что делает design partner | Что даёт проект | Результат |
|---|---|---|---|
| 1. Выбор объекта | Выбирает один продукт, ставку или market-entry question. | Помогает сформулировать research unit и границы. | Короткий object card. |
| 2. Внешний контур | Указывает публичные каналы объекта; собирает/проверяет sources. | Даёт channel inventory, alternative map и правила evidence ledger. | Pack с object, buyer и alternative сторонами. |
| 3. Evidence gaps | При необходимости предоставляет минимальный обезличенный export под конкретное утверждение. | Показывает, какие утверждения уже поддержаны и что ещё блокирует verdict. | Hypothesis map и diagnostic report. |
| 4. Review | Отмечает непонятные шаги, ложные сигналы, пустые поля и лишнюю работу. | Фиксирует failure mode как issue/улучшение template или validator. | Короткая de-identified learning note. |

Один run обычно ограничивается одним рынком, одной ролью/ситуацией и одним решением, которое нужно проверить. Если вопросов пять, сначала выберите тот, который сильнее всего меняет ближайшее бизнес-решение.

## Что нужно принести

Нужны публичная ссылка на объект либо согласованное описание, текущий business question, известные alternatives и доступные публичные каналы. Если внешний контур обнаружит пробел, полезен минимальный **обезличенный** export, например invoice cohort, source-to-conversation table или category-level support tags. Не нужен raw CRM dump.

| Вопрос | Достаточный private input, если без него нельзя | Не требуется |
|---|---|---|
| Есть ли paid exchange? | Date, segment, amount/plan, paid/refunded. | Имя, email, phone, notes клиента. |
| Есть ли completed outcome? | Cohort/segment, completion event, period. | Полная event stream или device ID. |
| Есть ли channel fit? | Source, role/segment, stage, outcome, period. | Контактный список или message content. |
| Есть ли delivery economics? | Job type, delivery time, support/cost band. | Доступ к production systems или банковским данным. |

## Privacy и публикация

Не присылайте credentials, API keys, browser sessions, личные контакты, customer messages, invoices с PII или полный CRM/analytics export. Project не будет публиковать реальный pack, название компании, source screenshots или подробности private data без вашего отдельного письменного разрешения. По умолчанию публичным может стать только de-identified lesson: например, «один template не различал pricing page и paid transaction».

Вы сами сохраняете права на данные и решения для своего бизнеса. Maintainer вправе использовать **обобщённую, обезличенную** обратную связь для улучшения docs, templates, validator, fixtures и roadmap проекта. Любая публикация идентифицирующего case требует отдельного согласования содержания, attribution и лицензии.

## Как понять, что run был полезен

Полезный run не обязан улучшить verdict. Он полезен, если он: разделил утверждение объекта и независимое evidence; выявил хотя бы один конкретный evidence gap; заблокировал необоснованное утверждение о готовности; либо сделал workflow/template заметно проще и точнее для следующего пользователя.

## Как присоединиться

Откройте issue с кратким описанием anonymized use case и выберите template `Research workflow improvement`, либо свяжитесь с Виктором через [сайт «восприятие»](https://vospri9tielandingpage.vercel.app/). В первом сообщении достаточно указать: тип объекта, вопрос, публичные каналы и готовы ли вы дать обезличенный export при необходимости. Не отправляйте private data до явного согласования нужного поля и способа передачи.
