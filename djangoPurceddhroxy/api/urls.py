from django.urls import path
from .views import FiltersListAPI, FilterDetailAPI, PacketsListAPI

urlpatterns = [
    path('filters-list/', FiltersListAPI.as_view(), name='filters-list'),
    path('filter-detail/<int:pk>/', FilterDetailAPI.as_view(), name='filter-detail'),
    path('packets-list/', PacketsListAPI.as_view(), name='packets-list'),
]
