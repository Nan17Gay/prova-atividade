from flask import Flask, request, render_template

app = Flask(__name__)

#Eu não faço ideia do que era pra fazer
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma/valor1=<int:n1>/valor2=<int:n2>")
def somar(valor1,valor2):
    return f'{valor1} + {valor2}'

@app.route("/subtrair/valor1=<int:n1>/valor2=<int:n2>")
def subtrair(valor1,valor2):
    return 

@app.route("/multiplicar/valor1=<int:n1>/valor2=<int:n2>")
def multiplicar(valor1,valor2):
    return 

@app.route("/dividir/valor1=<int:n1>/valor2=<int:n2>")
def dividir(valor1,valor2):
    return 

if __name__ == "__main__":
    app.run(debug=True)