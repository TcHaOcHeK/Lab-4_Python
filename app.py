from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        a = float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])
        if a !=0 and b!=0 and c!=0:
            D = b ** 2 - 4 * a * c
            if D > 0:
                x1 = (-b + D ** 0.5) / (2 * a)
                x2 = (-b - D ** 0.5) / (2 * a)
                result = f"Корни уравнения: x1 = {x1}, x2 = {x2}"
            elif D == 0:
                x = -b / (2 * a)
                result = f"Уравнение имеет один корень: x = {x}"
            else:
                result = "Уравнение не имеет действительных корней"
        elif a == 0:
            if b == 0:
                if c == 0:
                    result = "Бесконечное количество решений"
                else:
                    result = "Не имеет решений"
            else:
                x = -c / b
                result = x

    return render_template('index.html', result=result)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f'User page: {name} - {id}'




if __name__ == "__main__":
    app.run(debug=True)