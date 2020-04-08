"""Defines URL patterns for bloger"""

from django.urls import path

from . import views

app_name = 'bloger'
urlpatterns = [
	#Home page
	#path('', views.index, name = 'index'),
	path('', views.blogposts, name = 'blogposts'),
	#Detail page for a single post
	path('/<int:blogpost_id>/', views.blogpost, name='blogpost'),
	#Page for adding a new post
	path('new_blogpost/', views.new_blogpost, name='new_blogpost'),
	#Page for editing a post
	path('edit_blogpost/<int:blogpost_id>/', views.edit_blogpost, name='edit_blogpost'),
]