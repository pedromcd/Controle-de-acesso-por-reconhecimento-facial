import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QMessageBox, QLineEdit, QHBoxLayout
)
from PyQt5.QtGui import QFont


class CadastroWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastrar rosto")
        self.setFixedSize(350, 200)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        layout = QVBoxLayout()
        texto = QLabel("Digite o nome do usuário:")
        texto.setFont(QFont("Arial", 12))
        layout.addWidget(texto)
        layout.addStretch(1)

        self.nomeInput = QLineEdit()
        self.nomeInput.setPlaceholderText("Ex: Paulo da Silva")
        self.nomeInput.setStyleSheet("padding: 10px; border-radius: 5px;")
        self.nomeInput.setMinimumWidth(300)
        layout.addWidget(self.nomeInput)
        layout.addStretch(1)

        btnSalvar = QPushButton("Iniciar Captura")
        btnSalvar.setFont(QFont("Arial", 12))
        btnSalvar.setStyleSheet("background-color: #3ca25b; border-radius: 8px; height: 40px;")
        btnSalvar.clicked.connect(self.iniciar_cadastro)
        layout.addWidget(btnSalvar)

        self.setLayout(layout)

    def iniciar_cadastro(self):
        nome = self.nomeInput.text().strip()
        if nome == "":
            QMessageBox.warning(self, "Atenção", "Digite um nome válido.")
            return
        
        QMessageBox.information(self,
                                "Instruções",
                                "Aperte 'C' para capturar cada foto do rosto.\n'Q' para sair do cadastro."
                                )

        try:
            subprocess.run([sys.executable, "enroll.py", nome], check=True)
            QMessageBox.information(self, "Sucesso", f"{nome} cadastrado com sucesso!")
            self.close()
        except:
            QMessageBox.critical(self, "Erro", "Falha ao cadastrar rosto.")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Controle de Acesso Facial")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        layout = QVBoxLayout()
        self.setLayout(layout)

        titulo = QLabel("Sistema de Reconhecimento Facial")
        titulo.setFont(QFont("Arial", 14, QFont.Bold))
        titulo.setStyleSheet("padding: 15px; text-align: center;")
        layout.addWidget(titulo)

        btnCadastrar = QPushButton("Cadastrar Rosto")
        btnCadastrar.setFont(QFont("Arial", 12))
        btnCadastrar.setStyleSheet("background-color: #4646f0; border-radius: 10px; height: 45px;")
        btnCadastrar.clicked.connect(self.abrir_cadastro)
        layout.addWidget(btnCadastrar)

        btnReconhecer = QPushButton("Reconhecer Acesso")
        btnReconhecer.setFont(QFont("Arial", 12))
        btnReconhecer.setStyleSheet("background-color: #3ca25b; border-radius: 10px; height: 45px;")
        btnReconhecer.clicked.connect(self.reconhecer)
        layout.addWidget(btnReconhecer)

        btnSair = QPushButton("Sair")
        btnSair.setFont(QFont("Arial", 12))
        btnSair.setStyleSheet("background-color: #b02a2a; border-radius: 10px; height: 45px;")
        btnSair.clicked.connect(self.close)
        layout.addWidget(btnSair)

        self.setLayout(layout)

    def abrir_cadastro(self):
        self.cadastroWindow = CadastroWindow()
        self.cadastroWindow.show()

    def reconhecer(self):
        QMessageBox.information(self, "Instruções",
                                "Aperte 'Q' para sair do reconhecimento."
                                )
        try:
            subprocess.run([sys.executable, "recognize.py"], check=True)
        except:
            QMessageBox.critical(self, "Erro", "Falha no reconhecimento facial.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
