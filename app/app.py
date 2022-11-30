from flask import Flask
from flask import render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


class Todo(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(300), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/update/<int:item_id>', methods=('GET', 'POST'))
def update(item_id):
    todo = Todo.query.get_or_404(item_id)

    if request.method == 'POST':

        todo.title = request.form['title']
        todo.details = request.form['details']

        db.session.commit()

        return redirect('/')
    return render_template("update.html", todo=todo)


@app.route('/delete/<int:item_id>')
def delete(item_id):
    db.session.delete(Todo.query.get_or_404(item_id))
    db.session.commit()
    return redirect('/')


@app.route('/create/', methods=('GET', 'POST'))  # type: ignore
def create():
    if request.method == 'POST':
        title = request.form['title']
        details = request.form['details']
        if not title:
            return flash('Title is required.')
        if not details:
            return flash('Details are required.')
        db.session.add(Todo(title=title, details=details))
        db.session.commit()

        return redirect('/')
    return render_template("create.html")


@app.route("/")
def index():
    items = Todo.query.all()
    return render_template("main.html", items=items)


@app.route("/details/<int:item_id>")
def details(item_id):
    item = Todo.query.get_or_404(item_id)
    return render_template("details.html", item=item)

