
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
urlpatterns =[
     path('', views.index, name = 'home'),
     # # path('login/', views.login, name = 'login'),
     # path('index/', views.index, name = 'index'),
     path('register', views.register, name= 'register'),
     path('login', views.login, name = 'login'),
     path('logout', views.logout, name='logout')
     #  path('index/', views.index, name = 'index'),

]