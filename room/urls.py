from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms_list, name='rooms'),
    path('<int:pk>', views.room_detailed, name='room_detailed')
]