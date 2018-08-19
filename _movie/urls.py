from django.conf.urls import url
from django.contrib.auth import views
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = '_movie'

urlpatterns = [
    url(
        regex=r'^main/$',
        view=views.Main.as_view(),
        name='main',
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)