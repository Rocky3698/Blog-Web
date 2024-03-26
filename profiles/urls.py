from django.urls import path
from . import views
urlpatterns = [
    path('creat/',views.creat_profile,name='creat_profile')
]