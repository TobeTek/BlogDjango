from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, CreateCommentView, DeleteCommentView

urlpatterns= [
	path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name= 'post_delete'),
	path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name= 'post_edit'),
	path('post/new/', BlogCreateView.as_view(), name= 'post_new'),
	path('post/<int:pk>/', BlogDetailView.as_view(), name= 'post_detail'),
	path('comment/', CreateCommentView.as_view(), name= 'comment_create'),
	path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name= 'comment_delete'),
	path('', BlogListView.as_view(), name= 'home')]

