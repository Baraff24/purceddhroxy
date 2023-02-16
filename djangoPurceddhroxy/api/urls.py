from django.urls import path
from .views import FiltersListAPI, PacketsListAPI

urlpatterns = [
    path('filters/', FiltersListAPI.as_view()),
    path('packets/', PacketsListAPI.as_view()),
]
