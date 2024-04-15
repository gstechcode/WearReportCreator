from tkinter import *

class forminterval:
    def __init__(self, parent):
        self.parent= parent;
        self.checkStatus= IntVar();
        self.__buildComponent__();
        
    def __buildComponent__(self):
        self.frameMain = Frame(self.parent, bg="orange");
        
        self.check= Checkbutton(self.frameMain, onvalue=1, offvalue=0,text="Selecionar intervalo", bg="orange", fg="black", font="TrebuchetMS 13", variable= self.checkStatus, command= self.onOrOff);
        self.check.grid(row=1,column=1, columnspan=2, pady="20px");
        self.checkStatus.set(0);
             
        self.inicial= Entry(self.frameMain, justify="center", font="Arial 10");
        self.inicial.grid(row=2,column=1, pady="10px", padx="10px");
        self.inicial.insert(0, "1");
        self.inicial.config(state="disabled");
        self.final= Entry(self.frameMain, justify="center", font="Arial 10");
        self.final.insert(0, "12");
        self.final.config(state="disabled");
        self.final.grid(row=2,column=2, padx="10px");
        self.onOrOff();
        
    def onOrOff(self):
        if(not(self.checkStatus.get())):
            self.inicial.delete(0,END);
            self.inicial.insert(0, "1");
            self.final.delete(0,END);
            self.final.insert(0, "12");
            self.inicial.config(state="disabled");
            self.final.config(state="disabled");
        else:
            self.inicial.config(state="normal");
            self.final.config(state="normal");
            self.inicial.update();
            self.final.update();
            
    def getComponents(self):
        return {"inicial": self.inicial.get(), "final": self.final.get()}