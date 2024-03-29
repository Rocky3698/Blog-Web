from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('profile/',views.profile,name='edit_profile'),
    path('profile/password/change/',views.pass_change,name='change_pass'),
]