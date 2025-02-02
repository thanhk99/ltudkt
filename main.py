import json
from PyQt5.QtWidgets import QApplication
from fe import MainWindow
from be.mainBe import MainBackend

class App:
    def __init__(self):
        self.app = QApplication([])
        
        # Đọc file cấu hình
        with open("config.json", "r", encoding="utf-8") as config_file:
            self.config = json.load(config_file)
        
        # Khởi tạo giao diện với cấu hình
        self.main_window = MainWindow(self.config)
        self.backend = MainBackend()

    def run(self):
        self.main_window.show()
        self.app.exec_()

if __name__ == "__main__":
    app = App()
    app.run()