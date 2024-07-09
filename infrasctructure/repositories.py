from domain.interfaces import PersonRepository
from domain.entities import Person
from .database import get_db_connection


class SQLitePersonRepository(PersonRepository):

    def get_all_people(self) -> list[Person]:
        conn = get_db_connection()
        people = conn.execute('SELECT * FROM person').fetchall()
        conn.close()
        return [Person(row['id'], row['name'], row['age']) for row in people]

    def get_person_by_id(self, id: int) -> Person:
        conn = get_db_connection()
        person = conn.execute(
            'SELECT * FROM person WHERE id = ?', (id,)).fetchone()
        conn.close()
        if person:
            return Person(person['id'], person['name'], person['age'])
        return None

    def add_person(self, person: Person) -> None:
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO person(id, name, age) VALUES(?,?,?)', 
            (person.id, person.name, person.age))
        conn.commit()
        conn.close()

    def update_person(self, person: Person) -> None:
        conn = get_db_connection()
        conn.execute('UPDATE person SET name = ?, age = ? WHERE id = ?',
                     (person.name, person.age, person.id))
        conn.commit()
        conn.close()

    def delete_person(self, id: int) -> None:
        conn = get_db_connection()
        conn.execute('DELETE FROM person WHERE id = ?', (id,))
        conn.commit()
        conn.close()