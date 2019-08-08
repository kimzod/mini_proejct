from django.urls import path
from weather import views

app_name = 'weather'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<city_name>/', views.delete_city, name='delete_city')
]
