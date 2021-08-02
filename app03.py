# app.py
from flask import Flask, render_template, request
app = Flask(__name__)             # create an app instance

@app.route("/")
def main():
    return render_template("app03.html")

@app.route("/enviar", methods=['POST'])                   
def calc():

    def soma(x, y):
        return float(x)+float(y)  

    def subtracao(x, y):
        return float(x)-float(y)

    def multiplica(x, y):
        return float(x)*float(y)

    def divisao(x, y):
        if y == 0:
            print("Não existe divisão por 0!")
        else:
            return float(x)/float(y)

    if request.method == 'POST':
        x = request.form['num1']
        y = request.form['num2']
        n = request.form['operation']

    if n == "soma":
        z = soma(x,y)
        return render_template("app03.html", z=z)
    elif n == "subtracao":
        z = subtracao(x, y)
        return render_template("app03.html", z=z)
    elif n == "multiplicacao":
        z = multiplica(x,y)
        return render_template("app03.html", z=z)
    elif n == "divisao":
        z = divisao(x,y)
        return render_template("app03.html", z=z)
    

if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app