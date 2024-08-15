# utils/formatting.py
def format_book_list(books):
    """
    Форматирование списка книг для отчета.
    """
    formatted_books = "\n".join([f"{book['title']} by {book['author']} ({book['year']})" for book in books])
    return formatted_books
