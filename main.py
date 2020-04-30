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
    # menu = menu_depart(data)
    # menu.mainloop()

    selectTeam = menu_selection_equipe(data)
    selectTeam.mainloop()
    mainMarqueur = marqueur("Match", data)
    mainMarqueur.mainloop()