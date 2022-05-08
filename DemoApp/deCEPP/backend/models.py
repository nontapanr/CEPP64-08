from django.db import models

# Create your models here.
class Student(models.Model):
    StudentID = models.CharField(primary_key=True, max_length=500)
    SubjectID = models.CharField(max_length=500)
    Grade = models.CharField(max_length=2,default="ไม่มีข้อมูล")
    Semester = models.CharField(max_length=1)
    Year = models.CharField(max_length=4)
    Curriculum = models.CharField(max_length=500)