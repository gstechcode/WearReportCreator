from tkinter import *
from components.entrywithplaceholder import entrywithplaceholder;

class formdatacase:
    def __init__(self, parent, fileselector="", button="", checkboxtext= "Selecione um item"):
        self.checkboxtext= checkboxtext;
        self.button= button;
        self.fileselector= fileselector;
        self.parent= parent;
        self.checkStatus= IntVar();
        self.__buildComponent__();
        
    def __buildComponent__(self):
        self.frameMain = Frame(self.parent, bg="orange");
        
        self.check= Checkbutton(self.frameMain, onvalue=1, offvalue=0,text= self.checkboxtext, bg="orange", fg="black", font="TrebuchetMS 13", variable= self.checkStatus, command= self.onOrOff);
        self.check.grid(row=1,column=1, columnspan=2, pady="20px");
        self.checkStatus.set(0);
             
        self.paciente= entrywithplaceholder(self.frameMain, "Nome do Paciente", color="grey", font="Arial 10", justify="center", relief="flat")
        self.paciente.grid(row=2,column=1, pady="10px", padx="10px");
        self.paciente.config(state="disabled");
        self.dentista= entrywithplaceholder(self.frameMain, "Nome do Dentista", color="grey", font="Arial 10", justify="center", relief="flat")
        self.dentista.grid(row=2,column=2, padx="10px");
        self.dentista.config(state="disabled");
        self.onOrOff();
        
    def onOrOff(self):
        if(not(self.checkStatus.get())):
            self.fileselector.mainFrame.grid(row=2, column=1, columnspan=12);
            self.button.grid_forget(); 
            self.paciente.foc_out();
            self.dentista.foc_out();
            self.paciente.config(state="disabled");
            self.dentista.config(state="disabled");
        else:
            self.fileselector.mainFrame.grid_forget();
            self.button.grid(row=6, column=1, columnspan= 12, pady="20px");
            self.paciente.config(state="normal");
            self.dentista.config(state="normal");
            self.paciente.update();
            self.dentista.update();
            
    def getComponents(self):
        return {"paciente": self.paciente.get(), "dentista": self.dentista.get()}