# Протокол внешнего исследования для диагностики жизнеспособности бизнес-модели

## Зачем нужен этот контур

Внутренние данные владельца отвечают на вопрос «что произошло у нас». Внешний контур отвечает на другой вопрос: **какой рынок уже существует вокруг этой работы, чем люди решают её сейчас и есть ли у объекта право ожидать переключения на себя**.

Без обоих контуров verdict запрещён:

| Есть только | Что получится | Почему недостаточно |
|---|---|---|
| Лендинг/презентация объекта | Self-description | Компания сама выбирает, что назвать проблемой, сегментом и ценностью. |
| Внутренние метрики | Локальный результат | Можно не увидеть, что альтернативы дешевле/сильнее или что сегмент меняет способ решения. |
| Внешние источники | Market map | Нельзя подтвердить свой retention, money/delivery или реальный outcome без private data. |

## Исследовательская единица

Не «компания» и не «рынок». Единица исследования формулируется так:

> **[Роль] в [ситуации] пытается [выполнить работу / избежать потери] и сейчас использует [текущую альтернативу]. Объект предлагает [изменение результата/стоимости/усилия].**

Вымышленный пример: веб-студия, ведущая несколько клиентских сайтов на конструкторе, хочет снять platform lock-in и перенести сайт без потери форм. Сейчас она делает это вручную, оставляет сайт на платформе или покупает миграционную услугу.

## Шесть обязательных объектов внешнего исследования

| Объект | Вопрос | Минимальное доказательство | Источники |
|---|---|---|---|
| 1. Current alternative | Как задача реально решается без объекта? | 2–3 наблюдаемых способа: DIY, incumbent, агентство, spreadsheet, отказ от действия. | Competitor docs/pricing, user discussions, freelance marketplaces, app-store comparisons. |
| 2. Direct competitors | Кто решает тот же job для той же роли и контекста? | 3 closest alternatives; если их нет — доказать category gap, а не заявить «конкурентов нет». | Search, category pages, marketplaces, industry directories, app stores. |
| 3. Competitive claims | За что рынок уже просит/берёт деньги? | Price, unit, onboarding, SLA, integrations, paid plan/contract. | Official pricing/docs, partner pages, case studies. |
| 4. External demand traces | Что люди делают, когда проблема появляется? | Complaint with workaround, comparison/search, review, migration, hiring, request for service, paid transaction. | Reviews, forums, social, jobs, app stores, GitHub/issues, public procurement. |
| 5. Switching friction | Почему люди остаются с альтернативой? | Lock-in, data migration, team training, incumbent bundle, risk of failure, regulation. | Negative reviews, docs, comparison discussions, migration guides. |
| 6. Object-specific proof | Что этот объект уже доказал лучше альтернативы? | Independent review/case/usage signal; otherwise explicit `external_object_proof_missing`. | Third-party cases/reviews, marketplace metrics, partner mentions, public integrations. |

## Правило близости конкурента

Конкурент входит в основное сравнение, только если совпадают минимум два из трёх признаков:

1. тот же job/context;
2. тот же buyer/роль;
3. тот же тип обмена ценностью — продукт, услуга или paid workflow.

Большой бренд из соседней категории не должен маскировать отсутствие прямого сравнения.

## Классы внешних источников

| Класс | Примеры | Сила | Ограничение |
|---|---|---|---|
| Независимое поведение | Reviews, rankings, installs + review behavior, public migration, job post, payment marketplace | Выше | Метрика может быть неполной и не объясняет мотивацию. |
| Независимый рассказ | Форум, обсуждение, публичный case от клиента, медиа с проверяемым клиентом | Средняя | Может быть нерепрезентативен или спонсирован. |
| Коммерческая реальность конкурента | Pricing, contract terms, integration docs, public SLA | Средняя для market structure | Доказывает offer конкурента, не его usage. |
| Self-claim объекта | Лендинг, launch-пост, founder quote | Низкая | Годится только как claim, который нужно проверить. |

## Минимальный research pack до verdict

| Артефакт | Обязательные поля |
|---|---|
| Object card | Product, role, situation/job, offered change, business model, stage, claim sources. |
| Alternative map | Current DIY/doing-nothing + 3 closest competitors + why each is relevant. |
| Competitive ledger | Competitor, job, buyer, pricing unit, onboarding/switching friction, claim source. |
| External evidence ledger | Evidence, source class, URL, date, which claim it supports, alternative explanation. |
| Evidence gap register | Какая ключевая область не имеет external proof и какие private data нужны от owner. |

## Stop conditions

Не делать market-readiness verdict и не говорить «конкурентов нет», если:

- объект исследования не сведен к role + situation + job;
- не найдено хотя бы 3 альтернативы или нет объяснения, почему поиск категорийно пуст;
- у внешнего evidence нет source URL/происхождения;
- self-claim использован как независимое доказательство;
- не выделены switching costs и current workaround.
