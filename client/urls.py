from agent import views
from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('home/', views.home),
    path('house/', views.house),
    path('pages/<int:id>/', views.pages, name='pages'),
    path('home_insure/<int:id>/', views.home_form, name='home_insure'),
    path('vehicle_insure/<int:id>/', views.vehicle_form, name='vehicle_insure'),
    path('travel_insure/<int:id>/', views.travel_form, name='travel_insure'),
    path('health_insure/<int:id>/', views.health_form, name='health_insure'),
    path('life_insure/<int:id>/', views.life_form, name='life_insure'),
    path('mobile_insure/<int:id>/', views.mobile_form, name='mobile_insure'),
    path('order/', views.order),
    path('history/', views.history),
    path('prblm/',views.prblm),
    path('myaccount/', views.myaccount)

]