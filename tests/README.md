# Запуск тестов
## Тесты запускать, находясь в папке tests
```
pytest -v -m registration # тесты на регистрацию
pytest -v -m authorization # тесты авторизации
pytest -v -m exist # тесты существует/несуществует пользователь
pytest -v -m profile # тесты получения данных о профиле
pytest -v -m update # тесты на изменение имени в профиле
```