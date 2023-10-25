from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1',__name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
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

        <h1>
            <a href="/lab2">Вторая лабораторная</a>
        </h1>

        <footer>
            &copy; Салманов Юнус Арзу оглы, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@lab1.route("/lab1")
def lab():
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


@lab1.route("/lab1/oak")
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


@lab1.route("/lab1/student")
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


@lab1.route("/lab1/python")
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


@lab1.route("/lab1/mormish")
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