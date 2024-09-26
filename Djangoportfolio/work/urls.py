from django.urls import path
from .views import home, not_found

urlpatterns = [
    path('', home, name="home"),
    path('not_found/', not_found, name="not_found"),
]