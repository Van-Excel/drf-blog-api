from django.urls import path
from .views import PostsListView, PostsDetailView


urlpatterns = [
    path('<int:pk>/', PostsDetailView.as_view(), name='posts_detail'),
    path('', PostsListView.as_view(), name='posts_list'),
]
