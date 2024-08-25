from django.contrib import admin
from .models import Course, CourseInstance

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_code', 'description')

class CourseInstanceAdmin(admin.ModelAdmin):
    list_display = ('course', 'year', 'semester')

admin.site.register(Course)
admin.site.register(CourseInstance)
