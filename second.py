from flask_script import Manager
from alembic.autogenerate import render
from flask import Flask, render_template, url_for

app=Flask(__name__)
manager=Manager(app)

@app.route('/')
def index():
    return render_template('hello.html')


@app.route('/user/<name>/')
def user(name):
    return render_template('user.html', name=name)

# @app.route('/sec/')
# def sec():
#     comments=['hah','xuxu','hdjshf','dhhfu']
#     return render_template('comment_test.html',comments=comments)



@app.route('/func/')
def func():
    comments = ['ccsdhadfh', 'ccxuxdfu', 'chdjsdfdhf', 'csfddhhfu']
    return render_template('comment_test.html', comments=comments)

@app.route('/in/<hah>/')
def inherit(hah):
    return render_template('base1_inherit.html',hah=hah)

@app.route('/check/<name>/')
def checkqqq(name):
    urls=url_for('checkqqq',name="llll",page=2,pa=3,_external=True)
    return render_template('hello.html',urls=urls)

@manager.command
def home():
    return "aaaa"

if __name__ == '__main__':
    manager.run()