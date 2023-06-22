from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),

    path('company/update/', views.CompanySettings.as_view(), name='company_update'),
    path('calendar/', views.Calendar.as_view(), name='calendar'),

]