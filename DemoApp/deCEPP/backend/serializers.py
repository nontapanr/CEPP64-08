from rest_framework import serializers
from backend.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student 
        fields=('StudentID','SubjectID','Grade','Semester','Year','Curriculum')