from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField()
	picture = models.ImageField(upload_to="blog/images")
	date = models.DateField()

