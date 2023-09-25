# Currency Converter

Приложение для отслеживания хороших привычек.

## Стэк

![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=green)
![](https://img.shields.io/badge/Framework-DRF-informational?style=flat&logo=Django&logoColor=white&color=green)
![](https://img.shields.io/badge/Tools-Requests-informational?style=flat&logo=requests&logoColor=white&color=green)
![](https://img.shields.io/badge/database-Postgresql-informational?style=flat&logo=postgresql&logoColor=white&color=green)
![](https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=white&color=green)
![](https://img.shields.io/badge/Broker-Celery-informational?style=flat&logo=celery&logoColor=white&color=green)
![](https://img.shields.io/badge/Broker-Celery_beat-informational?style=flat&logo=celery&logoColor=white&color=green)
![](https://img.shields.io/badge/Cache-Redis-informational?style=flat&logo=redis&logoColor=white&color=green)

## Установка

1. Клонируйте репозиторий на свой компьютер:

   ```
   git@github.com:Heattehnik/good_habits_tracker.git
   ```

2. Создайте файл `.env` в корне приложения, используя образец из `.env_sample`.

3. Запустите приложение из каталога с приложением:

   ```
   docker-compose build
   docker-compose up -d
   ```

5. Приложение будет доступно по адресу `0.0.0.0:8000`.


## MISC

Приложение было протестировано со переменными окружения:

- `DB_NAME='postgres'`
- `DB_USER='postgres'`
- `DB_PASSWORD='postgres'`

