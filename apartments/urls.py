from django.contrib.auth.decorators import login_required
from django.urls import path, include

from .views import ApartmentListView, ApartmentCreateView, ApartmentUpdate, apartment_delete, filters

urlpatterns = [
    path('list/', login_required(ApartmentListView.as_view(), login_url="login"), name='list'),
    path('create/', login_required(ApartmentCreateView.as_view(), login_url="login"), name='create'),
    path('update/<int:id>/', login_required(ApartmentUpdate.as_view(), login_url="login"), name='update'),
    path('delete/<int:id>/', login_required(apartment_delete, login_url="login"), name='delete'),
    path('filter/', login_required(filters, login_url="login"), name="filter")
]
