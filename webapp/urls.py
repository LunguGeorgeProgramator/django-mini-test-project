from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^view$', views.show, name='show'),
 url(r'^edit/(?P<id>\d+)/$', views.edit, name='form'),
 path('update/<int:id>/', views.update, name='update'),
 path('person/create', views.create, name='create'),
 path('person/store', views.store, name='store'),
 path('person/<int:id>/delete', views.destroy, name='webapp.delete'),
]