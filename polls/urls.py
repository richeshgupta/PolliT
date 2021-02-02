from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    path('createpoll/',CreatePoll.as_view(),name='createPoll'),
    path('mypolls/',MyPolls,name='mypolls'),
    path('poll/<int:pk>/',SpecificPoll,name='poll'),
    path('update-poll/<int:pk>/',UpdatePoll.as_view(),name='updatepoll'),
    path('delete-poll/<int:pk>/',DeletePoll.as_view(),name='deletepoll'),
    path('countpoll/',CountPoll)

]
    