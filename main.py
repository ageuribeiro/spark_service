import sys
from PyQt6 import QtWidgets


class MyInterface(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        #Criando os Widgets
        self.label = QtWidgets.QLabel("Digite seu nome:")
        self.input_nome = QtWidgets.QLineEdit()
        self.btn_hellow = QtWidgets.QPushButton("Hello")

        #Definindo o layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_nome)
        layout.addWidget(self.btn_hellow)
        self.setLayout(layout)

        #Conectando os sinais aos slots
        self.btn_hellow.clicked.connect(self.greetings)

    def greetings(self):
        name = self.input_nome.text()
        message = f"Hello, {name}"
        QtWidgets.QMessageBox.information(self, "Saudação", message)


if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyInterface()
    window.show()
    sys.exit(app.exec())