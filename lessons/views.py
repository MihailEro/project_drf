from rest_framework import generics
from rest_framework.permissions import AllowAny

from lessons.models import Lesson
from lessons.serializers import LessonSerializers, LessonListSerializer

from users.permissions import IsOwnerOrStaff, IsSuperuser

from lessons.paginators import LessonsPaginator


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers
    permission_classes = [AllowAny]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    pagination_class = LessonsPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
