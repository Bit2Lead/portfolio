from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
	posts = Blog.objects.all().order_by('-date')
	return render(request, 'blog/blogs.html', {'posts':posts})
