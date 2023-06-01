# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QShortcut)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 470)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(450, 470))
        MainWindow.setMaximumSize(QSize(450, 470))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/Icons/calc.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setIconSize(QSize(40, 40))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-family: Rubik;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")
        self.main = QLineEdit(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(20, 40, 411, 81))
        self.main.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.main.setMaxLength(13)
        self.main.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.main.setReadOnly(True)
        self.temp = QLabel(self.centralwidget)
        self.temp.setObjectName(u"temp")
        self.temp.setGeometry(QRect(20, 0, 411, 41))
        self.temp.setStyleSheet(u"color: #c4c4c4;")
        self.temp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridWidget = QWidget(self.centralwidget)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setGeometry(QRect(10, 120, 431, 331))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.gridWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_equals = QPushButton(self.gridWidget)
        self.btn_equals.setObjectName(u"btn_equals")
        sizePolicy.setHeightForWidth(self.btn_equals.sizePolicy().hasHeightForWidth())
        self.btn_equals.setSizePolicy(sizePolicy)
        self.btn_equals.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_equals, 4, 4, 1, 1)

        self.btn_3 = QPushButton(self.gridWidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_3, 3, 3, 1, 1)

        self.btn_c = QPushButton(self.gridWidget)
        self.btn_c.setObjectName(u"btn_c")
        sizePolicy.setHeightForWidth(self.btn_c.sizePolicy().hasHeightForWidth())
        self.btn_c.setSizePolicy(sizePolicy)
        self.btn_c.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_c, 0, 0, 1, 1)

        self.btn_5 = QPushButton(self.gridWidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_5, 2, 2, 1, 1)

        self.btn_1 = QPushButton(self.gridWidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_4 = QPushButton(self.gridWidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_8 = QPushButton(self.gridWidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_8, 1, 2, 1, 1)

        self.btn_dot = QPushButton(self.gridWidget)
        self.btn_dot.setObjectName(u"btn_dot")
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        self.btn_dot.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_dot, 4, 3, 1, 1)

        self.btn_minus = QPushButton(self.gridWidget)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        self.btn_minus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_minus, 2, 4, 1, 1)

        self.btn_backspace = QPushButton(self.gridWidget)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy)
        self.btn_backspace.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backspace.setIcon(icon1)
        self.btn_backspace.setIconSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.btn_backspace, 0, 3, 1, 1)

        self.btn_ce = QPushButton(self.gridWidget)
        self.btn_ce.setObjectName(u"btn_ce")
        sizePolicy.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
        self.btn_ce.setSizePolicy(sizePolicy)
        self.btn_ce.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_ce, 0, 2, 1, 1)

        self.btn_7 = QPushButton(self.gridWidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_divide = QPushButton(self.gridWidget)
        self.btn_divide.setObjectName(u"btn_divide")
        sizePolicy.setHeightForWidth(self.btn_divide.sizePolicy().hasHeightForWidth())
        self.btn_divide.setSizePolicy(sizePolicy)
        self.btn_divide.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_divide, 0, 4, 1, 1)

        self.btn_0 = QPushButton(self.gridWidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_0, 4, 2, 1, 1)

        self.btn_6 = QPushButton(self.gridWidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_6, 2, 3, 1, 1)

        self.btn_9 = QPushButton(self.gridWidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_9, 1, 3, 1, 1)

        self.btn_plus = QPushButton(self.gridWidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_plus, 3, 4, 1, 1)

        self.btn_2 = QPushButton(self.gridWidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_2, 3, 2, 1, 1)

        self.btn_plmi = QPushButton(self.gridWidget)
        self.btn_plmi.setObjectName(u"btn_plmi")
        sizePolicy.setHeightForWidth(self.btn_plmi.sizePolicy().hasHeightForWidth())
        self.btn_plmi.setSizePolicy(sizePolicy)
        self.btn_plmi.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_plmi, 4, 0, 1, 1)

        self.btn_multiply = QPushButton(self.gridWidget)
        self.btn_multiply.setObjectName(u"btn_multiply")
        sizePolicy.setHeightForWidth(self.btn_multiply.sizePolicy().hasHeightForWidth())
        self.btn_multiply.setSizePolicy(sizePolicy)
        self.btn_multiply.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_2.addWidget(self.btn_multiply, 1, 4, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440 by AK", None))
        self.main.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.temp.setText("")
        self.btn_equals.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)

        for sc in ('Enter', '=', 'Return'):
            QShortcut(sc, self.btn_equals).activated.connect(self.btn_equals.animateClick)

#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)

        for sc in ('.', ','):
            QShortcut(sc, self.btn_dot).activated.connect(self.btn_dot.animateClick)

#endif // QT_CONFIG(shortcut)
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_backspace.setText("")
        self.btn_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_divide.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_plmi.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.btn_multiply.setText(QCoreApplication.translate("MainWindow", u"*", None))
#if QT_CONFIG(shortcut)
        self.btn_multiply.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

