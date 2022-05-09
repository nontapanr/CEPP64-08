from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from backend.models import Student
from backend.serializers import StudentSerializer
from django.core.files.storage import default_storage
from datanly import views as datan
# Create your views here.

@csrf_exempt
def studentApi(request,id=0):
    if request.method=='GET':
        if id == 0:
            students = Student.objects.all()
            students_serializer=StudentSerializer(students,many=True)
            return JsonResponse(students_serializer.data,safe=False)
        else:
            student = Student.objects.get(StudentID=id)
            student_serializer=StudentSerializer(student)
            return JsonResponse(student_serializer.data,safe=False)
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        student_serializer=StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Student.objects.get(StudentID=student_data['StudentID'])
        student_serializer=StudentSerializer(student,data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        student=Student.objects.get(StudentID=id)
        student.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def upload(request):
    csv_file = request.FILES['path_to_csv']
    students = datan.testReturn(csv_file)
    print(students)
    for i in students:
        student_serializer = StudentSerializer(data=i)
        if student_serializer.is_valid():
            student_serializer.save()
        else:
            print(i)
    return JsonResponse("Good",safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)