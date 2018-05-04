from django.shortcuts import render, redirect

from .models import *

def blog(request):
	if request.method == 'POST':
		primarykey = request.POST.get('primarykey ')
		Post.objects.get(pk=primarykey ).delete()
	post_list = Post.objects.all()
	return render(request, 'blog.html', {'post_list': post_list})

def create(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		Post.objects.create(title=title, content=content)
		return redirect('/blog')
	return render(request, 'create.html')

def edit(request):
	pk = request.GET.get('q')
	post = Post.objects.get(pk=pk)
	if request.method == 'POST':
		post.title = request.POST.get('title')
		post.content = request.POST.get('content')
		post.save()
		return redirect('/blog')
	return render(request, 'edit.html', {'post': post})
