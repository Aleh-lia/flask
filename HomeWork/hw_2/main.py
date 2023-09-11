from flask import Flask, render_template, make_response, request, url_for
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/', methods=['GET', 'POST'])
def index():
    context = {
        'title': 'Главная',
    }
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        response = make_response(redirect(url_for('welcome')))
        response.set_cookie('user_name', name)
        return response
    return render_template('index.html', **context)


@app.route('/welcome/')
def welcome():
    context = {
        'title': 'Welcome',
    }
    user_name = request.cookies.get('user_name')
    if user_name:
        return render_template('welcome.html', user_name=user_name)
    else:
        return redirect(url_for('index', **context))


@app.route('/logout/')
def logout():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
