import sys
from urllib import error

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QMessageBox

from mainwindow import Ui_MainWindow
from weather import Weather


class MainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.pushButton_2.clicked.connect(self.get_weather)

    def __init__(self, window):
        super(MainWindow, self).__init__()
        self.setupUi(window)

    def get_weather(self):
        weather = Weather()
        try:
            self.label.setText(weather.get_weather(self.lineEdit.text()))
        except error.HTTPError:
            message = QMessageBox()
            message.setWindowTitle('Error')
            message.setText('Please, enter valid city')
            message.exec()
            return
        self.listWidget.clear()
        weather_data = weather.get_weather_on_days(self.lineEdit.text(), self.spinBox.text())
        for item in weather_data:
            self.listWidget.addItem(QListWidgetItem(item))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())
