from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home
urlpatterns = [
    path('',home,name='home'),
    
]
