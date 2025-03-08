from django.urls import path
from . import views
from .views.polars_search import polars_search_demo

urlpatterns = [
    path('', views.home, name='home'),
    path('polars-search/', polars_search_demo, name='polars_search_demo'),
]
