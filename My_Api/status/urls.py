from django.urls import path
from .views import (
    # StatusAPIView, 
    # StatusListAPIView, 
    # StatusCreateAPIView, 
    # StatusDetailAPIView, 
    # StatusUpdateAPIView,
    # StatusDeleteAPIView,
    # StatusListCreateView,
    # StatusDetailUpdateDeleteAPIView,
    StatusViewset,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'status', StatusViewset, basename="status")



urlpatterns = [
    # path('status/', StatusAPIView.as_view()),
    # path('status/', StatusListCreateView.as_view()),
    # path('status/<id>', StatusDetailUpdateDeleteAPIView.as_view()),
    # path('status/list/', StatusListAPIView.as_view()),
    # path('status/create/', StatusCreateAPIView.as_view()),
    # path('status/detail/<id>/', StatusDetailAPIView.as_view()),
    # path('status/update/<id>/', StatusUpdateAPIView.as_view()),
    # path('status/delete/<id>/', StatusDeleteAPIView.as_view()),
] + router.urls