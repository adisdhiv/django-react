from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('candidates/', views.candidates, name = "candidates"),
    path('interviewers/', views.interviewers, name = "interviewers"),
    path('createschedule', views.createschedule, name = "createschedule"),
    path('updateschedule/<str:pk>', views.updateschedule, name = "updateschedule"),
    path('deleteschedule/<str:pk>', views.deleteschedule, name = "deleteschedule"),
    path('createinterviewer', views.createinterviewer, name = "createinterviewer"),
    path('updateinterviewer/<str:pk>', views.updateinterviewer, name = "updateinterviewer"),
    path('deleteinterviewer/<str:pk>', views.deleteinterviewer, name = "deleteinterviewer"),
    path('createcandidate', views.createcandidate, name = "createcandidate"),
    path('updatecandidate/<str:pk>', views.updatecandidate, name = "updatecandidate"),
    path('deletecandidate/<str:pk>', views.deletecandidate, name = "deletecandidate"),
]
