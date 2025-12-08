from django.db import models
from django.conf import settings

class Course(models.Model):
    """
    Represents a course in the educational platform.
    Each course has a title, description, and is taught by a professor.
    """

    title = models.CharField(
        max_length=200
    )
    description = models.TextField(
        blank=True
    )
    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='courses',
        limit_choices_to={'is_professor': True}    
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['-created_at']
    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    """
    Links a student to a course (many students can enroll in many courses).
    """
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='enrollments',
        limit_choices_to={'is_student': True}
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    enrolled_at = models.DateTimeField(
        auto_now_add=True
    )
    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
        unique_together = ('student', 'course')
        ordering = ['-enrolled_at']
    def __str__(self):
        return f"{self.student.username} - {self.course.title}"

class Assignment(models.Model):
    """
    Represents an assignment for a specific course.
    Each assignment has a title, description, and a due date.
    """
    
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='assignments'
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    due_date = models.DateTimeField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"
        ordering = ['-due_date']
    def __str__(self):
        return f"{self.course.title} - {self.title}"