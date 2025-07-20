from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('create/', views.create, name="vehicle"),
]

router = DefaultRouter()
router.register("vehicle", views.UserViewset)
urlpatterns += router.urls
