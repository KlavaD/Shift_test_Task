# Тестовое задание на курс «Python»
## Реализуйте REST-сервис просмотра текущей зарплаты и даты следующего повышения. Из-за того, что такие данные очень важны и критичны, каждый сотрудник может видеть только свою сумму. Для обеспечения безопасности, вам потребуется реализовать метод где по логину и паролю сотрудника будет выдан секретный токен, который действует в течение определенного времени. Запрос данных о зарплате должен выдаваться только при предъявлении валидного токена.

Проект создавала я - 
* ### Клавдия Дунаева
**Как запустить проект:**

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

**Описание команд для запуска приложения в контейнерах**

Создайте файл .env с переменными окружения:
```
ALLOWED_HOSTS=*
DB_PROD=True
DEBUG=False
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
Запустите контейнер из папки infra/
```
docker-compose up -d --build
```

Выполните следующие команды:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```


## Примеры запросов: ##
Регистрация нового пользователя:
>**POST** http://127.0.0.1/api/auth/users/

```
{ 
    "email": "vpupkin3@yandex.ru",
    "username": "vpupkin3",
    "password": "Qwert77y3123"
}
```

Для получения токена отправьте логин и пароль:
>**POST** http://127.0.0.1:8000/api/auth/jwt/create/

```
{ 
    "username": "vpupkin3",
    "password": "Qwert77y3123"
}
```

Получение актуальной зп (токен JWT):
>**GET** http://127.0.0.1/api/salary/

Занести новую зп в БД для любого пользователя (может только админ):
>**POST** http://127.0.0.1/api/salary/

```
{
    "worker": "vpupkin3",
    "sum_of_salary": 5000,
    "next_date_of_increase": "2023-06-23"
}
```
