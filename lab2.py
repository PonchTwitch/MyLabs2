from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2',__name__)


@lab2.route("/lab2/example")
def example():
    name = 'Юнус Салманов'
    labnum = '2'
    coursenum = '3 курс'
    groupnum = 'ФБИ-13'

    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]

    books = [
        {'author': 'Лев Толстой', 'bookname': 'Война и мир', 'genre': 'Роман', 'pages': '1300 страниц'},
        {'author': 'Джордж Оруэлл', 'bookname': 1984, 'genre': 'Научная фантастика', 'pages': '320 страниц'},
        {'author': 'Джеймс Джойс', 'bookname': 'Улисс', 'genre': 'Роман', 'pages': '800 страниц'},
        {'author': 'Владимир Набоков', 'bookname': 'Лолита', 'genre': 'Роман', 'pages': '448 страниц'},
        {'author': 'Уильям Фолкнер', 'bookname': 'Звук и ярость', 'genre': 'Роман', 'pages': '416 страниц'},
        {'author': 'Ральф Эллисон', 'bookname': 'Человек-невидимка', 'genre': 'Научная фантастика', 'pages': '224 страницы'},
        {'author': 'Вирджиния Вулф', 'bookname': 'На маяк', 'genre': 'Роман', 'pages': '224 страницы'},
        {'author': 'Джейн Остен', 'bookname': 'Гордость и предубеждение', 'genre': 'Драма', 'pages': '416 страниц'},
        {'author': 'Данте Алигьери', 'bookname': 'Божественная комедия', 'genre': 'Эпос', 'pages': '768 страниц'},
        {'author': 'Джеффри Чосер', 'bookname': 'Кентерберийские рассказы', 'genre': 'Поэзия', 'pages': '800 страниц'}

    ]

    return render_template('example.html', name=name, labnum=labnum, coursenum=coursenum, groupnum=groupnum, fruits=fruits, books=books)

@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')

@lab2.route('/lab2/breakfast')
def breakfast():
    return render_template('breakfast.html')