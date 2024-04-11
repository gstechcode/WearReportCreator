from tkinter import *
from components.stagetable import stagetable;

class wrcgui:
    def __init__(self):
        self.root= Tk();
        self.root.title("WearReportCreator - 2024 Edition");
        self.root.config(bg="orange", padx="30px", pady="30px")
    def MainForm(self):
        self.frameMain= Frame(self.root);
        self.frameMain.pack();
        self.tabletop= stagetable(self.frameMain,[1,12]);
        self.root.mainloop();
        