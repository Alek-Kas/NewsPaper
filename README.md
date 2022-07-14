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
