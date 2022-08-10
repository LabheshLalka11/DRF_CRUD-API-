from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import is_valid_path
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Student
from .serializers import StudentSerializer

def Homepage(request):
    return HttpResponse('Home Page')

@csrf_exempt
def AllStudentDetail(request):
    try:
        students = Student.objects.all()
    except: 
        return HttpResponse('Not Found !! Sorry', status = 404)
    
    if request.method == 'GET':
        all_Student = StudentSerializer(students, many = True)
        return JsonResponse(all_Student.data, safe = False)
    
    elif request.method == 'POST':
        input_data = JSONParser().parse(request)
        serializer = StudentSerializer(data=input_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else: 
            return JsonResponse(serializer.errors, status=400)
        
def SingleStudentDetail(request, pk):
    try: 
        student = Student.objects.get(pk=pk)
    except:
        return HttpResponse('Not Found !! Sorry', status = 404)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data, status = 200)

    elif request.method == 'PUT':
        input_data = JSONParser().parse(request)
        serializer = StudentSerializer(student,input_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else: 
            return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse('Sucessfully Delete', status = 204)

    