from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=150)
	description = models.CharField(max_length=250, null=True, blank=True)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	img_link = models.CharField(max_length=400, default=None)


class User(models.Model):
	user_name = models.CharField(max_length=40)
	password = models.CharField(max_length=30)
