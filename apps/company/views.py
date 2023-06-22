from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from . import models as company_models


class HomePage(TemplateView):
    template_name = 'base.html'


class CompanySettings(TemplateView):
    template_name = 'profile_settings/index.html'


class Calendar(TemplateView):
    template_name = 'calendar/index.html'