from infrasctructure.database import init_db

import sys
import argparse

def run_web_app():
    from web.app import app
    app.run()


def run_desktop_app():
    from PyQt5.QtWidgets import QApplication
    from infrasctructure.repositories import SQLitePersonRepository
    from application.uses_cases import PersonUseCase
    from desktop.main import MainWindow

    app = QApplication(sys.argv)

    person_repository = SQLitePersonRepository()
    person_use_case = PersonUseCase(person_repository)

    window = MainWindow(person_use_case)
    window.show()

    sys.exit(app.exec_())


if __name__=='__main__':
    init_db()

    parser = argparse.ArgumentParser(description='Run the application.')
    parser.add_argument('--interface', choices=['web', 'desktop'], required=True, help='Choose the interface to run')
    args = parser.parse_args()

    try:
        if args.interface == 'web':
            run_web_app()
        elif args.interface == 'desktop':
            run_desktop_app()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)