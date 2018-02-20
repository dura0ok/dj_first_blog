from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<id>[0-9]+)$', views.getfull, name='full'),
    url(r'^add$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^', include('users.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)