from flask import Flask, render_template, request
from classes import classes
from flask_wtf import FlaskForm, CSRFProtect
import os
from dotenv import load_dotenv
from text_retrieve import Text
from datetime import date, datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
csrf = CSRFProtect(app)

current_year = datetime.now().year

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bhagavatam', methods=["GET", "POST"])
def bhagavatam():
    if request.method == "POST":
        subject_name = request.form.get("subject_name")
        canto_name = request.form.get("canto_name")
        chapter_name = request.form.get("chapter_name")
        text_number = request.form.get("text_number")

        if chapter_name == "not known" and text_number == "not known":

            return render_template("subject.html", chapter_list=classes[subject_name][canto_name],
                                   subject_name=subject_name, canto_name=canto_name, chapter_name="not known",
                                   text_number="not known", current_year=current_year)

        elif text_number == "not known":

            return render_template("subject.html", slokas_list=classes[subject_name][canto_name]['Chapters'][chapter_name], subject_name=subject_name,
                                   canto_name=canto_name, chapter_name=chapter_name, text_number="not known",
                                   current_year=current_year)
        else:

            translation = Text.bhagavatam(canto_name, chapter_name, text_number)

            return render_template("translation.html", translation=translation,
                                   current_year=current_year)

    if request.method == "GET":
        print('hi5')
        print(f'classes are {classes["Bhagavatam"]}')
        return render_template("subject.html", classes_list=classes['Bhagavatam'], subject_name='Bhagavatam', canto_name="not known",
                               chapter_name="not known", text_number="not known", current_year=current_year)



if __name__ == "__main__":
    app.run(debug=True)
