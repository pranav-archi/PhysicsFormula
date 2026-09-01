from app1.views import home
from . import views
from django.urls import path
urlpatterns = [
    path('', home),
    path('final_velocity1/', views.calc_final_velocity1())
]