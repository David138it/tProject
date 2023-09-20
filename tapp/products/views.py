from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
def index(request):
	return HttpResponse("Страница приложения products")
def pageNotFound(request, exception):
	return HttpResponseNotFound("Страница не найдена")