from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
 url(r'^reprezentanta$', views.index, name='reprezentanta_index'),
 url(r'^reprezentanta/view/(?P<id>\d+)$', views.show, name='reprezentanta_show'),
 url(r'^reprezentanta/edit/(?P<id>\d+)$', views.edit, name='reprezentanta_form'),
 path('reprezentanta/<int:id>/update', views.update, name='reprezentanta_update'),
 path('reprezentanta/create', views.create, name='reprezentanta_create'),
 path('reprezentanta/store', views.store, name='reprezentanta_store'),
 path('reprezentanta/<int:id>/delete', views.destroy, name='reprezentanta_delete'),
]