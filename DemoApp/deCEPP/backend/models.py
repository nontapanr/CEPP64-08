from django.db import models

# Create your models here.
class Student(models.Model):
    modelID = models.AutoField(primary_key=True)
    StudentID = models.CharField(max_length=500)
    SubjectID = models.CharField(max_length=500,default="ไม่มีข้อมูล")
    Grade = models.CharField(max_length=5,default="ไม่มีข้อมูล")
    Semester = models.CharField(max_length=5,default="ไม่มีข้อมูล")
    Year = models.CharField(max_length=10,default="ไม่มีข้อมูล")
    Curriculum = models.CharField(max_length=500,default="ไม่มีข้อมูล")