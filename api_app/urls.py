from urllib import request
from django.urls import path

from . import views

app_name = 'api_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('test/', views.test_vue, name='test'),
    path('result/', views.test_result, name='result')
]