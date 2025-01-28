from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        #all_books = collector.books_genre.keys()
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_two_books_negative(self): # тестируем добавление невалидных названий книг
        collector = BooksCollector()
        collector.add_new_book('')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить и съесть')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_two_books_twins(self):  # тестируем добавление одной и той же книги
        collector = BooksCollector()
        collector.add_new_book('Денискины рассказы')
        collector.add_new_book('Денискины рассказы')
        assert len(collector.get_books_genre()) == 1

    # напиши свои тесты ниже

# чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_add_genre(self):   # тестируем метод set_book_genre установления книге жанра
        collector = BooksCollector()
        collector.add_new_book('Денискины рассказы')  #  добавили книгу с названием Денискины рассказы в список books_genre
        collector.set_book_genre('Денискины рассказы','Комедии')  #  установили книге жанр
        assert collector.get_book_genre('Денискины рассказы')   #  проверяем, что у книги Денискины рассказы есть жанр


    def test_get_book_genre_name(self):  #тестируем метод get_book_genre  получения книги по ее жанру
        collector = BooksCollector()
        collector.add_new_book('Денискины рассказы')   # добавили книгу
        collector.set_book_genre('Денискины рассказы', 'Комедии')   # установили этой книге жанр
        assert collector.get_book_genre('Денискины рассказы') == 'Комедии'     # вызываем тестируемый метод

    def test_get_books_with_specific_genre_self_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Денискины рассказы')    # добавили книгу
        collector.set_book_genre('Денискины рассказы', 'Комедии') # установили этой книге жанр
        assert collector.get_books_with_specific_genre('Комедии') # проверяем вывод списка книг

    def test_get_books_for_children_only_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Денискины рассказы')  # добавили книгу
        collector.set_book_genre('Денискины рассказы', 'Комедии')  # установили этой книге жанр
        assert len(collector.get_books_for_children()) == 1 # проверяем список возвращенных книг, подходящих детям

    def test_get_books_for_children_only_genre_in_age_rating(self):    # проверяем, что в список попадут книги без возрастного ограничения
        collector = BooksCollector()
        collector.add_new_book('Денискины рассказы')  # добавили книгу
        collector.set_book_genre('Денискины рассказы', 'Ужасы')
        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_name(self):
        collector = BooksCollector()
        collector.add_new_book('Денискины рассказы')  # добавили книгу
        collector.add_book_in_favorites('Денискины рассказы')  # добавили книгу методом add_book_in_favorites в список favorites
        assert len(collector.get_list_of_favorites_books()) == 1   # проверили наличие этой книги в списке

    def test_add_book_in_favorites_name_twins(self): # проверяем, что одна и та же книга не попадет в список self.favorites
        collector = BooksCollector()
        collector.add_new_book('Денискины рассказы')
        collector.add_book_in_favorites('Денискины рассказы')
        collector.add_book_in_favorites('Денискины рассказы')
        assert len(collector.get_list_of_favorites_books()) == 1


    def test_delete_book_from_favorites_name(self):
        collector = BooksCollector()
        collector.add_new_book('Денискины рассказы')  # добавили книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.add_book_in_favorites('Денискины рассказы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')  #
        assert collector.get_list_of_favorites_books()

    #def




