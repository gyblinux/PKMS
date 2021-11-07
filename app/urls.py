from django.urls import path
from app import views

urlpatterns = [
    path('', views.api_root),
    path('posts/', views.PostListCreate.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('paras/', views.ParaListCreate.as_view()),
    path('paras/<int:pk>/', views.ParaDetail.as_view()),
]