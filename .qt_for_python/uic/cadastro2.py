# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons_qrc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(897, 467)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"color:rgb(255,255,255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(9, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, -1)
        self.LabelTopPyEsdras = QLabel(self.frame)
        self.LabelTopPyEsdras.setObjectName(u"LabelTopPyEsdras")

        self.horizontalLayout_4.addWidget(self.LabelTopPyEsdras)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(65, 65, 65);\n"
"\n"
"}\n"
"QToolBox{\n"
"text-align: left;\n"
"	background-color: rgb(228, 254, 255);\n"
"\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"\n"
"border-radius: 5px;\n"
"text-align: left;\n"
"background-color: rgb(228, 254, 255);\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMaximumSize(QSize(16777215, 16777215))
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"background-color:rgb(65,65,65);\n"
"border-top-left-radius:15px\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"color: rgb(255,255,255);\n"
"\n"
"}")
        self.Menu = QWidget()
        self.Menu.setObjectName(u"Menu")
        self.Menu.setGeometry(QRect(0, 0, 81, 320))
        self.verticalLayout_4 = QVBoxLayout(self.Menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, 0)
        self.BtnHome = QPushButton(self.Menu)
        self.BtnHome.setObjectName(u"BtnHome")
        self.BtnHome.setMinimumSize(QSize(0, 30))
        self.BtnHome.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(13)
        self.BtnHome.setFont(font)
        self.BtnHome.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.BtnHome)

        self.BtnCadastrar = QPushButton(self.Menu)
        self.BtnCadastrar.setObjectName(u"BtnCadastrar")
        self.BtnCadastrar.setMinimumSize(QSize(0, 30))
        self.BtnCadastrar.setSizeIncrement(QSize(0, 0))
        self.BtnCadastrar.setFont(font)
        self.BtnCadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.BtnCadastrar)

        self.BtnContatos = QPushButton(self.Menu)
        self.BtnContatos.setObjectName(u"BtnContatos")
        self.BtnContatos.setMinimumSize(QSize(0, 30))
        self.BtnContatos.setSizeIncrement(QSize(0, 0))
        self.BtnContatos.setFont(font)
        self.BtnContatos.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.BtnContatos)

        self.BtnSobre = QPushButton(self.Menu)
        self.BtnSobre.setObjectName(u"BtnSobre")
        self.BtnSobre.setMinimumSize(QSize(0, 30))
        self.BtnSobre.setFont(font)
        self.BtnSobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.BtnSobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.Menu, u"Menu")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 16, 320))
        self.page_2.setMaximumSize(QSize(16777215, 337))
        self.LabelTextPage2 = QLabel(self.page_2)
        self.LabelTextPage2.setObjectName(u"LabelTextPage2")
        self.LabelTextPage2.setGeometry(QRect(-10, 30, 201, 291))
        self.LabelTextPage2.setMinimumSize(QSize(0, 0))
        self.LabelTextPage2.setMaximumSize(QSize(16777215, 291))
        self.LabelTextPage2.setTextFormat(Qt.AutoText)
        self.LabelTextPage2.setAlignment(Qt.AlignCenter)
        self.LabelTextPage2.setWordWrap(True)
        self.toolBox.addItem(self.page_2, u"Informa\u00e7\u00f5es")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setMaximumSize(QSize(16777215, 16777215))
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.Btn_toggle = QPushButton(self.top_frame)
        self.Btn_toggle.setObjectName(u"Btn_toggle")
        self.Btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_toggle.setIcon(icon)
        self.Btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.Btn_toggle, 0, Qt.AlignLeft)

        self.LabelTitle = QLabel(self.top_frame)
        self.LabelTitle.setObjectName(u"LabelTitle")

        self.horizontalLayout_2.addWidget(self.LabelTitle)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.main_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, -1, -1, 0)
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_7 = QVBoxLayout(self.page_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.logo = QLabel(self.page_home)
        self.logo.setObjectName(u"logo")
        self.logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.logo)

        self.Pages.addWidget(self.page_home)
        self.page_cadastrar = QWidget()
        self.page_cadastrar.setObjectName(u"page_cadastrar")
        self.verticalLayout_5 = QVBoxLayout(self.page_cadastrar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tabWidget = QTabWidget(self.page_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Cadastro = QWidget()
        self.Cadastro.setObjectName(u"Cadastro")
        self.frame_4 = QFrame(self.Cadastro)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 30, 621, 261))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(160, 28))
        self.frame_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"	background-color: rgb(231, 231, 231);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.LineUf = QLineEdit(self.frame_4)
        self.LineUf.setObjectName(u"LineUf")

        self.gridLayout.addWidget(self.LineUf, 4, 1, 1, 1)

        self.LineCep = QLineEdit(self.frame_4)
        self.LineCep.setObjectName(u"LineCep")

        self.gridLayout.addWidget(self.LineCep, 4, 2, 1, 1)

        self.LineBairro = QLineEdit(self.frame_4)
        self.LineBairro.setObjectName(u"LineBairro")

        self.gridLayout.addWidget(self.LineBairro, 3, 2, 1, 1)

        self.BtnCadastrar_2 = QPushButton(self.frame_4)
        self.BtnCadastrar_2.setObjectName(u"BtnCadastrar_2")
        self.BtnCadastrar_2.setMinimumSize(QSize(160, 30))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.BtnCadastrar_2.setFont(font1)
        self.BtnCadastrar_2.setFocusPolicy(Qt.StrongFocus)
        self.BtnCadastrar_2.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius:15px;\n"
"    color: #ffffff\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius:15px;\n"
"background-color:rgb(243,243,243);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.BtnCadastrar_2, 6, 1, 1, 1, Qt.AlignHCenter)

        self.LineTelefone = QLineEdit(self.frame_4)
        self.LineTelefone.setObjectName(u"LineTelefone")

        self.gridLayout.addWidget(self.LineTelefone, 5, 0, 1, 1)

        self.LineEmail = QLineEdit(self.frame_4)
        self.LineEmail.setObjectName(u"LineEmail")

        self.gridLayout.addWidget(self.LineEmail, 5, 1, 1, 1)

        self.LineNumero = QLineEdit(self.frame_4)
        self.LineNumero.setObjectName(u"LineNumero")

        self.gridLayout.addWidget(self.LineNumero, 3, 0, 1, 1)

        self.LineComplemento = QLineEdit(self.frame_4)
        self.LineComplemento.setObjectName(u"LineComplemento")

        self.gridLayout.addWidget(self.LineComplemento, 3, 1, 1, 1)

        self.LineMunicipio = QLineEdit(self.frame_4)
        self.LineMunicipio.setObjectName(u"LineMunicipio")

        self.gridLayout.addWidget(self.LineMunicipio, 4, 0, 1, 1)

        self.LineNome = QLineEdit(self.frame_4)
        self.LineNome.setObjectName(u"LineNome")

        self.gridLayout.addWidget(self.LineNome, 1, 1, 1, 2)

        self.LineCnpj = QLineEdit(self.frame_4)
        self.LineCnpj.setObjectName(u"LineCnpj")

        self.gridLayout.addWidget(self.LineCnpj, 1, 0, 1, 1)

        self.LineLogradouro = QLineEdit(self.frame_4)
        self.LineLogradouro.setObjectName(u"LineLogradouro")
        self.LineLogradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.LineLogradouro, 2, 0, 1, 3)

        self.LabelEmpresas = QLabel(self.frame_4)
        self.LabelEmpresas.setObjectName(u"LabelEmpresas")
        self.LabelEmpresas.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"	background-color: rgb(249, 249, 249);\n"
"\n"
"")

        self.gridLayout.addWidget(self.LabelEmpresas, 0, 0, 1, 3)

        self.tabWidget.addTab(self.Cadastro, "")
        self.Empresas = QWidget()
        self.Empresas.setObjectName(u"Empresas")
        self.verticalLayout_9 = QVBoxLayout(self.Empresas)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.LabelEmpresasView = QLabel(self.Empresas)
        self.LabelEmpresasView.setObjectName(u"LabelEmpresasView")
        font2 = QFont()
        font2.setPointSize(12)
        self.LabelEmpresasView.setFont(font2)

        self.verticalLayout_9.addWidget(self.LabelEmpresasView)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(self.Empresas)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(252, 252, 252);\n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.Empresas)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 24, 74);\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(230, 255, 255)\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.Btn_Excel = QPushButton(self.frame_3)
        self.Btn_Excel.setObjectName(u"Btn_Excel")
        self.Btn_Excel.setMinimumSize(QSize(120, 30))
        self.Btn_Excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Excel.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(49, 147, 0);\n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_Excel)

        self.Btn_Alterar = QPushButton(self.frame_3)
        self.Btn_Alterar.setObjectName(u"Btn_Alterar")
        self.Btn_Alterar.setMinimumSize(QSize(120, 30))
        self.Btn_Alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Alterar.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(77, 53, 255);\n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_Alterar)

        self.Btn_Excluir = QPushButton(self.frame_3)
        self.Btn_Excluir.setObjectName(u"Btn_Excluir")
        self.Btn_Excluir.setMinimumSize(QSize(120, 30))
        self.Btn_Excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Excluir.setStyleSheet(u"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(255, 144, 32);\n"
"\n"
"}")

        self.verticalLayout_8.addWidget(self.Btn_Excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.Empresas, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.Pages.addWidget(self.page_cadastrar)
        self.page_contatos = QWidget()
        self.page_contatos.setObjectName(u"page_contatos")
        self.verticalLayout_6 = QVBoxLayout(self.page_contatos)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, -1, -1, 0)
        self.LabelContatos = QLabel(self.page_contatos)
        self.LabelContatos.setObjectName(u"LabelContatos")

        self.verticalLayout_6.addWidget(self.LabelContatos)

        self.LabelWhatsapp = QLabel(self.page_contatos)
        self.LabelWhatsapp.setObjectName(u"LabelWhatsapp")

        self.verticalLayout_6.addWidget(self.LabelWhatsapp)

        self.LabelEmail = QLabel(self.page_contatos)
        self.LabelEmail.setObjectName(u"LabelEmail")

        self.verticalLayout_6.addWidget(self.LabelEmail)

        self.LabelYoutube = QLabel(self.page_contatos)
        self.LabelYoutube.setObjectName(u"LabelYoutube")

        self.verticalLayout_6.addWidget(self.LabelYoutube)

        self.Pages.addWidget(self.page_contatos)
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.verticalLayout_10 = QVBoxLayout(self.page_sobre)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, 0, 0)
        self.LabelSobre = QLabel(self.page_sobre)
        self.LabelSobre.setObjectName(u"LabelSobre")

        self.verticalLayout_10.addWidget(self.LabelSobre)

        self.LabelTextSobre = QLabel(self.page_sobre)
        self.LabelTextSobre.setObjectName(u"LabelTextSobre")
        self.LabelTextSobre.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.LabelTextSobre)

        self.Pages.addWidget(self.page_sobre)

        self.verticalLayout_11.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.LabelFooter = QLabel(self.footer_frame)
        self.LabelFooter.setObjectName(u"LabelFooter")

        self.horizontalLayout_3.addWidget(self.LabelFooter)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LabelTopPyEsdras.setText(QCoreApplication.translate("MainWindow", u"PyEsdras", None))
        self.BtnHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.BtnCadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.BtnContatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.BtnSobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Menu), QCoreApplication.translate("MainWindow", u"Menu", None))
#if QT_CONFIG(tooltip)
        self.page_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.LabelTextPage2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.Btn_toggle.setText("")
        self.LabelTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:14pt;\">Sistema de cadastro</span></p></body></html>", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/logo4.png\"/></p></body></html>", None))
        self.LineUf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.LineCep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.LineBairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.BtnCadastrar_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.LineTelefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.LineEmail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.LineNumero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None))
        self.LineComplemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        self.LineMunicipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None))
        self.LineNome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.LineCnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.LineLogradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        self.LabelEmpresas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">EMPRESAS</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cadastro), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.LabelEmpresasView.setText(QCoreApplication.translate("MainWindow", u"EMPRESAS", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.Btn_Excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.Btn_Alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.Btn_Excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Empresas), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.LabelContatos.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CONTATOS</span></p></body></html>", None))
        self.LabelWhatsapp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/whatsApp.png\"/><span style=\" font-size:18pt; vertical-align:super;\">(71)9999-99999</span></p></body></html>", None))
        self.LabelEmail.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/email.png\"/><span style=\" font-size:18pt; vertical-align:super;\">Email</span></p></body></html>", None))
        self.LabelYoutube.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/Youtube.png\"/><span style=\" font-size:18pt; vertical-align:super;\">Youtube</span></p></body></html>", None))
        self.LabelSobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">SOBRE</span></p></body></html>", None))
        self.LabelTextSobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Este sistema faz consutla com receita federal</span></p></body></html>", None))
        self.LabelFooter.setText(QCoreApplication.translate("MainWindow", u"PyEsdras", None))
    # retranslateUi

