from rest_framework import serializers
from .models import Student, Department

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        # fields = ("pk", "department_name")
        fields = ("__all__")

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields = ("pk", "student_id", "student_name", "email", "department", "date_of_birth", "address", "phone")
        fields = ("__all__")
