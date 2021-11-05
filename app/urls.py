from django.urls import path
from app import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('paras/', views.ParaList.as_view()),
    path('paras/<int:pk>/', views.ParaDetail.as_view()),
]