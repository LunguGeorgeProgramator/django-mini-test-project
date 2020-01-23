from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^view$', views.show, name='show'),
 url(r'^masina/edit/(?P<id>\d+)$', views.edit, name='form'),
 path('masina/<int:id>/update', views.update, name='update'),
 path('masina/create', views.create, name='create'),
 path('masina/store', views.store, name='store'),
 path('masina/<int:id>/delete', views.destroy, name='webapp.delete'),
]