from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f"{self.course_code} - {self.title}"

class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.course.course_code} ({self.year} - Sem {self.semester})"
