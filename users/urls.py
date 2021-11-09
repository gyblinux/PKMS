from django.urls import path
from users import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetail.as_view()),
    path('register/', views.UserCreate.as_view()),
    path('login/', views.UserLogin.as_view()),
]