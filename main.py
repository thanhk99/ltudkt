from PyQt5.QtWidgets import QApplication
from mainFe import Homeui

class App:
    def __init__(self):
        self.app = QApplication([])

    def run(self):
        self.app.exec_()
if __name__ == "__main__":
    app = App()
    app.run()