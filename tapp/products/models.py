from django.db import models
from django.urls import reverse
#from django.contrib.auth import get_user_model
#User = get_user_model()
class Products(models.Model):
	title=models.CharField(max_length=255)
	content=models.TextField(blank=True)
	is_published=models.BooleanField(default=True)
	owner=models.ForeignKey('Person', on_delete=models.PROTECT, null=True)
	def __str__(self):
		return self.title	
	def get_absolute_url(self):
		return reverse('post', kwargs={'post_id':self.pk})
class Person(models.Model):
	name=models.CharField(max_length=255, db_index=True) 
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('person', kwargs={'person_id':self.pk})