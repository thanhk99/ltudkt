import json
from PyQt5.QtWidgets import QApplication
from fe.Home import Ui_Home
from mainBe import MainBackend

class App:
    def __init__(self):
        self.app = QApplication([])
        
        # Đọc file cấu hình
        with open("config.json", "r", encoding="utf-8") as config_file:
            self.config = json.load(config_file)
        
        # Khởi tạo giao diện với cấu hình
        self.backend = MainBackend()

    def run(self):
        # self.main_window.show()
        # self.app.exec_()
        self.backend.run()
if __name__ == "__main__":
    app = App()
    app.run()