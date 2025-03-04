from django.urls import path
from .views import home, add_condition, recommend

urlpatterns = [
    path('', home, name='home'),
    path('add_condition/', add_condition, name='add_condition'),
    path('recommend/', recommend, name='recommend'),
]