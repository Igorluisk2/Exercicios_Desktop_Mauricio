# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1275, 589)
        MainWindow.setStyleSheet(u"background-color: rgb(12, 12, 12);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color:rgb(255,255,255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(9, 16777215))
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_menu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(65,65,65);\n"
"}\n"
"\n"
"QToolBox{\n"
"\n"
"text-alight: left;\n"
"		background-color: rgb(228,254,255);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	\n"
"	background-color: rgb(194,232,255);\n"
"	text-align:left;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
" 	background-color:rgb(65,65,65);\n"
"	border-top-left-radius:15px\n"
"}\n"
"QPushButton{\n"
"\n"
"	color:rgb(255,255,255);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 63, 446))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        self.btn_home.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setSizeIncrement(QSize(0, 0))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.btn_contato = QPushButton(self.page)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 30))
        self.btn_contato.setSizeIncrement(QSize(0, 0))
        self.btn_contato.setFont(font)
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_contato)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setSizeIncrement(QSize(0, 0))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 97, 446))
        self.horizontalLayout_5 = QHBoxLayout(self.page_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 9, 0, 9)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.lbl_sistema = QLabel(self.top_frame)
        self.lbl_sistema.setObjectName(u"lbl_sistema")

        self.horizontalLayout_2.addWidget(self.lbl_sistema)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_6 = QVBoxLayout(self.pg_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")

        self.verticalLayout_6.addWidget(self.logo)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_7 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_10 = QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QLineEdit{\n"
"\n"
"	background-color:rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"background-color: rgb(231,231,231);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_cnpj = QLineEdit(self.frame_3)
        self.txt_cnpj.setObjectName(u"txt_cnpj")
        self.txt_cnpj.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cnpj, 1, 0, 1, 1)

        self.txt_nome = QLineEdit(self.frame_3)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 1, 1, 1, 2)

        self.txt_logradouro = QLineEdit(self.frame_3)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_logradouro, 2, 0, 1, 3)

        self.txt_numero = QLineEdit(self.frame_3)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_numero, 3, 0, 1, 1)

        self.txt_complemento = QLineEdit(self.frame_3)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_complemento, 3, 1, 1, 1)

        self.txt_bairro = QLineEdit(self.frame_3)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro, 3, 2, 1, 1)

        self.txt_municipio = QLineEdit(self.frame_3)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_municipio, 4, 0, 1, 1)

        self.txt_uf = QLineEdit(self.frame_3)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_uf, 4, 1, 1, 1)

        self.txt_cep = QLineEdit(self.frame_3)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cep, 4, 2, 1, 1)

        self.txt_telefone = QLineEdit(self.frame_3)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone, 5, 0, 1, 1)

        self.txt_email = QLineEdit(self.frame_3)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_email, 5, 1, 1, 2)

        self.lbl_empresas = QLabel(self.frame_3)
        self.lbl_empresas.setObjectName(u"lbl_empresas")
        self.lbl_empresas.setStyleSheet(u"color:rgb(0,99,148);\n"
"background-color: rgb(249,249,249);")

        self.gridLayout.addWidget(self.lbl_empresas, 0, 0, 1, 3)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.btn_cadastrar_2 = QPushButton(self.tab)
        self.btn_cadastrar_2.setObjectName(u"btn_cadastrar_2")
        self.btn_cadastrar_2.setMinimumSize(QSize(160, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_cadastrar_2.setFont(font1)
        self.btn_cadastrar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar_2.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(0,170,255);\n"
"	border-radius:15px;\n"
"	color:#fff\n"
"}\n"
"\n"
"QPushbutton{\n"
"			border-radius:15px;\n"
"			background-color: rgb(243,243,243);\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_cadastrar_2, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_9 = QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tableWidget = QTableWidget(self.tab_2)
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
"background-color:rgb(148,148,148);\n"
"	color: rgb(255,255,255);\n"
"	font:10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"\n"
"	background-color:rgb(252,252,252);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.tableWidget)

        self.Empresas = QFrame(self.tab_2)
        self.Empresas.setObjectName(u"Empresas")
        self.Empresas.setStyleSheet(u"QPushButton{\n"
"\n"
"	border-radius:15px;\n"
"	background-color:rgb(255,255,255);\n"
"	font: 11pt \"MS Shell Dlg 2\";\n"
"	color:rgb(0,24,74);\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgb(230,230,230);\n"
"}")
        self.Empresas.setFrameShape(QFrame.StyledPanel)
        self.Empresas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Empresas)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_excel = QPushButton(self.Empresas)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(120, 30))
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton:hover{\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(49,147,0)\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.Empresas)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(120, 30))
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(255,170,0);\n"
"	color: rgb(255,255,255)\n"
"}")

        self.verticalLayout_8.addWidget(self.btn_alterar)

        self.pushButton_8 = QPushButton(self.Empresas)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(120, 30))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(199,66,0);\n"
"	color: rgb(255,255,255)\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addWidget(self.Empresas)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.label_6 = QLabel(self.pg_contatos)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(360, 250, 221, 41))
        self.lbl_contato = QLabel(self.pg_contatos)
        self.lbl_contato.setObjectName(u"lbl_contato")
        self.lbl_contato.setGeometry(QRect(0, 0, 891, 111))
        self.lbl_contato.setStyleSheet(u"color:rgb(252,252,252);\n"
"background-color: rgb(62, 62, 62);\n"
"")
        self.Pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_11 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.pg_sobre)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_11.addWidget(self.label_7)

        self.label_8 = QLabel(self.pg_sobre)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_8)

        self.Pages.addWidget(self.pg_sobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Pytax</span></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Usu\u00e1rio: PyTax</p><p align=\"center\">Sistema: Cadastro</p><p align=\"center\">Status: Ativo</p><p align=\"center\">Venc: 12/12/2077</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_toggle.setText("")
        self.lbl_sistema.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Sistema de Cadastro</span></p></body></html>", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/logo4.png\"/></p></body></html>", None))
        self.txt_cnpj.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome empresarial", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numero", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lbl_empresas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">EMPRESAS</span></p></body></html>", None))
        self.btn_cadastrar_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
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
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/whatsApp.png\"/><span style=\" font-size:18pt;\"> (67) 9949-2638</span></p></body></html>", None))
        self.lbl_contato.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Contato</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">SOBRE</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Programa para cadastro de pessoal interno e terceirizado</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u00a9Pytax 2023</span></p></body></html>", None))
    # retranslateUi

