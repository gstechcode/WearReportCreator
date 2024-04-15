from _tkinter import TclError
from modules.wrcgui import wrcgui;

class WRC:
    def __init__(self):
        self.gui= wrcgui();
        self.gui.MainRoot();
        
root= WRC();