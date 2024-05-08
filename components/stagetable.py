from tkinter import *
import PIL
import os
from PIL import ImageFont
from pillowdrawtable.drawtable import Drawtable

class stagetable:
    def __init__(self, parent: Frame, interval: list):
        self.rawInterval= interval;
        self.__defineglobals__();
        self.parentFrame= Frame(parent, bg="orange");
        self.parentFrame.pack();
        self.tabelaSuperior= self.createTable(supOrInf="sup");
        self.tabelaSuperior.grid(row=1,column=1, padx="10px");
        self.tabelaInferior= self.createTable(supOrInf="inf");
        self.tabelaInferior.grid(row=1,column=2, padx="10px");
        
    def createTable(self, supOrInf) -> Frame:
        localFrame= Frame(self.parentFrame, bg="orange");
        
        #Cria duas legendas da tabela
        self.legendDentes= Label(localFrame, text="Dentes", bg="orange", fg="white", height= 2, font="Arial 12 bold");
        self.legendDentes.grid(row=1, column=1, rowspan=2);
        self.legendPlacas= Label(localFrame, text="Placas",bg="orange", fg="white", highlightbackground = "black", font="Arial 12 bold");
        self.legendPlacas.grid(row=1, column=2, columnspan=12);
        
        #Cria o Indice Coluna X
        for cell in self.indiceX:
            label= Label(localFrame, text= str(cell), bg="orange", fg="white", font="Arial 12");
            label.grid(row=2, column= (self.indiceX.index(cell) + 2));

        if (supOrInf == "sup"):
            #Cria o Indice Coluna Y Superior
            for cell in self.indiceYTop:
                label = Label(localFrame, text= str(cell), bg="orange", fg="white", font="Arial 12 bold");
                label.grid(row= (self.indiceYTop.index(cell) + 3), column= 1);
            
            #variaveis auxiliares para coluna e linha
            rowAux= 3;
            columnAux= 2;
            #Cria as Entrys da Matriz Tabela
            for celula in self.indiceYTop:
                for coluna in self.indiceX:
                    self.mapObjects[celula + "_" + str(coluna)] = Entry(localFrame, width= 5, relief="flat", borderwidth=1, justify="center", highlightbackground = "black", highlightthickness = 0.5);
                    self.mapObjects[celula + "_" + str(coluna)].grid(row= rowAux, column= columnAux);
                    columnAux += 1
                rowAux += 1;
                columnAux= 2;
        else:
            #Cria o Indice Coluna Y Inferior
            for cell in self.indiceYBottom:
                label = Label(localFrame, text= str(cell), bg="orange", fg="white", font="Arial 12 bold");
                label.grid(row= (self.indiceYBottom.index(cell) + 3), column= 1);
            
            #variaveis auxiliares para coluna e linha
            rowAux= 3;
            columnAux= 2;
            #Cria as Entrys da Matriz Tabela
            for celula in self.indiceYBottom:
                for coluna in self.indiceX:
                    self.mapObjects[celula + "_" + str(coluna)] = Entry(localFrame, width= 5, relief="flat", borderwidth=1, highlightbackground = "black", highlightthickness = 0.5, justify="center");
                    self.mapObjects[celula + "_" + str(coluna)].grid(row= rowAux, column= columnAux);
                    columnAux += 1
                rowAux += 1;
                columnAux= 2;
                
        return localFrame
            

        
        
    def __defineglobals__(self): # função por responsável por definir as variáveis globais
        try:
            os.mkdir(os.environ["USERPROFILE"] + "\\WRC");
        except Exception:
            pass
        widgets_height= 15;
        self.mapObjects= {};
        self.indiceX= self.getInterval();
        self.indiceYTop= ["18/17","17/16","16/15","15/14","14/13","13/12","12/11","11/21","21/22","22/23","23/24","24/25","25/26","26/27","27/28"];
        self.indiceYBottom= ["38/37","37/36","36/35","35/34","34/33","33/32","32/31","31/41","41/42","42/43","43/44","44/45","45/46","46/47","47/48"];
           
    def getInterval(self) -> list: #retorna os indicesX que serão as etapas
        interval= [];
        for i in range(self.rawInterval[0],self.rawInterval[1] + 1):
            interval.append(i);
            
        return interval;
    

    def generatePNGS(self, op):
        self.text_font =   PIL.ImageFont.truetype("arial.ttf", 20) #PIL.ImageFont.truetype(FONT_PATH,FONTSIZE)
        self.header_font =   PIL.ImageFont.truetype("arial.ttf", 20)
        
        tdata= [[""],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]];
        aux=0 
        
        print(self.indiceX)
        
        if(op == "sup"):
            filename= os.environ["USERPROFILE"] + "\\WRC\\sup.png";
            for cell in self.indiceX:
                tdata[0].append(cell);
            for item in tdata:
                if(aux == 0):
                    pass
                else:
                    tdata[aux].append(self.indiceYTop[aux-1]);
                aux += 1
            for cell in self.mapObjects:
                for item in tdata:
                    if(cell.split("_")[0] in item[0]):
                        item.append(self.mapObjects[cell].get());
                        
                        
        else:
            filename= os.environ["USERPROFILE"] + "\\WRC\\inf.png";
            for cell in self.indiceX:
                tdata[0].append(cell);
            for item in tdata:
                if(aux == 0):
                    pass
                else:
                    tdata[aux].append(self.indiceYBottom[aux-1]);
                aux += 1
            for cell in self.mapObjects:
                for item in tdata:
                    if(cell.split("_")[0] in item[0]):
                        item.append(self.mapObjects[cell].get());
    
        
                
        print(tdata);
        
        
        table = Drawtable(
            data=tdata,
            x=0,
            xend=1714,
            y=0,
            font=self.text_font,
            line_spacer=16,
            margin_text=10,
            image_width=1714,
            image_height=550,
            frame=True,
            grid=True,
            columngrid=True,
            rowgrid=True,
            header=True,
            text_color='black',
            header_color='black',
            headerfont=self.header_font,
            save= filename,
            kwargs= {"text_align": "center", "anchor": "c"}
        );
    
        table.draw_table()
    