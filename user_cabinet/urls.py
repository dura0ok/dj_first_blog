from django.conf.urls import url
from . import views
#main urls
#urls views.py STEPAN :D
urlpatterns = [
	url(r'^cabinet/$', views.cabinet, name='cabinet'),
]