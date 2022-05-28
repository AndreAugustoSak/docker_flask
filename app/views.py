from flask import render_template
from app import app

@app.route('/')
def home():
  return "<b>There has been a big big change!</b>"

@app.route('/template')
def template():
    return render_template('home.html')

@app.route('/hora')
def hora():
    return render_template('hora.html')

@app.route('/soma')
def soma():
    return render_template('soma.html')
