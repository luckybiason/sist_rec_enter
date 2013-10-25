# Create your views here.
from django.shortcuts  import render

def show_alerts(request):
    return render(request, 'alerts_messages/teste.html', locals())