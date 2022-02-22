import os
from flask import Flask, abort, jsonify, render_template, request
from math import sqrt
import Calculadora_dto as Calculadora

app = Flask(__name__)

@app.route('/',methods=['GET'])
def main():
    return render_template('Calc.html')

@app.route('/calculadora',methods=['POST','GET'])
def calculadora():
    valor1=int(request.form['valor1'])
    valor2=int(request.form['valor2'])
    tipo=request.form['operacao']
    print(type(valor1))
    print(type(valor2))
    print(tipo)

    try:
        valor1 = int(valor1)
    except ValueError:
        abort(404)

    try:
        valor2 = int(valor2)
    except ValueError:
        abort(404)

    if(tipo == 'soma'):
        resultado = Calculadora.somar(valor1, valor2)
    elif(tipo == 'subtracao'):
        resultado = Calculadora.subtrair(valor1, valor2)
    elif(tipo == 'divisao'):
        if(valor2 == 0):
            abort(422)
        else:
            resultado = Calculadora.dividir(valor1, valor2)
    elif(tipo == 'multiplicacao'):
        resultado = Calculadora.multiplicar(valor1, valor2)
    else:
        abort(404)
    
    print (resultado)
    return str(resultado)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)  