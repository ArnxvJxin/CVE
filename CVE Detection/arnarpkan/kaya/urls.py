from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('login/', views.login, name='login'),
    path('login/account/', views.account, name='account',),
    path('login/account/welcome/', views.welcome, name='welcome'),
]
