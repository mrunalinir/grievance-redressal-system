from django.urls import path
from . import views

urlpatterns=[
    path('',views.register_grievance,name='enter_grievance'),
]
