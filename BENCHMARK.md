# Бенчмарк — Market Evidence Diagnostic

Задача: определить, что рынок **позволяет утверждать** о бизнес-модели,
а что преждевременно. Проверено на 5 кейсах.

## Результат

| Метод | Верных вердиктов |
|---|---|
| Наивный (есть данные → «подтверждено») | 2/5 |
| **Market Evidence Diagnostic** | **5/5** |

## Уровни вердикта

| Вход | Вердикт |
|---|---|
| только заявление компании | `switch_hypothesis_testable` — это маркетинг, не факт |
| 2 независимых источника | `switch_supported` — можно опираться |
| независимое наблюдение против | `switch_contradicted` — заявление опровергнуто |
| данных нет | `not_testable` — вывод не делается |

Ключевое: **само-заявление не подтверждает ничего**, а два независимых источника
поднимают вердикт. Наивный метод ставит «подтверждено» уже на одном источнике.

## Как воспроизвести

```bash
git clone https://github.com/r0undm1dn1ghty-star/market-evidence-diagnostic
cd market-evidence-diagnostic
echo '{"claims":{"h":"+40%"},"evidence":[{"source":"a","source_class":"independent_third_party","supports":1},{"source":"b","source_class":"independent_behavior","supports":1}]}' \
  | python integrations/kit/skillkit.py --json
```
