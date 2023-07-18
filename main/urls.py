from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='main'),
    path('signup/', views.signup, name='signup')
]