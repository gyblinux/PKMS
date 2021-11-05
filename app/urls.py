from django.urls import path
from app import views

urlpatterns = [
    path('paras/', views.para_list),
    path('post/', views.post),
]