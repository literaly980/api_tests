# API-автотесты (pytest + requests)

Автоматизированные тесты REST API на Python. В качестве объекта тестирования —
публичный учебный API [JSONPlaceholder](https://jsonplaceholder.typicode.com/).
Проект показывает базовые навыки QA-автоматизатора: проверка статус-кодов,
структуры JSON, позитивные и негативные сценарии, тестирование CRUD-операций.

## Технологии

- Python 3
- `pytest` — фреймворк для тестов (фикстуры, параметризация)
- `requests` — HTTP-клиент
- `conftest.py` — общие фикстуры (сессия, базовый URL)

## Что проверяется

| Файл | Что тестируем |
|------|----------------|
| `test_posts.py` | GET: статус-коды, поля JSON, негативный тест 404, параметризация, вложенные ресурсы |
| `test_crud.py`  | POST (201), PUT (200), DELETE (200) |
| `test_users.py` | Валидация данных: количество, корректность email, обязательные поля |

## Запуск

```bash
pip install -r requirements.txt
pytest
```

## Пример вывода

```
tests/test_posts.py::test_get_single_post PASSED
tests/test_posts.py::test_get_all_posts PASSED
tests/test_posts.py::test_get_nonexistent_post PASSED
tests/test_crud.py::test_create_post PASSED
...
========== 11 passed ==========
```

## Заметка

Сессия настроена на прямое соединение (`trust_env=False`) — запросы идут мимо
системного прокси/VPN.
