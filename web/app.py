from flask import Flask, jsonify, request, render_template, redirect, url_for
from application.uses_cases import PersonUseCase
from infrasctructure.repositories import SQLitePersonRepository
from infrasctructure.database import init_db

app = Flask(__name__)

init_db()
person_repository = SQLitePersonRepository()
person_use_case = PersonUseCase(person_repository)


@app.route('/')
def index():
    people = person_use_case.get_all_people()
    return render_template('index.html', people=people)

@app.route('/people', methods=['GET'])
def get_people():
    people = person_use_case.get_all_people()
    return jsonify([person.__dict__ for person in people])


@app.route('/people/<int:id>', methods=['GET'])
def get_person(id):
    person = person_use_case.get_person_by_id(id)
    return jsonify(person.__dict__)if person else ('', 404)


@app.route('/people', methods=['POST'])
def add_person():
    data = request.get_json()
    person_use_case.add_person(data['id'], data['name'], data['age'])
    return ('', 201)

@app.route('/people/<int:id>', methods=['PUT'])
def update_person(id):
    data = request.get_json()
    person_use_case.update_person(id, data['name'], data['age'])
    return('', 204)

@app.route('/people/<int:id>', methods=['DELETE'])
def delete_person(id):
    person_use_case.delete_person(id)
    return('', 204)

@app.route('/add_person', methods=['POST'])
def add_person_form():
    id = request.form['id']
    name = request.form['name']
    age = request.form['age']
    person_use_case.add_person(int(id), name, int(age))
    return redirect(url_for('index'))

@app.route('/update_person/<int:id>', methods=['POST'])
def update_person_form(id):
    name = request.form['name']
    age = request.form['age']
    person_use_case.update_person(id, name, int(age))
    return redirect(url_for('index'))

@app.route('/delete_person/<int:id>', methods=['POST'])
def delete_person_form(id):
    person_use_case.delete_person(id)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)