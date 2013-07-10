#-*- coding: utf-8 -*-
from django.views.generic        import *
from django.views.generic.list   import MultipleObjectMixin, BaseListView
from operator                    import attrgetter
from mixins                      import *
from custom                      import *
from django.contrib              import messages
from django.shortcuts            import render
from django.views.generic.edit   import BaseCreateView
from django.utils.translation    import ugettext as _, ugettext_lazy as __
## - Detalhes (via Ajax)

def general_getdetail(model,request,template=Detalhes_template_name):
    details = detalhes(model,request)
    html    = render(request,template,locals()).content
    return { 'html':html, }

## - Listagem

class GeneralListView(ListContextMixin, ListView, BaseCreateView):
    template_name = ListView_template_name
    with_details  = False 
    
    def get(self, request, *args, **kwargs):
        self.paginate_by = int(request.GET.get("per_page","5"))
        return super(ListView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        # captura do contexto da model
        contextP = super(GeneralListView, self).get_context_data(**kwargs)
        per_page     = self.paginate_by
        with_details = self.with_details
        paginator, page, object_list, is_paginated = self.paginate_queryset(self.get_queryset(), per_page)
        params       = listagem(self.request, self.model, object_list, locals=locals(), with_details=self.with_details)
        return dict(contextP.items()  +locals().items() + params.items())

## - Criação, Deleção e Exclusão

class GeneralCreateView(BasicContextMixin,FormMessageMixin, CreateView):
    template_name = CreateView_template_name 
    msg_success   = _(u"Criado com sucesso.")
    msg_error     = _(u"um erro ocorreu.")

class GeneralUpdateView(BasicContextMixin,FormMessageMixin, UpdateView):
    template_name = UpdateView_template_name
    msg_success   = _(u"Alterado com sucesso.")
    msg_error     = _(u"um erro ocorreu.")

class GeneralDeleteView(BasicContextMixin, DeleteView):
    template_name = DeleteView_template_name 
    def delete(self, request, *args, **kwargs):
        messages.success(self.request,_(u"Deletado com sucesso."))
        return DeleteView.delete(self, request, *args, **kwargs)

class GeneralProtectDeleteView(BasicContextMixin,DeleteVerificaMixin, DeleteView):
    template_name = DeleteView_template_name 
       