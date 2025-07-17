from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name="create-page"),
    path('user-create/', views.UsersCreateList.as_view(), name="user-list-create"),
    path('user-create/<int:pk>', views.UserUpdateDelete.as_view(), name="user-list-create"),
]