from tkinter import *
from components.stagetable import stagetable;
from components.fileselector import fileselector;
from components.forminterval import forminterval;
from components.entrywithplaceholder import entrywithplaceholder;
from components.formdatacase import formdatacase;

class wrcgui:
    def __init__(self):
        self.root= Tk();
        self.root.title("WearReportCreator - 2024 Edition");
        self.root.config(bg="orange", padx="70px")
    def MainForm(self):
        self.frameMain= Frame(self.root);
        self.frameMain.grid(row=2, column=1, columnspan=12, pady="20px");
        self.tabletop= stagetable(self.frameMain,[1,12]);
        self.root.mainloop();
    def MainRoot(self):
        self.frameMain= Frame(self.root, bg="orange");
        self.frameMain.grid(row=2, column=1, columnspan=12, pady="20px");
        tituloapp= Label(self.root, text="WearReportCreator - App", fg="white", bg="orange", font="TrebuchetMS 20 bold");
        tituloapp.grid(row=1, column=1, columnspan=12, pady="30px");
        self.formOS= entrywithplaceholder(self.frameMain, "Digite o número da OS", color="grey", font="Arial 12", relief="flat", justify="center");
        self.formOS.grid(row=3, column=1, columnspan=12, pady="20px");
        self.fileJSON= fileselector(self.frameMain,"Selecione o arquivo do caso", self.loadVars);
        self.fileJSON.mainFrame.grid(row=2, column=1, columnspan=12);
        self.button= Button(self.frameMain, text="Pronto", bg="green", fg="white", font="Arial 13", relief="flat", command=self.loadVars)
        self.button.grid(row=6, column=1, columnspan= 12, pady="20px");
        self.formDataCase= formdatacase(self.frameMain, checkboxtext="Inserir dentista e paciente manualmente", fileselector= self.fileJSON, button= self.button);
        self.formDataCase.frameMain.grid(row=4, column=1, columnspan=12);
        self.formInterval= forminterval(self.frameMain);
        self.formInterval.frameMain.grid(row=5, column=1, columnspan= 12);
        self.root.mainloop();
    def loadVars(self):
        if(self.formDataCase.checkStatus.get()):
            self.dataCase= self.formDataCase.getComponents();
        else:
            self.dataCase= {
                "paciente": self.fileJSON.fileContentModeJson["paciente"],
                "dentista": self.fileJSON.fileContentModeJson["dentista"]     
            }

        self.OS= self.formOS.get();
        self.interval= self.formInterval.getComponents();
        print(self.dataCase,self.OS,self.interval);
        self.MainForm();
        