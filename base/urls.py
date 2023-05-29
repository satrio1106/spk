from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alternatif/', views.alternatif, name='alternatif'),
    path('kriteria/', views.kriteria, name='kriteria'),
    path('sub-kriteria/', views.sub_kriteria, name='sub-kriteria'),
    path('metode-saw/', views.metode_saw, name='metode-saw'),
    path('metode-wp/', views.metode_wp, name='metode-wp'),
    path('metode-ahp/', views.metode_ahp, name='metode-ahp'),
]