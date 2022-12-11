from flask import Flask
import fib

app = Flask('Fibonachi')


@app.route('/')
def welcome():
    return "Приложение Фибоначчи"


@app.route('/<int:n>')
def index(n):
    return str(list(fib.Get_Fib_n(n)))


if __name__ == '__main__':
    app.run()
