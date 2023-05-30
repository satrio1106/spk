from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alternatif/', views.alternatif, name='alternatif'),
    path('add-alternatif/', views.add_alternatif, name='add-alternatif'),
    path('edit-alternatif/<str:pk>', views.edit_alternatif, name='edit-alternatif'),
    path('delete-alternatif/<str:pk>', views.delete_alternatif, name='delete-alternatif'),

    path('kriteria/', views.kriteria, name='kriteria'),
    path('edit-kriteria/<str:pk>', views.edit_kriteria, name='edit-kriteria'),

    path('add-penilaian/', views.add_penilaian, name='add-penilaian'),
    path('edit-penilaian/<str:pk>', views.edit_penilaian, name='edit-penilaian'),

    path('sub-kriteria/', views.sub_kriteria, name='sub-kriteria'),
    path('metode-saw/', views.metode_saw, name='metode-saw'),
    path('metode-wp/', views.metode_wp, name='metode-wp'),
    path('metode-ahp/', views.metode_ahp, name='metode-ahp'),
]