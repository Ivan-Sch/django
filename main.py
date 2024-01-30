import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QWidget
from functools import partial

class OutputWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Output Window')
        self.setGeometry(100, 100, 800, 600)

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.output_text)

        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.setCentralWidget(self.widget)

    def custom_print(self, text):
        self.output_text.append(text)


def custom_print(text, window):
    print(text)
    window.custom_print(text)


def main():
    app = QApplication(sys.argv)

    output_window = OutputWindow()
    output_window.show()

    sys.stdout.write = partial(custom_print, window=output_window)
    sys.stderr.write = partial(custom_print, window=output_window)

    # Ваш код с использованием print
    print("Привет, это вывод из программы!")

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
