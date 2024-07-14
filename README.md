# Создание банковского виджета

Этот виджет показывает несколько последних успешных банковских операций клиента.

## Применение функций

1. ` get_mask_card_number() ` создаёт маску карты
2. `get_mask_account()` создаёт маску банковского счёта
3. `mask_account_card()` принимает или номер карты, или номер счёта и возвращает маску
4. `get_date()` обновляет формат даты
5. `filter_by_state()` фильтрует список словарей по значению индекса state.
6. `sort_by_date()` соритует список словарей по значению индекса date.
