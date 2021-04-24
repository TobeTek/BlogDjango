from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):

	title= models.CharField(max_length= 200)

	author=  models.ForeignKey( 'auth.User', on_delete= models.CASCADE, )

	body = models.TextField()

	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('post_detail', args= [str(self.id)])
		pass
class Comment(models.Model): # new

		
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments', default = Post)
	comment = models.CharField(max_length=140)
	author = models.ForeignKey(
	'auth.User',
	on_delete=models.CASCADE, 
		)
	active = models.BooleanField(default = False)
	def __str__(self):
		return self.comment
	def get_absolute_url(self):
		return reverse('home')
	