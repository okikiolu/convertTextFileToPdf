# This is a Python Script that converts Text Files to PDF
import sys

from PyQt6.QtCore import QStringListModel
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QWidget,
    QFileDialog,
)
from pathlib import Path
from fpdf import FPDF


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)

        self.setWindowTitle("Convert Text File to PDF App")

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Creating line edit
        self.line_edit = QLineEdit(self)

        # Setting geometry of line edit
        self.line_edit.setGeometry(200, 150, 400, 40)

        # Creating a push button
        self.button_browse = QPushButton("Browse", self)

        # Setting geometry of button
        self.button_browse.setGeometry(350, 220, 100, 40)

        # Adding action to button
        self.button_browse.clicked.connect(self.open_file_dialog)

        self.button_convert_to_pdf = QPushButton("Convert to PDF", self)

        self.button_convert_to_pdf.setGeometry(350, 270, 100, 40)

        self.button_convert_to_pdf.clicked.connect(self.convert_text_to_pdf)

        layout.addWidget(self.line_edit)
        layout.addWidget(self.button_browse)
        layout.addWidget(self.button_convert_to_pdf)

        # Showing all the widgets
        self.show()

    def convert_text_to_pdf(self):
        pdf = FPDF()
        # Add a page
        pdf.add_page()
        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size=15)
        filename = self.line_edit.text()
        file = open(filename, "r")
        for f in file:
            pdf.cell(200, 10, txt=f, ln=1, align='C')
            pdf.output(filename.replace('.txt', '.pdf'))

    def open_file_dialog(self):
        home_dir = str(Path.home())
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File",
            home_dir
        )
        if filename:
            path = Path(filename)
            self.line_edit.setText(str(path))


if __name__ == '__main__':
    # Create pyqt6 app
    app = QApplication(sys.argv)

    # Create the instance of our Window
    window = MainWindow()

    # Start the app
    app.exec()
