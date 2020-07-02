from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.search_page, name='search_page'),
    path('search_city',views.search_city,name='search_city'),
]
