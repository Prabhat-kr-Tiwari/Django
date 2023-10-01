from django.shortcuts import render
from .permission import is_admin,is_user
from django.http import HttpResponse
from django.http import HttpResponseForbidden
# Create your views here.

from django.contrib.auth.decorators import user_passes_test

# @user_passes_test(test_func, login_url=None, redirect_field_name='next')

def admin_dashboard(request):
    if is_admin(request.user):
        return render(request,'admin_dashboard.html')
    else:
        return HttpResponseForbidden('Permission denied')
    


def user_dashboard(request):
    if is_user(request.user):
        return render(request,'user_dashboard.html')
    else:
        return HttpResponseForbidden('Permission denied')


def permission_denied(request):
    if permission_denied(request.user):
        return render(request,'permission_denied.html')
    else:
        return HttpResponse('unable to respond')

