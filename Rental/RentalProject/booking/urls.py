from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('create/', views.create, name="booking"),
]

router = DefaultRouter()
router.register("booking", views.UserViewset)
urlpatterns += router.urls
