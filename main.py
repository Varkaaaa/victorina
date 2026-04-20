from flask import (
    Flask, session, render_template, request, redirect, url_for)
import os
from db import *
from random import shuffle

def start_quiz(id):
    session['last_question'] = db.execute_data(GET_FIRST, (id)) [0][0]-1
    session['quiz_id'] = id
    session['total'] = 0

def index():
    if request.method == 'GET':


        quiz = db.execute(SELECT+'quiz')

        return render_template('index.html', victorinas = quiz)
    if request.method == 'POST':
        quiz_id = request.form.get('victorina')
        print (quiz_id)
        start_quiz(quiz_id)
        return redirect(url_for('test'))

def set_question(question):
    print(question)
    id = question[0]
    vopros = question[1]
    right = question[2]
    wrong = question[3].split('~')
    wrong.append(right)
    shuffle(wrong)
    return render_template('voprosi.html', q_id = id, vopros = vopros, answers = wrong)

def test():
    if request.method == 'post':
        check()
    next_question = db.execute_data(NEXT_QUESTION_ID, (session['last_question'],session['quiz_id']))
    print(next_question)
    if len(next_question) > 0:
        return set_question(next_question[0])
    else:
        return redirect(url_for('result'))
    
def result():
    return 'hehehhehehhehhehehehehe'


def check():
    answer = request.form.get('answer')
    q_id = request.form.get('q_id')
    right = db.execute_data(CHECK_RIGHT, (q_id, answer))
    if len(right)>0 and right is not None:
        session['total'] += 1
    session['last_question'] = int(q_id) + 1




papka = os.getcwd()

db = DB()
app = Flask(__name__, static_folder=papka, template_folder=papka)
app.config['SECRET_KEY'] = 'r'
app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/test', 'test', test, methods=['GET', 'POST'])
app.add_url_rule('/result', 'result', result, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run()