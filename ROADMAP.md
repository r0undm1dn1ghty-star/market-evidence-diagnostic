# Roadmap

Roadmap показывает, что проект намерен проверить. Он не является обещанием delivery date, managed service или готовых integration.

| Этап | Цель | Проверяемый результат | Что сознательно не строим |
|---|---|---|---|
| `0.3.x` — field learning | Проверить workflow на реальных design-partner packs. | 3–5 de-identified outcome notes; два improvement PR по реальным failure modes. | SaaS dashboard, массовый outbound, universal business score. |
| `0.4.x` — source adapters | Добавить documentation/templates для наиболее повторяемых public/file adapters. | Один public-source adapter guide и один anonymized file-export example с tests. | OAuth/API integration без user demand и security review. |
| `0.5.x` — usability | Проверить Quickstart без сопровождения maintainers. | Внешний user создаёт valid pack и понятный issue/feedback. | Переписывание методологии ради более красивой терминологии. |
| `1.0.0` — stable open-source skill | Зафиксировать стабильный workflow, templates и compatibility. | 5+ reviewed packs, documented limitations, accepted contributor/security policy. | Гарантии PMF, revenue, lead generation или market success. |

## Критерий выбора следующей фичи

Фича имеет смысл только если она закрывает повторяющийся evidence gap в нескольких реальных packs, не требует secret/private access по умолчанию и не превращает проект в black-box advisor. Prioritize provenance, source coverage, privacy and reproducibility over automation volume.
