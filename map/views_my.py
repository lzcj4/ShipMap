from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from map.forms import MyAuthenticationForm, MyPasswordChangeForm
from map.utils import add_test_user


class MyLoginView(LoginView):
    """
        Login with MyAuthenticationForm
    """
    form_class = MyAuthenticationForm
    template_name = "login.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    #     return super(MyLoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.get_user()
        #add_test_user("")
        login(self.request, user)
        return JsonResponse(
            {"code": 200, 'msg': "login view succeed,current user:{0}".format(user.username)})
        # return HttpResponseRedirect(self.get_success_url())


class MyLogoutView(LogoutView):
    next_page = 'map:index'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('map:index')
    form_class = MyPasswordChangeForm
