from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pokebutton$', views.pokebutton, name='pokebutton'),
    url(r'^$', views.pokes, name='pokes'),
]
