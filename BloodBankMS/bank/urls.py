from django.urls import path
from bank import views

app_name = 'bank'

urlpatterns = [
path('', views.bloodbank, name='bloodbank'),
]