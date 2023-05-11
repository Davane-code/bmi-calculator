# -*- UTF-8-*- 
# Author : David Vane
from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "体重过轻"
    elif bmi >= 18.5 and bmi < 25:
        return "正常体重"
    elif bmi >= 25 and bmi < 30:
        return "超重"
    else:
        return "肥胖"

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = calculate_bmi(weight, height)
        interpretation = interpret_bmi(bmi)
        return render_template('result.html', bmi=bmi, interpretation=interpretation)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

