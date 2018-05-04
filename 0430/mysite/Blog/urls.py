from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^create/', views.create, name="create"),
    url(r'^edit/', views.edit, name="edit"),
]