from django.urls import path
from compare import views

app_name = 'cars'
urlpatterns = [
    path('',views.home, name = 'cars')
]