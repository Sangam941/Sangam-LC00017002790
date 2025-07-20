from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('create/', views.create, name="payment"),
]

router = DefaultRouter()
router.register("payment", views.UserViewset)
urlpatterns += router.urls
