from flask import Blueprint, render_template, request, redirect, url_for

# Создание Flask Blueprint с именем 'lab9'
lab9 = Blueprint('lab9', __name__)

# Роут для главной страницы '/lab9/'
@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')  # Отображение главной страницы

# Обработчик ошибки 404
@lab9.app_errorhandler(404)
def not_found(e):
    return '❄️❄️❄️Нет такой страницы, вернуться обратно <a href="/menu">Меню</a> ❄️❄️❄️', 404  # Сообщение об ошибке 404

@lab9.route('/lab9/500')
def server_error():
    raise Exception("Произошла некоторая ошибка")

@lab9.app_errorhandler(Exception)
def er500(e):
    return render_template('lab9/500.html', error=e), 500

# Роут для формы создания новогодней открытки '/lab9/new_year_card'
@lab9.route('/lab9/new_year_card', methods=['GET', 'POST'])
def new_year_card():
    if request.method == 'POST':
        # Получение данных из формы
        recipient_name = request.form.get('recipient_name')  # Получение имени получателя
        recipient_gender = request.form.get('recipient_gender')  # Получение пола получателя
        sender_name = request.form.get('sender_name')  # Получение имени отправителя

        # Тут можно добавить обработку данных и создание текста открытки

        # Перенаправление на URL с параметрами
        return redirect(url_for('lab9.show_card', recipient_name=recipient_name,
                                recipient_gender=recipient_gender, sender_name=sender_name))  # Перенаправление на страницу с готовой открыткой

    # Отображение формы для создания открытки
    return render_template('lab9/new_year_card_form.html')  # Отображение формы создания открытки

# Роут для отображения готовой открытки '/lab9/show_card'
@lab9.route('/lab9/show_card')
def show_card():
    # Получение параметров из URL
    recipient_name = request.args.get('recipient_name')  # Получение имени получателя
    recipient_gender = request.args.get('recipient_gender')  # Получение пола получателя
    sender_name = request.args.get('sender_name')  # Получение имени отправителя

    # Создание текста открытки
    card_text = f"С Новым Годом, {recipient_name}! Желаю быть счастлив{'ой' if recipient_gender == 'female' else 'ым'}! С наилучшими пожеланиями, {sender_name}."  # Формирование текста открытки

    # Отображение страницы с готовой открыткой
    return render_template('lab9/show_card.html', card_text=card_text)  # Отображение страницы с готовой открыткой
