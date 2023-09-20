from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *
menu=[
	{'title':"Меню1", 'url_name':'about'}, 
	{'title':"Меню2", 'url_name':'add_page'},
	{'title':"Меню3", 'url_name':'contact'},
	{'title':"Меню4", 'url_name':'login'}
]
def index(request):
	posts=Products.objects.all()
	context={
		'posts':posts, 
		'menu':menu, 
		'title':'Название1'
	}
	return render(request, 'products/index.html', context=context)
def pageNotFound(request, exception):
	return HttpResponseNotFound("Страница не найдена")
def show_post(request, post_id):
	return HttpResponse(f"Отображение статьи с id = {post_id}")
def show_person(request, cat_id):
		posts=Products.objects.filter(person_id=person_id)
		persons=Person.objects.all()
		if len(posts)==0:
			raise Http404()
		context={
			'posts':posts,
			'persons':persons,
			'menu':menu,
			'title':'Главная страница',
			'person_selected':person_id,
		}
		return render(request, 'products/index.html', context=context)