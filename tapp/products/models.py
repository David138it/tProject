from django.db import models
#from django.contrib.auth import get_user_model
#User = get_user_model()
class Products(models.Model):
	title=models.CharField(max_length=255)
	content=models.TextField(blank=True)
	is_published=models.BooleanField(default=True)
    #owner= models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
class Person(models.Model):
    name = models.CharField(max_length=255)