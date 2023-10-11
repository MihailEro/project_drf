from rest_framework import generics
from lessons.models import Lesson
from lessons.serializers import LessonSerializers, LessonListSerializer

from users.permissions import IsOwnerOrStaff, IsSuperuser


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers
    permission_classes = [IsSuperuser]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonListSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsSuperuser]
