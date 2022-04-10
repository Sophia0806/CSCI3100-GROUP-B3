from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    # 1017 email verification-add
    path('confirm/', views.user_confirm, name='confirm'),
    #4-3 for change password
    path('password/', views.change_password, name='password'),
    path('change_photo/', views.edit_profile, name='photo'),
]