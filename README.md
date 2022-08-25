# Сайт для поиска интересных мест в Москве 
## Главная сайта
![Главная страница сайта](https://user-images.githubusercontent.com/83189636/184546093-c0a0af23-70b8-4dbd-a3e8-b2f88a86e355.png)

На главной странице сайта вы увидите карту Москвы, на которой находятся маркеры. Нажав на этот маркер вы перейдёте к описанию места (на скриншоте слева).
Там вы можете почитать о выбранном месте и посмотреть фотографии с него.

[Ссылка на работающий сайт](https://callmeishimura.pythonanywhere.com/) - https://callmeishimura.pythonanywhere.com/

Сайт без проблем работает как на смартфонах, так и на вашем компьютере.

## Хочу такой же
Вы можете настроить сайт под себя и наполнить его выбранным вами контентом.
Для этого:
* Cкачайте этот репозиторий с Github (нажмите на зелёную кнопку ```code``` или воспользуйтесь Github Desktop).
* Перейдите в рабочую директорию.
* Установите виртуальное окружение при помощи команды ниже:
``` sh
python3 -m venv venv
```
И активируйте его.
``` sh
source venv/bin/activate
```
* Установите необходимые зависимости.

``` sh
pip install -r requirements.txt
```
* Настройте переменные окружения
Для этого создайте рядом с файлом ```manage.py``` папку ```.env``` и добавьте все необходимые данные, а именно:

  [ALLOWED_HOSTS](https://docs.djangoproject.com/en/4.1/ref/settings/#allowed-hosts)

  [SECRET_KEY](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-SECRET_KEY)

  [DEBUG](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-DEBUG)

  [MEDIA_ROOT](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-MEDIA_ROOT)

  [MEDIA_URL](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-MEDIA_URL)

  [STATIC_URL](https://docs.djangoproject.com/en/4.1/ref/settings/#static-url)

  [STATIC_ROOT](https://docs.djangoproject.com/en/4.1/ref/settings/#static-root)
  
* Если вы собираетесь деплоить этот сайт, то также стоит добавить:

  [SESSION_COOKIE_SECURE](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-SESSION_COOKIE_SECURE)

  [CSRF_COOKIE_SECURE](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-CSRF_COOKIE_SECURE)

  [SECURE_HSTS_SECONDS](https://docs.djangoproject.com/en/4.1/ref/settings/#secure-hsts-seconds)

  [SECURE_HSTS_INCLUDE_SUBDOMAINS](https://docs.djangoproject.com/en/4.1/ref/settings/#secure-hsts-include-subdomains)

  [SECURE_HSTS_PRELOAD](https://docs.djangoproject.com/en/4.1/ref/settings/#secure-hsts-preload)

  [SECURE_CONTENT_TYPE_NOSNIFF](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-SECURE_CONTENT_TYPE_NOSNIFF)

Пример готового ```.env``` файла

``` bash
DEBUG=True
ALLOWED_HOST=['localhost',]
SECRET_KEY='REPLACE_ME'
STATIC_URL='/static/'
STATIC_ROOT='static/'
MEDIA_URL='/media/'
```

Примеры использования [os](https://python-scripts.com/import-os-example) - https://python-scripts.com/import-os-example

Документация к [environs](https://pypi.org/project/environs/) - https://pypi.org/project/environs/
* Примените все миграции.
``` sh
python3 manage.py migrate
```
* Добавьте админа.
``` sh
python3 manage.py createsuperuser
``` 
После этого шага вы можете зайти в админку.
Для этого в адресной строке сайта необходимо написать:
```sh
http://127.0.0.1:8000/admin
```
Или же просто нажав [сюда](http://127.0.0.1:8000/admin).
И ввести данные, которые вы вписывали при регистрации админа.
После вас встречает панель администратора.
![Админка](https://user-images.githubusercontent.com/83189636/184547000-490b9026-9ca4-48d5-bcac-7acab335d2a0.png)
Теперь пришло время наполнить сайт контентом.
Здесь есть два возможных варианта:
* Сделать всё в ручную при помощи панели администратора.
* Воспользоваться командой ```load_place```.

Давайте разберём каждый из них пошагово.

### Добавление через панель администратора
Для этого необходимо перейти во вкладу ```Event``` и в левом верхнем углу нажать на ```Add Event```
Вас встречает такое окно, в которе необходимо добавить данные.
Здесь вы можете добавить фотографии (в самом низу страницы).
![Окно добавления ивента](https://user-images.githubusercontent.com/83189636/184547348-d3433243-5c5b-402f-bf39-2aa7a7f09f10.png)
После добавления всех данных нажимаем кнопку ```Save``` и видим, что на карте появилась метка.

Фотографии также можно добавить и в разделе ```Images```.
Для этого переходим в него и в левом верхнем углу нажимаем ```Add Image```.
![Окно добавления фото](https://user-images.githubusercontent.com/83189636/184547817-83ddfdb9-6744-49cc-9993-c6cce6a419d8.png)
Здесь необходимо выбрать нужное мероприятие из списка и добавить фото.

### Добавление через команду
Для этого просто прописываем в консоли следующую команду:
``` sh
python manage.py load_place (ссылка на данные в формате json)
```
Второй метод куда быстрее и удобнее =).

## Откуда брать данные?
Данные для проекта были взяты [здесь](https://github.com/devmanorg/where-to-go-places).
Там же есть гайд по тому, откуда брать нужные файлы.

## Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/).

Тестовые данные взяты с сайта [KudaGo](https://krd.kudago.com/).
