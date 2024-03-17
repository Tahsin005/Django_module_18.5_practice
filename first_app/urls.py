from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('pass_change/', views.pass_change, name='pass_change'),
    path('pass_change2/', views.pass_change2, name='pass_change2'),
    path('change_data/', views.change_data, name='change_data'),
]
