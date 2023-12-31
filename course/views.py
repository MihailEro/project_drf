from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from course.services import send_mail_for_update

from course.models import Course, Subscribe
from course.serializers import CourseSerializer, SubscribeSerializer

from users.permissions import IsSuperuser, IsOwnerOrStaff

from course.paginators import CoursePaginator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        elif self.action == 'destroy':
            self.permission_classes = [AllowAny]
        elif self.action == 'update':
            self.permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]


class SubscribeCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(is_active=True)


class SubscribeDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscribe.objects.all()
    permission_classes = [AllowAny]
