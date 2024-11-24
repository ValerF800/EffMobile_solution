#Library books app
##Консольное приложение для работы с файлом книг
###Возможности
<ul>
 <li>Добавлять новую книгу <i>add</i></li>
 <li>Отображать все книги <i>display</i></li>
 <li>Удалять книгу по id <i>delete -d id</i></li>
 <li>Изменять статус книги по id <i>change -i id</i></li>
 <li>Поиск книг по полям <i>search -q text</i></li>
</ul>

##Как работать с программой
###В командной строке <i>python books.py [опция: add, display, delete, change, search] [ключ: -i, -q]</i>
###Пример
<h4><i>python books.py delete -i 3</i> - удаление книги с id 3</h4>
<h4><i>python books.py search -q Valeriy</i> - поиск книг, где присутствует слово Valeriy</h4>
<h4><i>python books.py display</i> Отображение всех книг</h4>
<h4><i>python books.py add</i> Будет предложено ввести данные для новой книги, а именно title, author и year.
Книга добавится когда все поля будут введены корректно.</h4>
