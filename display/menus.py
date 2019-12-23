# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# File contains all classes related to menus

from tkinter import *
from tkinter import messagebox

class menu_depart(Tk):
    def __init__(self, data):
        Tk.__init__(self)
        self.grid()
        self.title("Menu Marqueur")
        logo = self._logo = PhotoImage(file = "KBM.gif")
        CanvasLogo = Canvas(self, width = logo.width(), height = logo.height())
        CanvasLogo.create_image(0,0, anchor = NW, image = logo)
        CanvasLogo.grid(row = 0, column = 0)

        Bouton_simple = Button(self, text="Mode match simple",command=lambda : self.run_simple(data))
        #Bouton_simple_o = Button(self, text="Mode match simple officiel", command=self.run_simple_off)
        Bouton_quitter = Button(self, text="Quitter", command=quit)

        Bouton_simple.grid(row = 1, column = 0, sticky = W)
        #Bouton_simple_o.grid(row = 1, column = 1)
        Bouton_quitter.grid(row=1, column = 0, sticky = E)

    def run_simple(self, data):
        # global choix
        data.choix = 1
        self.destroy()

class menu_selection_equipe(Tk):
    def __init__(self, data):
        Tk.__init__(self)
        self.grid()
        self.title("Sélection équipes")

        LabelEquipe1 = Label(self, text="Nom de l'équipe bleu")
        LabelEquipe1.grid(row=0, column=0)
        LabelEquipe2 = Label(self, text="Nom de l'équipe grise")
        LabelEquipe2.grid(row=0, column=1)
        LabelEquipe3 = Label(self, text="Nom de l'équipe noire")
        LabelEquipe3.grid(row=0, column=2)
        EntreeBleu = Entry(self)
        EntreeBleu.grid(row=1, column=0)
        EntreeGris = Entry(self)
        EntreeGris.grid(row=1, column=1)
        EntreeNoir = Entry(self)
        EntreeNoir.grid(row=1, column=2)

        BoutonOk = Button(self, text = "Ok", command=lambda: self.close(EntreeBleu.get(), EntreeGris.get(), EntreeNoir.get(), data))
        BoutonOk.grid(row=2, column=2)
        # self.NomBleu = ""

    def close(self, B, G, N, data):
        data.nameBlueTeam = B
        data.nameGreyTeam = G
        data.nameBlackTeam = N
        self.destroy()