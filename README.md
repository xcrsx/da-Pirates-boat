# Проект веб-сервиса по стримингу музыки
___________________________________________
### Стриминг новой музыки с сайтов Bandcamp и Soundcloud
![Превью](https://pp.userapi.com/c851132/v851132165/1284b1/58bhzTCdwvM.jpg)
______________________________________________________________________________
### Для запуска проекта необходимо:
- Установить, подключить и создать базу данных PostgrteSQL (по официальному мануалу)
- Подключить к проекту необходимые модули из requirements.txt
- В корневом каталоге репозитория создать файл конфигурации config.py, который содержит:
    - *class Config (italic)*
    - *в class Config добавляются все конфигурации и настройки базы данных и SQLAlchemy (italic)*
    - *SC_API_MAINPAGE - ссылка на json главной страницы Soundcloud (italic)*
    - *BC_API - список ссылок на json главной страницы Bandcamp (по различным жанрам) (italic)*
### Проект можно запускать из консоли командой 
Linux и Mac: export FLASK_APP=webapp && export FLASK_ENV=development && flask run
Windows: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
### ИЛИ
### Использовать файл run.sh для запуска приложения
