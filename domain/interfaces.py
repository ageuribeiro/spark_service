from abc import ABC, abstractmethod
from typing import List
from .entities import Person


class PersonRepository(ABC):
    @abstractmethod
    def get_all_people(self) -> List[Person]:
        pass

    @abstractmethod
    def get_person_by_id(self, id=int) -> Person:
        pass

    @abstractmethod
    def add_person(self, person: Person) -> None:
        pass
