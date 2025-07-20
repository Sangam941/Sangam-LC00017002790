from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('create/', views.create, name="order"),
]

router = DefaultRouter()
router.register("order", views.UserViewset)
urlpatterns += router.urls
