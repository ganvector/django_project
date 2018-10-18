from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/novo/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/atualiza/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/deletar/', PostDeleteView.as_view(), name = 'post-delete'),
    path('about/', views.about, name='blog-about'),
]