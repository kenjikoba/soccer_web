from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('app/user/', views.InputCreateView.as_view(), name='user_input'),
    path('app/user/complete/', views.InputCreateCompleteView.as_view(), name='user_input_complete'),
]