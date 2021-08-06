from django.db import models

# Create your models here.

class Portfolio(models.Model):
	title = models.CharField(max_length=120)
	description = models.CharField(max_length=350)
	image = models.ImageField(upload_to='portfolio/images')
	url = models.URLField(blank=True)