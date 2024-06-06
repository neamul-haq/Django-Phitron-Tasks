from django.urls import path, include
from . import views
urlpatterns = [
    path('signup', views.sign_up, name="signup"),
    path('login', views.log_in, name="login"),
    path('profile', views.profile, name="profile"),
    path('logout', views.log_out, name="logout"),
    path('pass_change/', views.pass_change, name='passchange'),
    path('pass_change2/', views.pass_change2, name='passchange2'),
]