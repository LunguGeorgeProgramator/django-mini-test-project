from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^recenzii$', views.index, name='recenzie_index'),
    # url(r'^recenzie/view/(?P<id>\d+)$', views.show, name='recenzie_show'),
    url(r'^recenzie/edit/(?P<id>\d+)$', views.edit, name='recenzie_edit'),
    # path('recenzie/<int:id>/update', views.update, name='recenzie_update'),
    path('recenzie/create/<int:masina_id>', views.create, name='recenzie_create'),
    path('recenzie/<int:id>/delete', views.destroy, name='recenzie_delete'),
    path('recenzie/<int:id>/delete/<str:redirect_to>', views.destroy, name='recenzie_delete'),
]