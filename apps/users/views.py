from django.shortcuts import render
from django.views.generic import FormView, TemplateView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from apps.users import forms as users_forms


class LoginPage(FormView):
    template_name = 'login/index.html'
    form_class = users_forms.LoginForm

    # def get_success_url(self):
    #     return reverse('users:profile_page')

    def form_valid(self, form):
        phone = form.cleaned_data.get('phone').strip('+_-.()').replace(' ', '')

        user = authenticate(self.request, phone=phone)
        if user:
            login(self.request, user)
            return super(LoginPage, self).form_valid(form)
        form.add_error('phone', 'Введен не правильный пароль или номер телефона')
        return super(LoginPage, self).form_invalid(form)

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect(reverse('main:home_page'))
    #     return super(LoginPage, self).dispatch(request, *args, **kwargs)
