from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('app/user/', views.InputCreate, name='user_input'),
    path('app/user/player', views.player_list, name='player_list'),
    path('app/user/complete', views.move_to_output, name='user_input_complete'),
]