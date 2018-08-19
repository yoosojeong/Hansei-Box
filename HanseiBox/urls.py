from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from django.contrib.auth import views
from django.conf import settings
from _user import forms 

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^main/login/$', views.LoginView.as_view(template_name="login.html", authentication_form=forms.LoginForm), name="login"),
    url(r'^main/logout/$', views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"),
    url(r'^', include(('_movie.urls', '_movie'), namespace='_movie')),
]
 