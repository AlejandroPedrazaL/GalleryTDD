from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addUser/', views.add_user_view, name='addUser'),
    path('getPortafolio/', views.get_portafolios, name='getPortafolio'),
    path('updateUser/', views.update_user_view, name='updateUser')
]
