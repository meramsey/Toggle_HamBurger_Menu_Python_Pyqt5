################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PyQt5
## V: 1.0.1
##
################################################################################
import os
import sys
import platform
# from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
# from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
# from PySide2.QtWidgets import *

from PyQt5 import uic, QtWidgets, QtCore, QtGui, QtSql, QtWebEngineWidgets, QtWebEngineCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

# GUI FILE
# from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        # QMainWindow.__init__(self)
        super(MainWindow, self).__init__()
        mainwindow_ui = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "ui_main.ui")
        uic.loadUi(mainwindow_ui, self)

        ## TOGGLE/BURGER MENU
        ########################################################################
        self.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.btn_page_hosts.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_hosts))

        # PAGE 2
        self.btn_page_keys.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_keys))

        # PAGE 3
        self.btn_page_groups.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_groups))

        # PAGE 4
        self.btn_page_config.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_config))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
