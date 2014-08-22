#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys; reload(sys)
sys.setdefaultencoding('utf-8')

from PySide import QtGui
from base64 import encodestring, decodestring

class FrameWindow(QtGui.QMainWindow):
    def __init__(self):
        super(FrameWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()

        exit = QtGui.QAction(u'Close', self)
        exit.triggered.connect(self.close)
        filemenu = menubar.addMenu(u'File')
        filemenu.addAction(exit)

        encrypt_file = QtGui.QAction(u'Encode File', self)
        encrypt_file.triggered.connect(self.encrypt_file)

        decrypt_file = QtGui.QAction(u'Decode File', self)
        decrypt_file.triggered.connect(self.decrypt_file)

        filemenu = menubar.addMenu(u'Base64')
        filemenu.addAction(encrypt_file)
        filemenu.addAction(decrypt_file)

        self.setCentralWidget(Base64Tool())
        self.setWindowTitle(u'String 和 Base64 互转')
        self.show()

    def encrypt_file(self):
        try:
            filename, _ = QtGui.QFileDialog.getOpenFileName(
                self, u'请选择要用 base64 加密的文件', '.')
            fileobj = open(filename, 'rb')
            s = fileobj.read()
            fileobj.close()

            s = unicode(s, 'utf-8').encode('utf-8')
            s = encodestring(s)
            print `s`

            files_types = 'All File (*)'
            filename, filter = QtGui.QFileDialog.getSaveFileName(
                self, u'保存 base64 加密后的文件', '', files_types)
            fileobj = open(filename, 'wb')
            fileobj.write(s)
            fileobj.close()
        except:
            QtGui.QMessageBox.about(self, u'错误提示', u'请检查输入是否正确')

    def decrypt_file(self):
        try:
            filename, _ = QtGui.QFileDialog.getOpenFileName(
                self, u'请选择要用 base64 解密的文件', '.')
            fileobj = open(filename, 'rb')
            s = fileobj.read()
            fileobj.close()

            s = unicode(s, 'utf-8').encode('utf-8')
            s = decodestring(s)

            files_types = 'All File (*)'
            filename, filter = QtGui.QFileDialog.getSaveFileName(
                self, u'保存 base64 解密后的文件', '', files_types)
            fileobj = open(filename, 'wb')
            fileobj.write(s)
            fileobj.close()
        except:
            QtGui.QMessageBox.about(self, u'错误提示', u'请检查输入是否正确')

class Base64Tool(QtGui.QWidget):
    def __init__(self):
        super(Base64Tool, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.gridlayout = gridlayout = QtGui.QGridLayout(self)

        self.lbl_source_code = QtGui.QLabel(u'原文')
        gridlayout.addWidget(self.lbl_source_code, 0, 0)
        self.txt_source_code = QtGui.QTextEdit()
        gridlayout.addWidget(self.txt_source_code, 0, 1, 1, 2)

        self.lbl_secret_code = QtGui.QLabel(u'Base64')
        gridlayout.addWidget(self.lbl_secret_code, 1, 0)
        self.txt_secret_code = QtGui.QTextEdit()
        gridlayout.addWidget(self.txt_secret_code, 1, 1, 1, 2)

        self.btn_encrypt = QtGui.QPushButton(u'原文转 Base64')
        self.btn_encrypt.clicked.connect(self.encrypt)
        gridlayout.addWidget(self.btn_encrypt, 2, 1)

        self.btn_decrypt = QtGui.QPushButton(u'Base64 转原文')
        self.btn_decrypt.clicked.connect(self.decrypt)
        gridlayout.addWidget(self.btn_decrypt, 2, 2)

        self.show()

    def encrypt(self):
        try:
            s = self.txt_source_code.toPlainText().encode('utf-8')
            s = encodestring(s)
            self.txt_secret_code.setText(s)
        except:
            QtGui.QMessageBox.about(self, u'错误提示', u'请检查输入是否正确')

    def decrypt(self):
        try:
            s = self.txt_secret_code.toPlainText().encode('utf-8')
            s = decodestring(s)
            self.txt_source_code.setText(s)
        except:
            QtGui.QMessageBox.about(self, u'错误提示', u'请检查输入是否正确')

def main():
    app  = QtGui.QApplication(sys.argv)
    framewindow = FrameWindow()
    sys.exit(app.exec_())

if '__main__' == __name__:
    main()
