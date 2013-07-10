#-*- coding: utf-8 -*-

def make_model_code(model , app_or_dominio_nome):
    '''
       uso (no shell : python manage.py shell):
       
from basiccrud import scaffold
from <<app>>.models import *
import <<app>>.models # para ver as models
dir(<<app>>.models)   # para ver as models
scaffold.make_model_code(<<Model>>, '<<app_nome_ou_dominio>>')

    '''
    model_name = model._meta.verbose_name
    model_class_name = str(model).split("models.")[1].split("'")[0]
    
    def _menu_item():
        return '''
                     { 
                         'titulo'    : _(u"%(verbose_name)s"),
                         'img'       : "img/icone_cadastro.gif",
                         'url-name'  : "%(app)s.listagem",
                         'id-html'   : "%(app)s",
                         'perm_need' : [''],
                     },
        '''%{ 'verbose_name' : model_name, 
              'app': app_or_dominio_nome 
         }
    
    def _detalhes():
        return '''
           ##- AJAX caso queira com detalhes
           # na urls.py inserir:
           # url(r'^detail/$',  'views.getdetail', name='%(app)s.getdetail'),
           # na views.py:
           # from basiccrud.views import general_getdetail
           # @ajax_json_view
           # def getdetail(request):
           #    return general_getdetail(%(model)s,request)
           '''%{ 'model': model_class_name, 
                 'app'  : app_or_dominio_nome 
         }
   
    
    def _make_urls():
        return '''
           ## - %(model)s
           url(r'^%(app)s/listagem/$',             GeneralListView.as_view(model=%(model)s),   name='%(app)s.listagem'),
           url(r'^%(app)s/cadastro/$',             GeneralCreateView.as_view(model=%(model)s), name='%(app)s.cadastro'),
           url(r'^%(app)s/cadastro/(?P<pk>\d+)/$', GeneralUpdateView.as_view(model=%(model)s), name='%(app)s.cadastro'),
           url(r'^%(app)s/excluir/(?P<pk>\d+)/$',  GeneralDeleteView.as_view(model=%(model)s), name='%(app)s.excluir'),
            '''%{ 'model'     : model_class_name,
                  'app'       : app_or_dominio_nome }
         
    def _apply_get_absolute_url():
        return '''
            @models.permalink
            def get_absolute_url(self):
                return ('%(app)s.cadastro', [], {'id': self.id})  
             '''%{'app' : app_or_dominio_nome }
         
    def _apply_success_url():
        return '''
            @staticmethod
                def success_url(): 
                    return "%(app)s.listagem"
             '''%{'app' : app_or_dominio_nome }
    
    def _apply_get_config():
        return '''
            @staticmethod
            def get_config():
                return { 
                   'titulo' : _(u"%(verbose_name)s"),
                   'app'    : "%(app)s",
                   # Opcional para o gridlist
                   'fields' : [ 
                       %(fields)s
                    ]
                }
            '''%{
                  'verbose_name' : model_name,
                  'app'          : app_or_dominio_nome,
                  'fields'       : "\n\t".join([ "('%s',_(u'%s'),True),"%(f.name,f.name) for f in model._meta.fields ]),
                 }   
    
    
    print "\nInstalação...",model_name,"...\n"   
    print "\nImportar: from django.utils.translation import ugettext as _ , ugettext_lazy as __\n" 
    print "\n- na model ...\n\n"
    print _apply_get_config(),"\n"
    print _apply_success_url(),"\n"
    print _apply_get_absolute_url(),"\n"
    print "\n- urls ...\n"
    print _make_urls()
    print "\n- detalhes (opcional) ...\n"
    print _detalhes()
    print "\n- menu ...\n"
    print  _menu_item()
    



