from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageGrab
from PIL.ImageQt import ImageQt
import sys
import time
import webbrowser
import qrcode
from pyzbar import pyzbar


class Main(Ui_MainWindow):
    def __init__(self, root):
        super().setupUi(root)
        self.root = root
        self.image = None
        self.label.setScaledContents(True)
        self.B_make.clicked.connect(self.make)
        self.B_make_clip.clicked.connect(self.make_clip)
        self.B_clip.clicked.connect(self.decode_clip)
        self.B_file.clicked.connect(self.decode_file)
        self.B_grab.clicked.connect(self.decode_grab)
        self.B_browse.clicked.connect(self.browse)
        self.B_save.clicked.connect(self.save)
        self.B_save_img.clicked.connect(self.save_img)
        self.B_save_text.clicked.connect(self.save_text)

    def make(self):
        text = self.textEdit.toPlainText()
        img = qrcode.make(data=text)
        self.label.setPixmap(QPixmap.fromImage(ImageQt(img)))
        self.image = img

    def make_clip(self):
        clip = QApplication.clipboard()
        self.textEdit.setText(clip.text())
        self.make()

    def decode(self, img):
        try:
            text = pyzbar.decode(img)[0].data.decode()
            self.textEdit.setText(text)
            if self.checkBox.isChecked() and text.startswith('http'):
                webbrowser.open(text, new=2)
        except:
            QMessageBox.critical(self.root, "错误", "无法识别二维码", QMessageBox.Ok)

    def decode_clip(self):
        try:
            img = ImageGrab.grabclipboard()
            assert img
            self.decode(img)
        except AssertionError:
            QMessageBox.critical(self.root, "错误", "剪贴板中不是图片", QMessageBox.Ok)

    def decode_file(self):
        try:
            path = self.lineEdit.text()
            img = Image.open(path)
            self.decode(img)
        except (AttributeError, OSError):
            QMessageBox.critical(self.root, "错误", "文件路径无效", QMessageBox.Ok)

    def decode_grab(self):
        self.root.showMinimized()
        time.sleep(1)
        img = ImageGrab.grab()
        self.root.showNormal()
        self.decode(img)

    def browse(self):
        path = QFileDialog.getOpenFileName(self.root, "浏览")[0]
        self.lineEdit.setText(path)

    def save(self):
        if not self.image:
            return
        path = QFileDialog.getSaveFileName(self.root, "保存")[0]
        try:
            assert path
            self.image.save(path)
        except:
            QMessageBox.critical(self.root, "错误", "保存路径无效", QMessageBox.Ok)

    def save_img(self):
        if not self.image:
            return
        clip = QApplication.clipboard()
        clip.setPixmap(QPixmap.fromImage(ImageQt(self.image)))

    def save_text(self):
        clip = QApplication.clipboard()
        text = self.textEdit.toPlainText()
        clip.setText(text)


app = QApplication(sys.argv)
window = QMainWindow()
ui = Main(window)
window.show()
sys.exit(app.exec_())
