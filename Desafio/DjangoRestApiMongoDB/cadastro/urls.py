from django.conf.urls import url 
from cadastro import views 
from rest_framework import permissions

 
urlpatterns = [ 
    url(r'^api/cadastrar$', views.cadastro_list),
    url(r'^api/cadastrar/(?P<pk>[0-9]+)$', views.cadastro_detail),
]