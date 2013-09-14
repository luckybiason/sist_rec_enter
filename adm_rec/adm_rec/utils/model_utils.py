# -*- coding: utf-8 -*-

get_ids     = lambda lista: [ str(item.id) for item in lista ]
get_ids_str = lambda lista: ",".join(get_ids(lista))