from django.shortcuts import render
import glob                        
import pandas as pd
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json



# Create your views here.
targetfile = "temp/Hashid_ComData.csv"

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def testReturn(csv_file):
    df = pd.read_csv(csv_file, encoding= 'utf-8')
    df = df.head()
    df = df.reset_index()  # make sure indexes pair with number of rows
    lis = []
    for index, row in df.iterrows():
        dic = {
            "StudentID":row['student_id'],
            "SubjectID":row['subject_id'],
            "Grade":row['grade'],
            "Semester":row['semester'],
            "Year":row['year'],
            "Curriculum":row['curriculum']
        }
        lis.append(dic)
    return lis
    
