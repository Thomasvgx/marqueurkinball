#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
# from tkMessageBox import *

#Classe gérant le menu où on donne un nom aux équipes

class menu_selection_equipe(Tk):
	def __init__(self):
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

		BoutonOk = Button(self, text = "Ok", command=lambda: self.close(EntreeBleu.get(), EntreeGris.get(), EntreeNoir.get()))
		BoutonOk.grid(row=2, column=2)
		self.NomBleu = ""

	def close(self, B, G, N):
		global Equipes
		Equipes = [B,G,N]
		self.destroy()


# Classe gérant le premier menu au départ de l'application

class menu_depart(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.grid()
		self.title("Menu Marqueur")
		logo = self._logo = PhotoImage(file = "KBM.gif")
		CanvasLogo = Canvas(self, width = logo.width(), height = logo.height())
		CanvasLogo.create_image(0,0, anchor = NW, image = logo)
		CanvasLogo.grid(row = 0, column = 0)

		Bouton_simple = Button(self, text="Mode match simple",command=self.run_simple)
		#Bouton_simple_o = Button(self, text="Mode match simple officiel", command=self.run_simple_off)
		Bouton_quitter = Button(self, text="Quitter", command=quit)

		Bouton_simple.grid(row = 1, column = 0)
		#Bouton_simple_o.grid(row = 1, column = 1)
		Bouton_quitter.grid(row=1, column = 0)

	def run_simple(self):
	 	global choix
	 	choix = 1
	 	self.destroy()

	# def run_simple_off(self):
	# 	global choix
	# 	choix = 2
	# 	self.destroy()


# Classe principale de l'application gérant la fenetre de marquage


class marqueur(Tk):
	G = 0
	N = 0
	B = 0
	equipedehors = None
	taille = 220
	chainetaille = "-size " + str(taille)

	def __init__(self, nom):
		Tk.__init__(self)
		self.title(nom)
		self.grid()
		global Equipes
		# IntVar sont les variables d'affichage de Tkinter
		self.Gn = IntVar()
		self.Nn = IntVar()
		self.Bn = IntVar()
		self.EquipeBleu = StringVar()
		self.EquipeGris = StringVar()
		self.EquipeNoir = StringVar()
		self.i = 0
		self.Hist = []
		self.HistoryFile = open("HistoryFile.data", "w")
		self.rowconfigure(0, weight=1)

		CanvasBleu = Canvas(self, width = 300, height = 600, background = 'blue')
		CanvasBleu.grid(row = 0, column = 1, sticky="nsew") 
		self.columnconfigure(2, weight=1)
		CanvasGris = Canvas(self, width = 300, height = 600, background = 'grey')
		CanvasGris.grid(row = 0, column = 2, sticky="nsew")
		self.columnconfigure(1, weight=1)
		CanvasNoir = Canvas(self, width = 300, height = 600, background = 'black')
		CanvasNoir.grid(row = 0, column = 3, sticky="nsew") 
		self.columnconfigure(3, weight=1)

		# Affichage du nom des équipes

		if choix == 1:
			self.EquipeBleu.set(Equipes[0])
			self.EquipeGris.set(Equipes[1])
			self.EquipeNoir.set(Equipes[2])
			nombleu = Label(self, textvariable=self.EquipeBleu, bg = 'blue')
			nombleu.configure(font="-size 50")
			nombleu.grid(column = 1, row = 0, sticky="n")
			nomgris = Label(self, textvariable=self.EquipeGris, bg = 'grey')
			nomgris.configure(font="-size 50")
			nomgris.grid(column = 2, row = 0, sticky="n")
			nomnoir = Label(self, textvariable=self.EquipeNoir, bg = 'black', fg = 'white')
			nomnoir.configure(font="-size 50")
			nomnoir.grid(column = 3, row = 0, sticky="n")

		labelbleu = Label(self, textvariable=self.Bn, bg = 'blue')
		labelbleu.configure(font=self.chainetaille)
		labelbleu.grid(column = 1, row = 0)

		labelgris = Label(self, textvariable=self.Gn, bg = 'grey')
		labelgris.configure(font=self.chainetaille)
		labelgris.grid(column = 2, row = 0)


		labelnoir = Label(self, textvariable=self.Nn, bg = 'black', fg = 'white')
		labelnoir.configure(font=self.chainetaille)
		labelnoir.grid(column = 3, row = 0)

		BoutonBleu = Button(self, text="Faute aux Bleus", command = self.fauteB).grid(row=2,column=1)
		BoutonGris = Button(self, text="Faute aux Gris", command = self.fauteG).grid(row=2,column=2)
		BoutonNoir = Button(self, text="Faute aux Noirs", command = self.fauteN).grid(row=2,column=3)

		# Gestion de la barre des menus

		BarreMenu = Menu(self)

		fichier = Menu(BarreMenu, tearoff=0)
		fichier.add_command(label="Nouveau ..", command = quit)
		#fichier.add_separator()
		#fichier.add_command(label="Enregister ..", command = quit)
		#fichier.add_command(label="Enregistrer sous ..", command = quit)

		affichage = Menu(BarreMenu, tearoff=0)
		affichage.add_command(label="Plein écran ..", command = self.pleinecran)
		affichage.add_command(label="Quitter plein écran ..", command = self.quitpleinecran)

		aide = Menu(BarreMenu, tearoff = 0)
		aide.add_command(label="Aide en ligne")
		aide.add_separator()
		aide.add_command(label="Crédits", command = self.credit)

		BarreMenu.add_cascade(label = "Fichier", menu = fichier)
		BarreMenu.add_command(label = "Précédent ..", command = self.revenir_en_arriere)
		BarreMenu.add_command(label="Remise à zéro..", command = self.remise)
		BarreMenu.add_cascade(label = "Affichage", menu = affichage)
		BarreMenu.add_cascade(label = "Aide", menu = aide) 
		self.config(menu=BarreMenu)

	# Méthode pour revenir à l'état précédent

	def revenir_en_arriere(self):
		self.Hist = self.Hist[:-1]
		self.B = self.Hist[len(self.Hist)-1][0]
		self.G = self.Hist[len(self.Hist)-1][1]
		self.N = self.Hist[len(self.Hist)-1][2]
		self.Bn.set(self.B)
		self.Gn.set(self.G)
		self.Nn.set(self.N)

	# Méthode qui gère le calcul des points après la sortie d'une équipe

	def comparaison(self):
		if self.equipedehors != None:
			if self.equipedehors == 'N':
				self.Nn.set(0)
				self.N = 0
			elif self.equipedehors == 'G':
				self.Gn.set(0)
				self.G = 0
			elif self.equipedehors == 'B':
				self.Bn.set(0)
				self.B = 0
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
		self.Hist.append([self.B, self.G, self.N])

	# Méthode qui gère le moment où une équipe doit sortir

	def sortie(self, couleur):
		print (couleur)
		if messagebox.askyesno("Sortie à 11", "Est-ce que les %s sortent ?" %couleur):
			self.equipedehors = couleur[0]
			if self.equipedehors == 'N':
				self.Nn.set(0)
				#self.N = 0
				BoutonNoir = Button(self, text = "Faute aux Noirs", state = "disabled").grid(row=2,column=3)
			elif self.equipedehors == 'G':
				self.Gn.set(0)
				#self.G = 0
				BoutonGris = Button(self, text = "Faute aux Gris", state = "disabled").grid(row=2, column=2)
			elif self.equipedehors == 'B':
				self.Bn.set(0)
				#self.B = 0
				BoutonBleu = Button(self, text = "Faute aux Bleus", state = "disabled").grid(row=2, column=1)
		else: self.equipedehors = None

	# Les 3 méthodes faute gèrent les points après une faute

	def fauteN(self):
		if messagebox.askyesno ('Confirmation', 'Faute aux noirs ?'):
			self.G = self.G + 1
			self.B = self.B + 1
			self.Gn.set(self.G)
			self.Bn.set(self.B)
			self.comparaison()
			# self.write_history()

	def fauteB(self):
		if messagebox.askyesno('Confirmation', 'Faute aux bleus ?'):
			self.G = self.G + 1
			self.N = self.N + 1
			self.Gn.set(self.G)
			self.Nn.set(self.N)
			self.comparaison()

	def fauteG(self):
		if messagebox.askyesno('Confirmation', 'Faute aux gris ?'):
			self.B = self.B + 1
			self.N = self.N + 1
			self.Nn.set(self.N)
			self.Bn.set(self.B)
			self.comparaison()

	# def write_history(self):
	#	#self.HistoryFile.write("%d\t%d\t%d", self.B, self.G, self.N)
	#	self.HistoryFile.write("%d", self.N)

	def pleinecran(self):
		self.attributes('-fullscreen', 1)

	def quitpleinecran(self):
		self.attributes('-fullscreen', 0)

	# Méthode pour la remise à 0

	def remise(self):
		self.G = 0
		self.N = 0
		self.B = 0
		self.Bn.set(0)
		self.Gn.set(0)
		self.Nn.set(0)
		self.equipedehors = None
		BoutonBleu = Button(self, text="Faute aux Bleus", command = self.fauteB).grid(row=2,column=1)
		BoutonGris = Button(self, text="Faute aux Gris", command = self.fauteG).grid(row=2,column=2)
		BoutonNoir = Button(self, text="Faute aux Noirs", command = self.fauteN).grid(row=2,column=3)
		self.Hist = []

	def credit(self):
		messagebox.showinfo('Crédits', 'Thomas VIGROUX (Kin-Ball Montalbanais, KBM)')

if __name__ == '__main__':
	menu = menu_depart()
	menu.mainloop()
	if choix == 1:
		menu_selection_equipe().mainloop()
		marqueur = marqueur("Match simple")
		marqueur.mainloop()
	# elif choix == 2:
	# 	selection = menu_selection_equipe()
	# 	selection.mainloop()
	# 	marqueur = marqueur("Match simple officiel")
	# 	marqueur.mainloop()

		