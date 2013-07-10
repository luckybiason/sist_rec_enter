from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger

def createPags(num_pag,collect,qnt):
    paginator = Paginator(collect,qnt)
    try:
        page = paginator.page(num_pag)
    except (EmptyPage,InvalidPage,PageNotAnInteger) :
        num_pag = 1
        page = paginator.page(num_pag)
        num_pag = int(num_pag)
    return page, paginator

def requestCatch(request):
    return request.GET.get('pagina','1')

def makePaginator(request,collect,group=5):
    num_pag = requestCatch(request)
    page, paginator = createPags(num_pag,collect,group)
    return num_pag, page, paginator


