from flask import Flask, render_template, url_for, request
import pandas as pd

app = Flask(__name__)
       
@app.route("/")
def homepage():  
    log=0
    return render_template("homepage.html", User=log)

@app.route("/submit", methods=['POST'])
def submit():
    log=1
    return render_template("homepage.html", User=log)

@app.route("/men")
def Menpage():
    item = pd.read_csv('Test.csv')
    produtos = item.to_dict('records')
    return render_template("masculino.html", DicLuxo=produtos)

@app.route("/women")
def Womenpage():
    item = pd.read_csv('Test.csv')
    produtos = item.to_dict('records') 
    return render_template("feminino.html", DicLuxo=produtos)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")