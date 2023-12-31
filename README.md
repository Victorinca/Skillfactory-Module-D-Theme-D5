# Skillfactory Module D. Theme D5

Completed homework for Skillfactory Course: 'Python Web Developer'. Module D - 'Backend-development in Python and Django'. Theme D5 - 'Authorization and Registration in Django'.

## Репозиторий учебного проекта NewsPaper для курсов "Веб-разработчик на Python" и "Fullstack-разработчик на Python"
### [Модуль D. Тема D5 "Авторизация и регистрация в Django"](https://victorinca.github.io/Skillfactory-Module-D-Theme-D5/)

Приложение новостного портала NewsPaper, созданное с помощью Python и Django, чтобы можно было: 1) смотреть новости 2) читать статьи.

Итоговое задание по теме D5 "Авторизация и регистрация в Django" заключается в создании страниц для регистрации и входа, а также создании возможности автоматически добавлять пользователей в определенные группы.

База данных: sqlite.

Состоит из приложений news и accounts.

#### Приложение news включает в себя модели:
1) Author - авторы статей, новостей (далее - постов).
2) Category - категории постов - темы, которые они отражают (бизнес и экономика, наука и технологии, образование и вакансии, стиль жизни и здоровье и т.д.).
3) Post - посты (статьи и новости), которые создают пользователи. Каждый объект может иметь одну или несколько категорий.
4) PostCategory - промежуточная модель (явная) для связи "многие ко многим".
5) Comment - хранение комментариев к постам, оставляемых под каждой новостью/статьёй.

Все модели собраны в единый скрипт (код) в приложении news в файл models.py.

#### В качестве результата задания нужно усовершенствовать новостной портал NewsPaper.

1) Реализовать в классе-представлении для страницы редактирования новости, созданной с помощью дженерика UpdateView, проверку наличия аутентификации с помощью миксина. 
В файле настроек проекта добавить адрес, по которому Django будет перенаправлять пользователей после успешного входа в систему.

2) Используя только пакет allauth, реализовать в своём приложении NewsPaper возможность входа в систему, а также регистрации по почте или через Google-аккаунт.
Выполнить необходимые настройки пакета allauth в файле конфигурации.

3) В файле конфигурации добавить адрес для перенаправления на страницу входа, по которому перенаправится неавторизованный пользователь при попытке перейти на защищённые страницы, и адрес перенаправления после успешного входа.

4) Реализовать шаблон с формой входа в систему и выполнить настройку конфигурации URL.

5) Реализовать шаблон страницы регистрации пользователей.

6) Реализовать возможность регистрации через Google-аккаунт.

7) При помощи панели администратора Django создать две группы: 1) common - для всех пользователей и 2) authors - для авторов.

8) Реализовать автоматическое добавление новых пользователей в группу common (при регистрации пользователь должен автоматически добавляться в группу common).

9) Создать возможность стать автором: добавить кнопку "Стать автором", при нажатии на которую пользователь добавляется в группу authors.

10) Используя панель администратора предоставить права на создание, редактирование и удаление объектов модели Post (новостей и статей) для группы authors, чтобы создавать, редактировать и удалять посты могли только пользователи из группы "authors".

11) В соответствующих классах-представлениях создания, редактирования и удаления новостей и статей добавить проверку прав доступа (миксин ограничения прав), чтобы создавать, редактировать и удалять посты могли только пользователи из группы "authors".
В атрибуте классов-представлений прописать, какими правами должен обладать пользователь для доступа к этим страницам.

#### Запуск проекта

1) Создать виртуальное окружение (далее - ВО) - изолированну версию Python, которая находится у вас в папке venv:

python -m venv venv

2) Активировать ВО:

2.1) В Windows _PowerShell_ или _cmd_:

venv\sripts\activate

2.2) В Windows _GitBash_

source venv/sripts/activate

2.3) Linux, MacOS

source venv/bin/activate

3) Установить через pip

3.1) Django с активированной средой (в виртуальную среду):

python -m pip install Django

3.2) Дополнительные пакеты:

pip install django-filter

pip install django-dbbackup

pip install django-allauth

4) Перейти в папку проекта, где находится файл manage.py с помощью команды: cd название_папки, например, 

cd NewsPaper

5) Проверить, что находимся в нужной папке с помощью команды ls. Если после выполнения команды в терминале виден файл manage.py - можно запускать проект. Иначе - см. п.4. 

6) Запускаем проект командой 

python manage.py runserver

или

./manage.py runserver

Сообщение говорит нам о том, что приложение начало работу по адресу 127.0.0.1:8000.

Открываем любой браузер и переходим по адресу http://127.0.0.1:8000/.

Полезные команды:

- посмотреть список доступных команд для Django:

python manage.py help

#### Доступы в приложении - учётные записи

Панель администратора:
http://127.0.0.1:8000/admin/ 

Администратор:
- логин: admin
- пароль: admin-admin

Пользователи:
- логин: user1@mail.com
- пароль: user1-user1

- логин: user2@mail.com
- пароль: user2-user2

- логин: test1@mail.com
- пароль: test1-test1

и т.п.

- логин: test5@mail.com
- пароль: test5-test5

## Поддержать, отблагодарить автора
Если представленная работа Вам понравилась, принесла пользу, сэкономила время, то Вы можете поддержать автора, воспользовавшись различными платежными системами.
- [Поддержать автора через ЮMoney](https://yoomoney.ru/to/4100117804016773)
- [Выразить признательность через Qiwi](https://qiwi.com/n/VICTORINCA)
- [Поблагодарить автора через WebMoney](https://donate.webmoney.com/w/SChu57RhLGfYrPmXfPMdWr)
#### Благодарю Вас за щедрость!
#### Ваша поддержка и признательность очень приятны и важны!

## Ссылки

- [Ссылка на страницу проекта](https://victorinca.github.io/Skillfactory-Module-D-Theme-D5/)
- [Ссылка на GitHub](https://github.com/Victorinca/Skillfactory-Module-D-Theme-D5)
  
По всем вопросам, которые касаются выполненного задания, можно писать на почту victoriavladimirskaya@gmail.com.
