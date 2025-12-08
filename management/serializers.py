from rest_framework import serializers               # DRF serializer base classes
from .models import Course, Enrollment, Assignment   # Our models
from users.serializers import UserSerializer  

class AssignmentSerializer(serializers.ModelSerializer):
    """
    Convert Assignment <-> JSON
    """
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'due_date', 'course', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class EnrollmentSerializer(serializers.ModelSerializer):
    """
    Convert Enrollment <-> JSON
    Includes nested student data for reads, and accepts student_id for writes.
    """
    student = UserSerializer(read_only=True)
    student_id = serializers.IntegerField(
        write_only=True, required=False)
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'student_id', 'course', 'enrolled_at']
        read_only_fields = ['id', 'enrolled_at']

class CourseSerializer(serializers.ModelSerializer):
    """
    Convert Course <-> JSON
    Includes nested professor, assignments, and enrollments for reads.
    """
    professor = UserSerializer(read_only=True)
    assignments = AssignmentSerializer(many=True, read_only=True)
    enrollments = EnrollmentSerializer(many=True, read_only=True)
    enrollment_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'professor', 'assignments', 'enrollments', 'enrollments_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    def get_enrollment_count(self, obj):
        return obj.enrollments.count()