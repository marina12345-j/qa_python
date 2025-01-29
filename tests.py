from tkinter.font import names

from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:

    @pytest.mark.parametrize('book',
                             [
                                 'Что делать, если ваш кот хочет вас убить',
                                 'Денискины рассказы',
                                 '33 коровы',
                                 'Дюна',
                                 'Приключения Шерлока Холмса'

                             ]
                             )
    def test_add_new_book_add_several_books(self, book, collector):
       collector.add_new_book(book)
       assert collector.get_books_genre()

    def test_add_new_book_add_two_books_negative(self, collector): # тестируем добавление невалидных названий книг
        collector.add_new_book('')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить и съесть')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_two_books_twins(self, collector):  # тестируем добавление одной и той же книги
        collector.add_new_book('Денискины рассказы')
        collector.add_new_book('Денискины рассказы')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_add_genre(self, collector):   # тестируем метод set_book_genre установления книге жанра
        collector.add_new_book('Денискины рассказы')  #  добавили книгу с названием Денискины рассказы в список books_genre
        collector.set_book_genre('Денискины рассказы','Комедии')  #  установили книге жанр
        assert collector.get_book_genre('Денискины рассказы') == 'Комедии'  #  проверяем, что у книги Денискины рассказы есть жанр


    def test_get_book_genre_name(self, collector):  #тестируем метод get_book_genre получения книги по ее имени
        collector.add_new_book('Денискины рассказы')   # добавили книгу
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Денискины рассказы', 'Комедии')   # установили этой книге жанр
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Денискины рассказы')    # вызываем тестируемый метод


    def test_get_books_with_specific_genre_self_genre(self, collector):
        collector.add_new_book('Денискины рассказы')    # добавили книгу
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Денискины рассказы', 'Комедии') # установили этой книге жанр
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_with_specific_genre('Комедии') # проверяем вывод списка книг


    def test_get_books_for_children_only_genre_in_age_rating(self, collector):
        collector.add_new_book('Денискины рассказы')  # добавили книгу
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Дюна')
        collector.add_new_book('Приключения Шерлока Холмса')
        collector.set_book_genre('Денискины рассказы', 'Комедии')  # установили этой книге жанр
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Приключения Шерлока Холмса', 'Детективы')
        assert len(collector.get_books_for_children()) == 2 and collector.get_books_for_children() != ('Ужасы', 'Детективы')# проверяем список возвращенных книг, подходящих детям


    def test_add_book_in_favorites_name(self,collector ):
        collector.add_new_book('Денискины рассказы')  # добавили книгу
        collector.add_book_in_favorites('Денискины рассказы')  # добавили книгу методом add_book_in_favorites в список favorites
        assert len(collector.get_list_of_favorites_books()) == 1   # проверили наличие этой книги в списке

    def test_add_book_in_favorites_name_twins(self, collector): # проверяем, что одна и та же книга не попадет в список self.favorites
        collector.add_new_book('Денискины рассказы')
        collector.add_book_in_favorites('Денискины рассказы')
        collector.add_book_in_favorites('Денискины рассказы')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_name(self, collector):
        collector.add_new_book('Денискины рассказы')  # добавили книгу
        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.add_book_in_favorites('Денискины рассказы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        favorites = collector.get_list_of_favorites_books()

        assert 'Денискины рассказы' in favorites
        assert 'Гордость и предубеждение и зомби' in favorites

        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')  #
        favorites = collector.get_list_of_favorites_books()
        assert 'Денискины рассказы' in favorites
        assert 'Гордость и предубеждение и зомби' not in favorites







