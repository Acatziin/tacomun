from django.urls import path, include
from . import views
# from places.models import Profile
# from places. import views

urlpatterns = [
    path ('signup/', views.SignUp.as_view(), name = 'signup'),
    path ('', include('django.contrib.auth.urls')),
    # path ('sigup/profile/<int:user_id', views.profile.as_view, name = 'profile')
]