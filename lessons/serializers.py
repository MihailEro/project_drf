from rest_framework import serializers
from lessons.models import Lesson
from course.models import Course
from rest_framework.relations import SlugRelatedField

from validators import URLValidator


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [URLValidator(field='field')]


class LessonListSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='course_name', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'
