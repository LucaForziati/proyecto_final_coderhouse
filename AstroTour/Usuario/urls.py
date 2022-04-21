from django.urls import path
from Usuario import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('padre', views.padre_template),
    path('login', views.login_request)
]