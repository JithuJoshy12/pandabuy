from django.urls import path
from . import views



app_name = 'core'

urlpatterns = [
    
    path('', views.main, name='main'),
    path('short-sleeves/', views.short_sleeves, name='short_sleeves'),
    path('long-sleeves/', views.long_sleeves, name='long_sleeves'),
    path('pants/', views.pants, name='pants'),
    path('shorts/', views.shorts, name='shorts'),
    path('shoes/', views.shoes, name='shoes'),
    path('accessories/', views.accessories, name='accessories'),
    path('sweaters/', views.sweaters, name='sweaters'),
    path('jackets/', views.jackets, name='jackets'),
    path('tracksuits/', views.tracksuits, name='tracksuits'),
    path('budget/', views.budget, name='budget'),
    path('watches/', views.watches, name='watches'),
    path('tech/', views.tech, name='tech'),
]