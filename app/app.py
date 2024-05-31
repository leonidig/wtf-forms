
from flask import Flask, render_template, request, redirect, url_for
import json
import os

from form import UserForm


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.get("/")
def index():
    form = UserForm()
    return render_template("index.html", form = form)


@app.post("/")
def submit():
    form = UserForm()
    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "email": form.email.data
        }
        save_to_json(data)
        return redirect(url_for('index'))
    return render_template("index.html", form=form)


def save_to_json(data):
    with open("data.json", "a", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
        file.write('\n')

if __name__ == '__main__':
    app.run(debug=True)
