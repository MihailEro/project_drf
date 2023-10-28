from django.contrib import admin

from course.models import Course, Subscribe


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name',)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('course', 'user',)
