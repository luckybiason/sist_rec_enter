#-*- coding: utf-8 -*-
from py_aumenu.methods import make_menu

def menu_maker(request):
    user = request.user
    menu = make_menu(user)
    return { 'MENU' : menu }