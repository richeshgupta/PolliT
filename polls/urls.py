from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    path('createpoll/',CreatePoll.as_view(),name='createPoll'),
    path('mypolls/',MyPolls,name='mypolls'),
    path('poll/<int:pk>/',SpecificPoll,name='poll'),
]
    