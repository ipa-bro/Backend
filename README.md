# Backend
## Общий план
- [ ] Основа
- [ ] БД
- [ ] Роуты
- [ ] Докер
- [ ] Асинхронность
- [ ] Кеширование
- [ ] Оптимизация
- [ ] Тестирование
- [ ] Админ-панель
- [ ] Оптимизация
- [ ] Тестирование
- [ ] Модуль платежка
- [ ] Тестирование
- [ ] Подготовка к деплойменту

## Методические рекомендации
- После клонирования создавать ветку со своим ником в ТГ
- Трбется наличие дополнительных ПО: PostgreSQL, PGadmin4, Redis + Docker
- В корне backend сделать файл `.env`

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_DB=fastapi
POSTGRES_PORT=5432

SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
SMTP_USER=aaaagmail.com
SMTP_PASS=qwerty

EMAIL_TO=test@mail.com

REDIS_HOST=localhost
REDIS_PORT=6379
```
- Добавить туда свои данные БД для сверки работы
- Если разработка ведется в VS Code, то тыкайте на файл `requirements.txt` и соглашайтесь с установкой виртуального окружения, если вы используйте PyCharm или иные среды разработки, тогда в командной строке прописывайте команду из корня `pip install -r requirements.txt`
- Для запуска проекта из корня введите команду `uvicorn app.main:app --reload`

