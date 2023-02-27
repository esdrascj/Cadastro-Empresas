from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from ui_main import Ui_MainWindow
import sys
from ui_functions import *
from database import Data_base
import pandas as pd
import sqlite3


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PyEsdras - Sistema de cadastro v1.0")
        appIcon = QIcon(u"icons/logo4.png")
        self.setWindowIcon(appIcon)

        ########TOGGLE BUTTON CHAMA MENU
        self.Btn_toggle.clicked.connect(self.LeftMenu)
        ################################################

        ############################################ Animação das Páginas do sistema
        self.BtnHome.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_home))
        self.BtnCadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_cadastrar))
        self.BtnSobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_sobre))
        self.BtnContatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page_contatos))

        #################################################################################

        ###########################PREENCHER AUTOMATICAMENTE DADOS DA EMPRESA ATRAVÉS DA BUSCA PELO CNPJ
        self.txt_cnpj_contr.editingFinished.connect(self.consult_api)
        ################################################################

        self.BtnCadastrar_2.clicked.connect(self.cadastrar_empresas)
        self.Btn_Alterar.clicked.connect(self.update_company)
        self.Btn_Excluir.clicked.connect(self.deletar_empresa)
        self.Btn_Excel.clicked.connect(self.gerar_excel)

    
    def LeftMenu(self):
        width = self.left_container.width()

        if width == 9:
            newWidth = 200
        else: 
            newWidth = 9
        
        self.animation = QtCore.QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def consult_api(self):
        campos = consulta_cnpj(self.txt_cnpj_contr.text())

        self.txt_nome_contr.setText(campos[0])
        self.txt_logradouro.setText(campos[1])
        self.txt_num.setText(campos[2])
        self.txt_complemento.setText(campos[3])
        self.txt_bairro.setText(campos[4])
        self.txt_mun.setText(campos[5])
        self.txt_uf.setText(campos[6])
        self.txt_cep.setText(campos[7].replace('.', '').replace('-',''))
        self.txt_tel_contr.setText(campos[8].replace('(','').replace('-','').replace(')',''))
        self.txt_email_contr.setText(campos[9])

    def cadastrar_empresas(self):
        db = Data_base()
        db.connect()

        fullDataSet = (
            self.txt_cnpj_contr.text(), self.txt_nome_contr.text(), self.txt_logradouro.text(), self.txt_num.text(), self.txt_complemento.text(),
            self.txt_bairro.text(), self.txt_mun.text(), self.txt_uf.text(), self.txt_cep.text(), self.txt_tel_contr.text(),
            self.txt_email_contr.text()

        )

        #cadastrar no banco de dados
        resp = db.register_company(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Cadastro Realizado")
            msg.setText("Cadastro Realizado com sucesso")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidas corretamente!")
            msg.exec()
            db.close_connection()
            return

    def buscar_empresas(self):


        db = Data_base()
        db.connect()
        result = db.select_all_companies()

        self.tb_company.clearContents()
        self.tb_company.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_company.setItem(row, column, QTableWidgetItem(str(data)))
        
        db.close_connection()

    def update_company(self):
        dados = []
        update_dados = []

        for row in range(self.tb_company.rowCount()):
            for column in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(row, column).text())
            update_dados.append(dados)
            dados = []
            
        #ATUALIZAR BANCO DE DADOS
        db = Data_base()
        db.connect()

        for emp in update_dados:
            db.update_company(tuple(emp))


        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro Realizado")
        msg.setText("Cadastro Realizado com sucesso")
        msg.exec()

        self.tb_company.reset()
        self.buscar_empresas()

    def deletar_empresa(self):

        db = Data_base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registro será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cnpj = self.tb_company.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_companies(cnpj)
            self.buscar_empresas()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("EMPRESAS")
            msg.setText(result)
            msg.exec()


        db.close_connection()

    #FUNCAO PRA GERAR EXCEL COM INTERAÇÃO DA INTERFACE
    def gerar_excel(self):

        dados = []
        all_dados = []

        for row in range(self.tb_company.rowCount()):
            for column in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(row, column).text())
        all_dados.append(dados)
        dados = []

        columns = ['CNPJ','NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 
        'MUNICIPIO', 'UF', 'CEP', 'TELEFONE', 'EMAIL']

        empresas = pd.DataFrame(all_dados, columns= columns)
        empresas.to_excel("Empresas.xlsx", sheet_name='empresas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatorio gerado com sucesso")
        msg.exec()

#FUNCAO PRA GERAR EXCEL DIRETO DO BANCO
    def gerar_excel_2(self):
        cnx = sqlite3.connect("system.db")

        empresas = pd.read_sql_query("""SELECT * FROM Empresas""", cnx)

        empresas.to_excel("Empresas.xlsx", sheet_name='empresas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatorio gerado com sucesso")
        msg.exec()

if __name__ == "__main__":


    db = Data_base()
    db.connect()
    db.create_table_company()
    db.close_connection()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()