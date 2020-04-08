from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

#def index(request):
#	"""The home page with all posts in the blog"""
#	return render(request, 'bloger/index.html')


def blogposts(request):
	"""Show all posts"""
	blogposts = BlogPost.objects.order_by('date_added')
	context = {'blogposts': blogposts}
	return render(request, 'bloger/index.html', context)


def blogpost(request, blogpost_id):
	"""Show a single post"""
	blogpost = BlogPost.objects.get(id = blogpost_id)
	context = {'blogpost': blogpost}
	return render(request, 'bloger/blogpost.html', context)

@login_required
def new_blogpost(request):
	"""Add a new post"""
	if request.method != 'POST':
		#No data submitted; create a blank form
		form = BlogPostForm()
	else:
		#POST data submitted, process data
		form = BlogPostForm(data= request.POST)
		if form.is_valid():
			new_blogpost = form.save(commit = False)
			new_blogpost.owner = request.user
			new_blogpost.save()
			return redirect('bloger:blogposts')

	#Display a blank or invalid form
	context = {'form': form}
	return render(request, 'bloger/new_blogpost.html', context)

@login_required
def edit_blogpost(request, blogpost_id):
	"""Edit an existing post"""
	blogpost = BlogPost.objects.get(id=blogpost_id)
	if blogpost.owner != request.user:
		raise Http404

	if request.method != 'POST':
		#Initial request, pre-fill form with the current post
		form = BlogPostForm(instance = blogpost)
	else:
		#POST data submitted, process data
		form = BlogPostForm(instance = blogpost, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('bloger:blogpost', blogpost_id = blogpost.id)

	context = {'blogpost': blogpost, 'form': form}
	return render(request, 'bloger/edit_blogpost.html', context)



