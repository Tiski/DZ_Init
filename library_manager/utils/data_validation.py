# utils/data_validation.py
def validate_book_data(title, author, year):
    """
    Валидация данных книги.
    Проверяет, что все данные не пустые и что год является числом.
    """
    if not title or not author or not isinstance(year, int):
        raise ValueError("Неверные данные книги: убедитесь, что все поля заполнены и год является числом.")
    return True
