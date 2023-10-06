from lessons.apps import LessonsConfig
from django.urls import path

from lessons.views import LessonCreateAPIView, LessonListAPIView, LessonUpdateAPIView, LessonRetrieveAPIView, \
    LessonDestroyAPIView

app_name = LessonsConfig.name

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

]
