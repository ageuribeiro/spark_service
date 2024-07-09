import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QListWidget, QLineEdit, QFormLayout, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from application.uses_cases import PersonUseCase
from infrasctructure.repositories import SQLitePersonRepository
from infrasctructure.database import init_db


class MainWindow(QMainWindow):
    def __init__(self, person_use_case):
        super().__init__()

        self.person_use_case = person_use_case
        self.setWindowTitle('Person Manager')
        self.setGeometry(100, 100, 100, 100)
        self.setStyleSheet("background-image : url('/static/img/background.png');")

        layout = QVBoxLayout()
        self.person_list = QListWidget()
        self.refresh_people()

        layout.addWidget(self.person_list)

        form_layout = QFormLayout()
        self.id_input = QLineEdit()
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        form_layout.addRow('ID:', self.id_input)
        form_layout.addRow('Name:', self.name_input)
        form_layout.addRow('Age:', self.age_input)
        layout.addLayout(form_layout)

        add_button = QPushButton('Add Person')
        add_button.setStyleSheet("backgrpund-color: rgba(0,0,0,0.7); color: white;")
        add_button.clicked.connect(self.add_person)
        layout.addWidget(add_button)

        update_button = QPushButton('Update Selected Person')
        update_button.setStyleSheet("backgrpund-color: rgba(0,0,0,0.7); color: white;")
        update_button.clicked.connect(self.update_person)
        layout.addWidget(update_button)

        delete_button = QPushButton('Delete Selected Person')
        delete_button.setStyleSheet("backgrpund-color: rgba(0,0,0,0.7); color: white;")
        delete_button.clicked.connect(self.delete_person)
        layout.addWidget(delete_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def refresh_people(self):
        self.person_list.clear()
        people = self.person_use_case.get_all_people()
        for person in people:
            self.person_list.addItem(
                f"{person.id}: {person.name} - {person.age}")

    def add_person(self):
        try:
            id = int(self.id_input.text())
            name = self.name_input.text()
            age = int(self.age_input.text())
            self.person_use_case.add_person(id, name, age)
            self.refresh_people()
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Invalid input.')

    def update_person(self):
        try:
            current_item = self.person_list.currentItem()
            if not current_item:
                raise ValueError('No person selected.')

            id_text = current_item.text().split(':')[0]
            id = int(id_text)
            name = self.name_input.text()
            age = int(self.age_input.text())
            self.person_use_case.update_person(id, name, age)
            self.refresh_people()
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Invalid input.')

    def delete_person(self):
        try:
            current_item = self.person_list.currentItem()
            if not current_item:
                raise ValueError('No person selected.')

            id_text = current_item.text().split(':')[0]
            id = int(id_text)
            self.person_use_case.delete_person(id)
            self.refresh_people()
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Invalid input.')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    init_db()
    person_repository = SQLitePersonRepository()
    person_use_case = PersonUseCase(person_repository)
    window = MainWindow(person_use_case)
    window.show()
    sys.exit(app.exec_())