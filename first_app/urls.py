from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('user_login/', views.user_login, name='user_login'),
]
