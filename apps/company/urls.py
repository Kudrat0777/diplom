from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
]