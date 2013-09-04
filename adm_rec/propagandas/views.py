#-*- coding: utf-8 -*-
from basiccrud.views          import *
from models                   import *
from django.contrib.auth.decorators import login_required

## - Propagandas
propagandas_listagem = login_required(GeneralListView.as_view(model=Propaganda))
propagandas_cadastro = login_required(GeneralCreateView.as_view(model=Propaganda, template_name='propagandas/cadastro.html'))
propagandas_editar   = login_required(GeneralUpdateView.as_view(model=Propaganda, template_name='propagandas/cadastro.html'))
propagandas_excluir  = login_required(GeneralDeleteView.as_view(model=Propaganda))