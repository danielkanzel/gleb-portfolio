import os
import random
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

# Flask config
app = Flask(__name__)

# Flask SQLAlchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.abspath(os.getcwd())+"\database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# Database structure
class Entries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=True)
    description = db.Column(db.String(100), unique=False, nullable=False)
    link_text = db.Column(db.String(100), unique=True, nullable=True)
    link = db.Column(db.String(100), unique=True, nullable=True)

# Database init
if os.path.isfile(os.path.abspath(os.getcwd())+"\database.db") == False:
    db.create_all()


@app.route('/')
def portfolio():
    """
    Page with portfolio
    """
    entry_list=[]
    for c in Entries.query.all():
        entry_list.append(c.__dict__)
    return render_template("index.html",entry_list=entry_list)

@app.route('/login')
def login():
    return "p"

@app.route('/admin')
def admin():
    return "p"

@app.route('/add_entry')
def add_contact():
    db.session.add(Entries(
        title="Дизайн-система в DRIVE2",
        description='''DRIVE2.RU — это сообщество машин и людей, 
        которое ежемесячно посещает больше 30 млн человек. 
        Сообщество развивалось эволюционно, поэтому со временем 
        накопился беспорядок. Помогаю с ним справится. ''',
        link_text="Интересненько",
        link=""))
    db.session.add(Entries(
        title="Тяжеловато",
        description='''Приложение, которое помогает экономить и дожить 
        до следующей зарплаты. Вместе с командой внедрили Дизайн-систему
         и сделали редизайн приложения.

        Это портфолио собрано за 5 минут на компонентах для Тяжеловато. ''',
        link_text="Че за Тяжеловато?",
        link="https://www.fuckgrechka.ru/tzlvt/"))
    db.session.add(Entries(
        title="Скиллбокс",
        description='''В блоге онлайн-университета рассказываю о том, 
        что дизайн — это не рай под пальмой, а дёргающиеся красные 
        глаза, вечный недосып и пиксель вправо-пиксель влево.''',
        link_text="А ну-ка",
        link="https://skillbox.ru/media/authors/gleb-letushov/"))
    db.session.commit()
    return "done"

# Run by file
if __name__ == "__main__":
    app.debug = True
    app.run()