from rest_framework import serializers

from course.models import Course

from rest_framework.fields import SerializerMethodField
from lessons.models import Lesson
from lessons.serializers import LessonSerializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonSerializers(source='lesson_set', many=True)

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.pk).count()


    class Meta:
        model = Course
        fields = '__all__'
