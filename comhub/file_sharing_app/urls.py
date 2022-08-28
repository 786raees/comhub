from django.urls import path
from . import views as file_sharing_views

urlpatterns = [
    path("", file_sharing_views.home, name="home"),
    path("about/", file_sharing_views.about, name="about"),
    path("users_/<str:username>/", file_sharing_views.update_user, name="update_user"),
    
]
