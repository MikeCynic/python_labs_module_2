BOOKS_DATABASE = [{"id": 1, "name": "test_name_1", "pages": 200, }, {"id": 2, "name": "test_name_2", "pages": 400, }]


# TODO: написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise TypeError("id must be an integer")
        self.id = id_
        if not isinstance(name, str):
            raise TypeError("name must be an string")
        self.name = name
        if not isinstance(pages, int):
            raise TypeError("pages must be an integer")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in
        BOOKS_DATABASE]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
