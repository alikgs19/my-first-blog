from django.db import models
from django.utils import timezone



class User(models.Model):

	def __str__(self):
		return self.username

	username = models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	family = models.CharField(max_length=30)
	#information
	birthdate = models.DateTimeField('birth date')

	#...
			



class Post(models.Model):
	def __str__(self):
		return self.title

	owner = models.ForeignKey(User)
	# author = owner()
	# author = models.CharField(max_length=30)
	title = models.CharField(max_length=100)#max title size = 100
	postcontent = models.TextField()

# Create your models here.

# class CommentHolder(models.Model):



class Comment(models.Model):
	# def __init__(self):
	# 	return 
	post = models.ForeignKey(Post)
	commenter = models.ForeignKey(User)
	content = models.TextField()