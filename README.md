# Сервис уведомлений
Cервис управления рассылками API администрирования и получения статистики.

## Описание

Необходимо реализовать методы создания новой рассылки, просмотра созданных и получения статистики по выполненным рассылкам.
Реализовать сам сервис отправки уведомлений на внешнее API.
Опционально вы можете выбрать любое количество дополнительных пунктов описанных после основного.

### Как запустить dev-версию
Скачайте код:
```sh
git clone https://github.com/ZusmanOne/notification_service.git
```

Перейдите в каталог проекта:
```sh
cd notification_service
```
[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`

Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```
Настройка: создать файл `.env` в каталоге `notification/` со следующими настройками:

- `DEBUG` — дебаг-режим. Поставьте `True`.
- `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. 
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `TOKEN` — предоставляется индивидуально.
- `URL_REDIS` - значение вашего redis-аккаунта в формате 'redis://:YOURpassword@YOURpublicendpoint/0'
-  используйте sqlite3 если не требутеся создавать собственную БД
- `DB_NAME` - имя бд
- `DB_USER`- имя юзера
- `DB_PASSWORD`- пароль юзера
- `DB_PORT`=5432
- `DB_HOST` - localhost

Применить миграции

```sh
python manage.py migrate
```

Запустить сервер
```sh
python manage.py runserver
```

Запустить celery
```
celery -A notification  worker -l INFO
```
```http://127.0.0.1:8000/api``` - api проекта

```http://127.0.0.1:8000/api/clients/``` - клиенты

```http://127.0.0.1:8000/api/clients/<pk>``` - детальная информация оп клиенту

```http://127.0.0.1:8000/api/distributions/``` - рассылки

```http://127.0.0.1:8000/api/statistic/``` - общая статистика по всем рассылкам

```http://127.0.0.1:8000/api/distributions/<pk>/mailing_messages/``` - детальная статистика по конкретной рассылке



***
## Запуск тестов
``` 
python manage.py test
```
### Сервис так же обернут в докер, что бы запустить проект в докере наберите команду:

``` 
docker-compose -f docker-compose.yml up  --build
```
###  Описание разработанного API в Swagger

```http://127.0.0.1:8000/swagger``` 

```http://127.0.0.1:8000/docs/``` 


