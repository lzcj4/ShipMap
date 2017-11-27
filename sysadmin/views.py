import json

from sysadmin.forms import MyAuthenticationForm
from sysadmin.models_car import CarFeature
from sysadmin.perms import Perms
from sysadmin.utils import log_time
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.auth.views import logout_then_login
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

HTTP_GET = "GET"
HTTP_POST = "POST"


@log_time
@login_required
def index(request):
    if request.user.is_authenticated():
        return HttpResponse(json.dumps({"code": 200, 'msg': "index.html user:{0}".format(request.user.username)}))
        # else:
        #     return HttpResponseRedirect("login")
        # return render(request, "user_login.html")


def add_perm(user):
    content_type = ContentType.objects.get_for_model(CarFeature)
    permission = Permission.objects.create(codename=Perms.CAR_LIST,
                                           name='车辆列表',
                                           content_type=content_type)
    user.user_permissions.add(permission)
    user.save()


@csrf_exempt
def user_login(request):
    if request.method == HTTP_POST:
        form = MyAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # user = authenticate(username=request.POST['username'], password=request.POST['password'])
            user = form.get_user()
            if user is not None:
                login(request, user)

            next_url = request.POST.get('next')
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                return JsonResponse(
                    {"code": 200, 'msg': "login succeed,current user:{0}".format(user.username)})
    else:
        form = MyAuthenticationForm()
        return render(request, "login.html", {'form': form})


@login_required
def user_change_pwd(request):
    logout(request)
    return HttpResponse(json.dumps({"code": 200, 'msg': "logout succeed"}))


# @permission_required('sysadmin.logout')
# @user_passes_test(email_check, redirect_field_name=None)
@login_required
def user_logout(request):
    # logout(request)
    return logout_then_login(request)
    # return HttpResponse(json.dumps({"code": 200, 'msg': "logout succeed"}))
