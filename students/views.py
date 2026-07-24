from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {
        'students': students
    })


@login_required
def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:

        form = StudentForm()

    return render(request, 'add_student.html', {
        'form': form
    })


@login_required
def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:

        form = StudentForm(instance=student)

    return render(request, 'edit_student.html', {
        'form': form
    })


@login_required
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect('student_list')


def login_user(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            messages.error(request, "Invalid Username or Password")

    return render(request, 'login.html')


def logout_user(request):

    logout(request)

    return redirect('login') 