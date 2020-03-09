from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
 path('masini', views.index, name='masina_index'),
 url(r'^masina/view/(?P<id>\d+)$', views.show, name='masina_show'),
 url(r'^masina/edit/(?P<id>\d+)$', views.edit, name='masina_form'),
 path('masina/<int:id>/update', views.update, name='masina_update'),
 path('masina/create/<int:reprezentanta_id>', views.create, name='masina_create'),
 path('masina/create', views.create, name='masina_create'),
 path('masina/store', views.store, name='masina_store'),
 path('masina/<int:id>/delete', views.destroy, name='masina_delete'),
 path('masina/<int:id>/delete_photo', views.destroy_photo, name='masina_delete_photo'),
]