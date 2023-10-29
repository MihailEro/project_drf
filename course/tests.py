from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from course.models import Course, Subscribe


class SubscribeTestCase(APITestCase):
    def setUp(self):
        self.data = {
            'user': 1,
            'course': 1,
            'is_active': True
        }
        User.objects.create(email='test@sky.com', password='test1')
        Course.objects.create(course_name='test', course_description='test')

    def test_create_subscribe(self):
        """"""
        url = reverse("course:create-subscribe")
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_subscribe(self):
        """"""
        user = User.objects.get()
        course = Course.objects.get()

        Subscribe.objects.create(id=1, user=user, course=course, is_active=True)

        url = reverse("course:delete-subscribe", kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
