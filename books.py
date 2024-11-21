import argparse, json, os

# Определение файла с данными книг, если его нет - создается новый со счетчиком внутри
# Счетчик нужен для создания уникальных id книг.

NAME_FILE = "data.json"
if not os.path.isfile(NAME_FILE):
    with open(NAME_FILE, 'a+') as file:
        json.dump({"counter" : 0}, file)




class Book:
    def __init__(self):
        """ При новом запросе всегда открывается файл только на чтение для считывания данных"""
        self.fname = NAME_FILE
        with open(self.fname, "r") as file:
            self.data = json.load(file)
        self.book_id = self.data.pop("counter") #'Выдергиваем' счетчик, чтобы дальше он не мешал.

        self.check_data = {"title": str.isalnum,
                            "author": str.isalpha,
                            "year": str.isdigit} # Поля и их методы для проверки введенных данных

    def add(self):
        self.data[self.book_id] = {}
        for k, w in self.check_data.items():
            while True:
                data = input(f"Введите {k}:")
                self.data[self.book_id][k] = data
                if w(data): break
                else: print("Некорректно")


        self.data[self.book_id]["status"] = "in stock"

        self.book_id += 1
        self.write_down()
        print("Книга успешно добавлена!")


    def delete(self, book_id):
        if self.is_book_id(book_id):
            del self.data[str(book_id)]
            self.write_down()
            print(f"Книга под id {book_id} удалена.")

    def write_down(self):
        with open(self.fname, "w") as file:
            self.data["counter"] = self.book_id
            json.dump(self.data, file)

    def display(self):
        if self.data:
            for k, w in self.data.items():
                print(f"id: {k}", w)
        else: print('Книг нет.')

    def search(self, query:str):
        books_id = [] # Список для id книг, в которых содержится запрос
        for k, w in self.data.items():
            for field, v in w.items():
                if query.lower() in str(v).lower() and field != 'status':
                    books_id.append(k)
                    break
        self.data = {pk: book for pk, book in self.data.items() if pk in books_id}
        if self.data:
            self.display()
        else: print("Ничего не найдено.")

    def change(self, book_id):
        if self.is_book_id(book_id):
            data = self.data.pop(str(book_id))
            data["status"] = "stock out" if data["status"] == "in stock" else "in stock"
            self.data[book_id] = data
            self.write_down()
            print(f"Статус книги под id {book_id} изменен.")

    def is_book_id(self, book_id):
        """Метод для проверки существования книги по id"""
        if str(book_id) in self.data.keys():
            return True
        else:
            print('Такой книги нет.')
            return False





if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("operation", choices=["add", "delete", "display", "change", "search"])
    parser.add_argument('-q', '--query', type=str)
    parser.add_argument('-i', '--id', type=int)

    args = parser.parse_args()

    a = Book()

    if args.operation == "add": a.add()
    elif args.operation == "display": a.display()

    elif args.operation == "search":
        if args.query:
            a.search(args.query)
        else: print("Введите аргумент -q для поиска")

    else:
        if args.id != None: # None для того, чтобы можно было обращаться по нулевому индексу
            if args.operation == "delete":
                a.delete(args.id)

            elif args.operation == "change":
                a.change(args.id)

        else: print("Введите аргумент -i для удаления или изменения")





