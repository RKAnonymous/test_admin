from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import sign_in, home, sign_out, ManagersListView, ManagerCreateView, ManagerUpdateView, manager_delete


urlpatterns = [
    path("managers/", login_required(ManagersListView.as_view(), login_url="login"), name="managers_list"),
    path("managers/create/", login_required(ManagerCreateView.as_view(), login_url="login"), name="manager_add"),
    path("managers/edit/<int:id>", login_required(ManagerUpdateView.as_view(), login_url="login"), name="manager_update"),
    path("managers/delete/<int:id>", login_required(manager_delete, login_url="login"), name="manager_delete"),
    path('', sign_in, name="login"),
    path('logout/', login_required(sign_out, login_url="login"), name="logout"),
    path('home/', login_required(home, login_url="login"), name="home")
]
