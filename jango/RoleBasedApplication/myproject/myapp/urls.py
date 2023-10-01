# role_permissions_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.decorators import user_passes_test

urlpatterns = [
    path('admin/', user_passes_test(views.is_admin, login_url='/permission-denied/')(views.admin_dashboard), name='admin_dashboard'),
    path('user/', user_passes_test(views.is_user, login_url='/permission-denied/')(views.user_dashboard), name='user_dashboard'),
    path('permission-denied/', views.permission_denied, name='permission_denied'),
]
