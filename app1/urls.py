from app1.views import home
from . import views
from django.urls import path
urlpatterns = [
    path('', home),
    path('final_velocity1/', views.final_velocity1),
    path('final_velocity2/', views.final_velocity2),
    path('displacement/', views.displacement),
    path('energy_atom/', views.energy_atom)
]