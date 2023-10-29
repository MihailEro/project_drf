from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from lessons.models import Lesson


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.data = {
            "lesson_name": "test",
            "lesson_description": "test"
        }

    def test_create_lessons(self):
        """ Тестирование создания урока """
        url = reverse("lessons:lesson-create")
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_lesson(self):
        """Тестирование получения урока"""
        Lesson.objects.create(id=1, lesson_name='test1', lesson_description='test1')
        url = reverse("lessons:lesson-get", kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        """Тестирование обновления урока"""
        Lesson.objects.create(id=1, lesson_name='test1', lesson_description='test1')
        url = reverse("lessons:lesson-update", kwargs={'pk': 1})
        response = self.client.put(url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        Lesson.objects.create(id=1, lesson_name='test1', lesson_description='test1')
        url = reverse("lessons:lesson-delete", kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
