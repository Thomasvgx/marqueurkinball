#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter
from tkMessageBox import *

class simpleapp_tk(Tkinter.Tk):

	G = 0
	N = 0
	B = 0
	equipedehors = None
	taille = 220
	chainetaille = "-size " + str(taille)

	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()

		self.Gn = Tkinter.IntVar()
		self.Nn = Tkinter.IntVar()
		self.Bn = Tkinter.IntVar()

		self.rowconfigure(0, weight=1)

		CanvasBleu = Tkinter.Canvas(self, width = 300, height = 600, background = 'blue')
		CanvasBleu.grid(row = 0, column = 1, sticky="nsew") 
		self.columnconfigure(2, weight=1)
		CanvasGris = Tkinter.Canvas(self, width = 300, height = 600, background = 'grey')
		CanvasGris.grid(row = 0, column = 2, sticky="nsew")
		self.columnconfigure(1, weight=1)
		CanvasNoir = Tkinter.Canvas(self, width = 300, height = 600, background = 'black')
		CanvasNoir.grid(row = 0, column = 3, sticky="nsew") 
		self.columnconfigure(3, weight=1)

		nombleu = Tkinter.Label(self, text="Kin-Ball Montalbanais", bg = 'blue')
		nombleu.configure(font="-size 20")
		nombleu.grid(column = 1, row = 0, sticky="n")

		labelbleu = Tkinter.Label(self, textvariable=self.Bn, bg = 'blue')
		labelbleu.configure(font=self.chainetaille)
		labelbleu.grid(column = 1, row = 0)

		labelgris = Tkinter.Label(self, textvariable=self.Gn, bg = 'grey')
		labelgris.configure(font=self.chainetaille)
		labelgris.grid(column = 2, row = 0)


		labelnoir = Tkinter.Label(self, textvariable=self.Nn, bg = 'black', fg = 'white')
		labelnoir.configure(font=self.chainetaille)
		labelnoir.grid(column = 3, row = 0)

		BoutonBleu = Tkinter.Button(self, text="Faute aux Bleus", command = self.fauteB).grid(row=2,column=1)
		BoutonGris = Tkinter.Button(self, text="Faute aux Gris", command = self.fauteG).grid(row=2,column=2)
		BoutonNoir = Tkinter.Button(self, text="Faute aux Noirs", command = self.fauteN).grid(row=2,column=3)

		## Début Barre de menu

		BarreMenu = Tkinter.Menu(self)

		fichier = Tkinter.Menu(BarreMenu, tearoff=0)
		fichier.add_command(label="Nouveau ..", command = quit)
		fichier.add_separator()
		fichier.add_command(label="Enregister ..", command = quit)
		fichier.add_command(label="Enregistrer sous ..", command = quit)

		affichage = Tkinter.Menu(BarreMenu, tearoff=0)
		affichage.add_command(label="Plein écran ..", command = self.pleinecran)
		affichage.add_command(label="Quitter plein écran ..", command = self.quitpleinecran)

		aide = Tkinter.Menu(BarreMenu, tearoff = 0)
		aide.add_command(label="Aide en ligne")
		aide.add_separator()
		aide.add_command(label="Crédits", command = self.credit)

		BarreMenu.add_cascade(label = "Fichier", menu = fichier)
		BarreMenu.add_command(label="Remise à zéro..", command = self.remise)
		BarreMenu.add_cascade(label = "Affichage", menu = affichage)
		BarreMenu.add_cascade(label = "Aide", menu = aide) 
		self.config(menu=BarreMenu)

		## Fin Barre de menu

	def comparaison(self): # utiliser tableau pour faciliter
		
		if self.equipedehors != None:
			if self.equipedehors == 'N':
				self.Nn.set(0)
			elif self.equipedehors == 'G':
				self.Gn.set(0)
			elif self.equipedehors == 'B':
				self.Bn.set(0)
		else:
			if (self.Gn.get() == 11):
				if (self.Bn.get() > self.Nn.get()):
					self.sortie('Noirs')
					return
				else:
					self.sortie ('Bleus')
					return

			if (self.Bn.get() == 11):
				if(self.Nn.get() > self.Gn.get()):
					self.sortie('Gris')
					return
				else:
					self.sortie('Noirs')
					return

			if (self.Nn.get() == 11):
				if(self.Gn.get() > self.Bn.get()):
					self.sortie('Bleus')
					return
				else:
					self.sortie('Gris')
					return
			
	def sortie(self, couleur):
		print couleur
		if askyesno("Sortie à 11", "Est-ce que les %s sortent ?" %couleur):
			self.equipedehors = couleur[0]
			if self.equipedehors == 'N':
				self.Nn.set(0)
			elif self.equipedehors == 'G':
				self.Gn.set(0)
			elif self.equipedehors == 'B':
				self.Bn.set(0)
		else: self.equipedehors = None

	def fauteN(self):
		self.G = self.G + 1
		self.B = self.B + 1
		self.Gn.set(self.G)
		self.Bn.set(self.B)
		self.comparaison()


	def fauteB(self):
		self.G = self.G + 1
		self.N = self.N + 1
		self.Gn.set(self.G)
		self.Nn.set(self.N)
		self.comparaison()

	def fauteG(self):
		self.B = self.B + 1
		self.N = self.N + 1
		self.Nn.set(self.N)
		self.Bn.set(self.B)
		self.comparaison()

	def pleinecran(self):
		self.attributes('-fullscreen', 1)

	def quitpleinecran(self):
		self.attributes('-fullscreen', 0)
		#self.taille.set(50)

	def remise(self):
		self.G = 0
		self.N = 0
		self.B = 0
		self.Bn.set(0)
		self.Gn.set(0)
		self.Nn.set(0)
		self.equipedehors = None

	def credit(self):
		showinfo('Crédits', 'Thomas VIGROUX (Kin-Ball Montalbanais, KBM)')


		
if __name__ == '__main__':

		app = simpleapp_tk(None)
		app.title('Marqueur Kin-Ball')
		app.mainloop()
		
