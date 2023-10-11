from rest_framework import viewsets

from course.models import Course
from course.serializers import CourseSerializer, CourseDetailSerializer

from users.permissions import IsSuperuser, IsOwnerOrStaff


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseDetailSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsSuperuser]
        elif self.action == 'destroy':
            self.permission_classes = [IsSuperuser]
        elif self.action == 'update':
            self.permission_classes = [IsOwnerOrStaff]
        elif self.action == 'retrieve':
            self.permission_classes = [IsOwnerOrStaff]
        return [permission() for permission in self.permission_classes]
