# NewsPaper
D2.9. Итоговое задание

Файл с командами (tasks.txt) в корневой папке, а так же в папке NewsPaper


D3.6 Итоговое задание

+ 1) Создать новую страницу с адресом /news/, на которой должен выводиться список всех новостей.
+ 2) Вывести все статьи в виде заголовка, даты публикации и первых 20 символов текста.
Новости должны выводиться в порядке от более свежей к самой старой.
+ 3) Сделать отдельную страницу для полной информации о статье /news/<id новости>.
На этой странице должна быть вся информация о статье.
Название, текст и дата загрузки в формате день.месяц.год.
+ 4) Написать собственный фильтр censor, который заменяет буквы нежелательных слов 
в заголовках и текстах статей на символ «*».
+ 5) Все новые страницы должны использовать шаблон default.html как основу.

D4.7 Итоговое задание

+ 1) Добавьте постраничный вывод на /news/, чтобы на одной странице было не больше 10 новостей и 
были видны номера лишь ближайших страниц, а также возможность перехода к первой или последней странице.
+ 2) Добавьте страницу /news/search. На ней должна быть реализована возможность искать новости 
по определённым критериям. Критерии должны быть следующие:
 - по названию;
 - по тегу;
 - позже указываемой даты.
+ 3) Убедитесь, что можно выполнить фильтрацию сразу по нескольким критериям.
+ 4) Запрограммируйте страницы создания, редактирования и удаления новостей и статей. 
Предлагаем вам расположить страницы по следующим ссылкам:
 - /news/create/
 - /news/<int:pk>/edit/
 - /news/<int:pk>/delete/
 - /articles/create/
 - /articles/<int:pk>/edit/
 - /articles/<int:pk>/delete/

D5.6 Итоговое задание

+ 1) В классе-представлении редактирования профиля добавить проверку аутентификации.
+ 2) Выполнить необходимые настройки пакета allauth в файле конфигурации.
+ 3) В файле конфигурации определить адрес для перенаправления на страницу входа в систему и 
адрес перенаправления после успешного входа.
+ 4) Реализовать шаблон с формой входа в систему и выполнить настройку конфигурации URL.
+ 5) Реализовать шаблон страницы регистрации пользователей.
+ 6) Реализовать возможность регистрации через Google-аккаунт(сделал через GitHub).
+ 7) Создать группы common и authors.
+ 8) Реализовать автоматическое добавление новых пользователей в группу common.
+ 9) Создать возможность стать автором (быть добавленным в группу authors).
+ 10) Для группы authors предоставить права создания и редактирования объектов модели Post (новостей и статей).
+ 11) В классах-представлениях добавления и редактирования новостей и статей добавить проверку прав доступа.
+ 12) Исходный код залить в git-репозиторий. 