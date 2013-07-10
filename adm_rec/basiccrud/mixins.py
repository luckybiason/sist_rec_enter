#-*- coding: utf-8 -*-
from django.views.generic        import *
from basiccrud.custom          import *
from django.views.generic.list   import MultipleObjectMixin
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers    import reverse
from django.utils.decorators     import method_decorator
from django.contrib              import messages
from django.utils.translation    import ugettext as _ , ugettext_lazy as __

''' 
#########################################################################
   Geradores de contexto: 
   -Capturam as urls_names a partir no nome da model e do sufixo determinado
#########################################################################
'''
def catch_urls(model):
        appname     = model.get_config()["app"]
        url_context = {
                       'cadastro'   : appname+".cadastro",
                       'excluir'    : appname+".excluir",
                       'listagem'   : appname+".listagem",
                       'detail_ajax': appname+".getdetail",
        }
        return url_context
    
# - Para usar em listagem
class ListContextMixin(object):
    
    def get_context_data(self, **kwargs):
        contextP    = super(ListContextMixin, self).get_context_data(**kwargs)
        url_context = catch_urls(self.model).items()
        return dict(contextP.items()+url_context+self.model.get_config().items())

# - Para usar em cadastros
#   (necessário o método statico success_url() na model)
class BasicContextMixin(SingleObjectMixin):
    
    def get_success_url (self, **kwargs):
        return reverse(self.model.success_url())
    
    def get_context_data(self, **kwargs):
        contextP    = super(BasicContextMixin, self).get_context_data(**kwargs)
        url_context = catch_urls(self.model).items()
        return dict(contextP.items()+url_context+self.model.get_config().items())   

# - Controle de Mensagens para criaçao e exclusão
class FormSuccessMixin(object):
    msg_success = __(u"Sucesso.")
    def form_valid(self, form):
        messages.success(self.request,self.msg_success)
        return super(FormSuccessMixin, self).form_valid(form)

class FormErrorMixin(object):
    msg_error = __(u"Erro.")
    def form_invalid(self, form):
        messages.error(self.request,self.msg_error)
        return  super(FormErrorMixin, self).form_invalid(form)

class FormMessageMixin(FormSuccessMixin,FormErrorMixin):
    pass    

class DeleteVerificaMixin(object):
    def delete(self, request, *args, **kwargs):
        if self.model._meta.get_all_related_objects():            
            for related_object in self.model._meta.get_all_related_objects():
                related = related_object.model.objects
                campo   = related_object.field.get_attname().replace('_id','')
                if related.get_query_set().filter(**{campo.lower():id}):
                    messages.error(self.request,__(u"O Registro contêm outros registros que dependem dele."))
                    return False
            messages.success(self.request,__(u"Deletado com sucesso."))
            return super(DeleteVerificaMixin, self).delete(self, request, *args, **kwarg)
        else:                   
            messages.success(self.request,__(u"Deletado com sucesso."))    
            return super(DeleteVerificaMixin, self).delete(self, request, *args, **kwarg)
   
###################################################################
        
class SelectRelatedMixin(object):
    """
    Mixin allows you to provide a tuple or list of related models to
    perform a select_related on.
    """
    select_related = None  # Default related fields to none

    def get_queryset(self):
        if self.select_related is None:  # If no fields were provided,
                                         # raise a configuration error
            raise ImproperlyConfigured(u"%(cls)s is missing the "
                "select_related property. This must be a tuple or list." % {
                    "cls": self.__class__.__name__})

        if not isinstance(self.select_related, (tuple, list)):
            # If the select_related argument is *not* a tuple or list,
            # raise a configuration error.
            raise ImproperlyConfigured(u"%(cls)s's select_related property "
                "must be a tuple or list." % {"cls": self.__class__.__name__})

        # Get the current queryset of the view
        queryset = super(SelectRelatedMixin, self).get_queryset()

        # Return the queryset with a comma-joined argument to `select_related`.
        return queryset.select_related(
            ", ".join(self.select_related)
        )
        
class CreateAndRedirectToEditView(CreateView):
    """
    Subclass of CreateView which redirects to the edit view.
    Requires property `success_url_name` to be set to a
    reversible url that uses the objects pk.
    """
    success_url_name = None

    def get_success_url(self):
        # First we check for a name to be provided on the view object.
        # If one is, we reverse it and finish running the method,
        # otherwise we raise a configuration error.
        if self.success_url_name:
            self.success_url = reverse(self.success_url_name,
                kwargs={'pk': self.object.pk})
            return super(CreateAndRedirectToEditView, self).get_success_url()

        raise ImproperlyConfigured(
            "No URL to reverse. Provide a success_url_name.")
        
class UserFormKwargsMixin(object):
    """
    CBV mixin which puts the user from the request into the form kwargs.
    Note: Using this mixin requires you to pop the `user` kwarg
    out of the dict in the super of your form's `__init__`.
    """
    def get_form_kwargs(self, **kwargs):
        kwargs = super(UserFormKwargsMixin, self).get_form_kwargs(**kwargs)
        # Update the existing form kwargs dict with the request's user.
        kwargs.update({"user": self.request.user})
        return kwargs



