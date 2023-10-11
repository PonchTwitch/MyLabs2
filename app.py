from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)


@app.route("/menu")
def menu():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="'''+url_for ('static',filename='lab1.css')+'''">
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h1>
            <a href="/lab1">Первая лабораторная</a>
        </h1>

        <footer>
            &copy; Салманов Юнус Арзу оглы, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="'''+url_for ('static',filename='lab1.css')+'''">
    <head>
        <title>Салманов Юнус Арзу оглы, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </h1>
        <a href="/menu">Меню</a>
        <h2> Реализованные роуты </h2>
        <ul>
            <li><a href="/lab1/oak">/lab1/oak - дуб</a></li>
            <li><a href="/lab1/student">/lab1/student - студент</a></li>
            <li><a href="/lab1/mormish">/lab1/mormish - Мормышка</a></li>
        </ul>
        <footer>
            &copy; Юнус Салманов, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route("/lab1/oak")
def oak():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="'''+url_for ('static',filename='lab1.css')+'''">
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''

@app.route("/lab1/student")
def student():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="'''+url_for ('static',filename='lab1.css')+'''">
    <body>
        <h1>Салманов Юнус Арзу оглы</h1>
        <img src="''' + url_for('static', filename='nstu.jpg') + '''">
    </body>
</html>
'''

@app.route("/lab1/python")
def python():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="'''+url_for ('static',filename='lab1.css')+'''">
    <body>
        <div>
            Python — это скриптовый язык программирования. Он универсален,
            поэтому подходит для решения разнообразных задач и для многих
            платформ: начиная с iOS и Android и заканчивая серверными операционными системами.
        </div>
        <div>
            Чаще всего Python используют в веб-разработке. Для него написано множество
            фреймворков: FastAPI, Flask, Tornado, Pyramid, TurboGears, CherryPy и, самыq
            популярный, Django.
        </div>
        <div>
            Ещё одна область применения Python — автоматизация тестирования.
            Многие специалисты по автоматизации QA выбирают Python из-за его
            простоты. Он отлично подходит тем, кто имеет небольшой опыт в 
            разработке приложений. Развитое сообщество, логичный синтаксис 
            и удобочитаемость упрощают процесс обучения.
        </div>
        <img src="''' + url_for('static', filename='python.jpg') + '''">
    </body>
</html>
'''

@app.route("/lab1/mormish")
def mormish():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="'''+url_for ('static',filename='lab1.css')+'''">
    <body>
        <div>
            Мормы́шка — рыболовная снасть: крючок, впаянный в свинцовую или оловянную дробинку.
        </div>
        <div>
            Используется в любительском и спортивном рыболовстве. Как правило, для привлечения
            рыбы поверхность дробинки с одной стороны (обычно с верхней) имеет блестящее покрытие
            (обычно золотистое, серебристое, бронзовое) или окрашена. Иногда успех приносят мормышки
            тёмных цветов. Применяется для зимней (чаще) и летней рыбной ловли.
        </div>
        <div>
            Слово происходит от русского слова мормыш — названия мелких пресноводных рачков.
        </div>
        <img src="''' + url_for('static', filename='mormish.jpg') + '''">
    </body>
</html>
'''

@app.route("/lab2/example")
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

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/breakfast')
def breakfast():
    return render_template('breakfast.html')