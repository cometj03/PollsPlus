from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('signup/', views.signup, name='signup'),
   path('signin/', views.signin, name='login'),
   path('signout/', views.signout, name='logout')
]