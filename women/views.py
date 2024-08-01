from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *
menu = [{'title':"О сайте", 'url_name':'about'},
        {'title':"Добавить статью", 'url_name':'add_page'},
        {'title':"Обратная связь", 'url_name':'contact'},
        {'title':"Войти", 'url_name':'login'}]
def index(request):
    posts = Women.objects.all()

    context = {"menu":menu, "title":"Главный страница", "posts":posts, "cat_selected":0,}
    return render(request, "women/index.html",context=context)

def about(request):
    return render(request, "women/about.html", {"menu":menu, "title":"О сайте"})

def addpage(request):
    return HttpResponseNotFound('bet kosu')

def login(request):
    print(request.POST)
    return HttpResponseNotFound('login')

def contact(request):
    return HttpResponseNotFound('contact')

def categories(request, catid):
    print(request.POST)
    return HttpResponse(f'{catid}')

def show_post(request, post_id):
    return HttpResponse(f'{post_id}')

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts)==0:
        raise Http404
    context = {"menu": menu, "title": "Отображение по рубрикам", "posts": posts,  "cat_selected": cat_id, }
    return render(request, "women/index.html", context=context)

# def categories(request):
#     return HttpResponse("222")

def archive(request,year):
    print(year)
    if int(year)>2020:
        raise Http404()
        #return redirect('home', permanent=True)
    return HttpResponse(f'{year}')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Бет табылмады<h1>')