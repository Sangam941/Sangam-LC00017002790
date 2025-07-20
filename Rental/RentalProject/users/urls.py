from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('create/', views.create, name="create-user"),
]

router = DefaultRouter()
router.register("user", views.UserViewset)
urlpatterns += router.urls
