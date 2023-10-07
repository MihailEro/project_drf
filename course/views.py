from rest_framework import viewsets

from course.models import Course
from course.serializers import CourseSerializer, CourseDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()
