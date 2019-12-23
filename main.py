#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter         import *
from tkinter         import messagebox
from display.menus   import menu_depart
from display.menus   import menu_selection_equipe
from display.app     import marqueur
from data.managedata import dataManager

if __name__ == '__main__':
	data = dataManager()
	menu = menu_depart(data)
	menu.mainloop()
	
	if data.choix == 1:
		selectTeam = menu_selection_equipe(data)
		selectTeam.mainloop()
		marqueur = marqueur("Match simple", data)
		marqueur.mainloop()
	
	# elif choix == 2:
	# 	selection = menu_selection_equipe()
	# 	selection.mainloop()
	# 	marqueur = marqueur("Match simple officiel")
	# 	marqueur.mainloop()

		