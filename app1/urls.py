from app1.views import home
from . import views
from django.urls import path
urlpatterns = [
    path('', home),
    path('final_velocity1/', views.final_velocity1,name='final_velocity1'),
    path('final_velocity2/', views.final_velocity2,name='final_velocity2'),
    path('displacement/', views.displacement, name='displacement'),
    path('energy_light/', views.energy_light, name='energy_light'),
    path('time_flight/', views.time_flight, name='time_flight'),
    path('max_height/', views.max_height, name='max_height'),
    path('horizontal_range/', views.horizontal_range, name='horizontal_range'),
    path('capacitance/', views.parallel_plate_capacitance, name='par_plate_capacitance'),
    path('half_life/', views.half_life, name='half_life'),
    path('energy_kinetic/', views.kinetic_energy, name='kinetic_energy'),
]