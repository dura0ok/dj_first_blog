from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

#main urls
#urls views.py STEPAN :D
urlpatterns = [
	url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)