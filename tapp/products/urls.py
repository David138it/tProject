from django.urls import path, re_path
from .views import *
urlpatterns = [
	path('', index, name='home'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('person/<int:person_id>/', show_person, name='person'),
]