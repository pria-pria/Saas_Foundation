
from .views import Home, about_View
from django.urls import path

urlpatterns = [
    path('', Home),
    path('about/', about_View )
]