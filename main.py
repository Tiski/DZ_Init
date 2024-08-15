from library_manager import Library, generate_report
from library_manager.utils.data_validation import validate_book_data

# Создаем объект библиотеки
my_library = Library()

# Валидация и добавление книг
try:
    validate_book_data("Мастер и Маргарита", "М. Булгаков", 1967)
    my_library.add_book("Мастер и Маргарита", "М. Булгаков", 1967)

    validate_book_data("Война и мир", "Л. Толстой", 1869)
    my_library.add_book("Война и мир", "Л. Толстой", 1869)
except ValueError as e:
    print(e)

# Поиск книг
found_books = my_library.search_books(author="М. Булгаков")
print("Найденные книги:", found_books)

# Удаление книги
my_library.remove_book("Мастер и Маргарита")

# Генерация отчета
print(generate_report(my_library))
