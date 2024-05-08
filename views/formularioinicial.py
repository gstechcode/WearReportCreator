from PySide6 import QtWidgets, QtCore, QtGui;
from PySide6.QtWidgets import *
import os
from tkinter import filedialog
from views.formulariostagetable import formulariostagetable;

class formularioinicial(QtWidgets.QWidget):
     def __init__(self):
        super().__init__();
        self.setStyleSheet("""QWidget{background: orange}""");
        self.setWindowTitle("WearReportCreator");
        
        self.title= QLabel(parent=self, text="WearReportCreator");
        self.title.setGeometry(225,0,300,100);
        self.title.setStyleSheet("color: white; font-family: Trebuchet MS; font-size: 30px");
        

        self.manual= QGroupBox(self, title="Entrada Manual");
        self.manual.setGeometry(20,225,300,150);
        self.manual.setStyleSheet("""
            QGroupBox{
                background: transparent;
                font-size: 15px;
            }
            QGroupBox:title{
                background: orange;
                color: white;
            }
                                 """);
        
        self.OS= QLineEdit(parent= self);
        self.OS.setAlignment(QtCore.Qt.AlignCenter);
        self.OS.setPlaceholderText("Número da OS");
        self.OS.setGeometry(205,130, 300, 50);
        self.OS.setStyleSheet("background: white; border: 0; font-size: 20px; padding: 5px; font-family: Trebuchet MS; border-radius: 5px; text-align: center");

        self.paciente= QLineEdit(parent= self.manual);
        self.paciente.setGeometry(10,40, 280, 30);
        self.paciente.setAlignment(QtCore.Qt.AlignCenter);
        self.paciente.setPlaceholderText("Nome do Paciente");
        self.paciente.setStyleSheet("background: white; border: 0; font-size: 16px; padding: 5px; font-family: Trebuchet MS; border-radius: 5px; text-align: center");

        
        self.dentista= QLineEdit(parent= self.manual);
        self.dentista.setGeometry(10,80, 280, 30);
        self.dentista.setAlignment(QtCore.Qt.AlignCenter);
        self.dentista.setPlaceholderText("Nome do Dentista");
        self.dentista.setStyleSheet("background: white; border: 0; font-size: 16px; padding: 5px; font-family: Trebuchet MS; border-radius: 5px; text-align: center");

        
        self.buttonReady= QPushButton("Selecione um arquivo", parent=self);
        self.buttonReady.setStyleSheet("""
            QPushButton{
                color: white;
                font: Arial;
                font-size: 15px;
                background: orange;
                padding: 10px;
                border: 1px solid white;
                border-radius: 5px;
            }
            
            QPushButton::pressed{
                background: lightgreen;
            }
            """);
        
        self.buttonReady.setGeometry(350,320,300,50)
        
        self.checkManual= QCheckBox(parent= self, text="Entrada Manual");
        self.checkManual.setGeometry(350,230,200,50);
        self.checkManual.setStyleSheet("""
            color: white;
            font-size: 15px;
                                       """);
        
        self.checkArquivo= QCheckBox(parent= self, text="Entrada CFG");
        self.checkArquivo.setGeometry(350,270,200,50);
        self.checkArquivo.setStyleSheet("""
            color: white;
            font-size: 15px;
                                       """);
        
        self.intervalo= QGroupBox(self);
        self.intervalo.setGeometry(350,420,300,100);
        self.intervalo.setStyleSheet("""
            QGroupBox{
                background: transparent;
                font-size: 15px;
            }
            QGroupBox:title{
                background: orange;
                color: white;
            }
                                 """);
        
        self.checkIntervalo= QCheckBox(parent= self, text="Definir Intervalo");
        self.checkIntervalo.setGeometry(380,390,170,50);
        self.checkIntervalo.setStyleSheet("""
            color: white;
            font-size: 15px;
            padding-left: 20px;
            padding-right: 20px;
                                       """);
        
        self.inicial= QLineEdit(parent= self.intervalo);
        self.inicial.setStyleSheet("""
            padding: 5px;
            border-radius: 5px;
            background: white;
            font-size: 20px;
                                   """);
        self.inicial.setGeometry(20,30,100,50);
        self.inicial.setPlaceholderText("Inicial");
        self.inicial.setAlignment(QtCore.Qt.AlignCenter);
        
        self.final= QLineEdit(parent= self.intervalo);
        self.final.setStyleSheet("""
            padding: 5px;
            border-radius: 5px;
            background: white;
            font-size: 20px;
                                   """);
        self.final.setGeometry(150,30,100,50);
        self.final.setPlaceholderText("Final");
        self.final.setAlignment(QtCore.Qt.AlignCenter);
        
        self.manual.setDisabled(True);
        self.checkArquivo.setChecked(True);
        self.intervalo.setDisabled(True);
        self.inicial.setText("1");
        self.final.setText("12");
        
        self.errorbar= QMessageBox()
        self.errorbar.setIcon(QMessageBox.Critical);
        
        self.checkManual.stateChanged.connect(self.checkManualFunc);
        self.checkArquivo.stateChanged.connect(self.checkArquivoFunc);
        self.checkIntervalo.stateChanged.connect(self.checkIntervaloFunc);
        self.buttonReady.clicked.connect(self.searchFile);
        
     def checkIntervaloFunc(self):
        if(self.checkIntervalo.isChecked()):
            self.intervalo.setDisabled(False);
            self.inicial.clear();
            self.final.clear();
        else:
            self.intervalo.setDisabled(True);
            self.inicial.setText("1");
            self.final.setText("12");
         
     def checkManualFunc(self):
        if(self.checkManual.isChecked()):
            self.manual.setDisabled(False);
            self.checkArquivo.setChecked(False);
        else:
            self.paciente.clear();
            self.dentista.clear();
            self.manual.setDisabled(True);
            self.checkArquivo.setChecked(True);
            
     def checkArquivoFunc(self):
        if(self.checkArquivo.isChecked()):
            self.paciente.clear();
            self.dentista.clear();
            self.manual.setDisabled(True);
            self.checkManual.setChecked(False);
            self.checkArquivo.setChecked(True);
            self.buttonReady.setDisabled(False);
        else:
            self.manual.setDisabled(False);
            self.checkManual.setChecked(True);
            self.checkArquivo.setChecked(False);
            
     def searchFile(self):
         self.fileSelected= filedialog.askdirectory(title="Escolha o arquivo CFG");
         
         if(self.fileSelected == ""):
             pass
         else:
             erro= 0;
             if(self.checkManual.isChecked()):
                 if(self.paciente.text() == ""):
                     print("Executei aqui")
                     self.displayError("Atenção - Campos não preenchidos", "Campo paciente não foi preenchido!");
                     return 0;
                 if(self.dentista.text() == ""):
                     self.displayError("Atenção - Campos não preenchidos", "Campo dentista não foi preenchido!")
                     return 0;
             if(self.OS.text() == ""):
                 self.displayError("Atenção - Campos não preenchidos", "Campo OS não foi preenchido!")
                 return 0;
             if(self.inicial.text() ==""):
                 self.displayError("Atenção - Campos não preenchidos", "Campo Inicial não foi preenchido!")
                 return 0;
             if(self.final.text() ==""):
                 self.displayError("Atenção - Campos não preenchidos", "Campo Final não foi preenchido!")
                 return 0;
             if(os.path.exists(self.fileSelected + "\\cfg\\cfg.json") and os.path.exists(self.fileSelected + "\\cfg\\Model.svg")):
                 self.buttonReady.setText(self.fileSelected);
                 self.destroy();
                 self.nextPage= formulariostagetable(interval=[int(self.inicial.text()), int(self.final.text())]);
             if(not(os.path.exists(self.fileSelected + "\\cfg\\cfg.json")) or not(os.path.exists(self.fileSelected + "\\cfg\\Model.svg"))):
                 if(not(os.path.exists(self.fileSelected + "\\cfg\\cfg.json")) and not(os.path.exists(self.fileSelected + "\\cfg\\Model.json"))):
                    self.displayError("Erro - Arquivo(s) ausente(s)","A pasta informada está com arquivos ausentes na pasta cfg.\n\nArquivo(s) Faltante(s):\n\n- cfg.json \n - Model.svg");
                 elif(not(os.path.exists(self.fileSelected + "\\cfg\\cfg.json"))):
                    self.displayError("Erro - Arquivo(s) ausente(s)","A pasta informada está com arquivos ausentes na pasta cfg.\n\nArquivo(s) Faltante(s):\n\n- cfg.json");
                 elif(not(os.path.exists(self.fileSelected + "\\cfg\\Model.svg"))):
                    self.displayError("Erro - Arquivo(s) ausente(s)","A pasta informada está com arquivos ausentes na pasta cfg.\n\nArquivo(s) Faltante(s):\n\n- Model.svg");
                     
     def displayError(self, title, error):
         self.errorbar.setWindowTitle(title);
         self.errorbar.setText(error);
         self.errorbar.show();
class formularioinicialapp:
    def __init__(self):
        self.app= QtWidgets.QApplication();
        self.widget= formularioinicial();
        self.widget.show();
        self.widget.resize(700,550);
        self.app.exec();  
        
