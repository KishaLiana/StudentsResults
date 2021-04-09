from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def index (request):
    students = Student.objects.all()
    context = {
        "mystudents":students,
    }
    return render(request, 'students.html', context)

def add(request):
    students = Student.objects.all()
    context = {
        "mystudents":students,
    }
    if 'register' in request.POST:
        mname = request.POST['Name']
        mreg = request.POST['Regno']
        mcourse = request.POST['Courseunit']
        mmarks = request.POST['Mark']

        student = Student(Name=mname,RegNo=mreg,CourseUnit=mcourse,Mark=mmarks)

        student.save()
        print("Inserrrteedddd............")
        messages.success(request,"Success: Record inserted successfully")
        return render(request, "students.html",context)
    
    
    return render(request, "index.html",context)


def editstudent(request, id):
    student = Student.objects.get(id=id)
    
    if 'update' in request.POST:
        student.Name = request.POST["namer"]
        student.RegNo = request.POST["regnor"]
        student.CourseUnit = request.POST["courseunitr"]
        student.Mark = request.POST["markr"]


        student.save()
        students = Student.objects.all()
        context = {
            "mystudents":students,
        }
        messages.info(request,"Success: Record Updated successfully")
        return render(request, 'students.html', context)
        
    
    return render(request, 'edit.html', {'student':student})


def student_delete(request, id):
    
    student = Student.objects.get(id=id)
    student.delete()

    data = dict()
    messages.error(request,"Deleted: Record Deleted")

    students = Student.objects.all()
    context = {
            "mystudents":students,
        }
    return render(request, "students.html",context)
