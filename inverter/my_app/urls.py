from django.urls import path
from . import views
from .views import api_inverter1_data


urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('evaluation/', views.evaluation, name='evaluation'),  # evaluation page
    path('inverter_data/', views.inverter1, name='inverter1'),  # inverter-data page
    path('weather/', views.weather, name='weather'),  # weather-data page
    path('report/', views.report, name='report'),  # report page
    path('api/inverter1_data/', api_inverter1_data, name='api_inverter1_data'),
]
