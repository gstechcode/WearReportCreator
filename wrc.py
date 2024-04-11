from modules.wrcgui import wrcgui

class WRC:
    def __init__(self):
        self.gui= wrcgui();
        
root= WRC();
root.gui.MainForm();