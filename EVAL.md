# Eval — Market Evidence Diagnostic на реальных кейсах

Диагностика проверена на **6 реальных кейсах** рыночного окружения.

## Результаты

| Кейс | Вердикт | Уверенность | Незав. источников |
|---|---|---|---|
| Profi.ru (2 независимых) | switch_supported | medium | 2 |
| Profi.ru (само-заявление) | switch_hypothesis_testable | low | 0 |
| Skyeng (outcome-claim) | switch_hypothesis_testable | low | 0 |
| EdTech (независимый рейтинг) | switch_supported | medium | 2 |
| Противоречие в отзывах | switch_contradicted | medium | 1 |
| Стартап без данных | not_testable | low | 0 |

## Что учитывает

| Правило | Как работает |
|---|---|
| Независимое наблюдение | `supported` требует внешнего подтверждения, а не заявления компании |
| **Правило одного источника** | 1 независимый locator → вердикт не выше гипотезы |
| Направление наблюдения | источник должен явно указывать, **что** он поддерживает — иначе не считается |
| Противоречия | независимое наблюдение против заявления → `switch_contradicted` |
| Уровни вердикта | `not_testable` → `switch_hypothesis_testable` → `switch_supported` → `switch_contradicted` |
| Уверенность | `high` требует 4+ источников, из них 3+ независимых |
| Adversarial self-check | обязателен: какой вывод был бы без сверки и чем грозил |

## Что показывают реальные данные

- **Само-заявление не подтверждает ничего.** Skyeng («89% достигают цели за 30
  уроков») получает `switch_hypothesis_testable` / `low` — это маркетинг, не факт.
- **Два независимых источника поднимают вердикт.** Отзывы + независимый рейтинг →
  `switch_supported` / `medium`.
- **Противоречие фиксируется отдельно.** Отзывы против заявления → `switch_contradicted`.

## Границы

- Метод не заменяет маркетинговое исследование — он показывает, **чего не хватает**
  для безопасного решения.
- Red-team набор: `python skill/scripts/test_adversarial.py` — 6/6 сценариев завышения.

## Проверка

```bash
git clone https://github.com/r0undm1dn1ghty-star/market-evidence-diagnostic && cd market-evidence-diagnostic
python integrations/kit/skillkit.py --json --input \
  '{"claims":{"headline":"GMV +40%"},"evidence":[{"source":"otzovik","source_class":"independent_behavior","supports":1},{"source":"markswebb","source_class":"independent_third_party","supports":1}]}'
# -> switch_supported, medium, 2 независимых
```
