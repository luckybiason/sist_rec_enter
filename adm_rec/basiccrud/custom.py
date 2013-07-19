#-*- coding: utf-8 -*-

##########################
##- Customização Geral -##
##########################

##- Templates utilizados
CreateView_template_name = "basic/cadastro.html" # Criação
UpdateView_template_name = "basic/cadastro.html" # Alteração
DeleteView_template_name = "basic/excluir.html"  # Exclusão 
ListView_template_name   = "basic/listagem.html" # Listagem
Detalhes_template_name   = "basic/detalhes.html" # Detalhes

##- Função para componente de listagem
from gridlist import make_table
def listagem_integracao(request, model, object_list, locals={},  with_details=False):
    return make_table(request, model, object_list, locals=locals,  with_details=with_details)

##- Função para detalhes
from gridlist import make_details
def detalhes(model,request):
    return make_details(model,request)


######### - Notas Importantes - ###########
## - Sobre Templates
'''
  - Variáveis de contexto (listagem.html):
    |-  {{ titulo }}       - Título da Página
    |-  {% url cadastro %} - URL de cadastro(criação)
    |-  {{table|safe}}     - tabela de listagem
        Nesses templates: paginator, page, num_pag(opcional)
  - Variáveis de contexto (excluir.html):
    |-  {{ object.? }}  - o objeto (pode referenciar qualquer atributo dessa model)
  - Variáveis de contexto (cadastro.html):
    |-  {{form}}  - formulario de cadastro
'''
## - Sobre Models
'''    
    - Caso precise de um contexto específico para a model. os que estão abaixo são obrigatórios
    @staticmethod
    def get_context():
        return { 
           'titulo' : "Cadastro de clientes ", # Título da Página
           'app'    : "clientes"               # OBRIGATÓRIA GERA AS URLS
        }
        
    - Url para sucesso em cadastro/alteração/exclusao (obrigatório)
    @staticmethod
    def success_url(): 
        return "clientes.listagem"
'''