# Веб-приложение "Магазин Котиков". Омега. ГУАП. Практика 2024.

## Технологии

- Разрабатывали в стеке Python/Flask + SQLAlchemy  ( база данных sqlite)
- Фронт написали с использованием bootstrap
- AJAX запросы для отправки данных
- Автотесты реализованы через Pytest


## Функционал

- Есть регистрация пользователей и распределения по ролям (админ и юзер, созданные аккаунты хранятся в бд)
- Гостю доступен просмотр позиций с котами
- Зарегистрированному пользователю доступен просмотр позиции и выбор позиции. (при выборе позиции выбранный кот вместе со своей позицией удаляется из бд)
- У администратора есть все права зарегистрированного пользователя + возможность добавить кота и его позицию / отредактировать существующего кота.
- Коты и соответствующие им позиции также хранятся в бд.
- Предусмотрены неправильные варианты взаимодействия пользователя с приложением (без прав админа не даст создать кота и т.д.)
- Было реализовано логирование (действия пользователей сохраняются в бд вместе с их ролью, типом действия и датой)
- Предусмотрена некорректная работа сервера (404, 401,500 - отображается отдельный html шаблон при обработке ошибочных кодов с соответствующим для них сообщением)
- Реализовано автоматизированное тестирование (осуществляются тесты создания нового пользователя, вход нового пользователя в аккаунт, добавление нового кота, редактирование созданного кота, переход по ссылке на созданного кота, удаление созданного кота.


## Скриншоты с работой приложения


Главная страница приложения:
![image](https://github.com/user-attachments/assets/1fec21a5-7cd0-4460-bc04-f34e4dd0673c)
\
Вход в аккаунт администратора:
\
![image](https://github.com/user-attachments/assets/1aed0530-a966-400a-a703-7dcedb760cc1)
\
Добавление нового кота администратором:
\
![image](https://github.com/user-attachments/assets/398c6e80-a47f-45d2-bc08-185f1c483572)
\
Варианты взаимодействия с котом с правами администратора:
\
![image](https://github.com/user-attachments/assets/75676f08-0c32-405b-9d91-ec0b73370674)
\
Редактирование кота администратором:
\
![image](https://github.com/user-attachments/assets/b8b49591-2ff5-4729-9588-d8dbcb8271e9)
\
Выбор кота с аккаунта с правами пользователя:
\
![image](https://github.com/user-attachments/assets/b92e3268-53d8-4ed2-a496-39bbaae68c97)
\
Результаты вышеперечисленных операций:
\
![image](https://github.com/user-attachments/assets/5619b17e-ca4b-4bf7-a2bd-6860fb944a4a)
\
Пример посещения пользователем несуществующей страницы (404):
\
![image](https://github.com/user-attachments/assets/9b577057-5fec-4381-bfd4-6d0646e82431)










