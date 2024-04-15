from tkinter import *
from tkinter import filedialog
import json

class fileselector:
    def __init__(self, parent, placeholder, nextDisplay,fg="white", bg= "orange", fontSize=13):
        self.parent= parent;
        self.fontSize= fontSize;
        self.nextDisplay= nextDisplay;
        self.bg= bg;
        self.fg= fg;
        self.placeholder= placeholder;
        self.__buildComponent__();
        
    def __buildComponent__(self):
        self.mainFrame= Frame(self.parent, bg="orange");
        self.label= Button(self.mainFrame, command=self.selectFile,relief="groove",text= self.placeholder, bg= self.bg, fg= self.fg, borderwidth=1, highlightbackground = self.fg, highlightthickness = 10, font= f"TrebuchetMS {self.fontSize}");
        self.label.pack()
        
    def selectFile(self):
        file= filedialog.askopenfile(title="Selecione um arquivo");
        fileContent= "";

        for line in file.readlines():
            fileContent += line;
            
        fileContentModeJson= json.loads(fileContent);
        
        self.fileContentModeJson= fileContentModeJson;
        
        self.parent.pack_forget();
        
        self.nextDisplay();
        
        
        
        
    
    
    