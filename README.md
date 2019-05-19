# Web-app for streaming new music from SoundCloud and Bandcamp
___________________________________________

![Превью](https://pp.userapi.com/c851132/v851132165/1284b1/58bhzTCdwvM.jpg)
______________________________________________________________________________
### The requirements to start the app:
- Install, create and connect PostgreSQL data base(follow the PostgreSQL tutorial)
- Install all required modules from requirements.txt(Don't forget to use venv)
- In the root directory of repo create configuration file config.py, which consists from:
    - *class Config
    - *in the class you must add all configurations and settings of your data base and SQLAlchemy
    - *SC_API_MAINPAGE -- the url to json the main page of SoundCloud
    - *BC_API -- the list of urls to json the main page of BandCamp(to various genres)

P.S.: If you have the issues to find the urls to json, feel free to ask us! :)

### You can start the app from the terminal by using this script:

Linux and Mac: export FLASK_APP=webapp && export FLASK_ENV=development && flask run

Windows: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

### OR you can use the file run.sh to start the app.


## PLEASE, NOTE: The project is on the stage of under development.

_____________________________________________________

### In the project we are going to realize the following tasks:
- [ ] Create front-end;
- [ ] Make the opportunity for users to create their list of favorite tracks;
- [ ] Make the opportunity for users to create their playlists;
- [ ] Write our own audio player;
- [ ] More new music: make the opportunity for users to add their own music and share it with another users.


### If you have any issues, please feel free to contact us by the email:
alexnemcev@mail.ru, xcrsx@icloud.com (or by the Telegram: @Gullkin, @xcrsx)


# Проект веб-сервиса по стримингу свежей музыки
___________________________________________
### Стриминг новой музыки с сайтов Bandcamp и Soundcloud
______________________________________________________________________________
### Для запуска проекта необходимо:
- Установить, подключить и создать базу данных PostgrteSQL (по официальному мануалу)
- Подключить к проекту необходимые модули из requirements.txt (Вы можете использовать виртуальное окружение, не забудтье позаботиться об этом)
- В корневом каталоге репозитория создать файл конфигурации config.py, который содержит:
    - *class Config (italic)*
    - *в class Config добавляются все конфигурации и настройки базы данных и SQLAlchemy (italic)*
    - *SC_API_MAINPAGE - ссылка на json главной страницы Soundcloud (italic)*
    - *BC_API - список ссылок на json главной страницы Bandcamp (по различным жанрам) (italic)*

P.S. Если Вы не смогли обнаружить json ссылки, Вы можете обратиться к нам за помощью

### Проект можно запускать из консоли командой 
Linux и Mac: export FLASK_APP=webapp && export FLASK_ENV=development && flask run

Windows: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

### ИЛИ
### Использовать файл run.sh для запуска приложения

## ВНИМАНИЕ: Проект находится в стадии разработки
_____________________________________________________
### В рамках проекта будут реализованы следующие задачи:
- [ ] Создадим frontend часть проекта
- [ ] Реализуем возможность добавления пользователями композиций в "избранное"
- [ ] Сделаем добавление и создание собственных плейлистов
- [ ] Напишем интересный музыкальный плеер для более комфортного прослушивания музыки
- [ ] ЕЩЕ БОЛЬШЕ НОВОЙ МУЗЫКИ: Добавить возможность пользователям добавлять свою собственную музыку и делиться ею с другими пользователями

#### Если у вас возникли вопросы, вы всегда можете связаться с нами по почте
alexnemtsev@mail.ru, xcrsx@icloud.com (или в Телеграмм: @Gullkin, @xcrsx)

