from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from map.forms import MyAuthenticationForm, MyPasswordChangeForm
from map.utils import log_time

HTTP_GET = "GET"
HTTP_POST = "POST"


class MapIndexView(FormView):
    template_name = "index.html"
    form_class = MyAuthenticationForm
    success_url = reverse_lazy("map:index")

    def get_form_kwargs(self):
        kwargs = super(MapIndexView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.get_user()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class MapLoginView(LoginView):
    """
        Login with MyAuthenticationForm
    """
    form_class = MyAuthenticationForm
    template_name = "login.html"

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.get_user()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context["gps"] = [120.015449, 30.2822]
        return context


class MapLogoutView(LogoutView):
    next_page = 'map:index'


class MapPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('map:index')
    form_class = MyPasswordChangeForm


@log_time
@login_required
def index(request):
    context = {"gps": [120.015449, 30.2822]}
    return render(request, 'index.html', context)
