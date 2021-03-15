from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_links, name='show_links'),
]
