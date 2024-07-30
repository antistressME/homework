# Создание банковского виджета

Этот виджет показывает несколько последних успешных банковских операций клиента.

## Инструкция по установке

Для установки проекта введите в командную строку команду ` git clone git@github.com:antistressME/homework.git `.
Обратие внимание, что для связи локального и удолённого репозиториев используется SSH-ключ.

## Зависимости проекта

В данной программе используются зависимости для редактирования проекта. 
Также в качестве удалённого репозитория используется GitHub. 
Ниже вы найдёте названия и настройки зависимостей.

### Poetry

[tool.poetry]
name = "antipina-anastasia"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"


[tool.poetry.group.lint.dependencies]
flake8 = "^7.1.0"
mypy = "^1.10.1"
black = "^24.4.2"
isort = "^5.13.2"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

### Flake8

[flake8]
max-line-length = 119
ignore = E203, W503
exclude = .git, __pycache__, venv, .venv

### Mypy

[tool.mypy]
disallow_untyped_defs = true
no_implicit_optional = true
warn_return_any = true
exclude = 'venv'

### Black

[tool.black]
line-length = 119
exclude = '''
(
  /(
      \.eggs
    | \.git
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | dist
  )/
)
'''

### Isort

[tool.isort]
line_length = 119

## Применение функций

1. ` get_mask_card_number() ` создаёт маску карты
2. `get_mask_account()` создаёт маску банковского счёта
3. `mask_account_card()` принимает или номер карты, или номер счёта и возвращает маску
4. `get_date()` обновляет формат даты
5. `filter_by_state()` фильтрует список словарей по значению индекса state.
6. `sort_by_date()` соритует список словарей по значению индекса date.

## Применение итераторов

1. `filter_by_currency()` фильтрует транзакции по указанной валюте.
2. `transaction_descriptions()` выводит описание транзакции
3. `card_number_generator()` генерирует номер карты в указанном диапозоне

## Декораторы

В модуле `decorators.py` содержится декоратор, логирующий работу функции.
Декоратор `log` может принимать необязательный параметр, передающий название файла,
в который будут записаны логи работы функции. Если его не передать, то результат будет выведен в консоль.

## Тестирование

Тестирование осуществлено через Pytest.
Для установки нужно ввести функицию:
` poetry add --group dev pytest`

Тесты можно найти в директории tests. 
Каждому модулю с функциями соотвествует модуль из test/ 
с таким же названием, но начинающимся с test_

В тестах используются фикстуры, которые расположены в модуле conftest.py

