# This is a Python Script that converts Text Files to PDF
import sys

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)

        self.setWindowTitle("Convert Text File to PDF App")

        # Calling method
        self.ui_components()

        # Showing all the widgets
        self.show()

    def ui_components(self):
        # Creating line edit
        line_edit = QLineEdit(self)

        # Setting geometry of line edit
        line_edit.setGeometry(200, 150, 400, 40)

        # Creating a push button
        button = QPushButton("Convert to PDF", self)

        # Setting geometry of button
        button.setGeometry(350, 220, 100, 40)

        # Adding action to button
        button.clicked.connect(self.convert_text_to_pdf)

    def convert_text_to_pdf(self):
        print("Button Clicked")


# Create pyqt6 app
app = QApplication(sys.argv)

# Create the instance of our Window
window = MainWindow()

# Start the app
app.exec()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
