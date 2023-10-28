from course.apps import CourseConfig
from rest_framework.routers import DefaultRouter
from django.urls import path
from course.views import CourseViewSet, SubscribeCreateAPIView, SubscribeDestroyAPIView

app_name = CourseConfig.name


router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('subscriptions/create/', SubscribeCreateAPIView.as_view(), name='create-subscribe'),
    path('subscriptions/delete/<int:pk>/', SubscribeDestroyAPIView.as_view(), name='delete-subscribe'),
              ] + router.urls
