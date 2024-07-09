from domain.interfaces import PersonRepository
from domain.entities import Person


class PersonUseCase:
    def __init__(self, person_repository: PersonRepository):
        self.person_repository = person_repository

    def get_all_people(self):
        return self.person_repository.get_all_people()

    def get_person_by_id(self, id: int):
        return self.person_repository.get_person_by_id(id)

    def add_person(self, id: int, name: str, age: int):
        person = Person(id, name, age)
        self.person_repository.add_person(person)

    def update_person(self, id, name, age):
        person = self.get_person_by_id(id)
        if person:
            person.name = name
            person.age = age
            self.person_repository.update_person(person)

    def delete_person(self, id):
        self.person_repository.delete_person(id)