from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
	posts = Blog.objects.all().order_by('-date')
	return render(request, 'blog/blogs.html', {'posts':posts})

def single(request, blog_id):
	single = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/single.html', {"single":single})