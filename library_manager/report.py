# report.py
from library_manager.utils.formatting import format_book_list


def generate_report(library):
    """
    Генерация отчета обо всех книгах в библиотеке.
    """
    if not library.books:
        return "В библиотеке нет книг."

    report = format_book_list(library.books)
    return report
