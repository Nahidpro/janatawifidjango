from django.urls import path
from . import views

urlpatterns = [
    path('', views.showjson_homepage),
]
