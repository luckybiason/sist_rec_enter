#-*- coding: utf-8 -*-
from django.shortcuts  import render
from django.contrib.auth.decorators import login_required

@login_required
def menu(request):
    return render(request, 'index.html', locals())
