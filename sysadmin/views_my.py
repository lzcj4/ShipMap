
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, ListView

from sysadmin.forms import MyAuthenticationForm, MyPasswordChangeForm, MarkTaskCreateForm
from sysadmin.models import MarkTask, MarkFile, MarkUserTask
from sysadmin.utils import add_test_user, get_media_save_path, add_test_task


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
        # add_test_task(user)
        add_test_user("")
        login(self.request, user)
        return JsonResponse(
            {"code": 200, 'msg': "login view succeed,current user:{0}".format(user.username)})
        # return HttpResponseRedirect(self.get_success_url())


class MyLogoutView(LogoutView):
    next_page = 'sysadmin:index'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('sysadmin:index')
    form_class = MyPasswordChangeForm


class MarkTaskCreateView(FormView):
    template_name = 'task_create.html'
    success_url = reverse_lazy('sysadmin:task_list')
    form_class = MarkTaskCreateForm

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        task = self.create_task(form)
        print("create mark task:{0} succeed".format(task.id))
        return HttpResponseRedirect(self.get_success_url())
        # return JsonResponse({"code": 200, 'msg': "create mark task:{0} succeed".format(task.id)})

    def create_task(self, form: MarkTaskCreateForm):
        user = self.request.user
        task_name = form.cleaned_data['name']
        task = MarkTask(name=task_name, user_created=user)
        task.save()

        for k, v in form.files.items():
            save_name, save_path = get_media_save_path(v.name)
            with open(save_path, 'wb+') as new_file:
                new_file.write(v.file.read())
                file = MarkFile(file_name=v.name, file_path=save_name)
                file.task = task
                file.save()

        user_task = MarkUserTask(task=task, user=user)
        user_task.save()

        return task


class MarkTaskListView(ListView):
    template_name = 'task_list.html'
    context_object_name = "tasks"

    def get_queryset(self):
        return MarkTask.objects.filter(user_created=self.request.user)
