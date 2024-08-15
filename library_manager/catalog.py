# catalog.py
class Library:
    def __init__(self):
        # Инициализация библиотеки как пустого списка
        self.books = []

    def add_book(self, title, author, year):
        """
        Добавление книги в библиотеку.
        """
        book = {'title': title, 'author': author, 'year': year}
        self.books.append(book)
        print(f"Книга '{title}' добавлена в библиотеку.")

    def remove_book(self, title):
        """
        Удаление книги по названию.
        """
        self.books = [book for book in self.books if book['title'] != title]
        print(f"Книга '{title}' удалена из библиотеки.")

    def search_books(self, title=None, author=None, year=None):
        """
        Поиск книг по разным критериям: названию, автору или году.
        """
        results = self.books
        if title:
            results = [book for book in results if book['title'] == title]
        if author:
            results = [book for book in results if book['author'] == author]
        if year:
            results = [book for book in results if book['year'] == year]

        return results
