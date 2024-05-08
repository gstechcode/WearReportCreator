from tkinter import *
from components.stagetable import stagetable

class formulariostagetable(Tk):
    def __init__(self, interval= [1,12]):
        super().__init__();
        self.title("WearReportCreator")
        self.config(bg="orange", padx="10px", pady="30px")
        self.label= Label(self, text="Informe os desgastes", fg="white", bg="orange", font="TrebuchetMS 18")
        self.label.grid(row=1, column=1, pady="20px")
        self.frame1= Frame(self)
        self.frame1.grid(row= 2, column=1)
        self.stagetable= stagetable(self.frame1, interval)
        self.btn= Button(self, fg="white", text="Gerar Relatório", bg="green", relief="flat", font="Arial 18", command=self.generateReport)
        self.btn.grid(row=3, column=1, pady="20px");
        self.mainloop();
    def generateReport(self):
        self.stagetable.generatePNGS("sup");
        self.stagetable.generatePNGS("inf");