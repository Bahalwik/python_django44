from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('advertisements', views.advertisement_list, name='advertisement_list'),
    # path('create_advertisement', views.create_advertisement, name='create_advertisement'),
    # path('contacts', views.contacts, name='contacts'),
    # path('about', views.about, name='about')
]
