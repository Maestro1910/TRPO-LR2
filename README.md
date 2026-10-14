# Calc — учебный калькулятор (ЛР №2, CI/CD)

Библиотека `calc` с базовыми арифметическими операциями.

## Установка и запуск

```
pip install -r requirements.txt
python main.py
```

## API

| Функция | Описание |
|---|---|
| `add(a, b)` | сумма `a + b` |
| `sub(a, b)` | разность `a - b` |
| `mul(a, b)` | произведение `a * b` |
| `div(a, b)` | частное `a / b`, при `b == 0` — `ZeroDivisionError` |
| `power(a, n)` | возведение `a` в степень `n` |

## Тесты

```
python -m pytest -v
```

## CI/CD

- `.github/workflows/main.yml` — проверка кода flake8 и unit-тесты pytest при каждом push и pull request;
- автоматическое слияние PR в `main` после успешного прохождения проверки `test`;
- `.github/workflows/docs.yml` — генерация HTML-документации (pdoc) при каждом обновлении `main`,
  публикация в ветку `gh-pages` и в артефакт `docs`.
