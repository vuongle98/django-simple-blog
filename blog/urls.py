from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='blog'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('detail/<slug:slug>', views.Detail.as_view(), name='post')
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)