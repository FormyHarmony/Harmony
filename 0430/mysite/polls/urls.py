from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.search_form, name='search_form'),
    url('a', views.search, name='search'),
]
